from collections import defaultdict
import random
from field import Field


class Learning:

    # definition of states, actions and rewards.
    def __init__(self):
        self.states = [(row, column, tool) for row in range(0, 4) for column in range(0, 9) for tool in [True, False]]
        self.actions = ["above", "below", "left", "right"]
        self.rewards = {"final": 10, "tool": 1, "not_final": -0.5, "wall": -150}
        d_dict = defaultdict(lambda: defaultdict(float))
        for state in self.states:
            for action in self.actions:
                d_dict[state][action] = random.uniform(-0.1, 0.1)
        self.d_dict = d_dict

    # select an action at random.
    def action(self, state, epsilon):
        if random.uniform(0, 1) < epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions, key=lambda action: self.d_dict[state][action])

    def do_action(self, state, action):
        row, column, tool = state

        if (row, column, action) in Field.internal_wall():
            return state, self.rewards['wall']

        match action:
            case 'above':
                row -= 1
            case 'below':
                row += 1
            case 'left':
                column -= 1
            case 'right':
                column += 1

        # if the previous cell is the teleport cell
        if (row, column) == (3, 4):
            if action == 'left':
                column -= 1
            if action == 'right':
                column += 1

        if Field.external_wall(row, column):
            return state, self.rewards["wall"]

        # you are in the cell of the oven
        if (row, column) == (0, 7):
            if tool:
                return (row, column, tool), self.rewards["final"]
            else:
                return (row, column, tool), self.rewards["not_final"]

        if Field.tool_for_cook(row, column) and not tool:
            return (row, column, True), self.rewards["tool"]
        else:
            return (row, column, tool), self.rewards["not_final"]

    def update_new_value(self, state, action, next_state, reward, alpha, gamma):
        # alpha is the learning rate while gamma is the discount factor
        old_value = self.d_dict[state][action]
        max_move = max(self.actions, key=lambda action: self.d_dict[next_state][action])
        new_value = self.d_dict[next_state][max_move]
        self.d_dict[state][action] = old_value + alpha * (reward + (gamma * new_value) - old_value)

    def train(self):
        for try_path in range(10000):
            print(f'Try {try_path}:')
            state = Field.starting_cell()
            path = [state]
            while not Field.final_state(state):
                action = self.action(state, 0.1)
                next_state, reward = self.do_action(state, action)
                self.update_new_value(state, action, next_state, reward, 0.8, 1.0)
                path.append(next_state)
                state = next_state
            print(path)

    def path(self, state):
        path = [state]
        while not Field.final_state(state):
            action = self.action(state, 0.0)
            next_state, reward = self.do_action(state, action)
            path.append(next_state)
            state = next_state
        return path


