from copy import deepcopy
##from date import datetime


class Puzzle():
    'Represents a sudoku puzzle and manipulates it'

    idealset = set(range(1,10))

    def __init__(self, new_puzzle: bool = True):
        self.puzzle = self._set_puzzle(new_puzzle)
        self.solution = deepcopy(self.puzzle)
        
##        self.solution = deepcopy(self.puzzle)
##        time = datetime.now()
##        self.solve_BruteForce()
##        time = datetime.now() - time

    def _set_puzzle(self, new_puzzle:bool = True):
        '''Creates new puzzle
        Input puzzle row by row no spaces, blank for empty slot.
        If new_puzzle == False, a default puzzle is used'''
        if (new_puzzle):
            temp_puzzle = list()
            for row in range(9):
                inp = input(f"Input row {row + 1}: ")
                while (len(inp) != 9):
                    inp = input(f"Input row {row + 1}: ")
                temp_row = list()
                for char in inp:
                    temp_row.append(char)                    
                temp_puzzle.append(temp_row)
                
        else:
            temp_puzzle = [[2,8,' ',3,4,5,9,7,6],
                           [5,6,3,9,7,2,4,1,8],
                           [7,4,9,8,6,' ',5,2,3],
                           [3,1,4,2,8,9,6,5,7],
                           [8,5,2,7,3,6,1,9,4],
                           [6,9,' ',5,1,4,3,8,2],
                           [4,2,6,1,9,8,7,3,5],
                           [9,3,5,6,2,7,8,4,1],
                           [1,7,8,4,5,3,2,6,9]]
##            self.puzzle = [[2,8,1,3,4,5,9,7,6],
##                           [5,6,3,9,7,2,4,1,8],
##                           [7,4,9,8,6,1,5,2,3],
##                           [3,1,4,2,8,9,6,5,7],
##                           [8,5,2,7,3,6,1,9,4],
##                           [6,9,7,5,1,4,3,8,2],
##                           [4,2,6,1,9,8,7,3,5],
##                           [9,3,5,6,2,7,8,4,1],
##                           [1,7,8,4,5,3,2,6,9]]
        return temp_puzzle

    def solve_BruteForce(self, r=0, c=0):
        '''Solve Brute Force method:
        Iterates through puzzle in search of empty spots and fills
        them recursively with a number in range 1-9. Upon every recursion
        the puzzle is checked if it meets the 'solution' requirements.'''
        if self.is_solution():
            return True

        while r < 9:
            while c < 9:
                if self.puzzle[r][c] == ' ':
                    self.solution[r][c] = 0
                    while self.solution[r][c] < 9:
                        self.solution[r][c] += 1
                        if self.solve_BruteForce((r + ((c + 1) // 9)), (c + 1) % 9):
                            return True
                c += 1
            r += 1
            c = 0
        return False

    ######\/##### 
    def is_solution(self):
        if (self.rowtest() == True) and (self.coltest() == True) and (self.blocktest() == True):
            return True
        else:
            return False
        
    # Helpers
    def rowtest(self):
        for row in self.solution:
            if set(row) != self.idealset:
                return False
        return True
    
    def coltest(self):
        for col in range(9):
            tempcol = set()
##            for row in range(9):
##                tempcol.add(self.solution[row][col])
            for row in self.solution:
                tempcol.add(row[col])
            if tempcol != self.idealset:
                return False
        return True

    def blocktest(self):
        for iblock in range(3):
            for jblock in range(3):
                tempset = set()
                for row in range(3):
                    for col in range(3):
                        tempset.add(self.solution[iblock*3 + row][jblock*3 + col])
                if tempset != self.idealset:
                    return False
        return True
    ######/\#####

    def print_puzzle(self):
        print("Puzzle:   ")
        for row in range(9):
            if ((row % 3 == 0) and (row != 0)):
                print("-----------------------------------", end='\n')
            for col in range(9):
                if ((((col + 1) % 3) == 0) and (col != 0)):
                    print(f'{self.puzzle[row][col]} | ', end = '')
                else:
                    print(f'{self.puzzle[row][col]}   ', end = '')
            print('', end = '\n')

    def print_solution(self):
        # if self.solution == None:
        #     print('Not solved')
        #     return 
        print("Solution:    ")
        for row in range(9):
            if ((row % 3 == 0) and (row != 0)):
                print("-----------------------------------", end='\n')
            for col in range(9):
                if ((((col + 1) % 3) == 0) and (col != 0)):
                    print(f'{self.solution[row][col]} | ', end = '')
                else:
                    print(f'{self.solution[row][col]}   ', end = '')
            print('', end = '\n')

