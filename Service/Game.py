import random
from typing import List

from Entity.Board import Board
from Entity.Values.DifficultyLevel import DifficultyLevel
from Entity.AssistCondition import AssistCondition

class Game:
    def __init__(self, board: Board, difficulty_level: DifficultyLevel):
        self.board = board
        self.remaining_hint: int = 3
        self.difficulty_level = difficulty_level
        board.complete_answer = self.generateSudoku()
        board.puzzle = self.createPuzzle(self.board.complete_answer, self.difficulty_level)
        self.solved = True

    def generateSudoku(self):
        base = 3
        side = base * base

        def pattern(r,c): return (base * (r % base) + r // base + c) % side

        from random import sample
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g * base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g * base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1, base * base + 1))

        answer: List[List[int]] = [ [nums[pattern(r, c)] for c in cols] for r in rows ]
        return answer

    def createPuzzle(self, answer, difficulty_level: DifficultyLevel):
        def init_subgrid_constraint(value):
            numbers: List[int] = []

            if difficulty_level == DifficultyLevel.HARD:
                for i in range(9):
                    numbers.append(random.randint(value["bottom"], value["top"]))

                remaining_sum = 17 - sum(numbers)

                while remaining_sum > 0:
                    index = random.randint(0, 8)
                    if numbers[index] < 3:
                        if numbers[index] == 2:
                            numbers[index] += 1
                            remaining_sum -= 1
                        if numbers[index] == 1:
                            num = random.randint(1, 2)
                            if remaining_sum - num >= 0:
                                numbers[index] += num
                                remaining_sum -= num
                        if numbers[index] == 0:
                            num = random.randint(1, 3)
                            if remaining_sum - num >= 0:
                                numbers[index] += num
                                remaining_sum -= num
            else: 
                bottom: int = value["bottom"]
                top: int = value["top"]
                for i in range(9):
                    numbers.append(random.randint(value["bottom"], value["top"]))    

            random.shuffle(numbers)

            return numbers

        subgrid_constraint: List[int] = init_subgrid_constraint(difficulty_level.value)

        puzzle: List[List[int]] = [
            [], [], [], [], [], [], [], [], []
        ]

        for i in range(9):
            for j in range(9):
                puzzle[i].append(answer[i][j])           

        constraint_counter = 0
        for i in range(3):
            for j in range(3):
                indexes_to_remove = random.sample(range(9), 9 - subgrid_constraint[constraint_counter])
                for k in range(len(indexes_to_remove)):
                    if indexes_to_remove[k] == 0:
                        puzzle[0 + 3 * i][0 + 3 * j] = 0
                    elif indexes_to_remove[k] == 1:
                        puzzle[0 + 3 * i][1 + 3 * j] = 0
                    elif indexes_to_remove[k] == 2:
                        puzzle[0 + 3 * i][2 + 3 * j] = 0
                    elif indexes_to_remove[k] == 3:
                        puzzle[1 + 3 * i][0 + 3 * j] = 0
                    elif indexes_to_remove[k] == 4:
                        puzzle[1 + 3 * i][1 + 3 * j] = 0
                    elif indexes_to_remove[k] == 5:
                        puzzle[1 + 3 * i][2 + 3 * j] = 0
                    elif indexes_to_remove[k] == 6:
                        puzzle[2 + 3 * i][0 + 3 * j] = 0
                    elif indexes_to_remove[k] == 7:
                        puzzle[2 + 3 * i][1 + 3 * j] = 0
                    elif indexes_to_remove[k] == 8:
                        puzzle[2 + 3 * i][2 + 3 * j] = 0

                constraint_counter += 1

        return puzzle

    def findMistake(self, i: int, j: int):
        return self.board.puzzle[i][j] != self.board.complete_answer[i][j]
    
    # Buat sistem scoring yang lebih adil
    def countScore(self, completion_time: int, assist_condition: AssistCondition, help_remaining):
        result: int = 10000 * 1 / completion_time * 100
        sub_percentage: int = 0

        if assist_condition.highlightAnswer:
            sub_percentage += 5
        if assist_condition.highlightSameDigit:
            sub_percentage += 7
        if assist_condition.incorrectAnswer:
            sub_percentage += 10

        if help_remaining != 3:
            sub_percentage += 20

        if (
            assist_condition.highlightAnswer and 
            assist_condition.highlightSameDigit and 
            assist_condition.incorrectAnswer
            ):
            sub_percentage += 15
        elif (
            (assist_condition.highlightAnswer and assist_condition.highlightSameDigit) or 
            (assist_condition.highlightAnswer and assist_condition.highlightSameDigit) or 
            (assist_condition.highlightSameDigit and assist_condition.highlightSameDigit)
            ):
            sub_percentage += 10

        result -= result * sub_percentage / 100
        return int(result)