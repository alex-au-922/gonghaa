# GongHaa · 講吓

<!-- markdownlint-disable MD033 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/gonghaa-reverse.svg">
  <img alt="GongHaa" src="assets/gonghaa.svg" width="320">
</picture>
<!-- markdownlint-enable MD033 -->

> 有個 idea？不如講吓。

GongHaa is being developed as a **free and open-source software (FOSS) project**
for community conferences. It aims to provide self-hostable call for proposals
(CFP) and review software for volunteer organisers who want to reuse a
submission form, give reviewers access to the right event, and hand a working
setup over to the next team.

The first goal is to run a conference CFP and review cycle affordably.
Deploy to **Cloudflare Workers with D1** or self-host independently with
**Docker and PostgreSQL**. The self-hosted option needs no Cloudflare account
or services.

The [hosting cost model](docs/hosting-cost.md) covers 10 to 10,000 proposals.
See the [GitHub Project][roadmap] for milestones and acceptance criteria.

## Status

GongHaa is in early development. The first implementation is `GET /readyz`,
which runs `SELECT 1` against the deployment's database. The planned first
CFP workflow takes one event from configuring a versioned form to accepting
or rejecting submissions. The [control plane contract draft](docs/control-plane.md)
describes the first proposal field API for review.

Each deployment defines its FastAPI app in its Python entry point. Both share
the readiness response model in `src/gonghaa/`.

- [`deployments/cloudflare-d1/`](deployments/cloudflare-d1) runs the Python
  Worker and its D1 database in Wrangler's local runtime.
- [`deployments/docker/`](deployments/docker) builds the application from
  source and connects to PostgreSQL. Kubernetes is a planned deployment target.

## Development

Install [mise](https://mise.jdx.dev/getting-started.html) and run these commands
from the GongHaa project directory. The test environment installs the released
[`coverage-wasm`](https://pypi.org/project/coverage-wasm/) package from PyPI.

```sh
mise install
mise run test
```

Start a Docker daemon before running the suite. Pytest runs the same HTTP
readiness test against the Workerd bundle with local D1 and the Docker image
with PostgreSQL. The Worker fixture builds the bundle with
`pywrangler deploy --dry-run` and starts it with Wrangler.

Collect Worker coverage and generate `htmlcov/index.html` with this command.

```sh
mise run test -- --cov --cov-report=html
```

Both readiness tests run. The report measures the D1 Worker and shared
GongHaa source exercised in Workerd. The Docker/PostgreSQL case verifies
readiness over HTTP.

GitHub Actions runs both readiness cases and saves the Worker HTML report.
As CFP features land, each shared HTTP scenario will exercise both deployments.
Pytest fixtures own setup and teardown, and the tests show each API call and
assertion in order.

[`mise.toml`](mise.toml) pins the toolchain. `uv.lock` locks `workers-py` and
`workers-runtime-sdk`. The Cloudflare deployment locks Wrangler in
`package-lock.json`.

Run `mise run lint:markdown` to check the Markdown documentation.

## Contributing

If you organise a community event, share where you spend time setting up
a CFP, coordinating reviewers, or handing over to the next organiser.
Examples from real events help us prioritise the first workflow.

## License

GongHaa is available under the [MIT License](LICENSE).

[roadmap]: https://github.com/users/alex-au-922/projects/1/views/1
