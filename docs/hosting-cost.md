# Hosting costs

Choose **Cloudflare Workers with D1** or **Docker with PostgreSQL**. The Docker
deployment runs on infrastructure you control and needs no Cloudflare account
or services. GongHaa has no software licence fee. Hosting and operating costs
depend on your deployment and workload.

## Cloudflare Workers with D1

These are estimates for one event in one active billing month. Each proposal
stands for 100 dynamic Worker requests, 2,000 billed D1 rows read and 50 billed
D1 rows written across submission, review and decisions. We model 25% of each
in the same deadline day. For Workers Paid, we assume an average of 20 ms of
CPU per request and up to 5 GB of included D1 storage across the account.

| Proposals | Requests  | Rows read  | Rows written | Paid CPU (ms) |
| --------: | --------: | ---------: | -----------: | ------------: |
|        10 |     1,000 |     20,000 |          500 |        20,000 |
|       100 |    10,000 |    200,000 |        5,000 |       200,000 |
|     1,000 |   100,000 |  2,000,000 |       50,000 |     2,000,000 |
|    10,000 | 1,000,000 | 20,000,000 |      500,000 |    20,000,000 |

| Proposals | Deadline requests | Deadline reads | Deadline writes |
| --------: | ----------------: | -------------: | --------------: |
|        10 |               250 |          5,000 |             125 |
|       100 |             2,500 |         50,000 |           1,250 |
|     1,000 |            25,000 |        500,000 |          12,500 |
|    10,000 |           250,000 |      5,000,000 |         125,000 |

- **10, 100 or 1,000 proposals:** US$0 on Free if each Worker invocation fits
  its 10 ms CPU limit and the account stays within all Free limits. The
  modelled counts fit the daily request and row limits. Otherwise, budget
  US$5 on Paid if usage fits its included allowances.
- **10,000 proposals:** US$5 on Paid under the model. The deadline day exceeds
  Free's 100,000 daily requests and 100,000 daily writes. Reads reach its
  5 million daily limit. The monthly totals fit Paid's 10 million requests,
  30 million CPU ms, 25 billion rows read and 50 million rows written.

The 20 ms CPU assumption applies to the Paid estimate. Free also caps each D1
database at 500 MB, with 5 GB across the account. Paid's US$5 monthly minimum
and usage allowances are shared across the account. Include other workloads
on that account and every billing month the event is active in your estimate.
[Workers pricing][workers] · [D1 pricing][d1] · [D1 limits][limits]

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
