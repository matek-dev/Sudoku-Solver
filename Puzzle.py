from copy import deepcopy
from datetime import datetime

class Puzzle():
    '''Sudoku Puzzle abstraction
    ...
    Methods:
    - print_puzzle()
    - print_solution()
    - solve(type=None)
    '''

    __idealset = set(range(1,10))

    def __init__(self, new_puzzle: bool = True):
        self.__puzzle = self.__set_puzzle(new_puzzle)
        self.__solution = None

    def __set_puzzle(self, new_puzzle:bool = True):
        '''Creates new puzzle
        Input puzzle row by row no spaces, blank for empty slot.
        If new_puzzle == False, a default puzzle is used'''
        if (new_puzzle):
            temp_puzzle = list()
            for row in range(9):
                inp = input(f"Input row {row + 1}: ")
                while (len(inp) != 9 or not inp.isdigit()):
                    inp = input(f"Input row {row + 1}: ")
                temp_row = list()
                for char in inp:
                    temp_row.append(int(char))                    
                temp_puzzle.append(temp_row)
                
        else:
            temp_puzzle = [[2,8,0,3,4,5,9,7,6],
                           [5,6,3,9,7,2,4,1,8],
                           [7,4,9,8,6,0,5,0,3],
                           [3,1,0,2,8,9,6,5,7],
                           [8,5,2,7,3,0,1,9,4],
                           [6,9,7,5,1,4,3,8,2],
                           [4,2,6,1,9,0,7,3,5],
                           [0,3,5,6,2,7,8,0,1],
                           [1,7,8,4,5,3,2,6,9]]
##                          [[2,8,1,3,4,5,9,7,6],
##                           [5,6,3,9,7,2,4,1,8],
##                           [7,4,9,8,6,1,5,2,3],
##                           [3,1,4,2,8,9,6,5,7],
##                           [8,5,2,7,3,6,1,9,4],
##                           [6,9,7,5,1,4,3,8,2],
##                           [4,2,6,1,9,8,7,3,5],
##                           [9,3,5,6,2,7,8,4,1],
##                           [1,7,8,4,5,3,2,6,9]]
        return temp_puzzle


    def __solve_BruteForce(self):
        '''Solve Brute Force method:
        Iterates through puzzle in search of empty spots and fills
        them recursively with a number in range 1-9. Upon every recursion
        the puzzle is checked if it meets the 'solution' requirements.'''
        if self.__is_solution():
            return True
        for r in range(9):
            for c in range(9):
                if self.__solution[r][c] == 0:
                    for i in range(1,10):
                        self.__solution[r][c] = i
                        if self.__solve_BruteForce():
                            return True
                        self.__solution[r][c] = 0
        return False

    
    def __solve_BruteForceImproved(self):
        '''Solve Brute Force method with efficiency:
        Iterates through puzzle in search of empty spots and fills
        them recursively with a VALID number in range 1-9. Upon every recursion
        the puzzle is checked if it meets the 'solution' requirements.'''
        if self.__is_solution():
            return True
        for r in range(9):
            for c in range(9):
                if self.__solution[r][c] == 0:
                    for i in range(1,10):
                        if self.__is_valid(r,c,i):
                            self.__solution[r][c] = i
                            if self.__solve_BruteForceImproved():
                                return True
                            self.__solution[r][c] = 0
        return False
    

    def __is_valid(self, r, c, num):
        # Check if number is in row, column, or 3x3 subblock
        transposed = list(zip(*self.__solution))
        if num in self.__solution[r] or num in transposed[c]:
            return False
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if self.__solution[start_row + i][start_col + j] == num:
                    return False
        return True

    ######\/##### 
    def __is_solution(self):
        if (self.__rowtest() == True) and (self.__coltest() == True) and (self.__blocktest() == True):
            return True
        return False
        
    # Helpers
    def __rowtest(self):
        for row in self.__solution:
            if set(row) != self.__idealset:
                return False
        return True
    
    def __coltest(self):
        for col in range(9):
            tempcol = set()
            for row in self.__solution:
                tempcol.add(row[col])
            if tempcol != self.__idealset:
                return False
        return True

    def __blocktest(self):
        for iblock in range(3):
            for jblock in range(3):
                tempset = set()
                for row in range(3):
                    for col in range(3):
                        tempset.add(self.__solution[iblock*3 + row][jblock*3 + col])
                if tempset != self.__idealset:
                    return False
        return True
    ######/\#####

    def __del__(self):
        print("Puzzle has been deleted from memory")

    def solve(self, type:str='BruteForceImproved'):
        '''
        Solve the puzzle with desired method.
        ...
        Methods: 
        - Brute Force (backtracking)
        - in progress
        '''
        dt0 = datetime.now()
        self.__solution = deepcopy(self.__puzzle)
        if type == 'BruteForce':
            print('Solving Brute Force')
            if not self.__solve_BruteForce():
                self.__solution = False
        if type == 'BruteForceImproved':
            print('Solving Brute Force Improved')
            if not self.__solve_BruteForceImproved():
                self.__solution = False
        print('Time to solve: ', datetime.now() - dt0)
        self.print_solution()

    def print_puzzle(self):
        print("Puzzle:   ")
        for row in range(9):
            if ((row % 3 == 0) and (row != 0)):
                print("-----------------------------------", end='\n')
            for col in range(9):
                char = self.__puzzle[row][col] if self.__puzzle[row][col] != 0 else ' '
                if ((((col + 1) % 3) == 0) and (col != 0)):
                    print(f'{char} | ', end = '')
                else:
                    print(f'{char}   ', end = '')
            print('', end = '\n')

    def print_solution(self):
        if None == self.__solution:
            print('Not solved. Use the .solve() method and try again.')
            return 
        elif False == self.__solution:
            print('No solution to this puzzle.')
            return
        print("Solution:    ")
        for row in range(9):
            if ((row % 3 == 0) and (row != 0)):
                print("-----------------------------------", end='\n')
            for col in range(9):
                if ((((col + 1) % 3) == 0) and (col != 0)):
                    print(f'{self.__solution[row][col]} | ', end = '')
                else:
                    print(f'{self.__solution[row][col]}   ', end = '')
            print('', end = '\n')
