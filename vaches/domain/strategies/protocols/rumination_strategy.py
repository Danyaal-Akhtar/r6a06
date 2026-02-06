from typing import Protocol

class rumination_strategy(Protocol) :
    def calculer_lait(self, vache : "Vache", panse_avant: float) -> float :
    #test
