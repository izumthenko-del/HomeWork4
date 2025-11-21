class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello from {self.name}!")
class PythonLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Python")
    def greet(self):
        print(f"Greetings! The language name is {self.name}.")
class JavaLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Java")
    def greet(self):
        print(f"Bonjour! The language name is {self.name}")
class CLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__("C")
    def greet(self):
        print(f"Hello! The language name is {self.name}.")

python_lang = PythonLanguage()
python_lang.greet()
java_lang = JavaLanguage()
java_lang.greet()
c_lang = CLanguage()
c_lang.greet()
