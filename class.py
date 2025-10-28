# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.__storage = storage      # Encapsulated attribute (private)
        self.battery = battery

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def charge(self):
        print(f"🔋 Charging {self.brand} {self.model}... Battery at {self.battery}%")

    def get_storage(self):
        return self.__storage  # Accessing a private attribute safely

# Subclass (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        print(f"🎮 Playing '{game}' on {self.brand} {self.model} with {self.gpu} GPU...")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 85)
phone2 = GamingPhone("ASUS", "ROG Phone 8", "512GB", 90, "Adreno 750")

# Using methods
phone1.call("0712345678")
phone1.charge()
print(f"{phone1.brand} storage: {phone1.get_storage()}")

phone2.play_game("Call of Duty Mobile")
phone2.charge()
