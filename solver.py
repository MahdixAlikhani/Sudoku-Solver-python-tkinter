# Build empty grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Make a list for get any number
listnumber = list()

# Function for check the number is in this row, column or 3*3 grid or not
# O(n^2)
def valid_move(grid, row, column, number):
    if number in grid[row]:
        return False

    for x in range(9):
        if grid[x][column] == number:
            return False

    corner_row = row - (row % 3)
    corner_column = column - (column % 3)

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_column + y] == number:
                return False

    return True

# Function for increase cells, rows and columns and then put the number in cells
# O(n)
def solving(grid, row, column):
    if column == 9:
        if row == 8:
            return True
        else:
            row += 1
            column = 0

    if grid[row][column] > 0:
        return solving(grid, row, column + 1)

    for number in range(1, 10):
        if valid_move(grid, row, column, number):
            grid[row][column] = number

            listnumber.append(number)

            if solving(grid, row, column + 1):
                return True

        grid[row][column] = 0

    return False

# Function for return grid to main file
# O(n)
def solver(grid):
    if solving(grid, 0, 0):
        for i in range(0, len(listnumber), 20):
            print(listnumber[i:i + 20])
        return grid
    else:
        return "no"