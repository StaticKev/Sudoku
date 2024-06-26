# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TopScoreView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from Repository.ScoreManager import Score, ScoreManager
from Entity.Values.DifficultyLevel import DifficultyLevel

class TopScoreView(QDialog):
    def __init__(self, widget, score_manager: ScoreManager):
        super(TopScoreView, self).__init__()
        self.setupUi(self)
        self.widget = widget
        self.score_manager: ScoreManager = score_manager
        self.difficulty: DifficultyLevel = DifficultyLevel.EASY

        self.resetLabel()
        self.showInitialTopScore()

        self.backButton.clicked.connect(self.backToMainMenu)
        self.comboBox.currentIndexChanged.connect(self.showTopScore)
    
    def resetLabel(self):
        for l in range(1, 6):
            player_label = self.findChild(QLabel, f"player{l}")
            player_label.setText("")
            time_label = self.findChild(QLabel, f"time{l}")
            time_label.setText("")
            score_label = self.findChild(QLabel, f"score{l}")
            score_label.setText("")

    def showInitialTopScore(self):
        score_to_be_shown: list[Score] = []
        for score in self.score_manager.scores:
            if score.difficulty == self.difficulty:
                score_to_be_shown.append(score)
        score_to_be_shown = self.sortRecord(score_to_be_shown)
        for i in range(len(score_to_be_shown)):
            player_label = self.findChild(QLabel, f"player{i + 1}")
            time_label = self.findChild(QLabel, f"time{i + 1}")
            score_label = self.findChild(QLabel, f"score{i + 1}")
            player_label.setText(score_to_be_shown[i].name)
            time_mins = "{:02d}".format(int(int(score_to_be_shown[i].time) / 60))
            time_secs = "{:02d}".format(int(int(score_to_be_shown[i].time) % 60))
            time_label.setText(f"{time_mins} : {time_secs}")
            score_label.setText(str(score_to_be_shown[i].score))

    def showTopScore(self):
        self.resetLabel()
        self.difficulty = DifficultyLevel[self.comboBox.currentText().upper()]
        score_to_be_shown: list[Score] = []
        for score in self.score_manager.scores:
            if score.difficulty == self.difficulty:
                score_to_be_shown.append(score)
        score_to_be_shown = self.sortRecord(score_to_be_shown)
        for i in range(len(score_to_be_shown)):
            player_label = self.findChild(QLabel, f"player{i + 1}")
            time_label = self.findChild(QLabel, f"time{i + 1}")
            score_label = self.findChild(QLabel, f"score{i + 1}")
            player_label.setText(score_to_be_shown[i].name)
            time_mins = "{:02d}".format(int(int(score_to_be_shown[i].time) / 60))
            time_secs = "{:02d}".format(int(int(score_to_be_shown[i].time) % 60))
            time_label.setText(f"{time_mins} : {time_secs}")
            score_label.setText(str(score_to_be_shown[i].score))

    
    def backToMainMenu(self):
        self.widget.setCurrentIndex(0)
        self.hide()

    def sortRecord(self, scores: list[Score]):
        while True:
            swapped = 0
            for s in range (len(scores) - 1):
                if scores[s].score < scores[s + 1].score:
                    swapped += 1
                    temp = scores[s]
                    scores[s] = scores[s + 1]
                    scores[s + 1] = temp
            if swapped == 0:
                break
        return scores


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 615)
        self.player5 = QtWidgets.QLabel(Dialog)
        self.player5.setGeometry(QtCore.QRect(60, 360, 101, 16))
        self.player5.setObjectName("player5")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(80, 160, 231, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 440, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.player3 = QtWidgets.QLabel(Dialog)
        self.player3.setGeometry(QtCore.QRect(60, 300, 101, 16))
        self.player3.setObjectName("player3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(180, 200, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 440, 81, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.player4 = QtWidgets.QLabel(Dialog)
        self.player4.setGeometry(QtCore.QRect(60, 330, 101, 16))
        self.player4.setObjectName("player4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 351, 111))
        font = QtGui.QFont()
        font.setFamily("A bit sketchy")
        font.setPointSize(54)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 200, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.player1 = QtWidgets.QLabel(Dialog)
        self.player1.setGeometry(QtCore.QRect(60, 240, 101, 16))
        self.player1.setObjectName("player1")
        self.player2 = QtWidgets.QLabel(Dialog)
        self.player2.setGeometry(QtCore.QRect(60, 270, 101, 16))
        self.player2.setObjectName("player2")
        self.time1 = QtWidgets.QLabel(Dialog)
        self.time1.setGeometry(QtCore.QRect(180, 240, 41, 16))
        self.time1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.time1.setObjectName("time1")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(80, 400, 231, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(300, 200, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_11.setObjectName("label_11")
        self.time2 = QtWidgets.QLabel(Dialog)
        self.time2.setGeometry(QtCore.QRect(180, 270, 41, 16))
        self.time2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.time2.setObjectName("time2")
        self.time3 = QtWidgets.QLabel(Dialog)
        self.time3.setGeometry(QtCore.QRect(180, 300, 41, 16))
        self.time3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.time3.setObjectName("time3")
        self.time4 = QtWidgets.QLabel(Dialog)
        self.time4.setGeometry(QtCore.QRect(180, 330, 41, 16))
        self.time4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.time4.setObjectName("time4")
        self.time5 = QtWidgets.QLabel(Dialog)
        self.time5.setGeometry(QtCore.QRect(180, 360, 41, 16))
        self.time5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.time5.setObjectName("time5")
        self.score1 = QtWidgets.QLabel(Dialog)
        self.score1.setGeometry(QtCore.QRect(290, 240, 41, 20))
        self.score1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score1.setObjectName("score1")
        self.score2 = QtWidgets.QLabel(Dialog)
        self.score2.setGeometry(QtCore.QRect(290, 270, 41, 20))
        self.score2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score2.setObjectName("score2")
        self.score3 = QtWidgets.QLabel(Dialog)
        self.score3.setGeometry(QtCore.QRect(290, 300, 41, 20))
        self.score3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score3.setObjectName("score3")
        self.score4 = QtWidgets.QLabel(Dialog)
        self.score4.setGeometry(QtCore.QRect(290, 330, 41, 20))
        self.score4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score4.setObjectName("score4")
        self.score5 = QtWidgets.QLabel(Dialog)
        self.score5.setGeometry(QtCore.QRect(290, 360, 41, 20))
        self.score5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score5.setObjectName("score5")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(100, 500, 191, 51))
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sudoku"))
        self.player5.setText(_translate("Dialog", "Player 5"))
        self.comboBox.setItemText(0, _translate("Dialog", "Easy"))
        self.comboBox.setItemText(1, _translate("Dialog", "Medium"))
        self.comboBox.setItemText(2, _translate("Dialog", "Hard"))
        self.player3.setText(_translate("Dialog", "Player 3"))
        self.label_10.setText(_translate("Dialog", "Time"))
        self.label_7.setText(_translate("Dialog", "Difficulty"))
        self.label_8.setText(_translate("Dialog", "Level"))
        self.player4.setText(_translate("Dialog", "Player 4"))
        self.label_6.setText(_translate("Dialog", "Top Score"))
        self.label_9.setText(_translate("Dialog", "Player"))
        self.player1.setText(_translate("Dialog", "Player 1"))
        self.player2.setText(_translate("Dialog", "Player 2"))
        self.time1.setText(_translate("Dialog", "00 : 00"))
        self.label_11.setText(_translate("Dialog", "Score"))
        self.time2.setText(_translate("Dialog", "00 : 00"))
        self.time3.setText(_translate("Dialog", "00 : 00"))
        self.time4.setText(_translate("Dialog", "00 : 00"))
        self.time5.setText(_translate("Dialog", "00 : 00"))
        self.score1.setText(_translate("Dialog", "000000"))
        self.score2.setText(_translate("Dialog", "000000"))
        self.score3.setText(_translate("Dialog", "000000"))
        self.score4.setText(_translate("Dialog", "000000"))
        self.score5.setText(_translate("Dialog", "000000"))
        self.backButton.setText(_translate("Dialog", "Back to Main Menu"))