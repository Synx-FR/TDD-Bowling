from bowling import Joueur
from bowling import Scorer
# from bowling import Partie

"""
    Périphérique de gestion des quilles (input)
            v
    L'application prend en compte l'input (le tir du joueur)
    Calculer le score à chaque instant
    Gérer les cycles de jeu 
    Afficher les scores (vers le périphérique de sortie)
            v
    Périphérique d'affichage (output)
"""

# Etape 1 : le scorer accepte un nouveau tir et calcule a tout moment le score.
#           on ne tient pas compte des spare et strike et une partie est infinie

# Etape 2 : le scorer sait maintenant évaluer les spares
#           le score d'un spare est 10 + le tir suivant

# Etape 3 : gestion du strike

# Etape 4 : une partie dure 10 frames

class TestJoueur():

    def setup(self):
        self.joueur = Joueur()

    def teardown(self):
        del self.joueur

    def test_etape_1_score_debut_joueur_vaut_zero(self):
        assert self.joueur.get_score() == 0

    def test_etape_1_joueur_recoit_premier_tir(self):
        self.joueur.shoot(5)
        assert self.joueur.get_score() == 5

    def test_etape_1_joueur_recoit_deux_premiers_tir(self):
        self.joueur.shoot(5)
        self.joueur.shoot(3)
        assert self.joueur.get_score() == 8

    def test_etape_2_joueur_fait_un_spare(self):
        self.joueur.shoot(3)
        self.joueur.shoot(7)
        self.joueur.shoot(5)
        assert self.joueur.get_score() == 20

    def test_etape_3_joueur_fait_un_strike_puis_4_et_2(self):
        self.joueur.shoot(10)
        self.joueur.shoot(4)
        self.joueur.shoot(2)
        assert self.joueur.get_score() == 22

    def test_etape_3_joueur_fait_deux_strikes_puis_4_et_2(self):
        self.joueur.shoot(10)
        self.joueur.shoot(10)
        self.joueur.shoot(4)
        self.joueur.shoot(2)
        assert self.joueur.get_score() == (24 + 16 + 6)