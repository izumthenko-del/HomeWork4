class Person:
    def __init__(self, name, age):
        self.name=name
        self._age=age
    def get_age(self):
        return self._age
class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number
driver = Driver("Vitaly",22,"75 45 123456")
print("Name:", driver.name)
print("Age:", driver.get_age())
print("License Number:", driver.license_number)
