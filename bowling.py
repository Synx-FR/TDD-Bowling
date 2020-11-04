STRIKE = 10

class Scorer():
    def __init__(self):
        self._is_first_shoot = True
        self._frame_score = []
        self.current_frame_score = 0

    def calculate_total_score(self, shoots_list: []) -> int:
        self._frame_score = []
        self._is_first_shoot = True
        self.current_frame_score = 0

        idx = 0
        tab_len = len(shoots_list)
        while idx < tab_len:
            if self._is_first_shoot: # Premier Tir
                self._manage_first_shoot(shoots_list, idx, tab_len)

            else: # Deuxieme Tir
                self._manage_second_shoot(shoots_list, idx, tab_len)

            self._is_first_shoot = not self._is_first_shoot
            idx += 1
        
        return sum(self._frame_score)

    def _manage_first_shoot(self, shoots_list: [], idx: int, tab_len: int):
        self.current_frame_score = shoots_list[idx]

        # Gestion du STRIKE
        if self.current_frame_score == STRIKE:                  
            self._manage_strike(idx, tab_len, shoots_list)

        elif idx == tab_len - 1: # Cas du dernier tir
            self._frame_score.append(self.current_frame_score)

    def _manage_second_shoot(self, shoots_list: [], idx: int, tab_len: int):
        self.current_frame_score += shoots_list[idx]

        # Gestion du SPARE
        if self.current_frame_score == STRIKE and (idx + 1) < tab_len:
            self.current_frame_score += shoots_list[idx + 1]

        self._frame_score.append(self.current_frame_score)

    def _manage_strike(self, idx, tab_len, shoots_list):
        if (idx + 1) < tab_len:
            self.current_frame_score += shoots_list[idx + 1]

        if (idx + 2) < tab_len:
            self.current_frame_score += shoots_list[idx + 2]

        self._is_first_shoot = False
        self._frame_score.append(self.current_frame_score)

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
