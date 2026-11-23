# Control plane contract draft

The first API slice is one reusable proposal field. It gives an IaC client
enough behaviour to create a field, look it up by a predictable identifier,
detect drift, and apply the desired state on either deployment.

## Project requirements

- A control plane exposes the same HTTP API on Cloudflare Workers with D1 and
  self-hosted Docker or Kubernetes with PostgreSQL.
- Deployment tooling provisions infrastructure and runs schema migrations.
  IaC clients configure GongHaa through its HTTP API.
- Use SQLModel for persistence models and Pydantic for HTTP payloads.
- Proposal templates reference fields by URN. Publishing a template revision
  freezes the field definitions it uses. A proposal records its template
  revision so later edits preserve the form the submitter filled in.
- People sign in through social login. The provider issuer and subject identify
  a login account. IaC uses a separate service principal.
- Policies define allowed actions on resources. Roles attach policies. Grants
  assign roles to principals within a scope such as an organisation or event.
  Requests require an applicable grant and policy.

## Proposed proposal field API

An organisation key and a field key are stable lowercase slugs. The URN is
derived from them within a control-plane installation. IaC state identifies
the installation by its API endpoint and identifies the resource by its URN.

```text
urn:gonghaa:org:pyconhk:proposal-field:talk-title
```

The collection URL is `/v1/orgs/{org}/proposal-fields`. Append `/{key}` for
the canonical field URL.

- `GET` the field to read it with its `ETag`, or receive `404`.
- `GET` the collection with `?urn={urn}` for an `items` list containing the
  exact match, or an empty list.
- `PUT` the field with `If-None-Match: *` to create it. Success returns `201`
  with its `Location`. An existing field returns `412`.
- `PUT` the field with `If-Match: <etag>` to apply to the matching revision.
  Success returns `204`. A stale revision returns `412`.

The first writable field properties are `label` and `kind`, with `short_text`
as the first supported kind. The response also includes the field's `urn`.
Clients read the canonical URL after a write to get its current representation
and `ETag`. Applying identical values with the current `ETag` preserves the
revision. A write without a precondition returns `428`.
[Precondition Required][rfc6585]

The database applies the expected revision and write atomically. When a response
is lost or a precondition fails, the client reads the field again and compares
it with the desired state before retrying. [HTTP conditional requests][rfc9110]

Field requests require `proposal-field:read` or `proposal-field:write` on the
requested organisation. The first deployment can provision an IaC service
principal with only those actions for its own organisation.

## First acceptance test

Run the same HTTP cases against the Pywrangler bundle with local D1 and the
Docker image with PostgreSQL.

1. Create a field, check its URN, and resolve it through the lookup route.
2. Apply the same field again and check that `ETag` stays the same.
3. Make an actual change, then verify that a write with the old `ETag` fails.
4. Confirm a read-only principal can read the field and cannot write it.

The team still needs to settle the exact URN vocabulary, which changes to a
field definition create a new key, and how operators bootstrap their first
service principal. Template publication, social login, proposal submission and
review follow this API slice.

[rfc9110]: https://www.rfc-editor.org/rfc/rfc9110.html#section-13
[rfc6585]: https://www.rfc-editor.org/rfc/rfc6585.html#section-3
