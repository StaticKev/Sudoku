from PyQt5.QtCore import QTimer

class Stopwatch():
    def __init__(self, parent=None):
        self.time_taken_in_text = "00 : 00"
        self.time_taken_in_sec = 0
        self.timer = QTimer(parent)
        self.paused = False

    def updateStopwatch(self):
        if not self.paused:
            elapsed_mins: int = self.time_taken_in_sec / 60
            elapsed_secs: int = self.time_taken_in_sec % 60
            mins_output = "{:02d}".format(int(elapsed_mins))
            secs_output = "{:02d}".format(int(elapsed_secs))
            self.time_taken_in_text = f"{mins_output} : {secs_output}"
            self.time_taken_in_sec += 1 

    def stop(self):
        self.timer.stop()
        self.paused = True
    
    def getTimeInSec(self):
        return self.time_taken_in_sec - 1