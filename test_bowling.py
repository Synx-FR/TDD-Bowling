import bowling

"""
    Le jeu
        Une partie ou ligne se joue en 10 frames, soit 10 fois les 10 quilles à faire tomber. 
        Vous devez en 2 lancers maximum, abattre les 10 quilles, si possible. 
        En 1 seul lancer, vous avez réussi le mythique Strike , en 2 lancers, vous réalisez un Spare. 
    Le score
        Les scores sont désormais calculés automatiquement par la machine. 
        Pour une frame et 2 lancers n'ayant pas permis d'abattre toutes les quilles, 
        on comptabilise les quilles de chaque lancer, soit 9 au maximum pour 1 frame.
        Un Spare compte 10 plus les quilles du lancer suivant, soit 20  si le lancer suivant est 1 Strike. 
        Un Strike compte 10 plus les quilles des 2 lancers suivants, soit 30 au maximum si les 2 lancers suivants sont des Strikes. 
        Le score parfait maximum est ainsi de 300. 
        Le Spare est symbolisé par une barre dans la 2ème case de la frame et le Strike  par une croix dans la 1ère case.
        La dernière frame possède 3 cases, car en cas de Spare ou de Strike, vous avez un lancer supplémentaire à jouer. 
"""



def test_1():
    assert False

def test_2():
    assert False

def test_3():
    assert False