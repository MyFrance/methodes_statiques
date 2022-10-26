class Voiture:
    voiture_cree = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_cree +=1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod    
    def lamborghini(cls):
        return cls(marque = "Lamborghini", vitesse = 250, prix = 200000 )
    
    @classmethod
    def porsche(cls):
        return cls(marque = "Porsche", vitesse = 200, prix = 180000)
    
    @staticmethod
    def Afficher_nombre_voiture(): 
        print(f"Vous avez {Voiture.voiture_cree} dans votre garage")

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.Afficher_nombre_voiture()