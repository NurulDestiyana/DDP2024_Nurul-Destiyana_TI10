from animal import Animal

class Cat (Animal):
    # Konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, ras):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.ras = ras
        
    # method info
    def info_cat(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.warna,
              "\nJenis Ras\t\t: ", self.ras)
        
cat = Cat ("Kucing", "Daging", "Di Darat", "Melahirkan", "Abu-Abu", "Chartreux")
print("## Info Cat ##")
cat.info_cat()
