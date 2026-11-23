# GongHaa pilot proposal

GongHaa gives conference teams a CFP they can run, hand over and move. The
pilot covers one event on Cloudflare Workers with D1 or independent Docker
with PostgreSQL. An organiser can review configuration changes in Git and
apply the same event setup on either deployment.

## When Sessionize already fits

Sessionize offers its full Community License to events with free admission,
attendance and speaking applications open to everyone, and unpaid volunteer
organisers. Its published exclusions include private, promotional,
for-profit, corporate-run and professionally managed events. Create and
describe the event, then submit the licence request for manual approval.
Sessionize may make exceptions for a symbolic fee. A standard ticket under
US$50 per participant is eligible for a discount enquiry. The Professional
list price is US$499 plus tax per event occurrence.
[Community License][sessionize-community] · [Pricing][sessionize-price]

Sessionize handles CFPs, evaluation and scheduling as a managed service. It
can duplicate a prior event's CFP and settings and carry over selected team
members with their roles. The exports cover sessions, speakers, evaluations,
comments, schedules and uploads. The per-event DPA addresses controller and
processor responsibilities. [Event duplication][sessionize-copy] ·
[Exports][sessionize-export] · [DPA][sessionize-dpa]

## Where GongHaa has to earn its place

- **Configuration handover.** Sessionize documents an event API for reading
  data. GongHaa's target is to apply the event, form versions and scoped
  reviewer grants from Git, repeat the apply without changes and detect drift.
  [Sessionize API][sessionize-api]
- **Provider exit.** A second organiser can take a private event archive and
  restore it onto an independent installation. Published decisions, proposal
  revisions and template history survive the move. Access is verified again
  at the destination.
- **Cost and operating effort.** Compare the licence, infrastructure, email,
  backups and team time over the active event period. Compare the hosted
  option the event qualifies for, including a free plan where applicable.
  The [hosting model](hosting-cost.md) separates submission counts from the
  read and write workload.

## Privacy and security requirements

Use private-by-default proposals and reviews. Publish only the fields chosen
for the public programme. Apply event-scoped access, require a second factor
for global administrators and use scoped automation credentials. Record
admin, export and grant activity without logging proposal text or secrets.

The organiser can set retention periods, handle an applicant's access or
correction request and carry out approved erasures. An applicant request and
a full event migration have different scopes. GDPR Article 20 covers
qualifying data provided by the individual, where processing is automated
and based on consent or contract. A full event archive is a GongHaa product
commitment. [GDPR][gdpr] · [EDPB guidance][data-rights]

GongHaa aims to help organisers meet applicable obligations under GDPR and
Hong Kong's PDPO. Organisers decide their purposes, legal basis, notices,
retention, processors and transfer safeguards. The deployment guide should
identify where the database, logs, backups, email and identity providers
handle data so an organiser can make those decisions.
[GDPR][gdpr] · [PCPD systems design guidance][pcpd]

## Pilot acceptance

Have a second organiser use the repository to set up a synthetic conference,
accept a proposal and assign a review. Repeat the apply, then restore the
event archive from D1 to a fresh PostgreSQL installation. Verify the records
and publication state, reapprove destination grants and confirm another event
cannot access the archive. Record setup and handover time alongside cost.
The [control plane contract](control-plane.md) describes the exit checks.

[sessionize-community]: https://sessionize.com/playbook/overview/community-license
[sessionize-price]: https://sessionize.com/pricing/
[sessionize-copy]: https://sessionize.com/playbook/organizers-multiple-events
[sessionize-export]: https://sessionize.com/playbook/using-data
[sessionize-dpa]: https://sessionize.com/trust/dpa
[sessionize-api]: https://sessionize.com/playbook/api/
[gdpr]: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/
[data-rights]: https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en
[pcpd]: https://www.pcpd.org.hk/english/resources_centre/industry_specific/files/publication.pdf
