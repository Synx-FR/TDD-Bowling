"""
    class Scorer():
        def __init__(self):
            pass

        def calculate_score():
            pass

    class Partie():
        def __init__(self):
            pass
"""

class Joueur():
    def __init__(self):
        self._score = 0

    def get_shoot(self, quilles: int):
        self._score += quilles

    def get_score(self) -> int:
        return self._score