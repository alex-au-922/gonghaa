from collections.abc import Iterator
from pathlib import Path
from shutil import copytree, ignore_patterns, unpack_archive
from uuid import uuid4

import pytest
from coverage_wasm import targets
from coverage_wasm.pytest_plugin import WasmCoverage
from testcontainers.community.postgres import PostgresContainer
from testcontainers.core.container import DockerContainer
from testcontainers.core.image import DockerImage
from testcontainers.core.network import Network
from testcontainers.core.wait_strategies import HttpWaitStrategy, LogMessageWaitStrategy

ROOT = Path(__file__).resolve().parents[1]
WORKER_DEPLOYMENT = Path("deployments/cloudflare-d1")
NODE_IMAGE = "node:24.18.0-bookworm"


@pytest.fixture(scope="session")
def worker_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    directory = tmp_path_factory.mktemp("worker")
    project = directory / "project"
    copytree(
        ROOT,
        project,
        symlinks=True,
        ignore=ignore_patterns(
            ".git",
            ".DS_Store",
            ".env*",
            ".dev.vars*",
            ".venv*",
            ".pytest_cache",
            ".ruff_cache",
            ".wrangler",
            "__pycache__",
            "node_modules",
            "python_modules",
            ".coverage*",
            "htmlcov*",
            "dist",
        ),
    )
    builder = (
        DockerContainer(NODE_IMAGE, docker_client_kw={"timeout": 300})
        .with_copy_into_container(project, "/")
        .with_env("CI", "true")
        .with_env("WRANGLER_SEND_METRICS", "false")
        .with_env("UV_PYTHON", "3.14.3")
        .with_kwargs(working_dir="/project/deployments/cloudflare-d1")
        .with_command(
            [
                "sh",
                "-ec",
                """
                curl -fsSL https://astral.sh/uv/0.13.4/install.sh -o /tmp/install-uv.sh
                UV_UNMANAGED_INSTALL=/usr/local/bin sh /tmp/install-uv.sh
                npm ci --no-audit --no-fund
                worker=/bundle/deployments/cloudflare-d1
                mkdir -p "$worker"
                uv run --locked --project /project pywrangler deploy --dry-run \
                    --outdir /bundle/src
                mv /bundle/src/python_modules /bundle/src/entrypoint.py "$worker/"
                cp wrangler.toml "$worker/"
                tar -czf /bundle/node_modules.tar.gz node_modules
                tar -cf /tmp/worker-bundle.tar -C / bundle
                """,
            ]
        )
    )
    archive = directory / "worker-bundle.tar"
    with builder:
        if builder.wait() != 0:
            pytest.fail(b"".join(builder.get_logs()).decode(errors="replace"))
        builder.copy_from_container("/tmp/worker-bundle.tar", archive)
    unpack_archive(archive, directory, filter="data")
    return directory / "bundle"


@pytest.fixture
def worker_container(
    worker_bundle: Path, wasm_coverage: WasmCoverage
) -> Iterator[DockerContainer]:
    app = (
        DockerContainer(NODE_IMAGE)
        .with_env("CI", "true")
        .with_env("WRANGLER_SEND_METRICS", "false")
        .with_kwargs(working_dir="/bundle/deployments/cloudflare-d1")
        .with_command(
            [
                "sh",
                "-ec",
                """
                tar -xzf /bundle/node_modules.tar.gz -C /bundle
                exec /bundle/node_modules/.bin/wrangler dev --local --no-bundle \
                    --ip 0.0.0.0 --port 8787 --persist-to /tmp/d1
                """,
            ]
        )
        .with_exposed_ports(8787)
        .waiting_for(LogMessageWaitStrategy("Ready on http://"))
    )
    with wasm_coverage(
        targets.workerd_container(
            app, worker_bundle, python_modules=WORKER_DEPLOYMENT / "python_modules"
        )
    ) as running:
        yield running


@pytest.fixture
def worker_url(worker_container: DockerContainer) -> str:
    host = worker_container.get_container_host_ip()
    port = worker_container.get_exposed_port(8787)
    return f"http://{host}:{port}"


@pytest.fixture(scope="session")
def docker_image() -> Iterator[DockerImage]:
    with DockerImage(
        ROOT,
        tag=f"gonghaa-test:{uuid4().hex}",
        dockerfile_path="deployments/docker/Dockerfile",
        rm=True,
    ) as image:
        yield image


@pytest.fixture
def docker_network() -> Iterator[Network]:
    with Network() as network:
        yield network


@pytest.fixture
def postgres_url(docker_network: Network) -> Iterator[str]:
    database = (
        PostgresContainer(
            "postgres:17-alpine", username="test", password="test", dbname="gonghaa"
        )
        .with_network(docker_network)
        .with_network_aliases("postgres")
    )
    with database:
        yield "postgresql://test:test@postgres:5432/gonghaa"


@pytest.fixture
def docker_url(
    docker_image: DockerImage, docker_network: Network, postgres_url: str
) -> Iterator[str]:
    app = (
        DockerContainer(str(docker_image))
        .with_network(docker_network)
        .with_env("DATABASE_URL", postgres_url)
        .with_exposed_ports(8080)
        .waiting_for(HttpWaitStrategy(8080, "/readyz"))
    )
    with app:
        yield f"http://{app.get_container_host_ip()}:{app.get_exposed_port(8080)}"


@pytest.fixture(
    params=[
        pytest.param("worker_url", id="cloudflare-d1"),
        pytest.param("docker_url", id="docker"),
    ]
)
def base_url(request: pytest.FixtureRequest) -> str:
    url = request.getfixturevalue(request.param)
    assert isinstance(url, str)
    return url
