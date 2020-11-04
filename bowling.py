STRIKE = 10

class Scorer():
    def __init__(self):
        self._is_first_shoot = True
        self._frame_score = []

    def calculate_total_score(self, shoots_list: []) -> int:
        self._frame_score = []
        self._is_first_shoot = True
        current_frame_score = 0

        idx = 0
        tab_len = len(shoots_list)
        while idx < tab_len:
            if self._is_first_shoot:
                current_frame_score = shoots_list[idx]

                if current_frame_score == STRIKE:                  
                    if (idx + 1) < tab_len:
                        current_frame_score += shoots_list[idx + 1]

                    if (idx + 2) < tab_len:
                        current_frame_score += shoots_list[idx + 2]

                    self._is_first_shoot = False
                    self._frame_score.append(current_frame_score)
                
                elif idx == tab_len - 1:
                        self._frame_score.append(current_frame_score)

            else:
                current_frame_score += shoots_list[idx]

                if current_frame_score == STRIKE and (idx + 1) < tab_len:
                    current_frame_score += shoots_list[idx + 1]
                self._frame_score.append(current_frame_score)

            self._is_first_shoot = not self._is_first_shoot
            idx += 1
        
        return sum(self._frame_score)

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
