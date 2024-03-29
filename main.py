import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import View.AboutView 
import View.TopScoreView
import View.GameView
import View.PauseView
import View.SolvedView
import View.SettingsView
import View.MainMenuView
from Repository.ScoreManager import ScoreManager
from Repository.GameSettings import GameSettings

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(615)
widget.setFixedWidth(391)

score_manager = ScoreManager("score.txt")
game_settings = GameSettings("game_state.txt")

about_view = View.AboutView.AboutView(widget)
top_score_view = View.TopScoreView.TopScoreView(widget, score_manager)
settings_view = View.SettingsView.SettingsView(widget, game_settings)
main_menu_view = View.MainMenuView.MainMenuView(widget, about_view, top_score_view, settings_view, score_manager)

widget.addWidget(main_menu_view)
widget.addWidget(about_view)
widget.addWidget(top_score_view)
widget.addWidget(settings_view)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")