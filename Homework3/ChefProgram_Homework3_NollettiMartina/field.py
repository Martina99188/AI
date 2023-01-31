import numpy as np


class Field:

    # I see if it's an external wall, so it's walls that define where the playing field ends.
    @staticmethod
    def external_wall(row, column):
        return (row == 0 and column == 4) or (row == 1 and column == 4) or (row == 2 and column == 4) \
               or (row == 3 and column == 4) or row < 0 or row >= 4 or column < 0 or column >= 9

    # I see if it is a wall inside the playing field.
    @staticmethod
    def internal_wall():
        return [
            (0, 0, 'below'),
            (0, 7, 'below'),
            (0, 8, 'below'),
            (1, 0, 'above'),
            (1, 0, 'right'),
            (1, 1, 'left'),
            (1, 1, 'below'),
            (1, 2, 'below'),
            (1, 6, 'right'),
            (1, 7, 'above'),
            (1, 7, 'left'),
            (1, 8, 'above'),
            (2, 0, 'below'),
            (2, 1, 'above'),
            (2, 1, 'below'),
            (2, 2, 'above'),
            (2, 6, 'right'),
            (2, 7, 'left'),
            (2, 7, 'below'),
            (3, 0, 'above'),
            (3, 1, 'above'),
            (3, 7, 'above')
        ]

    # I check if in a certain cell there is the object that I need to take.
    @staticmethod
    def tool_for_cook(row, column):
        return (row, column) == (1, 0) or (row, column) == (1, 7)

    # I set the initial position of the agent.
    @staticmethod
    def starting_cell():
        row = np.random.randint(4)
        column = np.random.randint(9)
        while Field.external_wall(row, column) or Field.tool_for_cook(row, column):
            row = np.random.randint(4)
            column = np.random.randint(9)
        return row, column, False

    # Arrive at the final cell to cook.
    @staticmethod
    def final_state(state):
        return state == (0, 7, True)
