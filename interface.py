from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print(self):
        print("Printing...")
    
    def scan(self):
        print("Scanning...")

class BasicPrinter(Printer):
    def print(self):
        print("Printing...")
