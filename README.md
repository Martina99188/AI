## AI

# The Cooking Chef Problem
Consider the case where the agent is your personal Chef.
In particular, the agent (the smiley on the map) wants to cook the eggs recipe according to your
indication (scrambled or pudding).

In order to cook the desired recipe, the agent must first collect the needed tools (the egg beater on the
map). Then he must reach the stove (the frying pan or the oven on the map). Finally, he can cook.
Not that there are two special interlinked cells (marked with the G) that allow the agent to go from
one side of the map to the other. But to do so, the agent needs to express his will to go on the other
side.

Cells in (4, 1) and (6, 1) are the special gate ones. They allow the agent to go from one side of the
map to another. Those two special cells are interlinked, but the agent needs to express his will to go
on the other side (Left or Right).
Since you have a lot hungry, it is fundamental that the agent cooks the eggs accordingly to your taste
(scrambled/pudding) as fast as he can without letting you wait for more than necessary.



Figure 1: A particular instance of the cooking Chef problem. The goal is for the agent currently
located in state (4, 3) to have a policy that always leads to cooking the eggs in location (4, 4) or (8, 4).
Cells in (4, 1) and (6, 1) are the special gate ones.

In order to apply optimal control techniques such as value iteration, you need to model the aforementioned scenario as an MDP. Recall that an MDP is defined as tuple (S, A, P, R, γ), where:

+ S: The (finite) set of all possible states.
+ A: The (finite) set of all possible actions.
+ P: The transition function P : S × S × A → [0, 1], which maps (s0,s,a) to P(s0|s,a), i.e., the probability of transitioning to state s0 ∈ S when taking action a ∈ A in state s ∈ S. Note that P s0 ∈ S P(s0|s,a) = 1 for all s ∈ S, a ∈ A.
R: The reward function R : S × A × S → R, which maps (s,a,s0) to R(s,a,s0), i.e., the reward obtained when taking action a ∈ A in state s ∈ S and arriving at state s0 ∈ S.
γ: The discount factor, which controls how important are rewards in the future.

In order to encode this problem as an MDP, you need to define each of the components of the tuple
for our particular problem. Note that there may be many different possible encodings (specify it on
the report).

To answer the questions, consider the instance shown in Figure 1:
• In the figure, the agent is at (4, 3) (but it can start at any of the grid cells).
• The agent needed cooking tools as the egg beater is in position (1, 3) and (8, 3).
• There are two different final goals, displayed as the frying pan is in position (1, 4) and the oven in position (8, 4).
• Cells in (4, 1) and (6, 1) are the special gate ones. They allow the agent to go from one side of the map to another. Those two special cells are interlinked, but the agent needs to express his will to go on the other side.
• The agent is not able to move diagonally.
• Walls are represented by thick black lines.
• The agent cannot move through walls.
• An episode will end when the agent successfully cooks the scrambled eggs (see the above description).
