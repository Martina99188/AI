from learning import Learning
from field import Field


# write the results in a file txt.
def write(path):
    open('pathForCook.txt', 'w').close()
    f = open('pathForCook.txt', 'a')
    f.write('(row, column, tool_for_cook) \n')
    for step in path:
        f.write(f'{step} \n')
    f.close()


def main():
    learning = Learning()
    learning.train()

    # initial cell.
    cell = Field.starting_cell()
    # agent's path.
    path = learning.path(cell)
    write(path)


if __name__ == '__main__':
    main()
