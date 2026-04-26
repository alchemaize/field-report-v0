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

The first is *intent*. Specifying, unambiguously and completely enough that a machine can act on it, what you actually want the software to do. In the old world we called this requirements engineering and treated it as a ten-percent activity because typing was the ninety-percent. In the new world, intent clarity is the dominant input to output quality. If you're any good at this work now, you've already noticed it. The difference between an AI tool that does what you wanted and an AI tool that does some plausible thing you did not want is almost always a difference in the specification going in. There's no prompt-engineering trick that compensates for intent that was vague from the start.

The second is *verification*. Knowing, with reasonable confidence, that the code you shipped does what you intended it to do. In the old world we called this quality assurance and treated it as a downstream activity because typing was the expensive middle. In the new world, verification is the structural guarantee of the whole pipeline. If you cannot verify, you cannot ship at any speed, because shipping unverified AI output is a distinct and self-amplifying form of disaster, one this book will name specifically in a later chapter.

The bottleneck didn't go away. It moved. The typing step got cheap. The intent step and the verification step got dominant.

The implication, if you let it land, is that every framework currently in use at your company was designed for a bottleneck that no longer exists. That's a structural observation, not a polemical one. The thing Scrum's machinery is best at, coordinating the cost of human typing across a sprint, is no longer the cost that matters. The thing SAFe's machinery is best at, coordinating hundreds of human typists at ten-week resolution, is coordinating something that doesn't need to be coordinated anymore. Not as a criticism of the typists. As a statement about who's typing, which is now the machine.

The frameworks have become friction.

That's the structural observation of this book. Everything that follows, the methodology, the roles, the metrics, the adoption path, is an attempt to answer the question that opens up the moment you accept that observation. What, then, is the thing we should be building our organizations around?

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

*Excerpt ends. The full chapter continues through "The proof that the inversion holds," "A working definition," "A note from the Verification Owner" (Glenn's voice), "Who this book is for," and "The road ahead," closing with Casey's Field Note. Available in the full-length book.*
