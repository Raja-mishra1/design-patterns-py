class ComputerBuilder:
    def set_cpu(self):
        pass

    def set_ram(self):
        pass

    def set_storage(self):
        pass

    def get_computer(self):
        pass

# Concrete Builder for Gaming Computers
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer("Gaming")

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def get_computer(self):
        return self.computer

# Concrete Builder for Office Computers
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer("Office")

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def get_computer(self):
        return self.computer

# Product
class Computer:
    def __init__(self, computer_type):
        self.computer_type = computer_type
        self.cpu = ""
        self.ram = ""
        self.storage = ""

    def __str__(self):
        return f"{self.computer_type} Computer - CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"

# Director
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self, cpu, ram, storage):
        self.builder.set_cpu(cpu)
        self.builder.set_ram(ram)
        self.builder.set_storage(storage)
        return self.builder.get_computer()

if __name__ == "__main__":
    director = ComputerDirector(GamingComputerBuilder())
    print(director.build_computer("i7", "16GB", "256GB SSD"))

    director = ComputerDirector(OfficeComputerBuilder())
    print(director.build_computer("i5", "8GB", "512GB SSD"))
