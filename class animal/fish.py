from animal import Animal

class fish (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("bernapas\t\t: ", self.bernapas,
              "\nhabitat\t\t\t: ", self.habitat)

print()         
fish = fish("Hiu", "Daging", "Laut", "Melahirkan", "Insang", "Air Asin")
print("## Info Fish ##")
fish.info_fish()       