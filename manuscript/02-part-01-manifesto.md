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
