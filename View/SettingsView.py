from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from Entity.AssistCondition import AssistCondition
from Repository.GameSettings import GameSettings

class SettingsView(QDialog):
    def __init__(self, widget, game_settings: GameSettings):
        super(SettingsView, self).__init__()
        self.setupUi(self)
        self.widget = widget
        self.settings = game_settings

        self.assist_condition: AssistCondition = game_settings.check_assist_condition()
        self.assist1_checkBox.setChecked(self.assist_condition.highlightSameDigit)
        self.assist2_checkBox.setChecked(self.assist_condition.incorrectAnswer)
        self.assist3_checkBox.setChecked(self.assist_condition.highlightAnswer)

        self.assist1_checkBox.stateChanged.connect(lambda state: self.onStateChange(self.assist_condition, 'highlightSameDigit', state))
        self.assist2_checkBox.stateChanged.connect(lambda state: self.onStateChange(self.assist_condition, 'incorrectAnswer', state))
        self.assist3_checkBox.stateChanged.connect(lambda state: self.onStateChange(self.assist_condition, 'highlightAnswer', state))

        self.backButton.clicked.connect(self.backToMainMenu)

    def onStateChange(self, assist_condition, assist_type, state):
        condition: bool = True
        if state == 0:
            condition = False
        setattr(assist_condition, assist_type, condition)
        self.settings.update_assist_condition(self.assist_condition)

    def backToMainMenu(self):
        self.widget.setCurrentIndex(0)
        self.hide()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 615)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 351, 111))
        font = QtGui.QFont()
        font.setFamily("A bit sketchy")
        font.setPointSize(54)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.assist1_checkBox = QtWidgets.QCheckBox(Dialog)
        self.assist1_checkBox.setGeometry(QtCore.QRect(120, 220, 141, 17))
        self.assist1_checkBox.setObjectName("assist1_checkBox")
        self.assist2_checkBox = QtWidgets.QCheckBox(Dialog)
        self.assist2_checkBox.setGeometry(QtCore.QRect(120, 250, 141, 17))
        self.assist2_checkBox.setObjectName("assist2_checkBox")
        self.assist3_checkBox = QtWidgets.QCheckBox(Dialog)
        self.assist3_checkBox.setGeometry(QtCore.QRect(120, 280, 141, 17))
        self.assist3_checkBox.setObjectName("assist3_checkBox")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(100, 200, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(100, 360, 191, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(100, 500, 191, 51))
        self.backButton.setObjectName("backButton")
        self.music_checkBox = QtWidgets.QCheckBox(Dialog)
        self.music_checkBox.setGeometry(QtCore.QRect(120, 380, 171, 17))
        self.music_checkBox.setChecked(True)
        self.music_checkBox.setObjectName("music_checkBox")
        self.sfx_checkBox = QtWidgets.QCheckBox(Dialog)
        self.sfx_checkBox.setGeometry(QtCore.QRect(120, 410, 161, 17))
        self.sfx_checkBox.setChecked(True)
        self.sfx_checkBox.setObjectName("sfx_checkBox")
        self.darkMode_checkBox = QtWidgets.QCheckBox(Dialog)
        self.darkMode_checkBox.setGeometry(QtCore.QRect(120, 440, 181, 17))
        self.darkMode_checkBox.setChecked(False)
        self.darkMode_checkBox.setObjectName("darkMode_checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sudoku"))
        self.label_2.setText(_translate("Dialog", "Settings"))
        self.assist1_checkBox.setText(_translate("Dialog", "Highlight same digit"))
        self.assist2_checkBox.setText(_translate("Dialog", "Incorrect answer check"))
        self.assist3_checkBox.setText(_translate("Dialog", "Highlight answer boxes"))
        self.label.setText(_translate("Dialog", "Assist"))
        self.label_4.setText(_translate("Dialog", "Game Settings"))
        self.backButton.setText(_translate("Dialog", "Back to Main Menu"))
        self.music_checkBox.setText(_translate("Dialog", "Music On (Under Development)"))
        self.sfx_checkBox.setText(_translate("Dialog", "SFX On (Under Development)"))
        self.darkMode_checkBox.setText(_translate("Dialog", "Dark Mode (Under Development)"))
