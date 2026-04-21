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
