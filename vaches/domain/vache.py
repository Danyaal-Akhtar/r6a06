from vaches.domain.errors.exceptions import InvalidVacheException

AGE_MAX = 25
AGE_MINI = 0
POIDS_MIN = 2
POIDS_MAX = 10000
PANSE_MAX = 50
RENDEMENT_RUMINATION = 0.2


class Vache:

    def __init__(self, petitNom: str, age: int, poids: float):

        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("le nom peut pas etre vide")

        if age < AGE_MINI or age > AGE_MAX:
            raise InvalidVacheException("l'age doit etre entre 0 et 25 ans")

        if poids < POIDS_MIN:
            raise InvalidVacheException("erreur dans le poids")

        self.petitNom = petitNom
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

    def veillir(self):
        if self.age >= Vache.AGE_MAX:
            raise InvalidVacheException('')

        self.age += 1
