from vaches.domain.errors.exceptions import InvalidVacheException

class Vache:

    AGE_MAX = 25
    AGE_NAISSANCE = 0
    POIDS_MIN = 2
    POIDS_MAX = 10000
    PANSE_MAX = 50
    RENDEMENT_RUMINATION = 0.25


    def __init__(self, petit_nom: str, poids: float, age: int = AGE_NAISSANCE):

        if not petit_nom or petit_nom.strip() == "":
            raise InvalidVacheException("le nom peut pas etre vide")

        if poids < Vache.POIDS_MIN:
            raise InvalidVacheException("erreur dans le poids")

        if age < Vache.AGE_NAISSANCE or age > Vache.AGE_MAX:
            raise InvalidVacheException("l'âge doit être entre 0 et 25 ans")

        self.petit_nom = petit_nom
        self.poids = poids
        self.age = age
        self.panse = 0

    def brouter(self, quantite: float, nourriture=None):

        if nourriture is not None:
            raise InvalidVacheException("La vache ne peut pas brouter de nourriture ")

        if quantite <= 0:
            raise InvalidVacheException("La quantite doit etre positive.")

        if self.panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("Erreur sur la panse")

        self.panse += quantite

    def ruminer(self):

        if self.panse <= 0:
            raise InvalidVacheException("Erreur")

        gain = Vache.RENDEMENT_RUMINATION * self.panse
        self.poids += gain
        self.panse = 0.0

    def vieillir(self):
        if self.age >= Vache.AGE_MAX:
            raise InvalidVacheException('')
        self.age += 1
