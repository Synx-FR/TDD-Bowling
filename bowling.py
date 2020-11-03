
class Scorer():
    def __init__(self):
        pass

    def calculate_total_score(self, shoots_list: []):
        score = 0
        frame_score = 0
        is_first_shoot = True
        prev_spare = False

        for shoot in shoots_list:
            score += shoot
            if is_first_shoot:
                frame_score = shoot
                if prev_spare:
                    score += shoot
                    prev_spare = False
            else:
                frame_score += shoot
                if frame_score == 10:
                    prev_spare = True

            is_first_shoot = not is_first_shoot
        return score

class Partie():
    def __init__(self):
        pass

class Joueur():
    def __init__(self):
        self._scorer = Scorer()
        self._shoots_list = []

    def shoot(self, quilles: int):
        self._shoots_list.append(quilles)

    def get_score(self) -> int:
        return self._scorer.calculate_total_score(self._shoots_list)
