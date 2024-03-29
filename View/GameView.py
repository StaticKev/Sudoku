from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QTimer
from Entity.Board import Board
from Entity.Stopwatch import Stopwatch
from Entity.AssistCondition import AssistCondition
from Entity.Values.DifficultyLevel import DifficultyLevel
from Service.Game import Game
import random
from typing import List
from View.PauseView import PauseView
from View.SolvedView import SolvedView
from PyQt5.QtWidgets import QDialog

class GameView(QDialog):
    def __init__(self, widget, difficulty_level: DifficultyLevel, assist_condition: AssistCondition, score_manager, topScoreUpdateFunc):
        super(GameView, self).__init__()
        self.setupUi(self)
        self.widget = widget
        self.score_manager = score_manager
        self.topScoreUpdate_func = topScoreUpdateFunc

        self.game: Game = Game(Board(), difficulty_level)
        self.stopwatch: Stopwatch = Stopwatch(parent = self)
        self.chosen_number: str = "0"
        self.previous_choosen_number: str = "0"
        self.assist = assist_condition
        self.clickable: List[List[bool]] = [
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False]
            ]

        self.colorAssets = {
            'light_blue': '#9cddff',
            'light_red': '#ff5b5b',
            'white': "#ffffff",
            'black': '#000000'
        }

        def freezeButton(puzzle, clickable):
                for i in range(9):
                    for j in range(9):
                        if puzzle[i][j] == 0:
                            clickable[i][j] = True

        def showInitial(puzzle, clickable):
            for i in range(9):
                for j in range(9):
                    button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                    if clickable[i][j] == False:
                        button.setText(str(puzzle[i][j]))
                        
        def initButtonStyle(clickable):
            if self.assist.highlightAnswer:
                for i in range(9):
                    for j in range(9):
                        button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                        if clickable[i][j] == False:
                            button.setStyleSheet(
                                "background-color: white; "
                                "color: black; "
                                "border: 2px grey; "
                                "padding: 5px; " 
                                "border-radius: 5px;"
                            )
                        else:
                            button.setStyleSheet(
                                f"background-color: {self.colorAssets['light_blue']}; "
                                "color: black; "
                                "border: 2px grey; "
                                "padding: 5px; " 
                                "border-radius: 5px;"
                            )
            else:
                for i in range(9):
                    for j in range(9):
                        button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                        button.setStyleSheet(
                        "background-color: white; "
                        "color: black; "
                        "border: 2px grey; "
                        "padding: 5px; " 
                        "border-radius: 5px;"
                        )

        freezeButton(self.game.board.puzzle, self.clickable)
        showInitial(self.game.board.puzzle, self.clickable)
        initButtonStyle(self.clickable)

        ##################################### PRINT ANSWER #####################################
        for kunci in self.game.board.complete_answer:
            print(kunci)
        print("")
        ########################################################################################
            
        self.stopwatch.timer.timeout.connect(self.updateTimeSignature)
        self.stopwatch.timer.start(1000)

        self.checkButton.clicked.connect(self.checkResult)
        self.backButton.clicked.connect(self.backToMainMenu)
        self.restartButton.clicked.connect(self.restartGame)
        self.hintButton.clicked.connect(self.generateHint)
        self.pauseButton.clicked.connect(self.pauseGame)

        self.answerButton_1.clicked.connect(lambda: self.chooseNumber("1", self.previous_choosen_number))
        self.answerButton_2.clicked.connect(lambda: self.chooseNumber("2", self.previous_choosen_number))
        self.answerButton_3.clicked.connect(lambda: self.chooseNumber("3", self.previous_choosen_number))
        self.answerButton_4.clicked.connect(lambda: self.chooseNumber("4", self.previous_choosen_number))
        self.answerButton_5.clicked.connect(lambda: self.chooseNumber("5", self.previous_choosen_number))
        self.answerButton_6.clicked.connect(lambda: self.chooseNumber("6", self.previous_choosen_number))
        self.answerButton_7.clicked.connect(lambda: self.chooseNumber("7", self.previous_choosen_number))
        self.answerButton_8.clicked.connect(lambda: self.chooseNumber("8", self.previous_choosen_number))
        self.answerButton_9.clicked.connect(lambda: self.chooseNumber("9", self.previous_choosen_number))
        self.answerButton_0.clicked.connect(lambda: self.chooseNumber("0", self.previous_choosen_number))

        # Mengisi kotak
        self.grid_11.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 0))
        self.grid_12.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 1))
        self.grid_13.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 2))
        self.grid_14.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 3))
        self.grid_15.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 4))
        self.grid_16.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 5))
        self.grid_17.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 6))
        self.grid_18.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 7))
        self.grid_19.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 0, 8))
        self.grid_21.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 0))
        self.grid_22.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 1))
        self.grid_23.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 2))
        self.grid_24.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 3))
        self.grid_25.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 4))
        self.grid_26.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 5))
        self.grid_27.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 6))
        self.grid_28.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 7))
        self.grid_29.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 1, 8))
        self.grid_31.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 0))
        self.grid_32.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 1))
        self.grid_33.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 2))
        self.grid_34.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 3))
        self.grid_35.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 4))
        self.grid_36.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 5))
        self.grid_37.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 6))
        self.grid_38.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 7))
        self.grid_39.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 2, 8))
        self.grid_41.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 0))
        self.grid_42.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 1))
        self.grid_43.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 2))
        self.grid_44.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 3))
        self.grid_45.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 4))
        self.grid_46.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 5))
        self.grid_47.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 6))
        self.grid_48.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 7))
        self.grid_49.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 3, 8))
        self.grid_51.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 0))
        self.grid_52.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 1))
        self.grid_53.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 2))
        self.grid_54.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 3))
        self.grid_55.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 4))
        self.grid_56.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 5))
        self.grid_57.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 6))
        self.grid_58.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 7))
        self.grid_59.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 4, 8))
        self.grid_61.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 0))
        self.grid_62.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 1))
        self.grid_63.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 2))
        self.grid_64.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 3))
        self.grid_65.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 4))
        self.grid_66.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 5))
        self.grid_67.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 6))
        self.grid_68.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 7))
        self.grid_69.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 5, 8))
        self.grid_71.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 0))
        self.grid_72.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 1))
        self.grid_73.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 2))
        self.grid_74.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 3))
        self.grid_75.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 4))
        self.grid_76.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 5))
        self.grid_77.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 6))
        self.grid_78.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 7))
        self.grid_79.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 6, 8))
        self.grid_81.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 0))
        self.grid_82.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 1))
        self.grid_83.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 2))
        self.grid_84.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 3))
        self.grid_85.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 4))
        self.grid_86.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 5))
        self.grid_87.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 6))
        self.grid_88.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 7))
        self.grid_89.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 7, 8))
        self.grid_91.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 0))
        self.grid_92.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 1))
        self.grid_93.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 2))
        self.grid_94.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 3))
        self.grid_95.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 4))
        self.grid_96.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 5))
        self.grid_97.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 6))
        self.grid_98.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 7))
        self.grid_99.clicked.connect(lambda: self.onBoxClick(self.chosen_number, 8, 8))

    def backToMainMenu(self):
        self.stopwatch.stop()
        self.stopwatch.timer.deleteLater()
        widget_to_remove = self.widget.widget(4)
        widget_to_remove.deleteLater()
        self.widget.removeWidget(widget_to_remove)
        self.widget.setCurrentIndex(0)
        self.close()

    def chooseNumber(self, num, previousNum):
        self.chosen_number = num
        curr_option_button = self.findChild(QPushButton, f"answerButton_{num}")
        prev_option_button = self.findChild(QPushButton, f"answerButton_{previousNum}")
        prev_option_button.setStyleSheet('font-weight: normal;') 
        curr_option_button.setStyleSheet('font-weight: bold;') 

        bg_color_to_set = self.colorAssets['white']
        if self.assist.highlightAnswer:
            bg_color_to_set = self.colorAssets['light_blue']

        if self.assist.highlightSameDigit:
            if previousNum != num:
                for col in range(9):
                    for row in range(9):
                        button = self.findChild(QPushButton, f"grid_{row + 1}{col + 1}")
                        button_bg_color = button.palette().color(button.backgroundRole()).name()
                        if str(self.game.board.puzzle[row][col]) == previousNum:
                            if self.clickable[row][col]:
                                if self.assist.highlightAnswer:
                                    if button_bg_color == self.colorAssets['light_red']:
                                        button.setStyleSheet(
                                            f"background-color: {self.colorAssets['light_red']}; "
                                            "color: black; "
                                            "border: 2px grey; "
                                            "padding: 5px; " 
                                            "border-radius: 5px;"
                                        )
                                    else:
                                        button.setStyleSheet(
                                            f"background-color: {bg_color_to_set}; "
                                            "color: black; "
                                            "border: 2px grey; "
                                            "padding: 5px; " 
                                            "border-radius: 5px;"
                                        )
                            else:
                                button.setStyleSheet(
                                    f"background-color: {self.colorAssets['white']}; "
                                    "color: black; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"
                                )
                        elif str(self.game.board.puzzle[row][col]) == num:
                            if self.clickable[row][col]:
                                if self.assist.highlightAnswer:
                                    if button_bg_color == self.colorAssets['light_red']:
                                        button.setStyleSheet(
                                            f"background-color: {self.colorAssets['light_red']}; "
                                            "color: black; "
                                            "font-weight: bold; "
                                            "border: 2px grey; "
                                            "padding: 5px; " 
                                            "border-radius: 5px;"
                                        )
                                    else:
                                        button.setStyleSheet(
                                            f"background-color: {bg_color_to_set}; "
                                            "color: black; "
                                            "font-weight: bold; "
                                            "border: 2px grey; "
                                            "padding: 5px; " 
                                            "border-radius: 5px;"
                                        )
                            else:
                                button.setStyleSheet(
                                    f"background-color: {self.colorAssets['white']}; "
                                    "color: black; "
                                    "font-weight: bold; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"
                                )
        self.previous_choosen_number = num

    def onBoxClick(self, num, col, row):
        if self.clickable[col][row]:
            button = self.sender()
            if num == "0":
                button.setText("")
            else:
                button_bg_color = button.palette().color(button.backgroundRole()).name()
                bg_color_to_set = self.colorAssets['white']
                if self.assist.highlightAnswer:
                    bg_color_to_set = self.colorAssets['light_blue']
                
                if button_bg_color == self.colorAssets['light_red']:
                    if self.assist.highlightSameDigit:
                        button.setStyleSheet(
                            f"background-color: {self.colorAssets['light_red']}; "
                            "font-weight: bold; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )
                    else:
                        button.setStyleSheet(
                            f"background-color: {self.colorAssets['light_red']}; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )
                else:
                    if self.assist.highlightSameDigit:
                        button.setStyleSheet(
                            f"background-color: {bg_color_to_set}; "
                            "font-weight: bold; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )
                    else:
                        button.setStyleSheet(
                            f"background-color: {bg_color_to_set}; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )
                button.setText(num)
            self.game.board.puzzle[col][row] = int(num)

    def updateTimeSignature(self):
        self.stopwatch.updateStopwatch()
        self.timeSignature.setText(self.stopwatch.time_taken_in_text)

    def generateHint(self): 
        if self.game.remaining_hint != 0:
            clickable_box: List[List[int]] = []
            for row in range(9):
                for col in range(9):
                    if self.clickable[row][col]:
                        clickable_box.append([row, col])
            
            while True:
                if len(clickable_box) == 0:
                    break
                box_coord = random.randint(0, len(clickable_box) - 1)
                row = clickable_box[box_coord][0]
                col = clickable_box[box_coord][1]

                if self.game.board.puzzle[row][col] == 0:
                    self.game.board.puzzle[row][col] = self.game.board.complete_answer[row][col]
                    button = self.findChild(QPushButton, f"grid_{row + 1}{col + 1}")
                    button_bg_color = button.palette().color(button.backgroundRole()).name()

                    bg_color_to_set = self.colorAssets['white']
                    if self.assist.highlightAnswer:
                        bg_color_to_set = self.colorAssets['light_blue']

                    if button_bg_color == self.colorAssets['light_red']:
                        if self.assist.highlightAnswer and self.chosen_number == str(self.game.board.complete_answer[row][col]):
                            button.setStyleSheet(
                                    "background-color: #FF5B5B; "
                                    "font-weight: bold; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"                            
                                    )
                        else:
                            button.setStyleSheet(
                                    "background-color: #FF5B5B; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"                            
                                    )
                    else:
                        if self.assist.highlightSameDigit and self.chosen_number == str(self.game.board.complete_answer[row][col]):
                            button.setStyleSheet(
                                    f"background-color: {bg_color_to_set}; "
                                    "font-weight: bold; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"                            
                                    ) 
                        else:
                            button.setStyleSheet(
                                    f"background-color: {bg_color_to_set}; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"                            
                                    ) 

                    button.setText(str(self.game.board.complete_answer[row][col]))
                    self.game.remaining_hint -= 1
                    self.hintButton.setText(f"Random Fill ({self.game.remaining_hint} left)")
                    break
                clickable_box.pop(box_coord)

    def restartGame(self):
        for i in range(9):
            for j in range(9):
                if self.clickable[i][j] == True:
                    self.game.board.puzzle[i][j] = 0
                    button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                    button.setText("")

    def pauseGame(self):
        self.stopwatch.stop()
        pause_view = PauseView(self.widget, self)
        self.widget.addWidget(pause_view) 
        self.widget.setCurrentIndex(5)
        self.hide()

    def checkResult(self):
        self.game.solved = True
        if self.assist.incorrectAnswer:
            for i in range(9):
                for j in range(9):
                    button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                    if self.game.findMistake(i, j):
                        self.game.solved = False
                        if self.assist.highlightSameDigit:
                            if str(self.game.board.puzzle[i][j]) == self.chosen_number:
                                button.setStyleSheet(
                                    "background-color: #FF5B5B; "
                                    "color: black; "
                                    "font-weight: bold; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"
                                    )
                            else:
                                button.setStyleSheet(
                                    "background-color: #FF5B5B; "
                                    "color: black; "
                                    "border: 2px grey; "
                                    "padding: 5px; " 
                                    "border-radius: 5px;"
                                    )

                        else:
                            button.setStyleSheet(
                                "background-color: #FF5B5B; "
                                "color: black; "
                                "border: 2px grey; "
                                "padding: 5px; " 
                                "border-radius: 5px;"
                                )
            QTimer.singleShot(3000, self.revertBackgroundChange)
        else:
            for i in range(9):
                for j in range(9):
                    if self.game.findMistake(i, j):
                        self.game.solved = False
        if self.game.solved: 
            self.stopwatch.stop()
            solved_view = SolvedView(self.widget, self, self.score_manager, self.topScoreUpdate_func)
            solved_view.score = self.game.countScore(self.stopwatch.getTimeInSec(), self.assist, self.game.remaining_hint)
            self.widget.addWidget(solved_view)
            self.widget.setCurrentIndex(5)
            self.hide()

    def revertBackgroundChange(self):
        bg_color_to_set = self.colorAssets['white']
        if self.assist.highlightAnswer:
            bg_color_to_set = self.colorAssets['light_blue']

        for i in range(9):
            for j in range(9):
                if self.clickable[i][j]:
                    button = self.findChild(QPushButton, f"grid_{i + 1}{j + 1}")
                    if self.assist.highlightSameDigit and str(self.game.board.puzzle[i][j]) == self.chosen_number:
                        button.setStyleSheet(
                            f"background-color: {bg_color_to_set}; "
                            "font-weight: bold; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )
                    else:
                        button.setStyleSheet(
                            f"background-color: {bg_color_to_set}; "
                            "border: 2px grey; "
                            "padding: 5px; " 
                            "border-radius: 5px;"
                        )

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 615)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 420, 271, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.AnswerButtonGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.AnswerButtonGrid.setContentsMargins(0, 0, 0, 0)
        self.AnswerButtonGrid.setObjectName("AnswerButtonGrid")
        self.answerButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_2.sizePolicy().hasHeightForWidth())
        self.answerButton_2.setSizePolicy(sizePolicy)
        self.answerButton_2.setObjectName("answerButton_2")
        self.AnswerButtonGrid.addWidget(self.answerButton_2, 0, 1, 1, 1)
        self.answerButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_1.sizePolicy().hasHeightForWidth())
        self.answerButton_1.setSizePolicy(sizePolicy)
        self.answerButton_1.setObjectName("answerButton_1")
        self.AnswerButtonGrid.addWidget(self.answerButton_1, 0, 0, 1, 1)
        self.answerButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_4.sizePolicy().hasHeightForWidth())
        self.answerButton_4.setSizePolicy(sizePolicy)
        self.answerButton_4.setObjectName("answerButton_4")
        self.AnswerButtonGrid.addWidget(self.answerButton_4, 0, 3, 1, 1)
        self.answerButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_5.sizePolicy().hasHeightForWidth())
        self.answerButton_5.setSizePolicy(sizePolicy)
        self.answerButton_5.setObjectName("answerButton_5")
        self.AnswerButtonGrid.addWidget(self.answerButton_5, 0, 4, 1, 1)
        self.answerButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_3.sizePolicy().hasHeightForWidth())
        self.answerButton_3.setSizePolicy(sizePolicy)
        self.answerButton_3.setObjectName("answerButton_3")
        self.AnswerButtonGrid.addWidget(self.answerButton_3, 0, 2, 1, 1)
        self.answerButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_0.sizePolicy().hasHeightForWidth())
        self.answerButton_0.setSizePolicy(sizePolicy)
        self.answerButton_0.setObjectName("answerButton_0")
        self.AnswerButtonGrid.addWidget(self.answerButton_0, 1, 4, 1, 1)
        self.answerButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_9.sizePolicy().hasHeightForWidth())
        self.answerButton_9.setSizePolicy(sizePolicy)
        self.answerButton_9.setObjectName("answerButton_9")
        self.AnswerButtonGrid.addWidget(self.answerButton_9, 1, 3, 1, 1)
        self.answerButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_8.sizePolicy().hasHeightForWidth())
        self.answerButton_8.setSizePolicy(sizePolicy)
        self.answerButton_8.setObjectName("answerButton_8")
        self.AnswerButtonGrid.addWidget(self.answerButton_8, 1, 2, 1, 1)
        self.answerButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_7.sizePolicy().hasHeightForWidth())
        self.answerButton_7.setSizePolicy(sizePolicy)
        self.answerButton_7.setObjectName("answerButton_7")
        self.AnswerButtonGrid.addWidget(self.answerButton_7, 1, 1, 1, 1)
        self.answerButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerButton_6.sizePolicy().hasHeightForWidth())
        self.answerButton_6.setSizePolicy(sizePolicy)
        self.answerButton_6.setObjectName("answerButton_6")
        self.AnswerButtonGrid.addWidget(self.answerButton_6, 1, 0, 1, 1)
        self.checkButton = QtWidgets.QPushButton(Dialog)
        self.checkButton.setGeometry(QtCore.QRect(200, 540, 61, 51))
        self.checkButton.setObjectName("checkButton")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(30, 70, 331, 331))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.Grid = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.Grid.setContentsMargins(0, 0, 0, 0)
        self.Grid.setObjectName("Grid")
        self.subGrid_8 = QtWidgets.QGridLayout()
        self.subGrid_8.setObjectName("subGrid_8")
        self.grid_94 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_94.sizePolicy().hasHeightForWidth())
        self.grid_94.setSizePolicy(sizePolicy)
        self.grid_94.setText("")
        self.grid_94.setObjectName("grid_94")
        self.subGrid_8.addWidget(self.grid_94, 2, 0, 1, 1)
        self.grid_95 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_95.sizePolicy().hasHeightForWidth())
        self.grid_95.setSizePolicy(sizePolicy)
        self.grid_95.setText("")
        self.grid_95.setObjectName("grid_95")
        self.subGrid_8.addWidget(self.grid_95, 2, 1, 1, 1)
        self.grid_75 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_75.sizePolicy().hasHeightForWidth())
        self.grid_75.setSizePolicy(sizePolicy)
        self.grid_75.setText("")
        self.grid_75.setObjectName("grid_75")
        self.subGrid_8.addWidget(self.grid_75, 0, 1, 1, 1)
        self.grid_96 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_96.sizePolicy().hasHeightForWidth())
        self.grid_96.setSizePolicy(sizePolicy)
        self.grid_96.setText("")
        self.grid_96.setObjectName("grid_96")
        self.subGrid_8.addWidget(self.grid_96, 2, 2, 1, 1)
        self.grid_76 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_76.sizePolicy().hasHeightForWidth())
        self.grid_76.setSizePolicy(sizePolicy)
        self.grid_76.setText("")
        self.grid_76.setObjectName("grid_76")
        self.subGrid_8.addWidget(self.grid_76, 0, 2, 1, 1)
        self.grid_84 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_84.sizePolicy().hasHeightForWidth())
        self.grid_84.setSizePolicy(sizePolicy)
        self.grid_84.setText("")
        self.grid_84.setObjectName("grid_84")
        self.subGrid_8.addWidget(self.grid_84, 1, 0, 1, 1)
        self.grid_86 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_86.sizePolicy().hasHeightForWidth())
        self.grid_86.setSizePolicy(sizePolicy)
        self.grid_86.setText("")
        self.grid_86.setObjectName("grid_86")
        self.subGrid_8.addWidget(self.grid_86, 1, 2, 1, 1)
        self.grid_74 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_74.sizePolicy().hasHeightForWidth())
        self.grid_74.setSizePolicy(sizePolicy)
        self.grid_74.setText("")
        self.grid_74.setObjectName("grid_74")
        self.subGrid_8.addWidget(self.grid_74, 0, 0, 1, 1)
        self.grid_85 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_85.sizePolicy().hasHeightForWidth())
        self.grid_85.setSizePolicy(sizePolicy)
        self.grid_85.setText("")
        self.grid_85.setObjectName("grid_85")
        self.subGrid_8.addWidget(self.grid_85, 1, 1, 1, 1)
        self.Grid.addLayout(self.subGrid_8, 4, 2, 1, 1)
        self.subGrid_2 = QtWidgets.QGridLayout()
        self.subGrid_2.setObjectName("subGrid_2")
        self.grid_16 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_16.sizePolicy().hasHeightForWidth())
        self.grid_16.setSizePolicy(sizePolicy)
        self.grid_16.setText("")
        self.grid_16.setObjectName("grid_16")
        self.subGrid_2.addWidget(self.grid_16, 0, 2, 1, 1)
        self.grid_24 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_24.sizePolicy().hasHeightForWidth())
        self.grid_24.setSizePolicy(sizePolicy)
        self.grid_24.setText("")
        self.grid_24.setObjectName("grid_24")
        self.subGrid_2.addWidget(self.grid_24, 1, 0, 1, 1)
        self.grid_15 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_15.sizePolicy().hasHeightForWidth())
        self.grid_15.setSizePolicy(sizePolicy)
        self.grid_15.setText("")
        self.grid_15.setObjectName("grid_15")
        self.subGrid_2.addWidget(self.grid_15, 0, 1, 1, 1)
        self.grid_14 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_14.sizePolicy().hasHeightForWidth())
        self.grid_14.setSizePolicy(sizePolicy)
        self.grid_14.setText("")
        self.grid_14.setObjectName("grid_14")
        self.subGrid_2.addWidget(self.grid_14, 0, 0, 1, 1)
        self.grid_34 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_34.sizePolicy().hasHeightForWidth())
        self.grid_34.setSizePolicy(sizePolicy)
        self.grid_34.setText("")
        self.grid_34.setObjectName("grid_34")
        self.subGrid_2.addWidget(self.grid_34, 2, 0, 1, 1)
        self.grid_25 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_25.sizePolicy().hasHeightForWidth())
        self.grid_25.setSizePolicy(sizePolicy)
        self.grid_25.setText("")
        self.grid_25.setObjectName("grid_25")
        self.subGrid_2.addWidget(self.grid_25, 1, 1, 1, 1)
        self.grid_26 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_26.sizePolicy().hasHeightForWidth())
        self.grid_26.setSizePolicy(sizePolicy)
        self.grid_26.setText("")
        self.grid_26.setObjectName("grid_26")
        self.subGrid_2.addWidget(self.grid_26, 1, 2, 1, 1)
        self.grid_35 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_35.sizePolicy().hasHeightForWidth())
        self.grid_35.setSizePolicy(sizePolicy)
        self.grid_35.setText("")
        self.grid_35.setObjectName("grid_35")
        self.subGrid_2.addWidget(self.grid_35, 2, 1, 1, 1)
        self.grid_36 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_36.sizePolicy().hasHeightForWidth())
        self.grid_36.setSizePolicy(sizePolicy)
        self.grid_36.setText("")
        self.grid_36.setObjectName("grid_36")
        self.subGrid_2.addWidget(self.grid_36, 2, 2, 1, 1)
        self.Grid.addLayout(self.subGrid_2, 0, 2, 1, 1)
        self.subGrid_4 = QtWidgets.QGridLayout()
        self.subGrid_4.setObjectName("subGrid_4")
        self.grid_42 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_42.sizePolicy().hasHeightForWidth())
        self.grid_42.setSizePolicy(sizePolicy)
        self.grid_42.setText("")
        self.grid_42.setObjectName("grid_42")
        self.subGrid_4.addWidget(self.grid_42, 0, 1, 1, 1)
        self.grid_63 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_63.sizePolicy().hasHeightForWidth())
        self.grid_63.setSizePolicy(sizePolicy)
        self.grid_63.setText("")
        self.grid_63.setObjectName("grid_63")
        self.subGrid_4.addWidget(self.grid_63, 2, 2, 1, 1)
        self.grid_62 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_62.sizePolicy().hasHeightForWidth())
        self.grid_62.setSizePolicy(sizePolicy)
        self.grid_62.setText("")
        self.grid_62.setObjectName("grid_62")
        self.subGrid_4.addWidget(self.grid_62, 2, 1, 1, 1)
        self.grid_61 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_61.sizePolicy().hasHeightForWidth())
        self.grid_61.setSizePolicy(sizePolicy)
        self.grid_61.setText("")
        self.grid_61.setObjectName("grid_61")
        self.subGrid_4.addWidget(self.grid_61, 2, 0, 1, 1)
        self.grid_52 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_52.sizePolicy().hasHeightForWidth())
        self.grid_52.setSizePolicy(sizePolicy)
        self.grid_52.setText("")
        self.grid_52.setObjectName("grid_52")
        self.subGrid_4.addWidget(self.grid_52, 1, 1, 1, 1)
        self.grid_43 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_43.sizePolicy().hasHeightForWidth())
        self.grid_43.setSizePolicy(sizePolicy)
        self.grid_43.setText("")
        self.grid_43.setObjectName("grid_43")
        self.subGrid_4.addWidget(self.grid_43, 0, 2, 1, 1)
        self.grid_51 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_51.sizePolicy().hasHeightForWidth())
        self.grid_51.setSizePolicy(sizePolicy)
        self.grid_51.setText("")
        self.grid_51.setObjectName("grid_51")
        self.subGrid_4.addWidget(self.grid_51, 1, 0, 1, 1)
        self.grid_53 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_53.sizePolicy().hasHeightForWidth())
        self.grid_53.setSizePolicy(sizePolicy)
        self.grid_53.setText("")
        self.grid_53.setObjectName("grid_53")
        self.subGrid_4.addWidget(self.grid_53, 1, 2, 1, 1)
        self.grid_41 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_41.sizePolicy().hasHeightForWidth())
        self.grid_41.setSizePolicy(sizePolicy)
        self.grid_41.setText("")
        self.grid_41.setObjectName("grid_41")
        self.subGrid_4.addWidget(self.grid_41, 0, 0, 1, 1)
        self.Grid.addLayout(self.subGrid_4, 2, 0, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.Grid.addWidget(self.line_13, 0, 1, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.Grid.addWidget(self.line_14, 4, 3, 1, 1)
        self.subGrid_9 = QtWidgets.QGridLayout()
        self.subGrid_9.setObjectName("subGrid_9")
        self.grid_88 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_88.sizePolicy().hasHeightForWidth())
        self.grid_88.setSizePolicy(sizePolicy)
        self.grid_88.setText("")
        self.grid_88.setObjectName("grid_88")
        self.subGrid_9.addWidget(self.grid_88, 1, 1, 1, 1)
        self.grid_98 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_98.sizePolicy().hasHeightForWidth())
        self.grid_98.setSizePolicy(sizePolicy)
        self.grid_98.setText("")
        self.grid_98.setObjectName("grid_98")
        self.subGrid_9.addWidget(self.grid_98, 2, 1, 1, 1)
        self.grid_89 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_89.sizePolicy().hasHeightForWidth())
        self.grid_89.setSizePolicy(sizePolicy)
        self.grid_89.setText("")
        self.grid_89.setObjectName("grid_89")
        self.subGrid_9.addWidget(self.grid_89, 1, 2, 1, 1)
        self.grid_79 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_79.sizePolicy().hasHeightForWidth())
        self.grid_79.setSizePolicy(sizePolicy)
        self.grid_79.setText("")
        self.grid_79.setObjectName("grid_79")
        self.subGrid_9.addWidget(self.grid_79, 0, 2, 1, 1)
        self.grid_78 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_78.sizePolicy().hasHeightForWidth())
        self.grid_78.setSizePolicy(sizePolicy)
        self.grid_78.setText("")
        self.grid_78.setObjectName("grid_78")
        self.subGrid_9.addWidget(self.grid_78, 0, 1, 1, 1)
        self.grid_99 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_99.sizePolicy().hasHeightForWidth())
        self.grid_99.setSizePolicy(sizePolicy)
        self.grid_99.setText("")
        self.grid_99.setObjectName("grid_99")
        self.subGrid_9.addWidget(self.grid_99, 2, 2, 1, 1)
        self.grid_87 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_87.sizePolicy().hasHeightForWidth())
        self.grid_87.setSizePolicy(sizePolicy)
        self.grid_87.setText("")
        self.grid_87.setObjectName("grid_87")
        self.subGrid_9.addWidget(self.grid_87, 1, 0, 1, 1)
        self.grid_77 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_77.sizePolicy().hasHeightForWidth())
        self.grid_77.setSizePolicy(sizePolicy)
        self.grid_77.setText("")
        self.grid_77.setObjectName("grid_77")
        self.subGrid_9.addWidget(self.grid_77, 0, 0, 1, 1)
        self.grid_97 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_97.sizePolicy().hasHeightForWidth())
        self.grid_97.setSizePolicy(sizePolicy)
        self.grid_97.setText("")
        self.grid_97.setObjectName("grid_97")
        self.subGrid_9.addWidget(self.grid_97, 2, 0, 1, 1)
        self.Grid.addLayout(self.subGrid_9, 4, 4, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.Grid.addWidget(self.line_15, 1, 4, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.Grid.addWidget(self.line_16, 2, 1, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.Grid.addWidget(self.line_17, 1, 0, 1, 1)
        self.subGrid_7 = QtWidgets.QGridLayout()
        self.subGrid_7.setObjectName("subGrid_7")
        self.grid_73 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_73.sizePolicy().hasHeightForWidth())
        self.grid_73.setSizePolicy(sizePolicy)
        self.grid_73.setText("")
        self.grid_73.setObjectName("grid_73")
        self.subGrid_7.addWidget(self.grid_73, 0, 2, 1, 1)
        self.grid_81 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_81.sizePolicy().hasHeightForWidth())
        self.grid_81.setSizePolicy(sizePolicy)
        self.grid_81.setText("")
        self.grid_81.setObjectName("grid_81")
        self.subGrid_7.addWidget(self.grid_81, 1, 0, 1, 1)
        self.grid_72 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_72.sizePolicy().hasHeightForWidth())
        self.grid_72.setSizePolicy(sizePolicy)
        self.grid_72.setText("")
        self.grid_72.setObjectName("grid_72")
        self.subGrid_7.addWidget(self.grid_72, 0, 1, 1, 1)
        self.grid_71 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_71.sizePolicy().hasHeightForWidth())
        self.grid_71.setSizePolicy(sizePolicy)
        self.grid_71.setText("")
        self.grid_71.setObjectName("grid_71")
        self.subGrid_7.addWidget(self.grid_71, 0, 0, 1, 1)
        self.grid_91 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_91.sizePolicy().hasHeightForWidth())
        self.grid_91.setSizePolicy(sizePolicy)
        self.grid_91.setText("")
        self.grid_91.setObjectName("grid_91")
        self.subGrid_7.addWidget(self.grid_91, 2, 0, 1, 1)
        self.grid_82 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_82.sizePolicy().hasHeightForWidth())
        self.grid_82.setSizePolicy(sizePolicy)
        self.grid_82.setText("")
        self.grid_82.setObjectName("grid_82")
        self.subGrid_7.addWidget(self.grid_82, 1, 1, 1, 1)
        self.grid_83 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_83.sizePolicy().hasHeightForWidth())
        self.grid_83.setSizePolicy(sizePolicy)
        self.grid_83.setText("")
        self.grid_83.setObjectName("grid_83")
        self.subGrid_7.addWidget(self.grid_83, 1, 2, 1, 1)
        self.grid_92 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_92.sizePolicy().hasHeightForWidth())
        self.grid_92.setSizePolicy(sizePolicy)
        self.grid_92.setText("")
        self.grid_92.setObjectName("grid_92")
        self.subGrid_7.addWidget(self.grid_92, 2, 1, 1, 1)
        self.grid_93 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_93.sizePolicy().hasHeightForWidth())
        self.grid_93.setSizePolicy(sizePolicy)
        self.grid_93.setText("")
        self.grid_93.setObjectName("grid_93")
        self.subGrid_7.addWidget(self.grid_93, 2, 2, 1, 1)
        self.Grid.addLayout(self.subGrid_7, 4, 0, 1, 1)
        self.line_18 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_18.setAutoFillBackground(False)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.Grid.addWidget(self.line_18, 0, 3, 1, 1)
        self.subGrid_1 = QtWidgets.QGridLayout()
        self.subGrid_1.setObjectName("subGrid_1")
        self.grid_21 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_21.sizePolicy().hasHeightForWidth())
        self.grid_21.setSizePolicy(sizePolicy)
        self.grid_21.setText("")
        self.grid_21.setObjectName("grid_21")
        self.subGrid_1.addWidget(self.grid_21, 1, 0, 1, 1)
        self.grid_13 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_13.sizePolicy().hasHeightForWidth())
        self.grid_13.setSizePolicy(sizePolicy)
        self.grid_13.setText("")
        self.grid_13.setObjectName("grid_13")
        self.subGrid_1.addWidget(self.grid_13, 0, 2, 1, 1)
        self.grid_23 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_23.sizePolicy().hasHeightForWidth())
        self.grid_23.setSizePolicy(sizePolicy)
        self.grid_23.setText("")
        self.grid_23.setObjectName("grid_23")
        self.subGrid_1.addWidget(self.grid_23, 1, 2, 1, 1)
        self.grid_31 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_31.sizePolicy().hasHeightForWidth())
        self.grid_31.setSizePolicy(sizePolicy)
        self.grid_31.setText("")
        self.grid_31.setObjectName("grid_31")
        self.subGrid_1.addWidget(self.grid_31, 2, 0, 1, 1)
        self.grid_33 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_33.sizePolicy().hasHeightForWidth())
        self.grid_33.setSizePolicy(sizePolicy)
        self.grid_33.setText("")
        self.grid_33.setObjectName("grid_33")
        self.subGrid_1.addWidget(self.grid_33, 2, 2, 1, 1)
        self.grid_12 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_12.sizePolicy().hasHeightForWidth())
        self.grid_12.setSizePolicy(sizePolicy)
        self.grid_12.setText("")
        self.grid_12.setObjectName("grid_12")
        self.subGrid_1.addWidget(self.grid_12, 0, 1, 1, 1)
        self.grid_32 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_32.sizePolicy().hasHeightForWidth())
        self.grid_32.setSizePolicy(sizePolicy)
        self.grid_32.setText("")
        self.grid_32.setObjectName("grid_32")
        self.subGrid_1.addWidget(self.grid_32, 2, 1, 1, 1)
        self.grid_22 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_22.sizePolicy().hasHeightForWidth())
        self.grid_22.setSizePolicy(sizePolicy)
        self.grid_22.setText("")
        self.grid_22.setObjectName("grid_22")
        self.subGrid_1.addWidget(self.grid_22, 1, 1, 1, 1)
        self.grid_11 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_11.sizePolicy().hasHeightForWidth())
        self.grid_11.setSizePolicy(sizePolicy)
        self.grid_11.setText("")
        self.grid_11.setObjectName("grid_11")
        self.subGrid_1.addWidget(self.grid_11, 0, 0, 1, 1)
        self.Grid.addLayout(self.subGrid_1, 0, 0, 1, 1)
        self.subGrid_6 = QtWidgets.QGridLayout()
        self.subGrid_6.setObjectName("subGrid_6")
        self.grid_49 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_49.sizePolicy().hasHeightForWidth())
        self.grid_49.setSizePolicy(sizePolicy)
        self.grid_49.setText("")
        self.grid_49.setObjectName("grid_49")
        self.subGrid_6.addWidget(self.grid_49, 0, 2, 1, 1)
        self.grid_57 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_57.sizePolicy().hasHeightForWidth())
        self.grid_57.setSizePolicy(sizePolicy)
        self.grid_57.setText("")
        self.grid_57.setObjectName("grid_57")
        self.subGrid_6.addWidget(self.grid_57, 1, 0, 1, 1)
        self.grid_48 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_48.sizePolicy().hasHeightForWidth())
        self.grid_48.setSizePolicy(sizePolicy)
        self.grid_48.setText("")
        self.grid_48.setObjectName("grid_48")
        self.subGrid_6.addWidget(self.grid_48, 0, 1, 1, 1)
        self.grid_47 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_47.sizePolicy().hasHeightForWidth())
        self.grid_47.setSizePolicy(sizePolicy)
        self.grid_47.setText("")
        self.grid_47.setObjectName("grid_47")
        self.subGrid_6.addWidget(self.grid_47, 0, 0, 1, 1)
        self.grid_67 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_67.sizePolicy().hasHeightForWidth())
        self.grid_67.setSizePolicy(sizePolicy)
        self.grid_67.setText("")
        self.grid_67.setObjectName("grid_67")
        self.subGrid_6.addWidget(self.grid_67, 2, 0, 1, 1)
        self.grid_58 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_58.sizePolicy().hasHeightForWidth())
        self.grid_58.setSizePolicy(sizePolicy)
        self.grid_58.setText("")
        self.grid_58.setObjectName("grid_58")
        self.subGrid_6.addWidget(self.grid_58, 1, 1, 1, 1)
        self.grid_59 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_59.sizePolicy().hasHeightForWidth())
        self.grid_59.setSizePolicy(sizePolicy)
        self.grid_59.setText("")
        self.grid_59.setObjectName("grid_59")
        self.subGrid_6.addWidget(self.grid_59, 1, 2, 1, 1)
        self.grid_68 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_68.sizePolicy().hasHeightForWidth())
        self.grid_68.setSizePolicy(sizePolicy)
        self.grid_68.setText("")
        self.grid_68.setObjectName("grid_68")
        self.subGrid_6.addWidget(self.grid_68, 2, 1, 1, 1)
        self.grid_69 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_69.sizePolicy().hasHeightForWidth())
        self.grid_69.setSizePolicy(sizePolicy)
        self.grid_69.setText("")
        self.grid_69.setObjectName("grid_69")
        self.subGrid_6.addWidget(self.grid_69, 2, 2, 1, 1)
        self.Grid.addLayout(self.subGrid_6, 2, 4, 1, 1)
        self.subGrid_5 = QtWidgets.QGridLayout()
        self.subGrid_5.setObjectName("subGrid_5")
        self.grid_46 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_46.sizePolicy().hasHeightForWidth())
        self.grid_46.setSizePolicy(sizePolicy)
        self.grid_46.setText("")
        self.grid_46.setObjectName("grid_46")
        self.subGrid_5.addWidget(self.grid_46, 0, 2, 1, 1)
        self.grid_54 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_54.sizePolicy().hasHeightForWidth())
        self.grid_54.setSizePolicy(sizePolicy)
        self.grid_54.setText("")
        self.grid_54.setObjectName("grid_54")
        self.subGrid_5.addWidget(self.grid_54, 1, 0, 1, 1)
        self.grid_45 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_45.sizePolicy().hasHeightForWidth())
        self.grid_45.setSizePolicy(sizePolicy)
        self.grid_45.setText("")
        self.grid_45.setObjectName("grid_45")
        self.subGrid_5.addWidget(self.grid_45, 0, 1, 1, 1)
        self.grid_44 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_44.sizePolicy().hasHeightForWidth())
        self.grid_44.setSizePolicy(sizePolicy)
        self.grid_44.setText("")
        self.grid_44.setObjectName("grid_44")
        self.subGrid_5.addWidget(self.grid_44, 0, 0, 1, 1)
        self.grid_64 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_64.sizePolicy().hasHeightForWidth())
        self.grid_64.setSizePolicy(sizePolicy)
        self.grid_64.setText("")
        self.grid_64.setObjectName("grid_64")
        self.subGrid_5.addWidget(self.grid_64, 2, 0, 1, 1)
        self.grid_55 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_55.sizePolicy().hasHeightForWidth())
        self.grid_55.setSizePolicy(sizePolicy)
        self.grid_55.setText("")
        self.grid_55.setObjectName("grid_55")
        self.subGrid_5.addWidget(self.grid_55, 1, 1, 1, 1)
        self.grid_56 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_56.sizePolicy().hasHeightForWidth())
        self.grid_56.setSizePolicy(sizePolicy)
        self.grid_56.setText("")
        self.grid_56.setObjectName("grid_56")
        self.subGrid_5.addWidget(self.grid_56, 1, 2, 1, 1)
        self.grid_65 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_65.sizePolicy().hasHeightForWidth())
        self.grid_65.setSizePolicy(sizePolicy)
        self.grid_65.setText("")
        self.grid_65.setObjectName("grid_65")
        self.subGrid_5.addWidget(self.grid_65, 2, 1, 1, 1)
        self.grid_66 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_66.sizePolicy().hasHeightForWidth())
        self.grid_66.setSizePolicy(sizePolicy)
        self.grid_66.setText("")
        self.grid_66.setObjectName("grid_66")
        self.subGrid_5.addWidget(self.grid_66, 2, 2, 1, 1)
        self.Grid.addLayout(self.subGrid_5, 2, 2, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.Grid.addWidget(self.line_19, 4, 1, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.Grid.addWidget(self.line_20, 1, 2, 1, 1)
        self.subGrid_3 = QtWidgets.QGridLayout()
        self.subGrid_3.setObjectName("subGrid_3")
        self.grid_19 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_19.sizePolicy().hasHeightForWidth())
        self.grid_19.setSizePolicy(sizePolicy)
        self.grid_19.setText("")
        self.grid_19.setObjectName("grid_19")
        self.subGrid_3.addWidget(self.grid_19, 0, 2, 1, 1)
        self.grid_27 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_27.sizePolicy().hasHeightForWidth())
        self.grid_27.setSizePolicy(sizePolicy)
        self.grid_27.setText("")
        self.grid_27.setObjectName("grid_27")
        self.subGrid_3.addWidget(self.grid_27, 1, 0, 1, 1)
        self.grid_18 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_18.sizePolicy().hasHeightForWidth())
        self.grid_18.setSizePolicy(sizePolicy)
        self.grid_18.setText("")
        self.grid_18.setObjectName("grid_18")
        self.subGrid_3.addWidget(self.grid_18, 0, 1, 1, 1)
        self.grid_17 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_17.sizePolicy().hasHeightForWidth())
        self.grid_17.setSizePolicy(sizePolicy)
        self.grid_17.setText("")
        self.grid_17.setObjectName("grid_17")
        self.subGrid_3.addWidget(self.grid_17, 0, 0, 1, 1)
        self.grid_37 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_37.sizePolicy().hasHeightForWidth())
        self.grid_37.setSizePolicy(sizePolicy)
        self.grid_37.setText("")
        self.grid_37.setObjectName("grid_37")
        self.subGrid_3.addWidget(self.grid_37, 2, 0, 1, 1)
        self.grid_28 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_28.sizePolicy().hasHeightForWidth())
        self.grid_28.setSizePolicy(sizePolicy)
        self.grid_28.setText("")
        self.grid_28.setObjectName("grid_28")
        self.subGrid_3.addWidget(self.grid_28, 1, 1, 1, 1)
        self.grid_29 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_29.sizePolicy().hasHeightForWidth())
        self.grid_29.setSizePolicy(sizePolicy)
        self.grid_29.setText("")
        self.grid_29.setObjectName("grid_29")
        self.subGrid_3.addWidget(self.grid_29, 1, 2, 1, 1)
        self.grid_38 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_38.sizePolicy().hasHeightForWidth())
        self.grid_38.setSizePolicy(sizePolicy)
        self.grid_38.setText("")
        self.grid_38.setObjectName("grid_38")
        self.subGrid_3.addWidget(self.grid_38, 2, 1, 1, 1)
        self.grid_39 = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_39.sizePolicy().hasHeightForWidth())
        self.grid_39.setSizePolicy(sizePolicy)
        self.grid_39.setText("")
        self.grid_39.setObjectName("grid_39")
        self.subGrid_3.addWidget(self.grid_39, 2, 2, 1, 1)
        self.Grid.addLayout(self.subGrid_3, 0, 4, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.Grid.addWidget(self.line_21, 2, 3, 1, 1)
        self.line_22 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.Grid.addWidget(self.line_22, 3, 0, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.Grid.addWidget(self.line_23, 3, 2, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.gridLayoutWidget_8)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.Grid.addWidget(self.line_24, 3, 4, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 540, 61, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.TimeGrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.TimeGrid.setContentsMargins(0, 0, 0, 0)
        self.TimeGrid.setObjectName("TimeGrid")
        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.TimeGrid.addWidget(self.timeLabel)
        self.timeSignature = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeSignature.setFont(font)
        self.timeSignature.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.timeSignature.setObjectName("timeSignature")
        self.TimeGrid.addWidget(self.timeSignature)
        self.hintButton = QtWidgets.QPushButton(Dialog)
        self.hintButton.setGeometry(QtCore.QRect(60, 540, 131, 51))
        self.hintButton.setObjectName("hintButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.optionLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.optionLayout.setContentsMargins(0, 0, 0, 0)
        self.optionLayout.setObjectName("optionLayout")
        self.pauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setObjectName("pauseButton")
        self.optionLayout.addWidget(self.pauseButton)
        self.restartButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restartButton.sizePolicy().hasHeightForWidth())
        self.restartButton.setSizePolicy(sizePolicy)
        self.restartButton.setObjectName("restartButton")
        self.optionLayout.addWidget(self.restartButton)
        self.backButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName("backButton")
        self.optionLayout.addWidget(self.backButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sudoku"))
        self.answerButton_2.setText(_translate("Dialog", "2"))
        self.answerButton_1.setText(_translate("Dialog", "1"))
        self.answerButton_4.setText(_translate("Dialog", "4"))
        self.answerButton_5.setText(_translate("Dialog", "5"))
        self.answerButton_3.setText(_translate("Dialog", "3"))
        self.answerButton_0.setText(_translate("Dialog", "X"))
        self.answerButton_9.setText(_translate("Dialog", "9"))
        self.answerButton_8.setText(_translate("Dialog", "8"))
        self.answerButton_7.setText(_translate("Dialog", "7"))
        self.answerButton_6.setText(_translate("Dialog", "6"))
        self.checkButton.setText(_translate("Dialog", "Check"))
        self.timeLabel.setText(_translate("Dialog", "Time"))
        self.timeSignature.setText(_translate("Dialog", "00 : 00"))
        self.hintButton.setText(_translate("Dialog", "Random Fill (3 left)"))
        self.pauseButton.setText(_translate("Dialog", "Pause"))
        self.restartButton.setText(_translate("Dialog", "Restart"))
        self.backButton.setText(_translate("Dialog", "Back to Main Menu"))