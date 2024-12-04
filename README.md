# Sudoku Solver

## Overview
`Sudoku_Solver` is a Python-based application that solves Sudoku puzzles using brute-force and optimized brute-force algorithms. This project provides a class-based abstraction of Sudoku puzzles and offers multiple solving methods with detailed insights into performance.

## Features
- Input puzzles manually or use a default example puzzle.
- Two solving methods:
  - **Brute Force**: A straightforward backtracking algorithm.
  - **Brute Force Improved**: Optimized backtracking that checks for validity before attempting placement.
- Validates solutions using Sudoku rules:
  - Each row, column, and 3x3 subgrid must contain numbers 1–9 without repetition.
- Tracks and displays time taken to solve puzzles.
- Easy-to-read display of puzzles and solutions.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/matek-dev/Sudoku_Solver.git

2. Navigate to the project directory:
   ```bash
   cd Sudoku_Solver

### Usage
1. Create a Puzzle object:
   ```python
   from sudoku_solver import Puzzle
   puzzle = Puzzle(new_puzzle=True)  # Create a new puzzle
   ```
   - Custom: Enter the puzzle row by row when prompted, using 0 for blank cells.
   - Default: Use Puzzle(new_puzzle=False).

2. Solve the puzzle:
   ```python
   puzzle.solve(type="BruteForce")  # Or "BruteForceImproved"

3. Print the puzzle and solution:
   ```python
   puzzle.print_puzzle()
   puzzle.print_solution()

### Example
```python
from sudoku_solver import Puzzle

# Create a puzzle using the default board
puzzle = Puzzle(new_puzzle=False)

# Print the unsolved puzzle
puzzle.print_puzzle()

# Solve the puzzle with the improved brute force algorithm
puzzle.solve(type="BruteForceImproved")

# Print the solution
puzzle.print_solution()
```

### Sample Output
Unsolved Puzzle:
```
2   8     | 3   4   5 | 9   7   6 |
5   6   3 | 9   7   2 | 4   1   8 |
7   4   9 | 8   6     | 5       3 |
-----------------------------------
3   1     | 2   8   9 | 6   5   7 |
8   5   2 | 7   3     | 1   9   4 |
6   9   7 | 5   1   4 | 3   8   2 |
-----------------------------------
4   2   6 | 1   9     | 7   3   5 |
    3   5 | 6   2   7 | 8       1 |
1   7   8 | 4   5   3 | 2   6   9 |
```

Solved Puzzle:
```
2   8   1 | 3   4   5 | 9   7   6 |
5   6   3 | 9   7   2 | 4   1   8 |
7   4   9 | 8   6   1 | 5   2   3 |
-----------------------------------
3   1   4 | 2   8   9 | 6   5   7 |
8   5   2 | 7   3   6 | 1   9   4 |
6   9   7 | 5   1   4 | 3   8   2 |
-----------------------------------
4   2   6 | 1   9   8 | 7   3   5 |
9   3   5 | 6   2   7 | 8   4   1 |
1   7   8 | 4   5   3 | 2   6   9 |
```

## Class and Methods
`Puzzle`

Methods:
- `__init__(new_puzzle: bool = True)`

  Initializes the puzzle with a new input or default example. Default: `True`.

- `solve(type: str = 'BruteForceImproved)`

  Solves the puzzle using the specified method. Default: `BruteForceImproved`.

- `print_puzzle()`

  Prints the unsolved puzzle in a readable format.

- `print_solution()`

  Prints the solved puzzle or indicates that no solution exists.


## Future Enhancements
- Implement additional solving algorithms like Constraint Propagation and Dancing Links (leveraging Knuth's Algorithm X).
- Add a graphical interface for easier puzzle input and visualization.
- Support importing puzzles from text files.
