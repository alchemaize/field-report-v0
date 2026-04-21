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
