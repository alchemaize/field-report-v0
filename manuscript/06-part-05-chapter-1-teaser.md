# Part V. Chapter 1 Teaser

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 1:* The Shift. *Primary author: David Kim. This excerpt runs about 3,000 words, roughly the first half of the chapter. The full chapter runs about 6,850 words, closing with a Field Note in Casey's voice.*

---

## The Shift

Casey shipped his forty-second VOS of the quarter late on a Tuesday in February. He was working from his desk in a converted den in Claremore, Oklahoma, three states from either of his co-founders, neither of whom Alchemaize has ever asked him to share a room with. Close to midnight. The house was quiet. He typed a two-word commit message, pressed return, stood up, stretched, and noticed the coffee on his desk had gone cold at some point he didn't remember.

Walking down the hall to the kitchen, he realized a few things in no particular order. He hadn't been to a standup in three weeks. Nobody on the founding team had noticed. Nobody on the founding team cared, not because they were negligent but because there was no longer anything a standup would be for. And the way he'd understood software development to work, the way he'd watched every company he'd ever worked in do it, no longer described what he was doing at his desk.

The last thing he realized, a minute later at the counter, was that he isn't a software engineer, has never been one, and yet the thing he'd shipped was running in production against a real API, serving real users, and would keep serving them tomorrow.

This book is about that Tuesday.

It's also about the thing that Tuesday implies, which is that a twenty-five-year consensus about how software gets made is over. Over the next eighty thousand words we make that case. First as an argument. Then as a methodology. Then as a set of enterprise practices. And finally, in a chapter Casey wrote himself, as a lived experience. By the end we'll have done something the current literature on AI and software development hasn't yet done. We'll have described what replaces Scrum.

Say that plainly. A lot of what follows depends on it. This book isn't "AI and agile, together at last." It isn't "how to add prompt engineering to your sprint." It isn't one of the genuine and useful books being written right now about how to use AI coding tools more effectively inside an otherwise unchanged software-engineering practice. Those books have their place. This isn't that book.

The argument in your hands is that the software-engineering practice itself has to change, because the constraint it was designed for is gone, and the constraint it now faces isn't one any existing framework was built to hold.

The rest of this chapter is the case for that sentence. The rest of the book is what to do about it.

## The bottleneck moved

For twenty-five years, every method for building software at scale has been organized around the same assumption. Humans are the bottleneck at the implementation step. Typing code is slow, expensive, and error-prone, and a framework's job is to coordinate humans around that typing so their output gets used well.

Every framework you know, descended from every framework that preceded it, is a solution to that problem. Waterfall said plan exhaustively up front, because typing is the long pole and mistakes are expensive to rewrite. Scrum said slice the work into two-week increments, because typing is still the long pole but requirements change faster than the plan. Extreme Programming said pair the typists so they catch each other's errors in real time. Kanban said limit concurrent typing so throughput doesn't collapse under context-switching. SAFe said coordinate large groups of typists at ten-week resolution so the organization can plan. DevOps said automate everything around the typing that isn't typing, so the typists can concentrate on the typing. Continuous Delivery said the typing is fine; what happens after the typing is broken.

Every one of those is a careful, well-engineered answer to the same question. Typing is expensive; how do we organize an organization around that fact?

That question stopped being the right one.

It isn't exactly that AI has made typing free, though in some meaningful sense it has. It's that the step between a human specification and running code, the step we used to call implementation or coding or, on a bad day, "cutting the ticket," has become, in the hands of a competent operator, roughly the cheapest step in the pipeline. Not the fastest, not the most interesting, just the cheapest. Which is another way of saying the one that isn't worth organizing around anymore.

It isn't precisely free, of course. Model-inference cost exists. Verification cost exists. Operator time exists. The time it takes to write a specification well, which turns out to be the real expense, exists. But those aren't typing costs. They're the costs of the other steps, the ones that used to look cheap because typing dominated them. When the dominant cost is removed from a system, the structure of the system doesn't stay the same. It shifts to fit the new dominant cost.

Two costs, not one, on either side of the old bottleneck.

The first is intent. Specifying, completely enough that a machine can act on it, what you actually want the software to do. In the old world we called this requirements engineering, and treated it as a ten-percent activity because typing was the ninety-percent. In the new world, intent clarity is the dominant input to output quality. If you're any good at this work now, you've already noticed. The difference between an AI tool that does what you wanted and an AI tool that does some plausible thing that isn't what you wanted is almost always a difference in the specification going in. No prompt-engineering trick compensates for intent that was vague from the start.

The second is verification. Knowing, with reasonable confidence, that the code you shipped does what you intended. In the old world we called this quality assurance and treated it as a downstream activity because typing was the expensive middle. In the new world, verification is what keeps the whole pipeline honest. If you can't verify, you can't ship at any speed, because shipping unverified AI output is a distinct, self-amplifying form of disaster, one a later chapter names specifically.

The bottleneck didn't go away. It moved, permanently, from the typing step (which got cheap) to intent and verification (which got dominant).

If you let this land, the consequence is difficult. Every framework in use at your company was designed for a bottleneck that isn't there anymore. Not as a light criticism, but as a structural fact. What Scrum's machinery is best at, coordinating the cost of human typing across a sprint, is no longer the cost that matters. What SAFe's machinery is best at, coordinating hundreds of human typists at ten-week resolution, is coordinating something that doesn't need to be coordinated at that resolution anymore. Not because the typists are bad. Because the machine is doing the typing.

The frameworks have become friction.

That's the observation the rest of the book rests on. Everything that follows, the methodology, the roles, the metrics, the adoption path, is an attempt to answer the question that opens up once you accept it. What should we build our organizations around instead?

## A concession

"The frameworks have become friction" is the kind of sentence that can sound glib, and I've been in this industry long enough to know what happens when a new methodology talks about the old one that way. A third of the reader stops reading, having heard it three times this year. Another third reads defensively. The rest read with the enthusiasm of people who'd been waiting for permission to say it out loud. None of those three is the reader I'm writing for. I'm writing for the one who's weighing what is actually being claimed.

So. Scrum was a reasonable answer to a real problem. SAFe was a reasonable scaling of it. The individual practices these frameworks advocated (the standup, the retro, the sprint review, the Program Increment) were not absurd. They were, and in many contexts still are, the best answer a careful engineering culture ever gave to the question of how to organize humans whose typing was the long pole.

The criticism isn't that the frameworks were wrong then. The criticism is that the condition they were designed for isn't the condition we're in anymore. A design rational under one constraint becomes an impediment under a different constraint. That's how engineering works. That's how, for that matter, software works.

When a later chapter takes a scalpel to the specific thirty-two hours of ceremony a Scrum team currently pays per sprint, and demonstrates that the same coordination function can be done in thirty minutes a week under the new constraint, please read it the way I intend. Not as a criticism of Scrum the framework. As a description of the structural cost of running a machine calibrated for one constraint in a world that has moved to another.

The book isn't gleeful about this. The book is trying to be right.

## The new constraint and what it demands

If the bottleneck has moved to intent and verification, a method for building software at scale under the new constraint has to be organized around those two things. That's the whole design brief. The rest is details.

A useful way to see this is to notice what hasn't changed.

Business outcomes haven't changed. You still need to know what you're trying to build and why. What has changed is that you need to write it down with more precision than you did before, because something is going to act on it without the soft rails of a twenty-year-old engineering team's shared context. The intent specification isn't a communication artifact between humans who already know most of the answer. It's an input to an actor that doesn't know the answer and will act on whatever you give it.

Users haven't changed. You still need to verify that what you built works for them. What has changed is that you need to verify more, earlier, and continuously, because the output is arriving faster than a QA process built for human-speed generation can keep up with. The verification step hasn't been bypassed. It's been inverted: brought upstream of generation, made continuous, made the guarantee rather than the downstream check.

Organizations haven't changed. You still need to decide what to fund and why. What has changed is that the unit of funding, the project with its fixed scope and schedule and deliverable, was an instrument built for a world in which humans were the constraint and scope was negotiable. The new constraint wants a different instrument.

The methodology you'll meet in the next chapters builds from those three observations. It's called Continuous Intent Delivery, CID at the team layer, ELCID at the enterprise layer, and the rest of this book is what that means, how it works, what it costs, and how you adopt it. But the design move is already visible. The methodology is organized around what became dominant (intent clarity, verification rigor, and outcome-based funding), not around what became cheap (typing).

The slogan form is: *Intent is the artifact. Code is the exhaust.*

It's worth being precise about what that means, because the sentence does a lot of work and shows up in later chapters more than once. It doesn't mean code is unimportant. Of course code is important; it's what runs. It means something specific. The artifact humans should author, version, review, argue over, maintain, and treat as the organization's durable knowledge is the specification of intent. Not the generated implementation. The code is what comes out the other end when the specification is right. The code is, in a reasonable sense, the predictable output of a well-run pipeline, not the creative output of a human act.

---

*Excerpt ends. The full chapter continues through "The proof that the inversion holds," "A quick definition, and then the road map," "A note from the Verification Owner" (Glenn's voice), "Who this book is for," and "The road ahead," closing with Casey's Field Note. Available in the full-length book.*
