## Question

How would the approach towards designing the **wildcard policy** change if the agent was allowed to **loop around** the grid?  
That is, taking a right step on the right-most cell transports the agent to the left-most cell (and vice versa).

---

## Change in Environment Structure

With wrap-around, the 1D GridWorld changes from a line to a ring:

- Every state has exactly two neighbors.
- All states are topologically symmetric.
- The notion of “left end”, “right end”, or “center” disappears.

In a looped world:
- There are no walls to detect.
- Reversing direction provides no useful information.
- Any boundary-based or center-seeking strategy becomes meaningless.

Thus, position-based heuristics should be abandoned.

---

The best fixed strategy is to:

- Pick left or right at the start of the episode.
- Continue moving in that direction forever.
- Eventually, the agent will pass through every state exactly once per loop.

This minimizes expected time to reach the goal.
