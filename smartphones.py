# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Call parent constructor
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.device_info()}...")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()}")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 14", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S23", "Android", "512GB")

# Using methods
phone1.call("0768299985")
phone2.install_app("WhatsApp")
