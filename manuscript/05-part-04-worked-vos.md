# Part IV. One Worked VOS

## The deal-jacket assembly slice

To show what a VOS actually looks like, we reproduce one here in abbreviated form. It's a VOS Casey wrote in late February, against the Finaize application, for a feature called Deal Jacket Document Assembly.

The WHY and WHAT are reproduced in full. The HOW, CONTEXT, and OUTCOME are summarized. Appendix B of the book walks a different VOS end to end (the Trade Journal VOS, Casey's first, on TradeCodex), with annotations on each section and a second worked example showing what an eddy looks like when verification sends a VOS back. The two examples together cover both a clean first-pass shipment and a contract revision, which is the wider range a reader will encounter.

---

**VOS-FNZ-087. Deal Jacket Document Assembly.**

*Intent Engineer: Casey Robinson. Verification Owner: Glenn Knepp. AI Orchestrator: David Kim. Authored 2026-02-24. Shipped 2026-02-27.*

### WHY

A dealership F&I manager relies on this application to assemble the complete set of documents for a closed deal. If the jacket is missing a required disclosure for the customer's state of purchase, the dealership is exposed to compliance risk and the customer has not been properly informed. This slice ensures we either produce a complete jacket or refuse to mark the deal as closed.

### WHAT

The acceptance contract is written in Gherkin. A condensed version:

```gherkin
Feature: Deal jacket must include all required disclosures for state of purchase

  Scenario: Complete jacket marks deal as closeable
    Given a completed F&I transaction in state S
    And all required disclosure documents for state S are present
    When the jacket is assembled
    Then the jacket is marked "Complete"
    And the deal status allows closing

  Scenario: Incomplete jacket blocks closing
    Given a completed F&I transaction in state S
    And one or more required disclosure documents for state S are missing
    When the jacket is assembled
    Then the jacket is NOT marked "Complete"
    And the error banner displays "Missing required disclosures"
    And the banner lists each missing document by name

  Scenario: Disclosure requirements are state-specific
    Given any completed F&I transaction
    When the jacket assembly runs
    Then the required-document check uses the disclosure rules
      for the customer's state of purchase, not a generic list
```

### HOW (summarized)

Use the existing deal-structuring pipeline. Add a disclosure-check step at the pipeline's tail. Surface the error state through the existing error-banner component. No new UI components.

### CONTEXT (summarized)

Four files:

- `lib/finaize/deal-structuring.ts`, the deal-structuring module.
- `components/finaize/JacketDisplay.tsx`, the jacket display component.
- `components/ui/ErrorBanner.tsx`, the error-banner component.
- `lib/finaize/state-disclosure-rules.ts`, the state-specific disclosure rules utility.

### OUTCOME (summarized)

Incomplete-jacket rate visible to F&I managers drops to zero over the next billing cycle, because any jacket we can't verify as complete, we don't mark closeable. Compliance-related escalations drop by at least 80 percent week over week.

### What happened

The system generated the code in about six minutes. The pull request passed all unit tests on the first run, and passed the acceptance contract on the first run. Glenn signed the contract. The slice deployed to production on Thursday, February 27, around 3pm Central. On Friday the 28th, the ops team reported zero new incomplete-jacket escalations for the first time in a rolling seven-day window. The OUTCOME prediction held.

Casey's description of writing this VOS, and of realizing that the skill required was one he'd been practicing for twenty years in other jobs, is in Section 3 of the Chapter 8 excerpt in Part VI.
