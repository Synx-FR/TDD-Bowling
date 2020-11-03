
class Scorer():
    def __init__(self):
        self._is_first_shoot = True
        self._prev_spare = False
        self._prev_strike = 0
        self._score = 0
        self._frame_score = 0

    def calculate_total_score(self, shoots_list: []) -> int:
        self._score = 0
        self._frame_score = 0
        self._is_first_shoot = True
        self._prev_spare = False
        self._prev_strike = 0

        for shoot in shoots_list:
            self._calculate_shoot(shoot)
        
        return self._score

    def _calculate_shoot(self, shoot: int):
        self._score += shoot
        if self._is_first_shoot:
            self._frame_score = shoot
            if shoot == 10:
                self._prev_strike = 2
                self._is_first_shoot = False
            elif self._prev_spare:
                self._score += shoot
                self._prev_spare = False
            elif self._prev_strike > 0:
                self._add_strike_bonus(shoot)

        else:
            self._frame_score += shoot
            if self._frame_score == 10:
                self._prev_spare = True
            elif self._prev_strike > 0:
                self._add_strike_bonus(shoot)

        self._is_first_shoot = not self._is_first_shoot

    def _add_strike_bonus(self, shoot: int):
        self._score += shoot
        self._prev_strike = self._prev_strike - 1

# class Partie():
#     def __init__(self):
#         pass

class Joueur():
    def __init__(self):
        self._scorer = Scorer()
        self._shoots_list = []

    def shoot(self, quilles: int):
        self._shoots_list.append(quilles)

    def get_score(self) -> int:
        return self._scorer.calculate_total_score(self._shoots_list)
