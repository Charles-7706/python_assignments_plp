class Devices:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def device_info(self):
        print(f"Device Name: {self.name}, Brand: {self.brand}, Price: ${self.price}")

# inheritance  
class Phone(Devices):
    def __init__(self, name, brand, price, camera_megapixels, serial_number):
        self.camera_megapixels = camera_megapixels
        self._serial_number= serial_number # encapsulation
        super().__init__(name, brand, price)

    def device_info(self):
        print(f"Device name: {self.name}, Brand: {self.brand}, Price: ${self.price}, Camera: {self.camera_megapixels}px , serial_number: {self._serial_number}")

# creating objects
device1 = Devices("iPhone 15", "Apple", 999)
phone1 = Phone("iPhone 12", "Apple", 600, 48, "SN123456789")
# calling methods
device1.device_info()
phone1.device_info()