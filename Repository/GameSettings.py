from Entity.AssistCondition import AssistCondition

class GameSettings():
    def __init__(self, file_path):
        self.file_path = file_path
        self.assist_condition: AssistCondition = AssistCondition()

        self.check_settings()

    def update_assist_condition(self, assist_condition: AssistCondition):
        self.assist_condition = assist_condition
        self.update_settings()

    def check_assist_condition(self):
        return self.assist_condition

    def update_game_state(self):
        pass

    def check_game_state(self):
        pass

    def update_settings(self):
        with open(self.file_path, 'w') as file:
            file.write(f"higlightSameDigit,{int(self.assist_condition.highlightSameDigit)}")
            file.write(f"\nhiglightAnswer,{int(self.assist_condition.highlightAnswer)}")
            file.write(f"\nincorrectAnswer,{int(self.assist_condition.incorrectAnswer)}")

    def check_settings(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                assist_type, condition = line.strip().split(',')
                if assist_type == "higlightSameDigit":
                    self.assist_condition.highlightSameDigit = int(condition)
                elif assist_type == "highlightAnswer":
                    self.assist_condition.highlightAnswer = int(condition)
                elif assist_type == "incorrectAnswer":
                    self.assist_condition.highlightAnswer = int(condition)