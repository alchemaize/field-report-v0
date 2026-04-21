# Part VI. Chapter 8 Excerpts (Casey's Voice)

*From the book-in-progress,* Continuous Intent Delivery. *Chapter 8:* Field Report from the Test Pilot. *Primary author: Casey Robinson. Full chapter runs 7,500 to 8,500 words in the book. This excerpt reproduces Sections 1, 2, and 4 at compressed length, preserving the full voice.*

---

## 1. Who I am and what I'm not

I'm six-four and bearded and I look like I should be running a trucking company. That's relevant context, not a joke. When I walk into a meeting with David, people in the room sometimes assume he's the consultant and I'm his security. The assumption isn't unreasonable if all you have to go on is what I look like. I mention it because what I'm going to tell you in this chapter is that the thing I do for a living now is author the specifications for production software that runs against real customer data, and if you'd told me on the day I was hired that this would be part of my job, I would have laughed and asked what the actual job was.

The actual job, as posted, was COO. Chief operating officer of a then-three-person startup that was heads-down building a product called Ember. My background isn't engineering. It's consulting, customer service, operations, and Agile delivery, carried long enough that it's the shape my career has. For the year before Alchemaize I was at Amazon Web Services at the Senior Manager level, leading a team of Customer Solutions Managers. If you haven't encountered the role, a CSM at AWS is the person who stands in the seam between an enterprise customer and the technical capability they're trying to adopt. You guide the migration. You hold the plan together. You translate between the customer's internal politics and the technology's actual shape. A lot of it happens in Agile ceremonies, because that's the format enterprise delivery has mostly settled into. You don't write production code. That was my world for the immediate stretch before this one, and variations of it have been my world for most of my working life.

I say all of that so the rest of the chapter lands cleanly. I've been in software-delivery rooms for twenty years. I've run Agile programs. I've written requirements, backlogs, acceptance criteria, operating playbooks, and customer-facing documentation that had to survive a lawyer reading it. What I haven't done is write code. Not a little on the side. Not a year of bootcamp in my thirties. None. I don't know what a closure is. I know what a database is but I couldn't, at risk of my salary, tell you the difference between a B-tree index and a hash index. I've gotten good at reading Glenn's code review comments closely enough to tell when he's annoyed. That's a skill I had already developed in other jobs for other reasons.

I didn't come to Alchemaize planning to be anything other than the person who kept the company's operations intact while David and Glenn built Ember. That was the plan when I was hired. The plan didn't hold. I'm going to tell you in this chapter what happened instead.

Here's the fact this chapter is in the book to explain. In the hundred days covered by this book, I personally shipped production code, first on an app called thetradecodex.com, then on a cash-flow projection product called Finaize, without David or Glenn touching the code I shipped. I did it under a methodology David and Glenn had been building but hadn't yet named; the naming came after they watched me do it repeatedly. The methodology is what the rest of the book is about. This chapter is what it looked like from where I was sitting.

## 2. The day David asked me to write a spec instead of a wish list

It was a Monday in early January. A few things had just happened at the company. Ember, the product I'd been hired to help launch, had shipped its MVP the month before in December. The Series A push I'd been brought on to run was visible on the calendar. And in the week or two before this Monday, David and Glenn had decided to restructure how we built software, full stop. They'd reached a conclusion neither of them had expected to reach when the year started. The shape of software development itself was changing, at their desks, in real time, and Alchemaize was going to bet on the change rather than work around it.

On this Monday, David called me. We're a fully distributed company (David in Brentwood, Glenn in College Station, me in Claremore, no office, no shared zip code), and the serious conversations happen over video. When I picked up the call he said we needed to talk about something different.

The something different was that he and Glenn had been watching their own development speed up by an order of magnitude, and the speedup had surfaced a claim they couldn't yet verify. The claim was that the skills the speedup rewarded weren't the skills the old methodology had rewarded. The bottleneck had moved from typing to specification and verification, and a person whose career was about clarifying intent rather than implementing it could, given the right framework, ship production software. They weren't asking me this as a favor. They were asking because the claim was part of a bigger argument they were building, and I was the only non-engineer on the founding team. If the claim wasn't true, they needed to know now, not later.

I said I'd try. I figured I'd probably fail and we'd all learn something. I was wrong about the first part.

The first thing David asked me to do was write down what I wanted one specific piece of software to do. He was precise about the framing. He didn't ask me to "write the requirements." He didn't ask me to "describe the feature." He said: write down what you want it to do, in a way specific enough that a machine couldn't possibly misinterpret you, and test it by imagining the machine that could.

I'd been asked to write requirements documents before. I'd even been pretty good at it, in the context I'd been asked to do it. The context was writing requirements for human software engineers who would read the document, fill in the parts I was vague about from their own professional judgment, and produce something approximately correct. That's what requirements documents had always been for, in my experience. They were a rough sketch. The engineer then did the real work of completing them.

David was asking for something different. He was asking for the sketch to stand alone.

The first VOS I wrote took me four hours and was, Glenn later told me, very bad. He rejected three of its four acceptance contracts the next morning. He was right about two of them. The third he was wrong about, and I said so, and we argued for twenty minutes, and he came around.

The second VOS took me two hours. The third took me an hour and a half. By the fifth I was writing them in about forty-five minutes. By the tenth I was writing them in under an hour and the rejection rate was low enough that we stopped paying attention to it as a signal.

Here's what I want to tell you, and it isn't inspirational, it's practical. The skill of writing a VOS isn't the skill of writing code. It's the skill of knowing, precisely, what you want, and being willing to say it in a way that can't be negotiated. Those are two distinct skills. The second is harder than it sounds, because most of us spend our working lives writing descriptions of things that are deliberately fuzzy so they can be negotiated later. We call that diplomacy. We call it leaving room for the engineer's judgment. We call it not being prescriptive. Those are all real things, and in other contexts they're the right things.

What a VOS asks for is the opposite of diplomacy. It asks for a specification that would look rude in an email.

Writing a VOS is the practice of saying what you want.

It took me about three weeks to get reasonably good at it.

## 4. Three things that surprised me

Three things I didn't expect, because I think they're what matter most for a reader in roughly the position I was in.

**The first thing that surprised me** is that what people had told me was "technical" about software, for my whole career, turned out to be mostly about clarity. I'd been told for years I didn't understand software "because I didn't have the technical background." What I found, doing this work, is that almost every conversation I'd had with a software engineer where I'd been made to feel I didn't understand was actually a conversation where the engineer and I had different levels of precision about what we were trying to accomplish. Precision isn't technical. Precision is a discipline of writing. I've been writing operations memos for twenty years. I've got more practice at precision than the average software engineer, as long as the subject is one I understand. What a product needs to do is a subject I understand.

**The second thing that surprised me** is that what I'd been told was "easy" turned out to be clarity's opposite. I'd been told, over the years, that certain things were easy. Just add a button. Just show it in a list. Just tweak the copy. Every one of those things has collapsed under me at least once this sprint. "Just tweak the copy" is a vague VOS that produces plausible but wrong code. "Change the error message on the reconciliation failure from 'Unable to reconcile' to 'Some transactions could not be categorized; click here to review them' whenever the failing cases include at least one uncategorized transaction, otherwise keep the current message" is a VOS that produces correct code. The difference is fifty words. But those fifty words are the whole job.

**The third thing that surprised me** is this, and I debated whether to include it, and David and Glenn both said to include it, so here it is.

I was sitting at the kitchen table at my house in Claremore at some point in February, on a Saturday, working on a VOS for the Finaize application. The VOS had to do with how reports got exported. I'd been working on it for about three hours. The kitchen was quiet. My wife was out with our daughter. I hit return on a commit and the VOS shipped. A few minutes later my phone buzzed. It was an automated notification from the Finaize analytics saying the report-export feature had been used seventeen times in the last hour by customers in production.

That was when I realized I'd shipped production software that people were using. Me. The guy hired to run operations. The guy who looks like he should be moving desks.

I sat at the kitchen table for a minute and didn't do anything. I wasn't emotional about it. I was quiet, the way you get quiet when a thing you thought you understood about yourself turns out to be differently shaped. I've always understood myself as a person who enables the people who build things. I've spent my career enabling people to build things. I'm good at it. I like it. What I realized, sitting there, was that the methodology hadn't turned me into someone who builds things differently. It had taken the thing I already did, being precise about what a business needs software to do, and made it into something that could produce software directly, without being translated by someone else first.

The translation step was what had separated me from software for twenty years. The translation step was gone.

I sat at the kitchen table a little longer. Then I got up and made coffee and went back to work.

---

*End of excerpt. Section 3, the full worked example, and Section 5, the closing argument to non-engineering readers, are in the book. The full Chapter 8 is the first full-length chapter Manning will ship in the MEAP.*
