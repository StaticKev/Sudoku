from Entity.Values.DifficultyLevel import DifficultyLevel

class Score():
    def __init__(self, name: str, time: int, difficulty: DifficultyLevel, score:int):
        self.name: str = name
        self.time: int = time
        self.difficulty: DifficultyLevel = difficulty
        self.score: int = score

class ScoreManager():
    def __init__(self, file_path):
        self.scores: list[Score] = []
        self.file_path = file_path
        self.read_scores_from_file()

    def input_score(self, score: Score):
        specific_difficulty_index = [] 
        for r_index in range(len(self.scores)):
            if str(self.scores[r_index].difficulty) == str(score.difficulty):
                specific_difficulty_index.append(r_index)

        if len(specific_difficulty_index) < 5:
            self.scores.append(score)
            self.write_scores_to_file()
        elif len(specific_difficulty_index) == 5:
            index_to_change: int = 0
            counter = 0
            for s in range(len(specific_difficulty_index)):
                counter += 1
                if self.scores[specific_difficulty_index[s]].score < score.score:
                    index_to_change = specific_difficulty_index[s]
                    break
            for t in range(counter, len(specific_difficulty_index)):
                if (
                    self.scores[specific_difficulty_index[t]].score < score.score and 
                    self.scores[specific_difficulty_index[t]].score < self.scores[index_to_change].score
                    ):
                    index_to_change = specific_difficulty_index[t]
            self.scores[index_to_change] = score
            self.write_scores_to_file()
        self.read_scores_from_file()

    def write_scores_to_file(self):
        with open(self.file_path, 'w') as file:
            for score in self.scores:
                file.write(f"{score.name},{score.time},{score.difficulty},{score.score}\n")
    
    def read_scores_from_file(self):
        self.scores = []
        with open(self.file_path, 'r') as file:
            for line in file:
                name, time, difficulty, score = line.strip().split(',')
                self.scores.append(Score(name, time, DifficultyLevel[difficulty.split(".")[-1]], int(score)))