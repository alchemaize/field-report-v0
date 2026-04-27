# Part II. How CID Works

## What this part is for

The rest of Part II describes CID in enough depth that you can argue with it. It introduces the three roles, the four-stage pipeline plus parallel watching layer, the unit of work, and the four metrics that replace the velocity dashboard. It doesn't give you enough to run the methodology inside an organization. That's in the book.

The asymmetry is deliberate. An argument has to be made in public. The practice of running a method has to be taught carefully. This report does the first. The book does the second.

## The four-stage pipeline and the watching layer

CID is a pipeline, not a sprint. There's no fixed cadence. It runs at the pace verification allows. The pipeline is per-VOS, forward flow, with two reverse edges for fast correction. Observation runs as a parallel watching layer alongside, against the deployed inventory, and seeds new intents at the head of the stream.

**1. Intent.** A human, the Intent Engineer, writes a specification of what should be built. The specification is a VOS, a Verifiable Outcome Slice, and it's the unit of work in the methodology. A VOS has five sections: WHY, WHAT, HOW, CONTEXT, OUTCOME. We describe them below.

**2. Context.** The Intent Engineer curates four to fifteen files from the existing codebase that matter for the slice. This isn't a prompt. It's a reading list. The skill of choosing the right files, in the right configuration, is the single largest determinant of AI output quality in the methodology. More than the prompt. More than the model.

**3. Generation.** The AI Orchestrator hands the VOS plus the curated context to a generation layer (Claude, GPT, Cursor, Kiro, whatever the team has chosen) and watches the run. The AI Orchestrator's job isn't to type. It's to manage the generation session, catch drift, redirect on misinterpretation, and throw a slice out and restart if the generation heads somewhere wrong.

**4. Verification.** The Verification Owner runs the acceptance contract from the VOS against the generated code. The contract is executable. It either passes or it doesn't. If it doesn't, the slice goes back to the Intent Engineer with notes. The Verification Owner doesn't report to the delivery chain. Their job is to say no.

**5. Observation.** The slice ships. Production telemetry confirms, or fails to confirm, that the outcome described in the VOS was actually produced for real users. Observation watches the slice in production from the parallel watching layer. The shipped slice is terminal. When observation surfaces actionable signal, it seeds a fresh VOS at the head of the pipeline.

The pipeline is continuous. It doesn't run once per sprint. It runs as fast as the verification step can be honored, typically several slices per day per Intent Engineer once the pod has matured.

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

We include one full worked VOS (the deal-jacket assembly slice Casey shipped on Finaize) in Part IV. The book has ten more and an appendix of templates.

## The four metrics

CID replaces the velocity dashboard with four numbers. A CTO or VP of Engineering can read the entire engineering organization in thirty seconds using them. We introduce the four briefly here; the book walks through the diagnostic combinations.

**1. Cycle time.** Time from VOS written to slice shipped to production. In the case study, cycle time ran roughly 4 to 18 hours for team-owned slices, and 1 to 4 days for the handful of slices that required deep architectural work.

**2. First-pass verification rate.** Percent of slices that pass the acceptance contract on the first generation attempt. This is the single most diagnostic number in the methodology. Low first-pass rate means vague VOSes, weak context curation, or both. High first-pass rate means the pod is mature. In our case study, this number ran 30 to 50 percent in the first two weeks and rose to 80 to 95 percent by week eight.

**3. Outcome KPI delta.** Change in the business metric the OUTCOME section predicted, measured against a baseline. This is the number a CEO cares about. It's also the only one of the four that measures whether the methodology is producing value rather than throughput.

**4. Cost per shipped intent.** Total cost (people, inference, infrastructure) divided by the number of VOSes that shipped and passed observation. Inference cost is usually a decimal point on this number. The other costs are where the real math lives.

No velocity. No burndown. No story points. Four numbers, reviewed once a month for ninety minutes. The book has a full chapter on the monthly review.
