from copy import deepcopy
##from date import datetime


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


    def __solve_BruteForce(self, r=0, c=0):
        '''Solve Brute Force method:
        Iterates through puzzle in search of empty spots and fills
        them recursively with a number in range 1-9. Upon every recursion
        the puzzle is checked if it meets the 'solution' requirements.'''
        if self.__is_solution():
            return True

        while r < 9:
            while c < 9:
                if self.__puzzle[r][c] == ' ':
                    self.__solution[r][c] = 0
                    while self.__solution[r][c] < 9:
                        self.__solution[r][c] += 1
                        if self.__solve_BruteForce((r + ((c + 1) // 9)), (c + 1) % 9):
                            return True
                c += 1
            r += 1
            c = 0
        return False

    ######\/##### 
    def __is_solution(self):
        if (self.__rowtest() == True) and (self.__coltest() == True) and (self.__blocktest() == True):
            return True
        else:
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
##            for row in range(9):
##                tempcol.add(self.solution[row][col])
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

    def solve(self, type:str=None):
        '''
        Solve the puzzle with desired method.
        ...
        Methods: 
        - Brute Force (backtracking)
        - in progress
        '''
        
        if type == None:
            type = 'BruteForce'
        self.__solution = deepcopy(self.__puzzle)
        if type == 'BruteForce':
            if not self.__solve_BruteForce():
                self.__solution = False
            self.print_solution()

    def print_puzzle(self):
        print("Puzzle:   ")
        for row in range(9):
            if ((row % 3 == 0) and (row != 0)):
                print("-----------------------------------", end='\n')
            for col in range(9):
                if ((((col + 1) % 3) == 0) and (col != 0)):
                    print(f'{self.__puzzle[row][col]} | ', end = '')
                else:
                    print(f'{self.__puzzle[row][col]}   ', end = '')
            print('', end = '\n')

    def print_solution(self):
        if None == self.__solution:
            print('Not solved. Use the .solve() method and try again.')
            return 
        elif False == self.__solution:
            print('No solution to this puzzle.')
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

