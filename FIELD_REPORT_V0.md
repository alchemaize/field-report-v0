---
title: "Field Report from the First Hundred Days"
subtitle: "What happened when three founders stopped building software the old way"
author: "David Kim, Casey Robinson, Glenn Knepp"
date: "May 2026 — v0.1 draft"
---

\newpage

# Field Report from the First Hundred Days

**What happened when three founders stopped building software the old way.**

David Kim — Casey Robinson — Glenn Knepp

Alchemaize

v0.1 — April 2026 draft. Pre-release. Do not cite as final.

\newpage

## About this document

*Field Report from the First Hundred Days* is a free, ~60-page artifact released in advance of our full-length methodology book, *Continuous Intent Delivery*, currently in publisher discussions. It exists because the methodology we are describing is moving faster than the publishing industry. We did not want to wait eighteen months to start the conversation.

The report does four things:

1. It names the methodology — Continuous Intent Delivery, or CID — and describes it at *working depth*. Enough that a careful reader can argue with it. Not enough to run it in an enterprise.
2. It documents the 100-day case study that produced the methodology. What we built, what we counted, what we killed, what we got wrong.
3. It includes a teaser excerpt of Chapter 1 of the book, and three sections of Chapter 8 — the latter in Casey's voice. Chapter 8 is the chapter the non-engineering reader is likely to find most useful.
4. It answers the questions we have already been asked a hundred times, and honestly names the places the methodology is still uncertain.

The full methodology — the enterprise layer, the compliance framework, the adoption path, the four appendices — is held for the full-length book. This report is deliberately asymmetric: it gives away the argument and the evidence, and withholds the apparatus. If the argument lands for you, the book will give you the apparatus.

The report is released pay-what-you-like on Leanpub (minimum $0), mirrored on GitHub under Creative Commons BY-NC-SA, and linkable from `alchemaize.ai/field-report`. Pull requests for typos and corrections are welcome. Structural feedback should go to the GitHub issue tracker, or to the three of us directly.

The three of us — David Kim, Casey Robinson, Glenn Knepp — are the founding team of Alchemaize, a fully distributed company operating out of home offices in Brentwood, Tennessee; Claremore, Oklahoma; and College Station, Texas. We have never shared an office. We do not plan to.

— DK, CR, GK
April 2026

\newpage

# Part I — The Manifesto

## The Shift, in three hundred words

For twenty-five years, every method for building software at scale has been organized around a single assumption. The assumption was that humans are the bottleneck of the implementation step. Typing code was the expensive, slow, error-prone activity. The job of a framework was to coordinate humans around that expensive activity.

Every framework you know — Waterfall, Scrum, XP, Kanban, SAFe, DevOps, Continuous Delivery — is a rational, careful answer to a single question: *typing is expensive; how do we organize around that fact?*

The question has changed.

AI code generation has compressed the implementation step by one to two orders of magnitude. Typing is no longer the expensive step. The expensive steps are now *intent* — specifying, unambiguously, what you want software to do — and *verification* — confirming, with rigor, that what shipped does what you intended.

The bottleneck did not go away. It moved. Permanently. To the two steps that frameworks built for typing treated as overhead.

The implication, if you let it land, is that every framework currently in use at your company was designed for a bottleneck that no longer exists. The coordination machinery that was reasonable for typing-as-long-pole is, under the new constraint, friction. That is not a criticism of the old frameworks. They were the right answer to the question that was being asked. The question changed.

This report names what replaces them. The methodology is called **Continuous Intent Delivery**, or **CID**. Humans specify and verify. The machine implements. A small role-structured team runs a five-stage loop against an atomic unit called the **Verifiable Outcome Slice**. The organization scales the loop without breaking it.

The argument is in your hands. The evidence is in the next fifty pages. The methodology is in the book that follows.

— DK

\newpage

# Part II — The Methodology at Working Depth

## What you are about to read

The rest of Part II describes CID at enough depth to argue with. It introduces the three roles, the five-stage loop, the atomic unit of work, and the four metrics that replace the velocity dashboard. It does *not* give you enough to run the methodology inside an organization. That lives in the book.

We are aware of the asymmetry. We chose it deliberately. The argument is the part a methodology needs to establish in public; the apparatus is the part a methodology needs to be taught carefully. This report does the first. The book does the second.

---

## The five-stage loop

CID is a loop, not a sprint. It has no fixed cadence. It runs at the pace verification permits. The five stages are:

**1. Intent.** A human — the *Intent Engineer* — authors a specification of what should be built. The specification is called a **VOS**, a *Verifiable Outcome Slice*, and it is the atomic unit of work in the methodology. A VOS has five sections: WHY, WHAT, HOW, CONTEXT, OUTCOME. We describe it below.

**2. Context.** The Intent Engineer curates four-to-fifteen files from the existing codebase that are relevant to the slice. This is not a prompt. It is a reading list. The skill of choosing the right files, in the right configuration, is the single largest determinant of AI output quality in the methodology — more than the prompt, more than the model, more than the AI's raw reasoning ability.

**3. Generation.** The *AI Orchestrator* hands the VOS plus the curated context to a competent generation layer — Claude, GPT, Cursor, Kiro, whatever the team has chosen — and watches the generation step. The AI Orchestrator's job is not to type. It is to manage the generation session: catch drift, redirect on misinterpretation, throw a slice out and restart if the generation heads somewhere wrong.

**4. Verification.** The *Verification Owner* runs the acceptance contract written in the VOS against the generated code. The contract is executable. It either passes or it does not. If it does not, the slice returns to the Intent Engineer with notes. The Verification Owner does not report to the delivery chain. Their job is to say *no*.

**5. Observation.** The slice ships. Production telemetry confirms — or fails to confirm — that the outcome described in the VOS was actually produced for real users. The observation loops back into intent, either closing the slice or opening a new one.

The loop is continuous. It does not run once per sprint. It runs as fast as the verification step can be honored, which is typically several slices per day per Intent Engineer in a mature pod.

---

## The three roles

CID has three roles at the team layer. Each can be held by a different person. On a small team, one person can hold two or three. In the case study this report documents, two founders — David and Casey — held two roles each; Glenn held the third.

**Intent Engineer.** Authors the VOS. Curates the context. The Intent Engineer does not need to know how to code; they need to know what the business needs software to do, and how to say it with a precision that cannot be misread. In the case study, Casey is the Intent Engineer. He has never written a line of production code.

**AI Orchestrator.** Runs the generation session. Manages the model's behavior. Catches drift, restarts runs, escalates to the Intent Engineer when the VOS itself is wrong. The AI Orchestrator is usually an engineer, because the role benefits from knowing what good code looks like — but the role does not *produce* code. It produces generation sessions that yield verifiable code.

**Verification Owner.** Owns the acceptance contract. Blocks what does not pass. Writes the parts of the contract the Intent Engineer's domain knowledge cannot supply — the non-functional requirements, the security constraints, the compliance gates. In the case study, Glenn is the Verification Owner. He is also a career software engineer, and the contract-authoring half of his role has replaced most of the direct-coding half.

The three roles map onto the three steps that got dominant when typing got cheap. Intent Engineer owns the *intent* step. Verification Owner owns the *verification* step. AI Orchestrator sits in the middle and makes the machine do the step that used to be human.

---

## The Verifiable Outcome Slice (VOS)

The VOS is the atomic unit of work. It replaces the story, the ticket, the feature, the user-story-with-acceptance-criteria — all of which presupposed that typing was the long pole. A VOS has five sections.

**WHY.** Two to four sentences. What the slice is for. Written in business language. The Intent Engineer's mandate.

**WHAT.** The acceptance contract. Written in Gherkin — a small specification language that reads like English but is executable. The WHAT is the load-bearing section. If the WHAT is right, the rest of the slice usually works. If the WHAT is vague, the slice produces plausible but wrong code.

**HOW.** Three to five lines of design-level decisions. What existing components the slice plugs into. What gets reused, what gets extended. The HOW is the AI Orchestrator's section; it keeps the generated code consistent with the existing architecture.

**CONTEXT.** The four-to-fifteen files the generation session should read before generating. Not the whole codebase. Not the database schema. Just the files that matter for the slice.

**OUTCOME.** The production signal. One sentence describing what will be observable, in telemetry or user behavior, if the slice succeeds. The OUTCOME is what the Observation stage watches for.

We include one full worked VOS — the cash-flow reconciliation slice Casey shipped on Finaize — in Part IV of this report. The book contains ten more, plus an appendix of templates.

---

## The four metrics

CID replaces the velocity dashboard with four numbers. A CTO or VP of Engineering can read the entire engineering organization in thirty seconds using the four. We introduce them briefly here; the book walks through the diagnostic combinations.

**1. Cycle time.** Time from *VOS written* to *slice shipped to production*. In the case study, cycle time ran roughly 4–18 hours for team-owned slices and 1–4 days for the handful of slices that required deep architectural work.

**2. First-pass verification rate.** Percent of slices that pass the acceptance contract on the first generation attempt. This is the most diagnostic single number in the methodology. Low first-pass rate means vague VOSes, weak context curation, or both. High first-pass rate means the pod is mature. In our case study, this number ran 30–50 percent in the first two weeks and rose to 80–95 percent by week eight.

**3. Outcome KPI delta.** The change in the business metric the OUTCOME section predicted, measured against a baseline. This is the number a CEO cares about. It is also the only number in the four that measures whether the methodology is producing *value* versus producing *throughput*.

**4. Cost per shipped intent.** Total cost — people, inference, infrastructure — divided by the number of VOSes that shipped and passed observation. Inference cost is usually a decimal point on this number. The other costs are where the real math lives.

No velocity. No burndown. No story points. Four numbers, reviewed once per month, for ninety minutes. The book includes a full chapter on the monthly review.

\newpage

# Part III — The Case Study

## One hundred days, thirty-five applications

Between January 6 and April 15, 2026 — the one hundred days this report is named after — three founders of Alchemaize shipped thirty-five production applications using the methodology this report describes.

We had not named the methodology when we started. We named it after we had watched it work enough times that we trusted it. The naming came in late March, after the case study was substantially complete. The methodology itself had emerged in real time, in our own work, starting in the fall of 2025.

This section of the report is the evidence. It documents what we counted, what we did not count, which projects we killed, and what the measurement methodology was. We are doing this in public because an extraordinary claim without a counting methodology is a sales pitch, and we would rather be boring than wrong.

---

## Who we are and what we had

Alchemaize was founded in August 2025 by David Kim (CEO-shifting-to-CPO after the pivot) and Glenn Knepp (CEO/CTO after the pivot), for the purpose of building Ember — an AI-augmented reading application that shipped an MVP in December 2025. Casey Robinson joined as COO in October 2025, hired to run operations ahead of a Series A push.

Through the fall of 2025, David and Glenn's own development work was speeding up in ways neither of them had seen before. They were using Cursor and Kiro in the generation step, writing specifications with more precision than they were used to, and verifying output with small test harnesses they had built as they went. By the end of December, they had stopped calling what they were doing *using AI coding tools* and started calling it — roughly, informally — *the thing we are doing now.*

In the first week of January, they called Casey in and asked him if he would try running a slice end-to-end himself. He was a non-engineer. If the thing they were calling *the thing we are doing now* could be run by Casey, then it was a methodology. If it could not, it was a productivity hack.

He did. The next hundred days is what we are reporting on.

During the hundred days, the founding team was:

- **David Kim.** Intent Engineer and AI Orchestrator. Shipped against the Alchemaize product portfolio and the Catalyst consulting engagement surface.
- **Glenn Knepp.** Verification Owner. Authored the acceptance-contract templates used across the portfolio. Held the right of refusal on every merge.
- **Casey Robinson.** Intent Engineer. Test pilot. Shipped against TradeCodex and Finaize, the two applications the methodology was validated against first.

Combined FTE: approximately two. We were running commercial work in parallel — the AWS CATALYST partnership launched in March 2026 and the founding team was responsible for its early customer conversations. The hundred-day sprint was not our only activity. The 35 applications are what we shipped in the background, while the foreground was a Series-A push and a growing consulting practice.

We were based in Brentwood, Tennessee; Claremore, Oklahoma; and College Station, Texas. We did not share an office at any point during the hundred days. We did not share an office at any point in the company's history. We do not intend to. This is relevant to the methodology and is addressed in the book.

---

## What we counted

We counted an application as *shipped* if it met all of the following criteria:

1. It was deployed to a production environment accessible to end users or named pilot customers.
2. It passed at least one acceptance contract authored by the Verification Owner.
3. It had been used by at least one real user — internal or external — for a real task, not a demo.
4. The code was version-controlled in the Alchemaize monorepo or a public GitHub repository, with commit history auditable.

We did not count:

- Internal scripts, one-off automation, or tooling written to support the 35 applications. That code exists; it is not in the count.
- Branches that did not merge. Early-exploration VOSes that produced code the Verification Owner rejected and the Intent Engineer never resubmitted are not counted as shipped slices.
- Projects we killed. Three applications were started and killed during the hundred days, for reasons this section describes below. They are not in the count of 35.
- Work performed by contractors. Alchemaize did not use contract development during the period. The count is founding-team work only.

The 35 applications break down as follows:

- **12** apps in the Alchemaize portfolio — consumer and small-business applications, including Ember, Drawer, Flipmode, Noshmode, Radient, Renew, Skipday, Starfish, TradeCodex, VisibleWealth, Yeon, Alchemaize's own marketing site.
- **11** apps in the Finaize suite — the cash-flow product Casey spent most of the hundred days on. Finaize ships as a suite of applications: the web app, the mobile companion, the reconciliation engine, the bank-line ingestion service, the reporting service, several internal admin tools, and a small set of customer-facing microsites.
- **6** apps in the Catalyst partnership surface — the AWS-aligned consulting engagement artifacts: the assessment intake, the ROI calculator, the deal-desk automation, the customer-onboarding flow, and two partner-integration applications.
- **4** apps in the BoxLens / Albo / Ember-extension surface — small companion applications and experiments.
- **2** apps we are declining to name because they are under NDA with external pilot customers.

Of the 35, 8 are fully open-source on GitHub under the Alchemaize organization. The remaining 27 are either proprietary production applications, under NDA, or in regulated environments that preclude source-level disclosure.

---

## What we killed

Three projects started, ran for a few weeks, and stopped. We name them here because an honest case study needs to name its failures.

**Project A: the document-processing product.** A generalized document-ingestion service we started in late January. Killed in week 5. Reason: the VOSes we wrote for the ingestion layer kept producing code that passed the acceptance contract but did not pass any reasonable standard of *user-facing behavior*. We eventually realized the root issue was that our WHY sections were too abstract to be verifiable. The OUTCOME section could not be specified. If the OUTCOME cannot be specified, the slice cannot be verified; if the slice cannot be verified, CID does not apply. We killed it.

**Project B: the CRM integration.** A small CRM-sync utility we started in mid-February. Killed in week 8. Reason: the compliance constraints on the upstream CRM required an audit trail we had not yet built general infrastructure for. We could have built it in one sprint. We chose to defer until the Compliance-at-Generation-Time framework (see Chapter 11 of the book) was production-ready.

**Project C: the deprecated internal tool.** An internal productivity tool one of us (David) had built in December 2025 under the old methodology. Rewritten from scratch in March. The rewrite shipped; the original is deprecated and off-counted. The rewrite is one of the 35. The original is not.

Two of these three kills happened *because* CID's verification architecture surfaced a problem earlier than the old methodology would have. The third was deferred, not failed. We are counting all three as successful applications of the methodology, not failures of it. The methodology is supposed to kill things early. It did.

---

## The productivity multiplier

The headline number for this case study — two FTE, one hundred days, thirty-five applications — implies a throughput that is between one and two orders of magnitude higher than the industry baseline for a team of this size.

We want to be careful about how we claim this number, because productivity claims are the part of industry methodology books where the most bullshit lives.

Here is what we claim:

- Raw throughput, measured in shipped applications per FTE-day, is approximately 30× the industry benchmark we consider most defensible for this company stage (a small-team startup in the 5–15 FTE range). The benchmark is the DORA elite-performer baseline projected to our team size. We are using 30× as the conservative claim.
- The 30× multiplier is not uniform across the hundred days. The first two weeks ran closer to 5–8×; the final eight weeks ran closer to 40–50×. The average is 30×. The distribution is more informative than the average, and the book contains a full week-by-week breakdown.
- The multiplier is not uniformly applicable across application types. Greenfield applications ran higher multipliers than extensions of existing systems. Regulated applications ran lower multipliers than unregulated ones. The book contains the full breakout.

Here is what we do not claim:

- We do not claim 30× is replicable on day one of adoption. The pod maturity curve is real. First-pass verification rate — the most diagnostic of the four metrics — ran 30–50% in weeks one-and-two and 80–95% by week eight. The multiplier follows the maturity curve.
- We do not claim 30× transfers to teams of 50 or 500 engineers. The case study is a small-team case study. The book addresses scaling through ELCID and is honest about the fact that the enterprise layer is the less-proven half of the methodology.
- We do not claim 30× is the right multiplier for your team. It is the multiplier we measured, in our conditions, for our product mix, with our specific operators. Your number will be your number. We are reporting ours.

The book contains a full chapter — Chapter 3, *The Evidence* — that expands this section into roughly 10,000 words of measurement methodology. This report compresses it to two pages. If the multiplier is the reason you picked up this report, the book is where the full counting apparatus lives.

\newpage

# Part IV — One Worked VOS

## The cash-flow reconciliation slice

To give the reader the texture of what a VOS actually looks like, we reproduce one here in abbreviated form. This is a VOS Casey wrote in late February, against the Finaize application, for a feature called *Cash Flow Projection Bank-Line Reconciliation*.

We are reproducing the WHY and WHAT sections in full. The HOW, CONTEXT, and OUTCOME sections are summarized. The full VOS, including the thirty-line Gherkin acceptance contract, is in Appendix B of the book.

---

**VOS-FNZ-087 — Cash Flow Projection Bank-Line Reconciliation**

*Intent Engineer: Casey Robinson. Verification Owner: Glenn Knepp. AI Orchestrator: David Kim. Authored: 2026-02-24. Shipped: 2026-02-27.*

### WHY

A small-business owner relies on this application to tell them whether they will have money for payroll on the fifteenth. If the categorized view of the month disagrees with the bank-line total — even by a cent — the owner is being told something false, and we have failed the most basic job the product has. This slice ensures that we either show a reconciled projection or refuse to show a projection at all.

### WHAT

The acceptance contract is written in Gherkin. We reproduce a condensed version.

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

- `lib/finaize/categorize.ts` — transaction categorization module
- `components/finaize/ProjectionDisplay.tsx` — projection-display component
- `components/ui/ErrorBanner.tsx` — error-banner component
- `lib/finaize/aggregate.ts` — monthly-aggregation utility

### OUTCOME (summarized)

Reconciliation-failure rate visible to users drops to zero over the next billing cycle, because any projection we cannot reconcile, we do not show. Support-ticket volume for reconciliation-related issues drops by at least 80% week-over-week.

### What happened

The system generated the code in approximately six minutes. The pull request passed all unit tests on the first run and passed the acceptance contract on the first run. Glenn signed the contract. The slice deployed to production on Thursday, February 27, at approximately 3pm Central. On Friday, February 28, the support team reported zero new reconciliation-related tickets for the first time in a rolling seven-day window. The OUTCOME prediction held.

Casey's description of writing this VOS — and his description of realizing that the skill required to write it was a skill he had been practicing for twenty years in other jobs — is in Part VI below, in Section 3 of the Chapter 8 excerpt.

\newpage

# Part V — Chapter 1 Teaser

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 1:* The Shift. *Primary author: David Kim. This excerpt is approximately the first 3,000 words of the chapter. The full chapter runs ~6,850 words including the closing Field Note in Casey's voice.*

---

## The Shift

It is 11:47 on a Tuesday night in February. In a converted den on the ground floor of a house in Claremore, Oklahoma — three states from either of his two co-founders, neither of whom the company has ever asked him to share a physical building with — Casey is at his desk, and has been for five hours without interruption. The house is quiet. On the screen in front of him is a git diff that covers three files in an application called Finaize, and when he types the two-word commit message and presses return, he has shipped his forty-second VOS of the quarter. He stands up, stretches, notices that his coffee has gone cold at some point he doesn't remember, and walks down the hall to the kitchen.

At the counter, pouring the coffee he does not really need, he will realize something. It will not come to him as a revelation. It will come to him as a small, specific, practical observation, the way true realizations usually do. He will realize that he has not been to a standup in three weeks. He will realize that nobody on the founding team has noticed. He will realize that nobody on the founding team cares — not because they are negligent, but because there is no longer anything a standup would be for. And he will realize, with the kind of flat surprise that attaches to things you had not thought to name, that the way he had understood software development to work — the way he had watched every company he had ever worked in do it — no longer describes what he is actually doing.

The last thing he will realize, a minute or two later, standing in his own kitchen in a house his two co-founders have never been in, is that he is not a software engineer and has never been one, and yet the thing he shipped at 11:47 tonight is running in production against a real API, serving real users, and will continue to do so tomorrow.

This book is about that Tuesday.

---

It is also a book about the thing that Tuesday implies, which is that a twenty-five-year consensus about how software gets made is over. We are going to spend the next 80,000 words making that case, first as an argument, then as a methodology, then as a set of enterprise practices, and finally — in a chapter Casey has written himself — as a lived experience. By the end, we will have done something the current literature on AI and software development has not yet done. We will have described what replaces Scrum.

I want to say that plainly before we go further, because a lot of what follows depends on it. This book is not *AI and agile, together at last*. It is not *how to add prompt engineering to your sprint*. It is not one of the many genuine and useful books being written right now about how to use AI coding tools more effectively inside an otherwise unchanged software-engineering practice. Those books have their place. This is not that book.

The argument in your hands is that the software-engineering practice itself has to change, because the constraint it was designed for is gone, and the constraint it now faces is not one any existing framework was built to hold.

The rest of this chapter is the case for that sentence. The rest of the book is what to do about it.

## The bottleneck moved

For twenty-five years, every method for building software at scale has been organized around a single assumption. The assumption was that humans are the bottleneck of the implementation step, that typing code is the expensive, slow, error-prone activity, and that the job of a framework is to coordinate humans around that expensive activity so that their typing-output gets used well.

Every framework you know, descended from every framework that preceded it, is a solution to this problem. Waterfall said: plan exhaustively up front, because the typing is the long pole and mistakes are expensive to rewrite. Scrum said: slice the work into two-week increments, because the typing is still the long pole but requirements change faster than the plan. Extreme Programming said: pair the typists so they catch each other's errors in real time. Kanban said: limit concurrent typing so throughput doesn't collapse under context-switching. SAFe said: coordinate large groups of typists at ten-week resolution so the organization can plan. DevOps said: automate everything around the typing that isn't typing, so the typists can concentrate on the typing. Continuous Delivery said: the typing is fine; it's what happens after the typing that's broken.

Every one of those frameworks is a rational, careful, well-engineered answer to a single question: the typing is expensive, and how do we organize our organization around that fact?

The question has changed.

It is not that AI has made typing free, although in some meaningful sense it has. It is that the step between the human specification and the running code — the step that for decades we called *implementation* or *coding* or, on a bad day, *cutting the ticket* — has become, in the hands of a competent operator, roughly the cheapest step in the pipeline. Not the fastest. Not the most glamorous. Just the cheapest. Which is to say: the one that is no longer worth organizing around.

Of course it is not precisely *free*. There are still costs — model-inference costs, verification costs, operator costs, the very real cost of the time it takes to write the specification well. But those costs are not typing costs. They are the costs of the other steps, the steps that used to be cheap relative to typing because typing dominated them. And when the dominant cost is removed from a system, the structure of the system does not stay the same. It shifts, all at once, to fit the new dominant cost.

So: what is the new dominant cost?

Two things, not one. They sit on either side of the old bottleneck.

The first is *intent*. Specifying, unambiguously and completely enough that a machine can act on it, what you actually want the software to do. In the old world, we called this requirements engineering and treated it as a ten-percent activity because typing was the ninety-percent. In the new world, intent clarity is the dominant input to output quality. If you are any good at this work now, you have already noticed it. The difference between an AI tool that does what you wanted and an AI tool that does some plausible thing that is not at all what you wanted is almost always a difference in the specification going in. There is no prompt-engineering trick that compensates for intent that was vague from the start.

The second is *verification*. Knowing, with reasonable confidence, that the code you shipped does what you intended it to do. In the old world, we called this quality assurance and treated it as a downstream activity because typing was the expensive middle. In the new world, verification is the structural guarantee of the whole pipeline. If you cannot verify, you cannot ship at any speed — because shipping unverified AI output is a distinct and self-amplifying form of disaster, one this book will name specifically in a later chapter.

The bottleneck did not go away. It moved. It moved, permanently, from the typing step — which got cheap — to the intent step and the verification step, which got dominant.

The implication of this, if you let it land, is that every framework currently in use at your company was designed for a bottleneck that no longer exists. Not as a slight criticism. As a structural fact. The thing Scrum's machinery is best at — coordinating the cost of human typing across a sprint — is no longer the cost that matters. The thing SAFe's machinery is best at — coordinating hundreds of human typists at ten-week resolution — is coordinating something that does not need to be coordinated anymore. Not because the typists are bad. Because the machine is doing the typing.

The frameworks have become friction.

That is the load-bearing observation of this book. Everything that follows — the methodology, the roles, the metrics, the adoption path — is an attempt to answer the question that opens up the moment you accept that observation. What, then, is the thing we should be building our organizations around?

## A concession before we continue

I want to pause for a paragraph, because the sentence "the frameworks have become friction" is the kind of sentence that can sound glib, and I have been in this industry long enough to know what happens when a new methodology talks about the old one that way. What happens is that a third of the reader stops reading because they have heard this kind of thing three times this year already, and another third starts reading defensively, and the last third reads with the cheerful ferocity of people who had been waiting for permission to say what they already thought. I do not want any of those three readers right now. I want the careful reader.

So: Scrum was a reasonable solution to a real problem. SAFe was a reasonable scaling of that solution to larger organizations. The individual practices these frameworks advocated — the standup, the retro, the sprint review, the Program Increment — were not absurd; they were, and in many contexts still are, the best answer a careful engineering culture ever gave to the question of how to organize humans whose typing was the long pole.

The criticism is not that the frameworks were wrong then. The criticism is that the condition they were designed for is no longer the condition we are in. A design rational for one constraint becomes an impediment under a different constraint. That is how engineering works. That is how, for that matter, software works.

So when the next chapter takes a scalpel to the specific thirty-two hours of ceremony a Scrum team currently pays per sprint, and demonstrates that the same coordination function can be accomplished in thirty minutes per week in the new constraint, please read that chapter as I intend it. Not as a criticism of Scrum the framework. As a description of the structural cost of running a machine calibrated for one constraint in a world that has moved to another.

The book is not gleeful about this. The book is attempting to be right about it.

## The new constraint and what it demands

If the bottleneck has moved to intent and verification, then a method for building software at scale under the new constraint needs to be organized around *those* two things. This is the whole design brief. The rest is details.

A useful way to see what this looks like in practice is to notice what has *not* changed.

Business outcomes have not changed. You still need to know what you are trying to build and why. What has changed is that you now need to write that down with more precision than you did before, because now something is going to act on it without the soft rails of a twenty-year-old engineering team's shared context. The intent specification is no longer a communication artifact between humans who already know most of the answer. It is a load-bearing input to an actor that does not know the answer and will act on whatever you give it.

Users have not changed. You still need to verify that what you built works for them. What has changed is that now you need to verify *more*, and *earlier*, and *continuously*, because the output is arriving faster than any QA process designed for human-speed generation can keep up with. The verification step has not been bypassed. It has been inverted — brought upstream of generation, made continuous, made the structural guarantee rather than the downstream check.

Organizations have not changed. You still need to decide what you are going to fund and why. What has changed is that the unit of funding — *the project*, with its fixed scope and schedule and deliverable — is an instrument for a world in which humans are the constraint and scope is negotiable. The new constraint asks for a different instrument.

The methodology you will meet in the next chapters takes those three observations and builds from them. It is called Continuous Intent Delivery — CID at the team layer, ELCID at the enterprise layer, and for the rest of this book we will be explaining what that means, how it works, what it costs, and how you adopt it. But the load-bearing design move is already visible. The methodology is organized around the things that have become dominant: intent clarity, verification rigor, and outcome-based funding. It is not organized around the thing that became cheap: typing.

The slogan form of this — and the book will earn the right to use slogan forms only sparingly, I promise — is: *Intent is the artifact. Code is the exhaust.*

I want to be precise about what that means, because the sentence does a lot of work and will show up in later chapters more than once. It does not mean code is unimportant. Of course code is important; it is what runs. It means something specific: the artifact that humans should author, version, review, argue over, maintain, and treat as the organization's durable knowledge is the *specification of intent*, not the generated implementation. The code is what comes out the other end when the specification is right. The code is, in a reasonable sense, the predictable output of a well-run pipeline — not the creative output of a human act.

---

*Excerpt ends. The full chapter continues through "The proof that the inversion holds," "A quick definition, and then the road map," "A note from the Verification Owner" (Glenn's voice), "Who this book is for," and "The road ahead," closing with Casey's Field Note. Available in the full-length book.*

\newpage

# Part VI — Chapter 8 Excerpts (Casey's Voice)

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 8:* Field Report from the Test Pilot. *Primary author: Casey Robinson. Full chapter runs 7,500–8,500 words in the book. This excerpt reproduces Sections 1, 2, and 4 at compressed length, preserving the full voice.*

---

## 1. Who I am and what I'm not

I am six-four and bearded and I look like I should be running a trucking company. This is relevant context, not a joke. When I walk into a meeting with David, the people in the room sometimes assume he is the consultant and I am his security detail. The assumption is reasonable if all you have to go on is the fact that I look the way I do. I mention it because what I am going to tell you in this chapter is that the thing I do for a living now is author the specifications for production software that runs against real customer data, and if you had told me on the day I was hired that this would be part of my job, I would have laughed and then asked what the actual job was.

The actual job, as posted, was COO. Chief operating officer of a then-three-person startup that was heads-down building a product called Ember. My background is not engineering. It is consulting, customer service, operations, and Agile delivery, carried for long enough that it is the shape my career has. For the year immediately before Alchemaize, I was at Amazon Web Services, at the Senior Manager level, leading a team of Customer Solutions Managers. If you have not encountered that role before, a Customer Solutions Manager at AWS is the person who stands in the seam between an enterprise customer and the technical capability they are trying to adopt. You guide the migration. You hold the plan together. You translate between the customer's internal politics and the technology's actual shape. You do a great deal of it in Agile ceremonies, because that is the format enterprise delivery has mostly settled into. You do not write production code. That was my world for the immediate stretch before this one, and variations of that world have been my world for most of my working life.

I say all of that so the rest of the chapter lands cleanly. I have been in software-delivery rooms for twenty years. I have run Agile programs. I have written requirements, backlogs, acceptance criteria, operating playbooks, and the kind of customer-facing documentation that has to survive a lawyer reading it. What I have never done, in any of those rooms, is write code. Not a little on the side. Not a year of bootcamp in my thirties. None. I do not know what a closure is. I know what a database is but I could not, at risk of my salary, tell you the difference between a B-tree index and a hash index. I read just enough of Glenn's code review comments to understand when he is annoyed, which is a skill I had already developed in previous jobs for different reasons.

I did not come to Alchemaize planning to be anything other than the person who kept the company's operations intact while David and Glenn built Ember. That was the plan when I was hired. The plan did not hold. I am going to tell you in this chapter what happened instead.

And here is the fact this chapter is in the book to explain. In the hundred days covered by this book, I personally shipped production code — first on an app called thetradecodex.com, then on a cash-flow projection product called Finaize — without David or Glenn touching the code I shipped. I did it under a methodology David and Glenn had been building but had not yet named; the naming came after they watched me do it repeatedly. The methodology is what the rest of the book is about. This chapter is what it looked like from where I was sitting.

## 2. The day David asked me to write a spec instead of a wish list

It was a Monday in early January. A few things had just happened at the company. Ember — the product I had been hired to help launch — had shipped its MVP the month before, in December. The Series A push I had been brought on to run was visible on the calendar. And in the week or two immediately preceding this Monday, David and Glenn had decided to restructure the way we built software, full stop. They had reached a conclusion neither of them had expected to reach when the year began: the shape of software development itself was changing, at their desks, in real time, and Alchemaize was going to bet on the change rather than work around it.

On this particular Monday, David called me. We are a fully distributed company — David in Brentwood, Tennessee; Glenn in College Station, Texas; me in Claremore, Oklahoma; no office, no shared zip code — and most of the serious conversations happen over video. When I picked up the call he said we needed to talk about something different.

The something different was that he and Glenn had been watching their own development speed up by an order of magnitude, and the speedup had surfaced a claim they could not yet verify. The claim was that the skills the speedup rewarded were not the skills the old methodology had rewarded — that the bottleneck had moved from typing to specification and verification, and that a person whose career was about clarifying intent rather than implementing it could, given the right framework, ship production software. They were not asking me this as a favor. They were asking because the claim was load-bearing for something bigger they were building, and I was the only non-engineer on the founding team, and if the claim wasn't true they needed to know now, not later.

I said I'd try it. I thought I'd probably fail, and we would all learn something. I was wrong about the first part.

The first thing David asked me to do was write down what I wanted one specific piece of software to do. He was very precise about the framing. He did not ask me to "write the requirements." He did not ask me to "describe the feature." He said: *write down what you want it to do, in a way that is specific enough that a machine could not possibly misinterpret you, and test it by imagining the machine that could not.*

I had been asked to write requirements documents before. I had even been pretty good at it, in the context I had been asked to do it in — which was the context of writing requirements for human software engineers who would read the document, fill in the parts I had been vague about from their own professional judgment, and produce something approximately correct. That is what requirements documents had always been for, in my professional experience. They were a rough sketch that the engineer then did the real work to complete.

David was asking for something different. He was asking for the sketch to be complete enough to stand alone.

The first VOS I wrote took me four hours and was, Glenn later told me, very bad. He rejected three of its four acceptance contracts the next morning. He was right about two of them. The third one he was wrong about, and I said so, and we argued for about twenty minutes, and he came around.

The second VOS took me two hours. The third took me an hour and a half. By the fifth, I was writing them in about forty-five minutes. By the tenth, I was writing them in under an hour and the rejection rate was low enough that we stopped paying attention to it as a signal.

Here is the thing I want to tell you, and it is not an inspirational thing, it is a practical thing. The skill of writing a VOS is not the skill of writing code. It is the skill of knowing, precisely, what you want, and being willing to say it in a way that cannot be negotiated. Those are two distinct skills, and the second one is harder than it sounds, because most of us spend our working lives writing descriptions of things that are deliberately fuzzy so that they can be negotiated later. We call that diplomacy. We call it leaving room for the engineer's judgment. We call it not being prescriptive. Those are all real things, and in other contexts they are the right things.

What a VOS asks for is the opposite of diplomacy. It asks for a specification that would look rude in an email.

Writing a VOS is the practice of saying what you want.

It took me about three weeks to get reasonably good at it.

## 4. Three things that surprised me

I want to tell you three things I did not expect, because I think they are the three things that matter most for a reader who is in roughly the position I was in.

**The first thing that surprised me** is that what people had told me was "technical" about software, for my whole career, turned out to be mostly about clarity. I had always been told I didn't understand software "because I didn't have the technical background." What I found, doing this work, is that almost every conversation I had ever had with a software engineer where I had been made to feel I did not understand was actually a conversation where the engineer and I had different levels of precision about what we were trying to accomplish. Precision is not technical. Precision is a discipline of writing. I have been writing operations memos for twenty years. I have more practice at precision than the average software engineer does, as long as the subject is one I understand. The subject of what I want a product to do is a subject I understand.

**The second thing that surprised me** is that what I had been told was "easy" turned out to be clarity's opposite. I had been told, over the years, that certain things were easy — just add a button, just show it in a list, just tweak the copy. Every one of those things has collapsed under me at least once on this sprint. *Just tweak the copy* is a vague VOS that will produce plausible but wrong code. *Change the error message on the reconciliation failure from "Unable to reconcile" to "Some transactions could not be categorized; click here to review them" whenever the failing cases include at least one uncategorized transaction; otherwise keep the current message* — that is a VOS that will produce correct code. The difference is fifty words. But those fifty words are the whole job.

**The third thing that surprised me** is this, and I debated whether to include it, and David and Glenn both said to include it, so here it is.

I was sitting at the kitchen table at my house in Claremore at some point in February, on a Saturday, working on a VOS for the Finaize application. The VOS had to do with how reports were exported. I had been working on it for about three hours. The kitchen was quiet. My wife was out with our daughter. The sun was the color sunlight gets at about four in the afternoon in February in northeastern Oklahoma, which is thin and low and the color of something about to be winter again. I pressed return on a commit and the VOS shipped. A few minutes later, my phone buzzed. It was an automated notification from the Finaize analytics telling me that the report-export feature had been used seventeen times in the last hour, by customers, in production.

That was when I realized I had shipped production software that people were actually using. Me. The one who had been hired to run operations. The one who looks like he should be moving desks.

I sat at the kitchen table for a minute and did not do anything. I was not emotional about it. I was just sort of quiet, the way you get quiet when a thing you thought you understood about yourself turns out to be differently shaped than you thought. I had always understood myself as a person who enables the people who build things. I have spent my career enabling people to build things. I am good at it. I like it. And I realized, in that quiet moment at the kitchen table, that what the methodology had done was not turn me into a person who builds things in a *different* way. It had done something more subtle. It had made the thing I already did — being clear about what a business needs a piece of software to do — into a thing that could, directly, produce software, without needing to be translated by someone else first.

The translation step was what had separated me from software for twenty years. The translation step was gone.

I sat at the kitchen table a little longer. Then I got up and made coffee and went back to work.

---

*End of excerpt. Section 3 — the full worked example — and Section 5 — the closing argument to non-engineering readers — are available in the book. Full Chapter 8 is the first full-length chapter Manning will ship in the MEAP.*

\newpage

# Part VII — Anticipated Questions

*This section answers the questions we have been asked most often, in public talks and one-on-one conversations, during the hundred days and the weeks after. It is deliberately longer than an FAQ. The shorter answer is always "read the book when it comes out." These are the longer answers.*

---

### "Isn't this just Scrum, but with AI?"

No. The distinction is structural, not rhetorical.

Scrum is a coordination framework for human typists. The sprint, the story-point estimation, the standup, the sprint review — every element is calibrated to the pace at which humans can produce and review code. The unit of work (*the story*) is sized to a typing-hour budget. The ceremony (*the sprint*) is sized to the cadence at which human typing can be replanned.

CID is not a coordination framework for human typists. It is a methodology for the case in which typing is not the expensive step. The atomic unit (*the VOS*) is sized to *intent clarity*, not typing effort. The cadence (*continuous*) is sized to *verification throughput*, not sprint duration. The roles map onto the steps that got dominant when typing got cheap — intent, verification, orchestration — not the steps that were dominant when typing was the bottleneck.

A team can, in principle, run both frameworks side-by-side while adopting. The book describes how. But they are not the same thing. A CID pod running Scrum ceremonies on top of the CID loop is what we call, in Chapter 12, a *Costume CID* implementation — the vocabulary has been adopted; the behavior has not. It is the most common failure mode we predict for this methodology, and we name it specifically.

### "Why only three roles?"

Because the three roles map onto the three steps in the loop that are load-bearing for humans. Intent — authored by the Intent Engineer. Generation — orchestrated by the AI Orchestrator. Verification — owned by the Verification Owner. Every other concern in a traditional engineering team either lives inside one of those three roles or lives in the organizational layer above the pod (which is the enterprise layer — ELCID — covered in Chapters 9–11 of the book).

We considered more roles. We tried more roles, in early experiments. Every additional role in the pod either collapsed back into one of the three or added coordination overhead that did not pay for itself. The three-role shape is the one that survived a hundred days of applied pressure.

On a very small team — two or three people — one person holds two roles. In the case study, Casey held Intent Engineer; David held Intent Engineer and AI Orchestrator; Glenn held Verification Owner and AI Orchestrator for slices Casey authored. The roles are cleaner than the people. That is a feature, not a bug.

### "What happens when the AI makes a mistake?"

This is the correct question to ask. The answer is in two parts.

**Part one:** the AI makes mistakes continuously. Not as a rare event. As a normal event. The methodology is built for that. The Verification Owner's acceptance contract is the apparatus that catches mistakes before they ship. If the contract is written well, most AI mistakes are caught at the verification step. If the contract is written poorly, AI mistakes ship and become production bugs — the same way human mistakes used to ship and become production bugs under the old methodology, except faster. This is the self-amplifying disaster we reference in Chapter 1 and return to in Chapter 6.

**Part two:** when a mistake *does* ship — because no verification apparatus is perfect — the methodology's forensic response is different from the old methodology's. Under CID, the post-incident analysis focuses first on *the acceptance contract that let the bug through*, not on the AI that produced the code. The question is not *why did the AI generate bad code?* — the AI will always sometimes generate bad code, by the nature of the generation layer. The question is *why did our acceptance contract not catch it?* That question produces a contract-improvement action item, which is an artifact that lives in the codebase and protects the next hundred slices. The old post-incident-analysis question — *why did the engineer write this bug?* — produces a process-improvement action item that lives in a retrospective document nobody reads again.

Verification is the load-bearing concern in the methodology. The book has an entire chapter on it. Glenn wrote that chapter.

### "Is this replicable outside Alchemaize? You're a three-person startup."

The honest answer is a two-sided one.

**The parts we are confident replicate:** the loop, the three roles, the VOS form, the four metrics, the general pattern of intent-upstream / verification-upstream. These are the parts that were designed, not discovered. We designed them in response to what we were already doing, and they are portable to any team that accepts the underlying premise (the bottleneck has moved). The adoption path is in Chapter 13. The book names specifically what has to change on week one, week two, week four, and week twelve of adoption.

**The parts we are less confident replicate:** the specific 30× throughput multiplier is ours, in our conditions, against our product mix, with our specific operators. We do not claim it replicates. It is the number we measured; your number will be your number. We also acknowledge that the methodology's largest scaling question — how ELCID behaves in a 500-engineer organization — is not yet answered by the case study. ELCID is the enterprise layer, and it is the less-proven half of the methodology. The book is honest about this; this report inherits that honesty.

The case study is a small-team case study. It proves the methodology exists and works at small scale. The scaling argument is separate, and the book addresses it separately, and we are not going to pretend we have more data than we have.

### "What about security? Compliance? HIPAA, FedRAMP, PCI, all of it?"

This is addressed at length in Chapter 11 of the book — *Compliance at Generation Time*. Glenn's chapter. It argues a position some readers will find counterintuitive: regulated industries are the *strongest* candidates for AI-native development, not the weakest.

The short version: under the old methodology, compliance was an audit after the fact. Code got written; compliance reviewed it. The audit was a check. Under CID, compliance is enforced at the moment of generation — the acceptance contract includes the relevant regulatory controls as blocking constraints. If the generated code would violate HIPAA-164.312(b), the generation is blocked before the code is produced. This is a structurally better posture than audit-after-the-fact, because it is continuous rather than episodic, and it is enforced mechanically rather than by human review.

We have applied this to three regulatory surfaces — HIPAA, FedRAMP Moderate, and selected financial-services controls — and shipped 22 rules as executable constraints. The book documents all three and names the specific regulatory controls cited. Field Report v0 does not reproduce this material because (a) the compliance framework is the book's strongest single chapter and we would rather release it polished than draft, and (b) applying compliance at generation time is the methodology's highest-value enterprise capability and we did not want to give it away.

If you work in a regulated industry and you are evaluating AI-augmented development under a verification architecture that was designed for human typing, Chapter 11 is the chapter we would ask you to read. It is a reason to want the book.

### "Your non-engineer co-author must be a special case."

He is not. He is a specific kind of case, and the case is not as rare as the software industry has been assuming.

Casey has twenty years of operations, consulting, and Agile-delivery experience. He has written requirements documents for as long as he has been working. He has sat in delivery rooms where engineers translated his intent into software. He is very good at his job. The job, as he has understood it, has always been about precision in specifying what a business needs. That is a skill that exists independent of whether the person holding it also knows how to type code.

What we discovered is that the skill of writing a VOS is the skill Casey already had. It is not the skill of writing code. It is the skill of writing what you want with a precision that cannot be negotiated. A senior product manager has it. A senior business analyst has it. A senior program manager has it. A senior customer-solutions person has it. A senior operations leader has it. The industry has been training people in this skill for thirty years and then telling them they could not build software because they did not know how to type it.

The translation step is what separated them from software. The translation step is gone.

Our claim is not that every non-engineer can ship production code tomorrow. The claim is that the specific subset of non-engineers whose professional lives have been about specification-with-precision are the people this methodology was built for, and the industry has many more of them than it has admitted. Casey is one. Your senior PM is probably another. Your head of operations might be a third. Chapter 14 — *Who Builds Next* — argues this at length.

### "What AI tool do you use? Claude? GPT? Cursor? Kiro?"

We use several. The tool choice is deliberately not part of the methodology. CID is designed to be tool-agnostic. The methodology would survive a complete turnover of every AI coding tool currently on the market, as long as *a* competent generation layer exists. That layer now exists in several forms and will exist in more forms a year from now.

The point of the three-role structure, the VOS, and the acceptance contract is that the methodology does not depend on any particular model's quirks. If your tool is good enough to produce code against a specification and context bundle, the methodology runs on top of it. If your tool is not good enough, no methodology compensates.

We are happy to share the specific tool choices we made during the hundred days in a private conversation; we have declined to print them here because the book will outlive the current tool generation and we do not want the methodology to be read as an endorsement of a specific vendor.

### "Are you really three guys in three states with no office?"

Yes. Brentwood, Tennessee. Claremore, Oklahoma. College Station, Texas. No office, no co-working, no scheduled in-person weeks. We have met in person twice as a three-person team since October 2025. Everything else — every VOS, every code review, every verification gate, every production deploy — has happened over video, Slack, and git.

This is a feature of the methodology, not a coincidence of our circumstances. The CID loop does not require co-location. It does not benefit from co-location. The acceptance contract is the coordination mechanism; it is a written artifact that travels across time zones without degradation. The three-role structure is asynchronous by design.

We name this here because a small but vocal contingent of the readership is going to ask whether this methodology secretly requires an office. It does not. The book addresses this in Chapter 13 and again in Chapter 12 (the anti-pattern called *Geography Theater* — using return-to-office as a methodology-adoption crutch).

If you are running an RTO push at your company on the theory that AI-augmented development requires bodies in rooms, we would respectfully ask you to read the book before you renew the lease.

### "What if this is just hype? What if you're wrong?"

A fair question, and we take it seriously.

The honest answer is that we might be. The methodology has been applied, measured, and validated at small scale for one hundred days. It has not been applied at 50-engineer scale, 500-engineer scale, or 5000-engineer scale. The case study is the case study; the scaling argument is separate. We are putting the methodology in public so it can be argued with and improved. We are not claiming it is finished. We are claiming it is the first methodology we have seen that takes the new constraint seriously and designs from scratch for it.

If you are a CTO considering a CID pilot, the lowest-risk path we can point you to is Chapter 13 of the book — the adoption path. It is designed to be run on one team, for four weeks, producing measurable results either way, with a clean off-ramp if the methodology does not land in your context. We do not recommend company-wide adoption. We recommend one pod, four weeks, real slices, real measurement. Your number will be your number. If it is zero, you will know in four weeks.

The framework we are offering is a hypothesis backed by a hundred-day case study. Treat it as that. The book will earn the right to be treated as more than that; the book is a hypothesis becoming a claim. We are releasing this report because we would rather be argued with in public than ignored in private.

\newpage

# Part VIII — What This Is Not, and Where to Go Next

## What this report is not

This report is not the methodology book. It is the precursor artifact. We have deliberately held the enterprise layer, the compliance framework, the full adoption path, the anti-patterns chapter, and the four appendices for the full-length edition. If you want the apparatus to run CID inside your organization, the book is where it lives.

This report is not a sales pitch. We are selling the book only in the sense that the book is going to exist, we are going to ask people to pay for it, and we believe it will be worth paying for. This report is free. It will remain free. It is not a lead magnet; it is a public artifact.

This report is not finished thinking. It is a first-pass articulation of a methodology that is still being refined in practice. We expect the book to differ from this report in specific places. We will note the differences in the book's preface when it ships, so the readers of this report can see what changed and why.

## Where to go next

If the argument lands and you want to follow the methodology's development:

- **The mailing list.** `alchemaize.ai/field-report` has a single-purpose Beehiiv mailing list. We use it to announce the Manning MEAP launch, MEAP chapter drops, and the print-edition release. We will not use it for anything else. No marketing. No newsletter. No drip campaign.
- **The GitHub repository.** `github.com/alchemaize/field-report-v0` hosts the source markdown and diagrams for this report under CC BY-NC-SA. Pull requests for typos, clarifications, and factual corrections are welcome. Structural feedback should go to the issue tracker or to the three of us directly.
- **The Manning MEAP.** The full-length book, *Continuous Intent Delivery*, is in publisher discussions as of April 2026. When the MEAP launches — targeted late July / early August 2026 — the first three chapters (Chapter 1, Chapter 3, Chapter 8) go live to MEAP readers. The remaining chapters ship in batches through Q4 2026. Full manuscript by end of Q4 2026. Print edition Q1 2027. We will announce the publisher and the MEAP page as soon as the contract is signed.

If the argument does not land and you want to tell us why — we would rather hear from you than from the reviewer of the finished book. Email the three of us collectively at `team@alchemaize.ai` or file a GitHub issue. We are running the feedback loop actively between now and the publisher edition. The book will be written once. We would rather hear the hard feedback now than six months from now.

\newpage

# Part IX — About the Authors

**David Kim** is a career product and technology leader, author of two prior books in adjacent domains, and the lead author of *Continuous Intent Delivery*. He is the co-founder and Chief Product Officer of Alchemaize. David lives in Brentwood, Tennessee. He has been working on the problem this book addresses since late 2024 and the hundred-day case study that produced the methodology was run from his home office.

**Casey Robinson** is the Chief Operating Officer of Alchemaize and a co-author of *Continuous Intent Delivery*. He came to the company in October 2025 after a career in operations, consulting, and enterprise delivery, most recently as a Senior Manager at Amazon Web Services leading a team of Customer Solutions Managers. He had never written a line of production code before January 2026. He has now shipped production code on two applications inside the methodology the book describes, and is the primary author of the chapter (Chapter 8) that argues the methodology's central claim about who gets to build software next. Casey lives in Claremore, Oklahoma.

**Glenn Knepp** is the Chief Executive Officer and Chief Technology Officer of Alchemaize and a co-author of *Continuous Intent Delivery*. He is a career software engineer and engineering leader whose prior work includes senior technical roles at startups and at AWS. He is the Verification Owner on the founding team, the author of the acceptance-contract templates used across the hundred-day case study, and the primary author of the chapters on verification and compliance. Glenn lives in College Station, Texas.

The three of us founded Alchemaize in August 2025. We have never shared an office. We do not plan to.

\newpage

# Colophon

*Field Report from the First Hundred Days* was drafted in Markdown, typeset with pandoc, and produced as a PDF for the Leanpub and GitHub distribution. Cover and interior typography uses Inter, Instrument Serif, and JetBrains Mono.

The report is released under Creative Commons BY-NC-SA 4.0. You may share, adapt, and build on the material non-commercially with attribution. The full text of the license is at `creativecommons.org/licenses/by-nc-sa/4.0`.

Source repository: `github.com/alchemaize/field-report-v0`
Landing: `alchemaize.ai/field-report`
Leanpub: pay-what-you-like, $0 minimum

This is v0.1 — a draft release. v1.0 accompanies the Manning MEAP launch in late July / early August 2026, with corrections and the first round of reader feedback incorporated.

— DK, CR, GK
Alchemaize
April 2026
