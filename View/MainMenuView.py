from PyQt5 import QtCore, QtGui, QtWidgets

from Entity.Values.DifficultyLevel import DifficultyLevel
from Entity.AssistCondition import AssistCondition
from View.GameView import GameView
from View.AboutView import AboutView
from View.TopScoreView import TopScoreView
from View.SettingsView import SettingsView
from PyQt5.QtWidgets import QDialog, QApplication
from Repository.ScoreManager import ScoreManager

from PyQt5 import QtCore, QtGui, QtWidgets

class MainMenuView(QDialog):
    def __init__(
            self, 
            widget, 
            about_view: AboutView, 
            top_score_view: TopScoreView, 
            settings_view: SettingsView,
            score_manager : ScoreManager
            ):
        super(MainMenuView, self).__init__()
        self.setupUi(self)
        self.widget = widget

        self.about_view = about_view
        self.top_score_view = top_score_view
        self.settings_view = settings_view
        self.score_manager = score_manager

        self.difficulty_level = self.difficultiesComboBox.currentText()

        self.topScoreButton.clicked.connect(self.goToTopScore)
        self.aboutButton.clicked.connect(self.goToAbout)
        self.settingsButton.clicked.connect(self.goToSettings)
        self.exitButton.clicked.connect(QApplication.quit)
        self.newGameButton.clicked.connect(lambda: self.startGame())
        self.difficultiesComboBox.currentIndexChanged.connect(self.on_combobox_change)

    def on_combobox_change(self):
        selected_item = self.difficultiesComboBox.currentText()
        self.difficulty_level = selected_item
    
    def goToTopScore(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
    
    def goToAbout(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def goToSettings(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 3)

    def startGame(self):
        game_view: GameView
        if self.difficulty_level.upper() in DifficultyLevel.__members__:
            game_view = GameView(
                widget = self.widget, 
                difficulty_level = DifficultyLevel.__members__[self.difficulty_level.upper()], 
                assist_condition = self.settings_view.assist_condition,
                score_manager = self.score_manager,
                topScoreUpdateFunc = self.topScoreUpdate
                )
        self.widget.addWidget(game_view)
        self.widget.setCurrentIndex(4)
        self.hide()
        self.about_view.hide()
        self.top_score_view.hide()

    def topScoreUpdate(self):
        self.top_score_view.showTopScore()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 615)
        self.difficultiesComboBox = QtWidgets.QComboBox(Dialog)
        self.difficultiesComboBox.setGeometry(QtCore.QRect(220, 250, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficultiesComboBox.sizePolicy().hasHeightForWidth())
        self.difficultiesComboBox.setSizePolicy(sizePolicy)
        self.difficultiesComboBox.setMaxVisibleItems(10)
        self.difficultiesComboBox.setObjectName("difficultiesComboBox")
        self.difficultiesComboBox.addItem("")
        self.difficultiesComboBox.addItem("")
        self.difficultiesComboBox.addItem("")
        self.topScoreButton = QtWidgets.QPushButton(Dialog)
        self.topScoreButton.setGeometry(QtCore.QRect(100, 310, 191, 51))
        self.topScoreButton.setObjectName("topScoreButton")
        self.newGameButton = QtWidgets.QPushButton(Dialog)
        self.newGameButton.setGeometry(QtCore.QRect(100, 250, 111, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newGameButton.sizePolicy().hasHeightForWidth())
        self.newGameButton.setSizePolicy(sizePolicy)
        self.newGameButton.setObjectName("newGameButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(100, 490, 191, 51))
        self.exitButton.setObjectName("exitButton")
        self.aboutButton = QtWidgets.QPushButton(Dialog)
        self.aboutButton.setGeometry(QtCore.QRect(100, 430, 191, 51))
        self.aboutButton.setObjectName("aboutButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 351, 111))
        font = QtGui.QFont()
        font.setFamily("A bit sketchy")
        font.setPointSize(60)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.settingsButton = QtWidgets.QPushButton(Dialog)
        self.settingsButton.setGeometry(QtCore.QRect(100, 370, 191, 51))
        self.settingsButton.setObjectName("settingsButton")

        self.retranslateUi(Dialog)
        self.difficultiesComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sudoku"))
        self.difficultiesComboBox.setItemText(0, _translate("Dialog", "Easy"))
        self.difficultiesComboBox.setItemText(1, _translate("Dialog", "Medium"))
        self.difficultiesComboBox.setItemText(2, _translate("Dialog", "Hard"))
        self.topScoreButton.setText(_translate("Dialog", "Top Score"))
        self.newGameButton.setText(_translate("Dialog", "New Game"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.aboutButton.setText(_translate("Dialog", "About"))
        self.label_2.setText(_translate("Dialog", "Sudoku"))
        self.settingsButton.setText(_translate("Dialog", "Settings"))
