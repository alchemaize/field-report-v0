# Part III. The Case Study

## One hundred days, thirty-five applications

Between January 18 and April 20, 2026, three founders of Alchemaize shipped thirty-five production applications using the methodology described above. Two FTE, roughly. That hundred days is the case study. It is also the second hundred days of Alchemaize, not the first, and the first hundred days are why the second ones happened.

This section is the evidence. It documents what we counted, what we didn't, which projects we killed, and the measurement methodology. We're doing it in public because an extraordinary claim without a counting methodology is a sales pitch, and we'd rather be boring than wrong.

## Who we are and what we had

Alchemaize was founded in August 2025 by David Kim and Glenn Knepp for the purpose of building Ember, an AI-augmented reading application. Casey Robinson joined as COO on October 1, 2025, hired to run operations ahead of a Series A push. By October 20 we had a four-person development team in place, three developers and an AWS solutions architect, all part-time, all comped on options and deferred contingent compensation tied to seed and Series A milestones, all holding full-time jobs at FAANG companies.

Through the fall of 2025 we built Ember the old way. Standups, sprints, retros, sprint reviews, planning. Cursor and Kiro layered on top of that methodology rather than redesigning it. The Ember web-app MVP shipped on December 1, 2025. The user-acquisition story did not follow. The product worked beautifully on Project Gutenberg titles, and the audience the user-acquisition story depended on wanted commercial fiction (Harry Potter, Fourth Wing, the books actually being read), and DRM made that catalog inaccessible to us without a Kindle integration we had not yet been able to start a conversation about. By the end of December the development team was wound down. The first hundred days of Alchemaize, October 1, 2025 through January 9, 2026, ended with a finished MVP that could not yet sell at the scale we needed and a clear answer that the methodology we had been operating under was not going to make the company's future.

In the second week of January, the three of us concluded that we had to fundamentally change how Alchemaize worked. We named the new approach Continuous Intent Delivery. On January 18, 2026, we drew a line in the sand. The pod was the three founders. No development team, no architect. Three people, three states, three home offices.

Ten days later, on January 28, 2026, at four in the morning Central time, Amazon issued a company-wide reduction in force. Sixteen thousand Amazonians received notification of position elimination, with a 90-day notification period. David's entire team of fourteen, including Casey, who led a sub-team within David's broader org, and including David, was hit. The methodology we had agreed to test ten days earlier became, in the space of one morning, the only work either of them had in front of them. The next hundred days is what we're reporting on.

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
- **11** in the Finaize suite, the modernized Auto F&I product Casey spent most of the hundred days on. Finaize ships as a suite: the web app, the mobile companion, the deal-structuring engine, the lender integration service, the reporting service, several internal admin tools, and a small set of customer-facing microsites.
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
