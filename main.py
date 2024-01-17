# This code is a Sudoku Solver by Back Tracking Algorithm

# Import libraries and functions from other files
from tkinter import *
import tkinter
from solver import solver
from Grids import generateeasy
from Grids import generatenormal
from Grids import generatehard

# Build a root and customize size and color and header text
root = Tk()
root.title("Sudoku Solver")
root.geometry("324x600")
root.configure(background="#111111")

# Write a label and make text boxes
label = tkinter.Label(root, text="\nFill in the numbers and click solve\n Also this app can generate sudoku\n "
                        "Choose level\n\n Developers: Shakiba Nazari & Mahdi Alikhani\n",
                        bg="#111111", fg="#ffc905").grid(row=0, column=1, columnspan=10)

errLabel = tkinter.Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = tkinter.Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

# Function for validate numbers
def ValidateNumber(P):
    out = (P.isdigit or P == "") and len(P) < 2
    return out

reg = root.register(ValidateNumber)

# Make 3*3 Grid
# O(n^2)
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e

# Customize 9*9 grid color
# O(n^2)
def draw9x9Grid():
    color = "#f39c12"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#f39c12":
                color = "#98a148"
            else:
                color = "#f39c12"

# Function for clear the grid
# O(n^2)
def clearValues():
    errLabel.configure(text="", fg="orange")
    solvedLabel.configure(text="", fg="orange")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

# Function for getting grid after solving and update grid board
# O(n^2)
def getValues():
    board = []
    errLabel.configure(text="", fg="orange")
    solvedLabel.configure(text="", fg="orange")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    updateValues(board)
    return board

# Functions for generate random sudokus in three levels: easy/normal/hard
# O(n^2)
def updateValuese():
    sol = generateeasy()
    for rows in range(2, 11):
        for col in range(1, 10):
            cells[(rows, col)].delete(0, "end")
            cells[(rows, col)].insert(0, sol[rows - 2][col - 1])

# O(n^2)
def updateValuesn():
    sol = generatenormal()
    for rows in range(2, 11):
        for col in range(1, 10):
            cells[(rows, col)].delete(0, "end")
            cells[(rows, col)].insert(0, sol[rows - 2][col - 1])

# O(n^2)
def updateValuesh():
    sol = generatehard()
    for rows in range(2, 11):
        for col in range(1, 10):
            cells[(rows, col)].delete(0, "end")
            cells[(rows, col)].insert(0, sol[rows - 2][col - 1])

# Customize buttons
btn = Button(root, command=getValues, text="Solve", bg="#98a148", fg="#111111", width=10)
btn.grid(row=13, column=0, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", bg="#98a148", fg="#111111", width=10)
btn.grid(row=13, column=3, columnspan=5, pady=20)

btn = Button(root, command=quit, text="Exit", bg="#98a148", fg="#111111", width=10)
btn.grid(row=13, column=6, columnspan=5, pady=20)

btn = Button(root, command=updateValuese, text="Easy", bg="#98a148", fg="#111111", width=10)
btn.grid(row=14, column=0, columnspan=5, pady=20)

btn = Button(root, command=updateValuesn, text="Normal", bg="#98a148", fg="#111111", width=10)
btn.grid(row=14, column=3, columnspan=5, pady=20)

btn = Button(root, command=updateValuesh, text="Hard", bg="#98a148", fg="#111111", width=10)
btn.grid(row=14, column=6, columnspan=5, pady=20)

# Function for update sudoku and show it
# O(n^2)
def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
        solvedLabel.configure(text="Sudoku solved!")
    else:
        errLabel.configure(text="No solution exists for this sudoku")

draw9x9Grid()
root.mainloop()