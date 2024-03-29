from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class PauseView(QDialog):
    def __init__(self, widget, gameView):
        super(PauseView, self).__init__()
        self.setupUi(self)
        self.widget = widget

        self.gameView = gameView

        self.resumeButton.clicked.connect(self.resume)
        self.backToMainMenuButton.clicked.connect(self.backToMainMenu)

    def resume(self):
        self.widget.setCurrentIndex(4)
        self.deleteView()
        self.gameView.stopwatch.paused = False
        self.gameView.stopwatch.timer.start(1000)
        self.close()

    def backToMainMenu(self):
        self.widget.setCurrentIndex(0)
        self.deleteView()
        self.gameView.backToMainMenu()
        self.close()
    
    def deleteView(self):
        widget_to_remove = self.widget.widget(5)
        widget_to_remove.deleteLater()
        self.widget.removeWidget(widget_to_remove)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 615)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 351, 181))
        font = QtGui.QFont()
        font.setFamily("A bit sketchy")
        font.setPointSize(54)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.resumeButton = QtWidgets.QPushButton(Dialog)
        self.resumeButton.setGeometry(QtCore.QRect(100, 360, 191, 51))
        self.resumeButton.setObjectName("resumeButton")
        self.backToMainMenuButton = QtWidgets.QPushButton(Dialog)
        self.backToMainMenuButton.setGeometry(QtCore.QRect(100, 420, 191, 51))
        self.backToMainMenuButton.setObjectName("backToMainMenuButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sudoku"))
        self.label_6.setText(_translate("Dialog", "Game\n"
"Paused"))
        self.resumeButton.setText(_translate("Dialog", "Resume"))
        self.backToMainMenuButton.setText(_translate("Dialog", "Back to Main Menu"))
