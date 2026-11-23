# Hosting costs

Choose **Cloudflare Workers with D1** or **Docker with PostgreSQL**. The Docker
deployment runs on infrastructure you control and needs no Cloudflare account
or services. GongHaa has no software licence fee. Hosting and operating costs
depend on your deployment and workload.

## Cloudflare Workers with D1

These are estimates for one event in one active billing month. All profiles
model 100 dynamic Worker invocations per proposal across submission, review
and decisions. The busiest UTC day contains 25% of each billing metric. The
Paid estimate assumes 20 ms of CPU per invocation on average and up to 5 GB
of included D1 storage across the account.

| Profile | D1 rows read per proposal | D1 rows written per proposal |
| --- | ---: | ---: |
| Baseline | 2,000 | 50 |
| Read-heavy | 20,000 | 50 |
| Write-heavy | 2,000 | 500 |

The baseline monthly totals are below. The heavy profiles multiply the
corresponding monthly read or write total by ten.

| Proposals | Requests  | Rows read  | Rows written | Paid CPU (ms) |
| --------: | --------: | ---------: | -----------: | ------------: |
|        10 |     1,000 |     20,000 |          500 |        20,000 |
|       100 |    10,000 |    200,000 |        5,000 |       200,000 |
|     1,000 |   100,000 |  2,000,000 |       50,000 |     2,000,000 |
|    10,000 | 1,000,000 | 20,000,000 |      500,000 |    20,000,000 |

### Deadline-day usage

Free includes 100,000 Worker invocations, 5 million D1 reads and 100,000 D1
writes each UTC day. The monthly estimate below uses Free when volumes fit
those limits and Paid when they exceed a limit. [Workers pricing][workers] ·
[D1 pricing][d1]

| Proposals | Profile | Invocations | Reads | Writes | US$/mo |
| ---: | --- | ---: | ---: | ---: | ---: |
| 10 | Baseline | 250 | 5,000 | 125 | 0* |
| 10 | Read-heavy | 250 | 50,000 | 125 | 0* |
| 10 | Write-heavy | 250 | 5,000 | 1,250 | 0* |
| 100 | Baseline | 2,500 | 50,000 | 1,250 | 0* |
| 100 | Read-heavy | 2,500 | 500,000 | 1,250 | 0* |
| 100 | Write-heavy | 2,500 | 50,000 | 12,500 | 0* |
| 1,000 | Baseline | 25,000 | 500,000 | 12,500 | 0* |
| 1,000 | Read-heavy | 25,000 | 5,000,000 | 12,500 | 0* |
| 1,000 | Write-heavy | 25,000 | 500,000 | 125,000 | 5 |
| 10,000 | Baseline | 250,000 | 5,000,000 | 125,000 | 5 |
| 10,000 | Read-heavy | 250,000 | 50,000,000 | 125,000 | 5 |
| 10,000 | Write-heavy | 250,000 | 5,000,000 | 1,250,000 | 5 |

\* Free also requires each invocation to stay within its 10 ms CPU ceiling,
each D1 database to fit within 500 MB, and total D1 storage to fit within 5 GB.
The 20 ms average above applies to the Paid estimate. The read-heavy profile
at 1,000 proposals consumes the entire daily read allowance. Other events and
workloads on the same account can move any Free estimate to Paid.
[Workers pricing][workers] · [D1 pricing][d1] · [D1 limits][limits]

All three 10,000-proposal profiles fit within the US$5 Paid monthly minimum
under the model. The heaviest case for each metric reaches 1 million Worker
invocations, 20 million CPU ms, 200 million D1 reads and 5 million D1 writes.
Paid includes 10 million invocations, 30 million CPU ms, 25 billion D1 reads
and 50 million D1 writes per account and billing month.
[Workers pricing][workers] · [D1 pricing][d1]

### Paid D1 overage sensitivity

These separate account-wide examples isolate the overage from one metric.
They assume other usage stays within Paid allowances and exclude tax and
other services. [D1 pricing][d1]

| Monthly usage | Excess rows | Marginal rate | Overage | With US$5 base |
| --- | ---: | ---: | ---: | ---: |
| 30 billion reads | 5 billion | US$0.001 per million | US$5 | US$10 |
| 100 million writes | 50 million | US$1 per million | US$50 | US$55 |

D1 bills for rows scanned and can count extra writes for index updates.
During rehearsal, record `meta.rows_read`, `meta.rows_written` and Worker CPU
for each endpoint, then compare account totals and the peak day with the
model. Include every active billing month in the event budget.
[D1 billing metrics][d1] · [D1 response metadata][d1-meta]

## Docker with PostgreSQL

For each proposal scenario, budget for compute, database storage and off-site
backups. An existing host with spare capacity can have zero additional compute
cost. A new host adds its rental cost and a separate database service adds its
own charge. Measure peak throughput, CPU, RAM and disk usage in a rehearsal
to size the host for the deadline load.

For either deployment, budget separately for any domain, transactional email
and monitoring fees, plus the time spent on updates, backup restores and
incident response. Record the measured CPU, requests, database usage, storage
and cost after a rehearsal. Proposal counts alone do not establish capacity.

## Hosted and self-hosted alternatives

- **Conference Hall** describes its hosted CFP and review service as free to
  users and supported by sponsorship. It also publishes the application
  source under the AGPL. [Sponsorship][conference-hall-sponsor] ·
  [Source][conference-hall-source]
- **CFP.ninja** lists an early-adopter organiser fee of US$99 per event
  listing. The hosted plan includes proposal review, bulk email and export.
  The MIT-licensed application can also be self-hosted with PostgreSQL.
  [Pricing][cfp-ninja] · [Source][cfp-ninja-source]
- **Sessionize** is free for eligible free community events. Its professional
  plan costs US$499 plus tax per event occurrence. [Pricing][sessionize]
- **Pretalx** quotes managed hosting per event based on expected attendees
  and standard ticket price, with a community discount of up to 25%.
  Managed hosting includes maintenance and backups. Self-hosted Pretalx
  has no licence fee, and the organiser pays for infrastructure and
  operations. [Pricing][pretalx]
- **AgendaForge** lists US$2,000 per event for Core and US$4,000 for Pro.
  These plans bundle CFP and review with agenda, speaker portal and
  ticketing. Paid ticket fees can apply separately. [Pricing][agendaforge]

Academic conference tools offer another comparison for research peer review.

- **Microsoft CMT** is a free hosted service for academic and scientific peer
  review. Organisers submit a conference request, and at least one chair must
  use an eligible university email. [Service and eligibility][cmt]
- **EasyChair** is free up to 20 submissions. Its Professional tier costs
  US$3.90 per submission up to 60. The published Executive and VIP starting
  price is US$6 per submission on prepaid fixed plans, with possible volume
  discounts and a VIP setup fee. [Licence pricing][easychair]

Hosted event fees cover services beyond the infrastructure in this estimate.
For example, three months on Workers Paid at the included usage cost US$15
in base fees on a dedicated account. Compare that plus email, monitoring,
backups and operator time with the hosted fee for the same event period.
Proposal counts affect EasyChair's pricing tiers. For per-event or
attendee-based plans, use their published billing unit and eligibility rules.
Provider prices and terms checked 23 November 2026.

[workers]: https://developers.cloudflare.com/workers/platform/pricing/
[d1]: https://developers.cloudflare.com/d1/platform/pricing/
[d1-meta]: https://developers.cloudflare.com/d1/worker-api/return-object/
[limits]: https://developers.cloudflare.com/d1/platform/limits/
[conference-hall-sponsor]: https://github.com/sponsors/conference-hall
[conference-hall-source]: https://github.com/conference-hall/conference-hall
[cfp-ninja]: https://cfp.ninja/pricing
[cfp-ninja-source]: https://github.com/sreday/cfp.ninja
[sessionize]: https://sessionize.com/pricing/
[pretalx]: https://pretalx.com/p/pricing
[agendaforge]: https://agendaforge.app/pricing
[cmt]: https://cmt3.research.microsoft.com/docs/help/overview/CMT.html
[easychair]: https://easychair.org/licenses?cc=USD
