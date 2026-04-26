---
title: "Field Report from the First Hundred Days"
subtitle: "What happened when three founders stopped building software the old way"
author: "David Kim, Casey Robinson, Glenn Knepp"
date: "April 2026, v0.1 draft"
---

\newpage

# Field Report from the First Hundred Days

**What happened when three founders stopped building software the old way.**

David Kim, Casey Robinson, Glenn Knepp

Alchemaize

v0.1, April 2026 draft. Pre-release. Do not cite as final.

\newpage

## About this document

*Field Report from the First Hundred Days* is a free, roughly sixty-page artifact released ahead of our full-length methodology book, *Continuous Intent Delivery*, currently in publisher discussions. It exists because the methodology is moving faster than the publishing industry, and we didn't want to wait eighteen months to start the conversation.

What's in it.

First, it names the methodology, Continuous Intent Delivery (CID for short), and describes it in enough depth that a reader can argue with it. Not enough to run it inside an enterprise.

Second, it documents the 100-day case study that produced the methodology. What we built, what we counted, what we killed, what we got wrong.

Third, it includes a teaser of Chapter 1 of the book, and three sections of Chapter 8 in Casey's voice. Chapter 8 is the chapter non-engineering readers are most likely to want first.

Fourth, it answers the questions we've been asked a hundred times, and is honest about the places the methodology is still uncertain.

What's held back. The enterprise layer, the compliance framework, the full adoption path, and the four appendices are in the book. This report gives away the argument and the evidence, not the full toolkit. If the argument lands, the book is where the rest of the work lives.

The report is pay-what-you-like on Leanpub (minimum zero), mirrored on GitHub under CC BY-NC-SA, and linkable from `alchemaize.ai/field-report`. Typos and factual corrections via pull request. Structural feedback goes to the GitHub issue tracker, or directly to the three of us.

We founded Alchemaize in August 2025 to build Ember, an AI-augmented reading application. David is in Brentwood, Tennessee. Casey in Claremore, Oklahoma. Glenn in College Station, Texas. We've never shared an office. We don't plan to.

DK, CR, GK
April 2026

\newpage

# Part I. The Manifesto

## The Shift, in three hundred words

For twenty-five years, every method we have used to build software at scale has rested on the same assumption. Humans are the bottleneck at the implementation step. Typing code is slow, expensive, and error-prone, and a framework's job is to coordinate the humans who are doing it.

Waterfall, Scrum, XP, Kanban, SAFe, DevOps, Continuous Delivery. All of them are careful answers to that same question. Typing is expensive; how do we organize around that fact?

The question stopped being the right one sometime in the last two years, and most of the industry has not yet noticed.

AI code generation has compressed the typing step by one to two orders of magnitude. The expensive work is now on either side of it. Intent, meaning the specification of what the software should actually do, written with enough precision that a machine can act on it. Verification, meaning the confirmation that the code that shipped does what was specified. The bottleneck did not disappear. It moved to both ends at once.

The consequence is harder to sit with than the observation. Every framework currently in use at your company was built for a bottleneck that is no longer where the framework assumes. The coordination machinery that was reasonable when typing was the long pole has become friction. That is not an insult to the frameworks. They answered the question they were asked. Someone else started asking a different one.

This report names what replaces them. The methodology is Continuous Intent Delivery, CID for short. Humans specify. Humans verify. The machine writes the code. A small role-structured team runs a five-stage loop over a unit of work called a Verifiable Outcome Slice. Scaling the loop is a separate problem with a separate answer, and that answer is most of the book.

The argument is in the pages in your hands. The evidence starts on the next one.

DK

\newpage

# Part II. How CID Works

## What this part is for

The rest of Part II describes CID in enough depth that you can argue with it. It introduces the three roles, the five-stage loop, the unit of work, and the four metrics that replace the velocity dashboard. It doesn't give you enough to run the methodology inside an organization. That's in the book.

The asymmetry is deliberate. An argument has to be made in public. The practice of running a method has to be taught carefully. This report does the first. The book does the second.

## The five-stage loop

CID is a loop, not a sprint. There's no fixed cadence. It runs at the pace verification allows.

**1. Intent.** A human, the Intent Engineer, writes a specification of what should be built. The specification is a VOS, a Verifiable Outcome Slice, and it's the unit of work in the methodology. A VOS has five sections: WHY, WHAT, HOW, CONTEXT, OUTCOME. We describe them below.

**2. Context.** The Intent Engineer curates four to fifteen files from the existing codebase that matter for the slice. This isn't a prompt. It's a reading list. The skill of choosing the right files, in the right configuration, is the single largest determinant of AI output quality in the methodology. More than the prompt. More than the model.

**3. Generation.** The AI Orchestrator hands the VOS plus the curated context to a generation layer (Claude, GPT, Cursor, Kiro, whatever the team has chosen) and watches the run. The AI Orchestrator's job isn't to type. It's to manage the generation session, catch drift, redirect on misinterpretation, and throw a slice out and restart if the generation heads somewhere wrong.

**4. Verification.** The Verification Owner runs the acceptance contract from the VOS against the generated code. The contract is executable. It either passes or it doesn't. If it doesn't, the slice goes back to the Intent Engineer with notes. The Verification Owner doesn't report to the delivery chain. Their job is to say no.

**5. Observation.** The slice ships. Production telemetry confirms, or fails to confirm, that the outcome described in the VOS was actually produced for real users. Observation loops back into intent, closing the slice or opening a new one.

The loop is continuous. It doesn't run once per sprint. It runs as fast as the verification step can be honored, typically several slices per day per Intent Engineer once the pod has matured.

## The three roles

CID has three roles at the team layer. Each can be held by a different person. On a small team, one person holds two or three. In the case study this report documents, two founders (David and Casey) held two roles each, and Glenn held the third.

**Intent Engineer.** Writes the VOS. Curates the context. Doesn't need to know how to code. Does need to know what the business needs software to do, and how to say it with a precision that can't be misread. In the case study, Casey is the Intent Engineer. He has never written a line of production code.

**AI Orchestrator.** Runs the generation session. Manages model behavior. Catches drift, restarts runs, and escalates to the Intent Engineer when the VOS itself is wrong. Usually an engineer, because the role benefits from knowing what good code looks like, but the role doesn't produce code. It produces generation sessions that yield verifiable code.

**Verification Owner.** Owns the acceptance contract. Blocks what doesn't pass. Writes the parts of the contract the Intent Engineer's domain knowledge can't supply: non-functional requirements, security constraints, compliance gates. In the case study, Glenn is the Verification Owner. He's a career software engineer, and the contract-authoring half of his role has replaced most of the direct-coding half.

The three roles map onto the three steps that got dominant when typing got cheap. Intent Engineer owns intent. Verification Owner owns verification. AI Orchestrator sits between them and makes the machine do the step that used to be human.

## The Verifiable Outcome Slice (VOS)

The VOS is the unit of work. It replaces the story, the ticket, the feature, the user-story-with-acceptance-criteria, all of which presupposed that typing was the long pole. A VOS has five sections.

**WHY.** Two to four sentences. What the slice is for. Written in business language. The Intent Engineer's mandate.

**WHAT.** The acceptance contract. Written in Gherkin, a small specification language that reads like English but is executable. The WHAT is the section that matters most. If the WHAT is right, the rest of the slice usually works. If the WHAT is vague, the slice produces plausible but wrong code.

**HOW.** Three to five lines of design-level decisions. Which existing components the slice plugs into. What gets reused. What gets extended. The HOW is the AI Orchestrator's section. It keeps the generated code consistent with existing architecture.

**CONTEXT.** The four to fifteen files the generation session should read before generating. Not the whole codebase. Not the database schema. Just the files that matter for the slice.

**OUTCOME.** The production signal. One sentence describing what will be observable in telemetry or user behavior if the slice succeeds. Observation watches for this.

We include one full worked VOS (the cash-flow reconciliation slice Casey shipped on Finaize) in Part IV. The book has ten more and an appendix of templates.

## The four metrics

CID replaces the velocity dashboard with four numbers. A CTO or VP of Engineering can read the entire engineering organization in thirty seconds using them. We introduce the four briefly here; the book walks through the diagnostic combinations.

**1. Cycle time.** Time from VOS written to slice shipped to production. In the case study, cycle time ran roughly 4 to 18 hours for team-owned slices, and 1 to 4 days for the handful of slices that required deep architectural work.

**2. First-pass verification rate.** Percent of slices that pass the acceptance contract on the first generation attempt. This is the single most diagnostic number in the methodology. Low first-pass rate means vague VOSes, weak context curation, or both. High first-pass rate means the pod is mature. In our case study, this number ran 30 to 50 percent in the first two weeks and rose to 80 to 95 percent by week eight.

**3. Outcome KPI delta.** Change in the business metric the OUTCOME section predicted, measured against a baseline. This is the number a CEO cares about. It's also the only one of the four that measures whether the methodology is producing value rather than throughput.

**4. Cost per shipped intent.** Total cost (people, inference, infrastructure) divided by the number of VOSes that shipped and passed observation. Inference cost is usually a decimal point on this number. The other costs are where the real math lives.

No velocity. No burndown. No story points. Four numbers, reviewed once a month for ninety minutes. The book has a full chapter on the monthly review.

\newpage

# Part III. The Case Study

## One hundred days, thirty-five applications

Between January 6 and April 15, 2026, three founders of Alchemaize shipped thirty-five production applications using the methodology described above. Two FTE, roughly.

We hadn't named the methodology when we started. We named it after we'd watched it work enough times to trust it. The naming came in late March, after the case study was substantially complete. The methodology itself had emerged in real time in our own work starting in the fall of 2025.

This section is the evidence. It documents what we counted, what we didn't, which projects we killed, and the measurement methodology. We're doing it in public because an extraordinary claim without a counting methodology is a sales pitch, and we'd rather be boring than wrong.

## Who we are and what we had

Alchemaize was founded in August 2025 by David Kim and Glenn Knepp for the purpose of building Ember, an AI-augmented reading application that shipped an MVP in December 2025. David and Glenn have known each other since 1996, having served together in the United States Marine Corps. Casey Robinson joined as COO in October 2025, hired to run operations ahead of a Series A push.

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

\newpage

# Part IV. One Worked VOS

## The cash-flow reconciliation slice

To show what a VOS actually looks like, we reproduce one here in abbreviated form. It's a VOS Casey wrote in late February, against the Finaize application, for a feature called Cash Flow Projection Bank-Line Reconciliation.

The WHY and WHAT are reproduced in full. The HOW, CONTEXT, and OUTCOME are summarized. The full VOS, including the thirty-line Gherkin acceptance contract, is in Appendix B of the book.

---

**VOS-FNZ-087. Cash Flow Projection Bank-Line Reconciliation.**

*Intent Engineer: Casey Robinson. Verification Owner: Glenn Knepp. AI Orchestrator: David Kim. Authored 2026-02-24. Shipped 2026-02-27.*

### WHY

A small-business owner relies on this application to tell them whether they'll have money for payroll on the fifteenth. If the categorized view of the month disagrees with the bank-line total, even by a cent, the owner is being told something false, and we've failed the most basic job the product has. This slice ensures we either show a reconciled projection or refuse to show a projection at all.

### WHAT

The acceptance contract is written in Gherkin. A condensed version:

```gherkin
Feature: Cash-flow projection must reconcile with bank-line totals

  Scenario: Reconciled month displays projection
    Given a categorized month with transactions totaling $X
    And a bank-line total of exactly $X for the same month
    When the projection is requested
    Then the projection is displayed
    And the reconciliation badge shows "Reconciled"

  Scenario: Unreconciled month shows error, not projection
    Given a categorized month with transactions totaling $X
    And a bank-line total of any value not equal to $X for the same month
    When the projection is requested
    Then the projection is NOT displayed
    And the error banner displays "Some transactions could not be reconciled"
    And the banner offers a link to "Review uncategorized transactions"

  Scenario: Reconciliation is accurate to the cent
    Given any categorized month
    When the reconciliation check runs
    Then the check passes only if categorized total equals bank-line total
      exactly, with no tolerance
```

### HOW (summarized)

Use the existing transaction-categorization pipeline. Add a reconciliation step at the pipeline's tail. Surface the error state through the existing error-banner component. No new UI components.

### CONTEXT (summarized)

Four files:

- `lib/finaize/categorize.ts`, the transaction categorization module.
- `components/finaize/ProjectionDisplay.tsx`, the projection display component.
- `components/ui/ErrorBanner.tsx`, the error-banner component.
- `lib/finaize/aggregate.ts`, the monthly aggregation utility.

### OUTCOME (summarized)

Reconciliation-failure rate visible to users drops to zero over the next billing cycle, because any projection we can't reconcile, we don't show. Support-ticket volume for reconciliation-related issues drops by at least 80 percent week over week.

### What happened

The system generated the code in about six minutes. The pull request passed all unit tests on the first run, and passed the acceptance contract on the first run. Glenn signed the contract. The slice deployed to production on Thursday, February 27, around 3pm Central. On Friday the 28th, the support team reported zero new reconciliation-related tickets for the first time in a rolling seven-day window. The OUTCOME prediction held.

Casey's description of writing this VOS, and of realizing that the skill required was one he'd been practicing for twenty years in other jobs, is in Section 3 of the Chapter 8 excerpt in Part VI.

\newpage

# Part V. Chapter 1 Teaser

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 1:* The Shift. *Primary author: David Kim. This excerpt runs about 3,000 words, roughly the first half of the chapter. The full chapter runs about 6,850 words, closing with a Field Note in Casey's voice.*

---

## The Shift

In February of 2026, in a converted den on the ground floor of a house in Claremore, Oklahoma, Casey deployed his forty-second Verifiable Outcome Slice of the quarter. He was two states away from Glenn, five hundred miles from me, and not in a shared building with either of us. He had been at his desk for about five hours. The house was quiet. The code that shipped, across three files in an application called Finaize, was going to serve real users the following morning.

Casey is the third author of this book. He wasn't a software engineer, in any sense the industry would have recognized in 2025. His career is customer service, operations, consulting, and Agile program management, carried over two decades. Immediately before Alchemaize he spent a year at Amazon Web Services at the Senior Manager level, leading a team of Customer Solutions Managers, the people who guide enterprise customers through cloud migrations. He had never written a line of production code in his working life. He was hired as COO in October 2025 to help us get ready for a Series A raise, anticipated on the back of our reading application, Ember, launching its MVP. He wasn't hired to ship software. Nobody expected him to.

Then January came. Glenn and I had spent the preceding fall watching our own development work speed up by an order of magnitude under a way of building software we didn't yet have a name for. By early January we'd decided the company was going to stop building the old way. We had a claim we couldn't verify yet: that a person whose career is about clarifying intent, not implementing it, could ship production software directly under the right framework. Casey was the non-engineer among the three of us. We asked him to try.

He did. He didn't fail. In the hundred days between January 6 and April 15, 2026, Casey shipped dozens of VOSes against production code across two products, TradeCodex and Finaize, without Glenn or me touching the code that came out of his work. That fact is one of the three reasons this book exists.

This chapter is about what had to be true for that fact to be possible.

---

It is also a book about the thing that fact implies, which is that a twenty-five-year consensus about how software gets built is over. We'll spend the next 80,000 words making that case. First as an argument, then as a methodology, then as a set of enterprise practices, and last in a chapter Casey wrote himself, as a lived experience. By the end we'll have done something the current literature on AI and software development has not yet done. We'll have described what replaces Scrum.

I want to say that plainly before we go further, because a lot of what follows depends on it. This book is not *AI and Agile, together at last*. It is not *how to add prompt engineering to your sprint*. It is not one of the many books being written right now about how to use AI coding tools inside an otherwise unchanged engineering practice. Those books have their place. This is not that book.

The argument in your hands is that the engineering practice itself has to change, because the constraint it was designed for is gone, and the constraint it now faces is not one any existing framework was built to hold.

That sentence is the whole claim. The case for it takes a chapter. What to do about it takes the rest of the book.

## The bottleneck moved

For twenty-five years, every method for building software at scale has been organized around a single assumption. The assumption was that humans are the bottleneck of the implementation step, that typing code is the expensive, slow, error-prone activity, and that the job of a framework is to coordinate humans around that expensive activity so their typing-output gets used well.

Every framework you know, descended from every framework that preceded it, is a solution to this problem. Waterfall said plan exhaustively up front, because the typing is the long pole and mistakes are expensive to rewrite. Scrum sliced the work into two-week increments, because the typing was still the long pole but requirements changed faster than the plan. Extreme Programming paired the typists so they caught each other's errors in real time. Kanban limited concurrent typing so throughput didn't collapse under context-switching. SAFe coordinated large groups of typists at ten-week resolution so the organization could plan. DevOps automated everything around the typing that wasn't typing, so the typists could concentrate on the typing. Continuous Delivery declared that the typing was fine; what happened after the typing was broken.

Every one of those frameworks is a rational, careful, well-engineered answer to a single question. Typing is expensive. How do we organize an organization around that fact?

The question has changed.

It's not that AI has made typing free, though in some meaningful sense it has. It's that the step between the human specification and the running code, the step we used to call implementation or coding or, on a bad day, cutting the ticket, has become, in the hands of a competent operator, roughly the cheapest step in the pipeline. Cheapest is a specific claim. It isn't a claim about clock time (some generation runs are slow). It's a claim about where the constraint now sits: somewhere else entirely. The step isn't worth organizing around.

It isn't precisely free, of course. There are still costs: model-inference costs, verification costs, operator costs, the real cost of the time it takes to write the specification well. But those costs aren't typing costs. They're the costs of the other steps, steps that used to be cheap relative to typing because typing dominated them. When the dominant cost is removed from a system, the structure of the system does not stay the same. It shifts, all at once, to fit the new dominant cost.

The new dominant cost is two things, not one. They sit on either side of the old bottleneck.

The first is *intent*. Specifying, unambiguously and completely enough that a machine can act on it, what you actually want the software to do. In the old world we called this requirements engineering and treated it as a ten-percent activity because typing was the ninety-percent. In the new world, intent clarity is the dominant input to output quality. If you're any good at this work now, you've already noticed it. The difference between an AI tool that does what you wanted and an AI tool that does some plausible thing you did not want is almost always a difference in the specification going in. There's no prompt-engineering trick that compensates for intent that was vague from the start. you wanted is almost always a difference in the specification going in. No prompt-engineering trick compensates for intent that was vague from the start.

The second is *verification*. Knowing, with reasonable confidence, that the code you shipped does what you intended it to do. In the old world we called this quality assurance and treated it as a downstream activity because typing was the expensive middle. In the new world, verification is the structural guarantee of the whole pipeline. If you cannot verify, you cannot ship at any speed, because shipping unverified AI output is a distinct and self-amplifying form of disaster, one this book will name specifically in a later chapter.

The bottleneck didn't go away. It moved. The typing step got cheap. The intent step and the verification step got dominant.

The implication, if you let it land, is that every framework currently in use at your company was designed for a bottleneck that no longer exists. That's a structural observation, not a polemical one. The thing Scrum's machinery is best at, coordinating the cost of human typing across a sprint, is no longer the cost that matters. The thing SAFe's machinery is best at, coordinating hundreds of human typists at ten-week resolution, is coordinating something that doesn't need to be coordinated anymore. Not as a criticism of the typists. As a statement about who's typing, which is now the machine.

The frameworks have become friction.

That's the observation the rest of the book rests on. Everything that follows, the methodology, the roles, the metrics, the adoption path, is an attempt to answer the question that opens up once you accept it. What should we build our organizations around instead?

## A concession before we continue

The sentence "the frameworks have become friction" can sound glib, and I've been in this industry long enough to know what happens when a new methodology talks about the old one that way. A third of readers stop reading, because they've heard this kind of thing three times this year already. Another third reads defensively. The last third reads eagerly, waiting for permission to say what they already thought. I don't want any of those three readers right now. I want the reader who's willing to judge the claim on its merits.

So let me be fair to the frameworks we're about to name. Scrum was a reasonable solution to a real problem. SAFe was a reasonable scaling of that solution to larger organizations. The individual practices these frameworks advocated, the standup, the retro, the sprint review, the Program Increment, were not absurd. These were, and in many contexts still are, the best answer a careful engineering culture ever gave to the question of how to organize humans whose typing was the long pole.

The criticism isn't that the frameworks were wrong then. The criticism is that the condition they were designed for is no longer the condition we're in. A design rational for one constraint becomes an impediment under a different constraint. That's how engineering works. That is, for that matter, how software works.

So when the next chapter takes a scalpel to the specific thirty-two hours of ceremony a Scrum team currently pays per sprint, and demonstrates that the same coordination function can be accomplished in thirty minutes per week under the new constraint, please read that chapter the way I intend it. Not as a criticism of Scrum the framework, but as a description of the structural cost of running a machine calibrated for one constraint in a world that has moved to another.

The book isn't gleeful about this. The book is trying to be right about it.

## The new constraint and what it demands

If the bottleneck has moved to intent and verification, then a method for building software at scale under the new constraint needs to be organized around those two things. That's the whole design brief. The rest is details.

One useful way to see what this looks like in practice is to notice what has not changed.

Business outcomes haven't changed. You still need to know what you're trying to build and why. What has changed is that you now need to write that down with more precision than you used to, because something is going to act on it without the soft rails of a twenty-year-old engineering team's shared context. The intent specification is no longer a communication artifact between humans who already know most of the answer. It's a real input to an actor that does not know the answer and will act on whatever you give it.

Users haven't changed. You still need to verify that what you built works for them. What has changed is that you now need to verify more, and earlier, and continuously, because the output is arriving faster than any QA process designed for human-speed generation can keep up with. The verification step hasn't been bypassed. It's been inverted. Brought upstream of generation, made continuous, made the structural guarantee rather than the downstream check.

Organizations haven't changed. You still need to decide what you're going to fund and why. What has changed is that the unit of funding, the project, with its fixed scope and schedule and deliverable, was an instrument for a world in which humans were the constraint and scope was negotiable. The new constraint asks for a different instrument.

The methodology you'll meet in the next chapters takes those three observations and builds from them. It's called Continuous Intent Delivery. CID at the team layer. ELCID at the enterprise layer. The chapters to come will explain what that means, how it works, what it costs, and how you adopt it. But the central design move is already visible. The methodology is organized around the things that have become dominant: intent clarity, verification rigor, and outcome-based funding. It's not organized around the thing that became cheap, which is typing.

The shortest way to say this: *intent is the artifact, code is the exhaust.*

I need to be precise about what that means, because the sentence does a lot of work and will show up in later chapters more than once. It does not mean code is unimportant. Of course code is important; it's what runs. It means something specific. The artifact that humans should author, version, review, argue over, maintain, and treat as the organization's durable knowledge is the *specification of intent*, not the generated implementation. The code is what comes out the other end when the specification is right. The code is, in a reasonable sense, the predictable output of a well-run pipeline, not the creative output of a human act.

---

*Excerpt ends. The full chapter continues through "The proof that the inversion holds," "A quick definition, and then the road map," "A note from the Verification Owner" (Glenn's voice), "Who this book is for," and "The road ahead," closing with Casey's Field Note. Available in the full-length book.*

\newpage

# Part VI. Chapter 8 Excerpts (Casey's Voice)

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 8:* Field Report from the Test Pilot. *Primary author: Casey Robinson. Full chapter runs 7,500 to 8,500 words in the book. This excerpt reproduces Sections 1, 2, and 4 at compressed length, preserving the full voice.*

---

## 1. Who I am and what I'm not

Being from Oklahoma and a big sports enthusiast, I often get looked at as a retired football player more than a consultant or even a technologist. Standing at six foot two and a big frame, I'm often caught out on a football field somewhere coaching in my free time. That's relevant context, not a joke. When I walk into a meeting with David, the people in the room sometimes assume he's the consultant and I'm his security detail. The assumption's reasonable if all you have to go on is the way I look. I mention it because what I'm going to tell you in this chapter is that the thing I do for a living now is author the specifications for production software that runs against real customer data. If you'd told me on the day I was brought into Alchemaize that this would be part of my job, I'd have laughed, and then looked at how I can share knowledge or help streamline processes for operations.

The actual job I was brought in for was to become the Chief Operations Officer. Supporting a startup that was aspirational in looking to build a product called Ember, an AI-augmented reading application. My background is not in engineering or anything related to building a codebase or deploying infrastructure. Even though I was working for one of the biggest cloud providers, my roles were more akin to consulting, customer service, operations, and Agile delivery, carried for long enough that it's the shape my career has. For four years immediately before Alchemaize I was at Amazon Web Services, at the Senior Manager level, leading a team of Customer Solutions Managers. If you haven't encountered that role before, a Customer Solutions Manager at AWS is the person who stands in the seam between an enterprise customer and the technical capability they're trying to adopt. You guide the migration. You hold the plan together. You translate between the customer's internal politics and the technology's actual shape. You do a great deal of it in Agile ceremonies, because that's the format enterprise delivery has mostly settled into. You don't write production code. That was my world for the immediate stretch before this one, and variations of it have been my world for most of my working life.

I say all that so the rest of the chapter lands cleanly. I've been in software-delivery rooms for over twenty years. I've run Agile programs. I've written requirements, backlogs, acceptance criteria, operating playbooks, and the kind of customer-facing documentation that has to survive a lawyer reading it. What I've never done, in any of those rooms, is write code. Not a little on the side, not as part of any technology implementations, none developed in my career. I can discern how technology supports a customer, I can explain it, but the under-the-hood interworkings to make it work is like a foreign language to me. What I can't do is type the fix. The twenty years of enterprise-delivery rooms sharpened the first skill without ever teaching me the second one, and until January I'd thought of that as a ceiling.

I didn't come to Alchemaize planning to be anything other than the person who kept the company's operations intact while everyone else focused on building Ember. That was the plan when I was hired. Plans change and evolve. What happened instead was a change in what a certain kind of operational person can credibly do at work. The change is less dramatic than it sounds, and it's at the same time the most consequential professional thing that has happened to me.

And here's the fact this chapter is in the book to explain. In the hundred days covered by this book, I personally shipped production code, first on an app called The Trade Codex, then moved on to build Finaize, a modernized Auto F&I web app with a mobile companion, without David or Glenn touching the code I shipped. I did it under a methodology we created and evolved and had been building but hadn't yet named; the naming came after they watched me do it repeatedly. The methodology is what the rest of the book is about. This chapter is what it looked like from where I was sitting.

## 2. The day David helped me install the tool

It was a Thursday at the end of January. A few things had just happened at the company. Ember, the product I'd been hired to help launch, had shipped its MVP the month before, in December. The Series A push I'd been brought on to run was visible on the calendar. David and Glenn had been experimenting through the fall with AI-augmented development, using Cursor and Kiro and patterns of generation and review, and by early January they'd reached a conclusion neither of them had expected to reach when the year began. The shape of software development itself was changing, at their desks, in real time, and Alchemaize was going to bet on the change rather than work around it.

On this Thursday in January, during one of David and my daily calls, I finally decided to give this development approach a try. We're a fully distributed company. David lives in Brentwood, Tennessee; Glenn in College Station, Texas; me in Claremore, Oklahoma. No office, no shared zip code. Most of the serious conversations happen over video. This one was a video call we were already on, and I decided it was time to try something different. What David and Glenn had been showing and leading the way on, it was time for me to lean in and help.

The something different was that David and Glenn had been watching their own development speed up by an order of magnitude, and the speedup had surfaced a claim they couldn't yet verify. The claim was that the skills the speedup rewarded were not the skills the old methodology had rewarded. The bottleneck had moved from planning, typing, and iterating on code to specification and verification, and a person whose career was about clarifying intent rather than implementing it could, given the right framework, ship production software. When I decided it was time to try, it was out of a genuine curiosity to see what I could do. They got me set up and shared some guardrails I needed to be aware of and then let me go, checking in periodically, which then turned into the focal point of our conversations every time we met.

I was curious, and I also wanted to be helpful, and I'd spent enough years at AWS watching enterprise customers struggle with the same specification-and-handoff problem that I already had a theory the handoff was the expensive step. This new approach was to try a new way, with an IDE to help, and take an idea to production to see how far I could get on my own. I assumed I'd probably fail, and we'd all learn something, and we'd go back to the Series A push. I was wrong about the first part of that assumption.

The first thing David did was help me set up my tool. Then the fun part: we worked through the first specification of what we wanted to do, which spawned the VOS mentality. It wasn't me saying what the system is architected to do. It was me saying out loud what the outcome should be, what would be the acceptance of it, and how I wanted it to behave. No code, no architecture, nothing of that nature, just what I wanted to drive from an outcome, in human-to-human speaking language, nothing more.

I'd been asked to write requirements documents before, in other jobs. I'd even been pretty good at it in the context I'd been asked to do it in, which was the context of writing requirements for human software engineers who would read the document, fill in the parts I'd been vague about from their own professional judgment, and produce something approximately correct. That's what requirements documents had always been for, in my professional experience. They were a rough sketch the engineer then did the real work to complete.

Even though it seemed similar, we were working on something different. We were designing the outcome of the ask of the system to be complete enough to stand alone. What we were doing was taking out of the document all the assumptions I'd normally have left for the engineer to fill in, and replacing every one of them with a sentence as guardrail or ask.

Here's the practical thing. The skill of writing a VOS is not the skill of writing code. It's the skill of knowing, precisely, what you want, and being willing to say it in a way that cannot be negotiated. Those are two distinct skills, and the second one is harder than it sounds, because most of us spend our working lives writing descriptions of things that are deliberately fuzzy so they can be negotiated later. Sometimes that's diplomacy. Sometimes it's leaving room for the engineer's judgment. In most rooms, those are the right moves.

What a VOS asks for is the opposite of diplomacy. It asks for a specification that leaves no room for doubt. A machine reads what I wrote. If I write something vague, the machine will produce something that is, on average, close, and sometimes it will be right and sometimes it won't, and when it isn't, the bug is my fault, not the machine's, because I didn't say what I wanted.

Writing a VOS is the practice of saying what you want and being specific about it.

It took me about three weeks to get reasonably good at it.

## 4. Three things that surprised me

I want to share with you the three things that surprised me most about this journey.

**The first thing that surprised me** is how easy it was to get started. Yes, there's a lot to set up initially, but once you get going, it really is just something you interact with and as a result something great comes out the other side. You can speak to the tool like you would a human, type what you mean, be specific, and it will help shape what you want. The key is holding true to what you want to see and don't be afraid to iterate on it until you get it the way you want. You don't have to understand code, but you do have to have a vision, and that vision will help you develop and be proud of what you create.

**The second thing that surprised me** is that intent and clarity of that intent is important to get it right the first time. The tools are getting better at interpreting meaning and what we want to produce, but it's not perfect. You learn a lot by reading and seeing what the tool is doing, and as a result you quickly find out that the clearer you are with your intent and the better you write your Gherkin contracts, the better results you get.

**The third thing that surprised me** is this: why was I so afraid to do this in the first place?

I always looked at software development as a skillset needed, a language I needed to learn, or just the barrier to entry was too high for me. Glenn and David were always ready to support me and wanted to share with me how to develop something and to try it. I was always resistant, all through my career, but when I did try it, it opened a whole new world. David and Glenn tell me all the time that I sometimes create something that they feel is better or has a better look than what they can create. We quickly found out that you don't have to be an engineer to create something amazing. Just having the idea, a methodology to support it, you can create something quick and beautiful that fits your style. The hardest part is just getting started.

So my call to action for you is go try it. You may surprise yourself with what you're able to create. Don't be afraid of it, just try it and learn. You never know, it could open a whole new world for you.

---

*End of excerpt. Section 3, the full worked example, and Section 5, the closing argument to non-engineering readers, are in the book. The full Chapter 8 is the first full-length chapter to ship in the MEAP.*

\newpage

# Part VII. Anticipated Questions

*This section answers the questions we've been asked most often in public talks and one-on-one conversations during the hundred days and the weeks after. It's deliberately longer than an FAQ. The shorter answer is always "read the book when it comes out." These are the longer ones.*

---

### "Isn't this just Scrum, but with AI?"

No. The distinction is structural, not rhetorical.

Scrum is a coordination framework for human typists. The sprint, the story-point estimation, the standup, the sprint review: every element is calibrated to the pace at which humans can produce and review code. The unit of work (the story) is sized to a typing-hour budget. The ceremony (the sprint) is sized to the cadence at which human typing can be replanned.

CID isn't a coordination framework for human typists. It's a methodology for the case in which typing isn't the expensive step. The unit, the VOS, is sized to intent clarity, not typing effort. The cadence (continuous) is sized to verification throughput, not sprint duration. The roles map onto the steps that got dominant when typing got cheap (intent, verification, orchestration), not the steps that were dominant when typing was the bottleneck.

A team can, in principle, run both frameworks side by side while adopting. The book describes how. But they aren't the same thing. A CID pod running Scrum ceremonies on top of the CID loop is what we call, in Chapter 12, a *Costume CID* implementation: the vocabulary has been adopted, the behavior hasn't. It's the most common failure mode we predict for this methodology, and we name it specifically.

### "Why only three roles?"

The three roles map onto the three steps in the loop that need humans. Intent, authored by the Intent Engineer. Generation, orchestrated by the AI Orchestrator. Verification, owned by the Verification Owner. Every other concern in a traditional engineering team either lives inside one of those three or lives in the organizational layer above the pod, the enterprise layer (ELCID), covered in Chapters 9 through 11 of the book.

We considered more roles. We tried more roles, in early experiments. Every additional role in the pod either collapsed back into one of the three or added coordination overhead that didn't pay for itself. The three-role shape is the one that survived a hundred days of applied pressure.

On a very small team (two or three people) one person holds two roles. In the case study, Casey held Intent Engineer. David held Intent Engineer and AI Orchestrator. Glenn held Verification Owner and AI Orchestrator for slices Casey authored. The roles are cleaner than the people. That's a feature, not a bug.

### "What happens when the AI makes a mistake?"

Correct question. The answer has two parts.

First: the AI makes mistakes continuously. Not as a rare event. As a normal event. The methodology is built for that. The Verification Owner's acceptance contract is the mechanism that catches mistakes before they ship. If the contract is written well, most AI mistakes are caught at the verification step. If the contract is written poorly, AI mistakes ship and become production bugs, the same way human mistakes used to ship and become production bugs under the old methodology, except faster. This is the self-amplifying disaster referenced in Chapter 1 and returned to in Chapter 6.

Second: when a mistake does ship (because no verification process is perfect) the methodology's forensic response differs from the old methodology's. Under CID, the post-incident analysis focuses first on the acceptance contract that let the bug through, not on the AI that produced the code. The question isn't "why did the AI generate bad code?" The AI will always sometimes generate bad code, by the nature of the generation layer. The question is "why did our acceptance contract not catch it?" That question produces a contract-improvement action item, which is an artifact that lives in the codebase and protects the next hundred slices. The old post-incident question, "why did the engineer write this bug?," produces a process-improvement action item that lives in a retrospective document nobody reads again.

Verification is the central concern in the methodology. The book has an entire chapter on it. Glenn wrote that chapter.

### "Is this replicable outside Alchemaize? You're a three-person startup."

The honest answer has two sides.

The parts we're confident replicate: the loop, the three roles, the VOS form, the four metrics, the pattern of intent-upstream and verification-upstream. These are the parts we designed, not discovered. We designed them in response to what we were already doing, and they're portable to any team that accepts the underlying premise (the bottleneck has moved). The adoption path is in Chapter 13. The book names specifically what has to change in week one, week two, week four, and week twelve of adoption.

The parts we're less confident replicate: the specific 30x throughput multiplier is ours, in our conditions, against our product mix, with our specific people. We don't claim it replicates. It's the number we measured. Your number will be your number. We also acknowledge that the methodology's largest scaling question, how ELCID behaves in a 500-engineer organization, isn't yet answered by the case study. ELCID is the enterprise layer, and it's the less-proven half of the methodology. The book is honest about this. This report inherits that honesty.

The case study is a small-team case study. It proves the methodology exists and works at small scale. The scaling argument is separate, the book addresses it separately, and we're not going to pretend we have more data than we have.

### "What about security? Compliance? HIPAA, FedRAMP, PCI, all of it?"

This is addressed at length in Chapter 11 of the book, *Compliance at Generation Time*. Glenn's chapter. It argues a position some readers will find counterintuitive. Regulated industries are the strongest candidates for AI-native development, not the weakest.

The short version. Under the old methodology, compliance was an audit after the fact. Code got written; compliance reviewed it. The audit was a check. Under CID, compliance is enforced at the moment of generation. The acceptance contract includes the relevant regulatory controls as blocking constraints. If the generated code would violate HIPAA-164.312(b), the generation is blocked before the code is produced. That's structurally better than audit-after-the-fact, because it's continuous rather than episodic, and enforced mechanically rather than by human review.

We've applied this to three regulatory surfaces (HIPAA, FedRAMP Moderate, and selected financial-services controls) and shipped 22 rules as executable constraints. The book documents all three and names the specific regulatory controls cited. Field Report v0 doesn't reproduce this material because (a) the compliance framework is the book's strongest single chapter and we'd rather release it polished than draft, and (b) applying compliance at generation time is the methodology's highest-value enterprise capability, and we didn't want to give it away.

If you work in a regulated industry and you're evaluating AI-augmented development under a verification process that was designed for human typing, Chapter 11 is what we'd ask you to read. It's a reason to want the book.

### "Your non-engineer co-author must be a special case."

He isn't. He's a specific kind of case, and the case isn't as rare as the software industry has been assuming.

Casey has twenty years of operations, consulting, and Agile delivery experience. He's written requirements documents for as long as he's been working. He's sat in delivery rooms where engineers translated his intent into software. He's very good at his job. The job, as he's understood it, has always been about precision in specifying what a business needs. That's a skill that exists independent of whether the person holding it also knows how to type code.

What we discovered is that the skill of writing a VOS is the skill Casey already had. It isn't the skill of writing code. It's the skill of writing what you want with a precision that can't be negotiated. Senior product managers have it. Senior business analysts have it. So do senior program managers, customer-solutions people, and operations leaders. The industry has been training people in this skill for thirty years and then telling them they couldn't build software because they didn't know how to type it.

The translation step was what separated them from software. The translation step is gone.

Our claim isn't that every non-engineer can ship production code tomorrow. The claim is that the specific subset of non-engineers whose professional lives have been about specification-with-precision are the people this methodology was built for, and the industry has many more of them than it's admitted. Casey is one. Your senior PM is probably another. Your head of operations might be a third. Chapter 14, *Who Builds Next*, argues this at length.

### "What AI tool do you use? Claude? GPT? Cursor? Kiro?"

We use several. The tool choice isn't part of the methodology. CID is designed to be tool-agnostic. It would survive a complete turnover of every AI coding tool currently on the market, as long as a competent generation layer exists somewhere. That layer now exists in several forms and will exist in more forms a year from now.

The point of the three-role structure, the VOS, and the acceptance contract is that the methodology doesn't depend on any particular model's quirks. If your tool is good enough to produce code against a specification and context bundle, the methodology runs on top of it. If it isn't, no methodology compensates.

We're happy to share the specific tool choices we made during the hundred days in a private conversation. We've declined to print them here because the book will outlive the current tool generation, and we don't want the methodology to be read as an endorsement of a specific vendor.

### "Are you really three guys in three states with no office?"

Yes. Brentwood, Tennessee. Claremore, Oklahoma. College Station, Texas. No office, no co-working, no scheduled in-person weeks. We've met in person twice as a three-person team since October 2025. Everything else (every VOS, every code review, every verification gate, every production deploy) has happened over video, Slack, and git.

This is a feature of the methodology, not a coincidence of our circumstances. The CID loop doesn't require co-location. It doesn't benefit from co-location. The acceptance contract is the coordination mechanism. It's a written artifact that travels across time zones without degradation. The three-role structure is asynchronous by design.

We name this here because a small but vocal contingent of readers is going to ask whether the methodology secretly requires an office. It doesn't. The book addresses this in Chapter 13 and again in Chapter 12 (the anti-pattern called *Geography Theater*, using return-to-office as a methodology-adoption crutch).

If you're running an RTO push at your company on the theory that AI-augmented development requires bodies in rooms, we'd respectfully ask you to read the book before you renew the lease.

### "What if this is just hype? What if you're wrong?"

A fair question, and we take it seriously.

The honest answer is that we might be. The methodology has been applied, measured, and validated at small scale for one hundred days. It hasn't been applied at 50-engineer scale, 500-engineer scale, or 5,000-engineer scale. The case study is the case study. The scaling argument is separate. We're putting the methodology in public so it can be argued with and improved. We aren't claiming it's finished. We're claiming it's the first methodology we've seen that takes the new constraint seriously and designs from scratch for it.

If you're a CTO considering a CID pilot, the lowest-risk path we can point you to is Chapter 13 of the book, the adoption path. It's designed to be run on one team, for four weeks, producing measurable results either way, with a clean off-ramp if the methodology doesn't land in your context. We don't recommend company-wide adoption. We recommend one pod, four weeks, real slices, real measurement. Your number will be your number. If it's zero, you'll know in four weeks.

The framework we're offering is a hypothesis backed by a hundred-day case study. Treat it as that. The book will earn the right to be treated as more than that; the book is a hypothesis becoming a claim. We're releasing this report because we'd rather be argued with in public than ignored in private.

\newpage

# Part VIII. What This Is Not, and Where to Go Next

## What this report is not

This report isn't the methodology book. It's the precursor artifact. We've deliberately held the enterprise layer, the compliance framework, the full adoption path, the anti-patterns chapter, and the four appendices for the full-length edition. If you want what you'd need to run CID inside your organization, the book is where it lives.

This report isn't a sales pitch. We're selling the book only in the sense that the book is going to exist, we're going to ask people to pay for it, and we believe it will be worth paying for. This report is free. It will remain free. It isn't a lead magnet. It's a public artifact.

This report isn't finished thinking. It's a first-pass articulation of a methodology that is still being refined in practice. We expect the book to differ from this report in specific places. We'll note the differences in the book's preface when it ships, so readers of this report can see what changed and why.

## Where to go next

If the argument lands and you want to follow the methodology's development:

- **The mailing list.** `alchemaize.ai/field-report` has a single-purpose Beehiiv mailing list. We use it to announce the Manning MEAP launch, MEAP chapter drops, and the print-edition release. No marketing. No newsletter. No drip campaign.
- **The GitHub repository.** `github.com/alchemaize/field-report-v0` hosts the source markdown and diagrams for this report under CC BY-NC-SA. Pull requests for typos, clarifications, and factual corrections are welcome. Structural feedback goes to the issue tracker or directly to the three of us.
- **The Manning MEAP.** The full-length book, *Continuous Intent Delivery*, is in publisher discussions as of April 2026. When the MEAP launches (targeted late July or early August 2026), the first three chapters (Chapter 1, Chapter 3, Chapter 8) go live to MEAP readers. Remaining chapters ship in batches through Q4 2026. Full manuscript by end of Q4 2026. Print edition Q1 2027. We'll announce the publisher and MEAP page as soon as the contract is signed.

If the argument doesn't land, and you want to tell us why, we'd rather hear from you than from the reviewer of the finished book. Email the three of us collectively at `team@alchemaize.ai`, or file a GitHub issue. We're running the feedback loop actively between now and the publisher edition. The book will be written once. We'd rather hear the hard feedback now than six months from now.

\newpage

# Part IX. About the Authors

**David Kim** is the President and CFO of Alchemaize and the lead author of *Continuous Intent Delivery*. He is a United States Marine Corps veteran who served alongside Glenn Knepp beginning in 1996. David spent five years at Amazon Web Services, most recently at the Senior Manager level in enterprise technology customer leadership, product, and operations. His career carries both halves of the split that separates most software leaders: a technical coding background in the first half of his career and a deep consulting and Agile background in the second. He is the author of two prior books, *Bullets Don't Fly: A Supply Marine's Memoir* (2025) and *The Real Money Guide* (2025), both self-published via Amazon and IngramSpark. The latter is accompanied by a companion site, therealmoneyguide.com, hosting more than 30 interactive financial tools. David lives in Brentwood, Tennessee, and has been working on the problem this book addresses since late 2024.

**Casey Robinson** is the Chief Operating Officer of Alchemaize and a co-author of *Continuous Intent Delivery*. He joined the company in October 2025 after a career in customer service, consulting, operations, and enterprise delivery, most recently as a Senior Manager at Amazon Web Services leading a team of Customer Solutions Managers. Casey's career roots started in customer service as a technical representative at DirecTV; David brought him into the software and technology world years later, hiring him to a consulting firm in Austin, Texas. That hire is where the twenty-year professional relationship began. He had never written a line of production code before January 2026. He has now shipped production code on multiple applications inside the methodology the book describes, and is the primary author of the chapter (Chapter 8) that argues the methodology's central claim about who gets to build software next. Casey lives in Claremore, Oklahoma.

**Glenn Knepp** is the Chief Executive Officer and Chief Technology Officer of Alchemaize and a co-author of *Continuous Intent Delivery*. He is a career engineer, architect, and cybersecurity specialist whose career runs from classified military intelligence systems through enterprise platform development to startup founding. Glenn is a United States Marine Corps combat veteran who served from 1988 to February 1996 as a Signals Intelligence Specialist and Special Operations Reconnaissance Team Leader. After his uniformed service, he continued supporting the intelligence community as a civilian contractor, providing technical engineering and analysis to the U.S. Air Force, Marines, Navy, and CIA, and served as a trusted agent security manager for the NSA on classified systems. He is a named co-inventor on multiple patents spanning cloud computing, video streaming, and video cryptography. Glenn co-founded two prior startups, including Gazoo, Inc. (cloud-based Computer Labs as a Service, $1.9M in funding) and Ispira Technologies (cryptographic video streaming). He is the Verification Owner on the founding team, author of the acceptance-contract templates used across the hundred-day case study, and primary author of the chapters on verification and compliance. Glenn lives in College Station, Texas.

The three of us founded Alchemaize in August 2025 to build Ember, an AI-augmented reading application. CID emerged from the work of building Ember and watching what happened when the founding team tried something that worked better than any of us predicted. We've never shared an office. We don't plan to.

\newpage

# Colophon

*Field Report from the First Hundred Days* was drafted in Markdown, typeset with pandoc, and produced as a PDF for the Leanpub and GitHub distribution. Cover and interior typography uses Inter, Instrument Serif, and JetBrains Mono.

The report is released under Creative Commons BY-NC-SA 4.0. You may share, adapt, and build on the material non-commercially with attribution. The full text of the license is at `creativecommons.org/licenses/by-nc-sa/4.0`.

Source repository: `github.com/alchemaize/field-report-v0`
Landing: `alchemaize.ai/field-report`
Leanpub: pay-what-you-like, zero minimum

This is v0.1, a draft release. v1.0 accompanies the Manning MEAP launch in late July or early August 2026, with corrections and the first round of reader feedback incorporated.

DK, CR, GK
Alchemaize
April 2026
