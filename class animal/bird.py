from animal import Animal

class Bird (Animal):
    # Konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    # method info
    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.warna,
              "\nJenis Paruh\t\t: ", self.paruh)
        
bird = Bird("Jalak Bali", "Serangga", "Di Hutan", "Menghasilkan telur", "Putih", "Pendek dan Lancip")
print("## Info Bird ##")
bird.info_bird()

