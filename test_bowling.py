from bowling import Joueur
from bowling import Scorer
from bowling import Partie

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

# Etape 1 le scorer accepte un nouveau tir et calcule a tout moment le score.
#       on ne tient pas compte des spare et strike et une partie est infinie

class TestJoueur():

    def setup(self):
        self.joueur = Joueur()

    def teardown(self):
        del self.joueur

    def test_etape_1_score_debut_joueur_vaut_zero(self):
        assert self.joueur.get_score() == 0

    def test_etape_1_joueur_recoit_premier_tir(self):
        self.joueur.get_shoot(5)
        assert self.joueur.get_score() == 5

    def test_etape_1_joueur_recoit_deux_premiers_tir(self):
        self.joueur.get_shoot(5)
        self.joueur.get_shoot(10)
        assert self.joueur.get_score() == 15

    
