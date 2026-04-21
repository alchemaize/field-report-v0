# Part III. The Case Study

## One hundred days, thirty-five applications

Between January 6 and April 15, 2026, three founders of Alchemaize shipped thirty-five production applications using the methodology described above. Two FTE, roughly.

We hadn't named the methodology when we started. We named it after we'd watched it work enough times to trust it. The naming came in late March, after the case study was substantially complete. The methodology itself had emerged in real time in our own work starting in the fall of 2025.

This section is the evidence. It documents what we counted, what we didn't, which projects we killed, and the measurement methodology. We're doing it in public because an extraordinary claim without a counting methodology is a sales pitch, and we'd rather be boring than wrong.

## Who we are and what we had

Alchemaize was founded in August 2025 by David Kim (CEO shifting to CPO after the pivot) and Glenn Knepp (CEO/CTO after the pivot) for the purpose of building Ember, an AI-augmented reading application that shipped an MVP in December 2025. Casey Robinson joined as COO in October 2025, hired to run operations ahead of a Series A push.

Through the fall of 2025, David and Glenn's own development work was speeding up in ways neither had seen before. They were using Cursor and Kiro in the generation step, writing specifications with more precision than they were used to, and verifying output with small test harnesses they'd built along the way. By the end of December they had stopped calling what they were doing "using AI coding tools" and started calling it, roughly and informally, "the thing we are doing now."

In the first week of January, they called Casey in and asked him to try running a slice end-to-end himself. He was a non-engineer. If the thing they were calling "the thing we are doing now" could be run by Casey, then it was a methodology. If not, it was a productivity hack.

He did. The next hundred days is what we're reporting on.

During the hundred days, the founding team was:

- **David Kim.** Intent Engineer and AI Orchestrator. Shipped against the Alchemaize product portfolio and the Catalyst consulting engagement surface.
- **Glenn Knepp.** Verification Owner. Authored the acceptance-contract templates used across the portfolio. Held right of refusal on every merge.
- **Casey Robinson.** Intent Engineer. Test pilot. Shipped against TradeCodex and Finaize, the two applications the methodology was validated against first.

Combined FTE: roughly two. We were running commercial work in parallel. The AWS CATALYST partnership launched in March 2026 and the founding team was responsible for its early customer conversations. The hundred-day sprint wasn't our only activity. The 35 applications are what we shipped in the background, while the foreground was a Series-A push and a growing consulting practice.

We were in Brentwood, Tennessee; Claremore, Oklahoma; and College Station, Texas. We didn't share an office at any point during the hundred days. We haven't shared an office at any point in the company's history. We don't intend to. That fact is relevant to the methodology, and the book addresses it.

## What we counted

We counted an application as shipped if it met all of the following:

1. Deployed to a production environment accessible to end users or named pilot customers.
2. Passed at least one acceptance contract authored by the Verification Owner.
3. Used by at least one real user, internal or external, for a real task. Not a demo.
4. Version-controlled in the Alchemaize monorepo or a public GitHub repository, with auditable commit history.

We did not count:

- Internal scripts, one-off automation, or tooling written to support the 35 applications. That code exists. It isn't in the count.
- Branches that didn't merge. Early-exploration VOSes that produced code the Verification Owner rejected, and that the Intent Engineer never resubmitted, aren't counted as shipped slices.
- Projects we killed. Three applications were started and killed during the hundred days, for reasons described below. They aren't in the 35.
- Work by contractors. Alchemaize didn't use contract development during the period. The count is founding-team work only.

The 35 break down as follows:

- **12** in the Alchemaize portfolio (consumer and small-business applications): Ember, Drawer, Flipmode, Noshmode, Radient, Renew, Skipday, Starfish, TradeCodex, VisibleWealth, Yeon, and the Alchemaize marketing site.
- **11** in the Finaize suite, the cash-flow product Casey spent most of the hundred days on. Finaize ships as a suite: the web app, the mobile companion, the reconciliation engine, the bank-line ingestion service, the reporting service, several internal admin tools, and a small set of customer-facing microsites.
- **6** in the Catalyst partnership surface, the AWS-aligned consulting engagement artifacts: the assessment intake, the ROI calculator, the deal-desk automation, the customer-onboarding flow, and two partner-integration applications.
- **4** in the BoxLens / Albo / Ember-extension surface: small companion applications and experiments.
- **2** we're declining to name because they're under NDA with external pilot customers.

Of the 35, eight are fully open-source on GitHub under the Alchemaize organization. The other 27 are either proprietary production applications, under NDA, or in regulated environments that preclude source-level disclosure.

## What we killed

Three projects started, ran for a few weeks, and stopped. An honest case study has to name its failures.

**Project A: the document-processing product.** A generalized document-ingestion service we started in late January. Killed in week 5. The VOSes we wrote for the ingestion layer kept producing code that passed the acceptance contract but didn't pass any reasonable standard of user-facing behavior. We eventually realized the root cause. Our WHY sections were too abstract to be verifiable. The OUTCOME section couldn't be specified. If the OUTCOME can't be specified, the slice can't be verified, and if the slice can't be verified, CID doesn't apply. We killed it.

**Project B: the CRM integration.** A small CRM-sync utility we started in mid-February. Killed in week 8. The compliance constraints on the upstream CRM required an audit trail we hadn't built general infrastructure for. We could have built it in one sprint. We chose to defer until the Compliance-at-Generation-Time framework (Chapter 11 of the book) was production-ready.

**Project C: the deprecated internal tool.** An internal productivity tool one of us (David) had built in December 2025 under the old methodology. Rewritten from scratch in March. The rewrite shipped. The original is deprecated and off-counted. The rewrite is one of the 35. The original is not.

Two of the three kills happened because CID's verification step surfaced a problem earlier than the old methodology would have. The third was deferred, not failed. We count all three as successful applications of the methodology, not failures of it. A methodology that kills things early is doing its job.

## The productivity multiplier

The headline (two FTE, one hundred days, thirty-five applications) implies a throughput that is between one and two orders of magnitude above the industry baseline for a team this size.

We want to be careful about how we claim this number, because productivity claims are the part of industry methodology books where the most bullshit lives.

What we claim:

- Raw throughput, measured in shipped applications per FTE-day, is approximately 30x the industry benchmark we consider most defensible for this company stage (a small-team startup in the 5 to 15 FTE range). The benchmark is the DORA elite-performer baseline projected to our team size. 30x is the conservative claim.
- The 30x multiplier isn't uniform across the hundred days. The first two weeks ran closer to 5 to 8x. The last eight weeks ran closer to 40 to 50x. The average is 30x. The distribution is more informative than the average, and the book contains a full week-by-week breakdown.
- The multiplier isn't uniform across application types either. Greenfield applications ran higher multipliers than extensions of existing systems. Regulated applications ran lower multipliers than unregulated ones. The book has the full breakout.

What we don't claim:

- We don't claim 30x is replicable on day one of adoption. The pod maturity curve is real. First-pass verification rate, the most diagnostic of the four metrics, ran 30 to 50 percent in weeks one and two, and 80 to 95 percent by week eight. The multiplier follows the maturity curve.
- We don't claim 30x transfers to teams of 50 or 500 engineers. This is a small-team case study. The book addresses scaling through ELCID and is honest that the enterprise layer is the less-proven half.
- We don't claim 30x is the right multiplier for your team. It's the multiplier we measured, in our conditions, for our product mix, with our specific people. Your number will be your number. We're reporting ours.

The book's Chapter 3, The Evidence, expands this section into about 10,000 words of measurement methodology. This report compresses it to two pages. If the multiplier is the reason you picked up this report, the book is where the full counting method lives.
