class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    def get_cpu(self):
        return self.__cpu
    
    def get_memory(self):
        return self.__memory
    
    def __make_computations(self, operation):
        if operation == '+':
            result = self.__cpu + self.__memory
        elif operation == '-':
            result = self.__cpu - self.__memory
        elif operation == '*':
            result = self.__cpu * self.__memory
        elif operation == '/':
            if self.__memory != 0:
                result = self.__cpu / self.__memory
            else:
                result = "Division by zero!"
        else:
            result = "Invalid operation!"
        return result
    
    def info(self):
        print(f"Computer: CPU - {self.__cpu}, Memory - {self.__memory}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    
    def get_memory_card(self):
        return self.__memory_card
    
    def info(self):
        super().info()
        print(f"Memory Card: {self.__memory_card}")


comp1 = Computer(cpu=2, memory=4)
laptop1 = Laptop(cpu=3, memory=6, memory_card=128)

print("Computer:")
print("CPU:", comp1.get_cpu())
print("Memory:", comp1.get_memory())
print("Computations (+):", comp1._Computer__make_computations('+'))
print("Computations (-):", comp1._Computer__make_computations('-'))
print("Computations (*):", comp1._Computer__make_computations('*'))
print("Computations (/):", comp1._Computer__make_computations('/'))
comp1.info()
print()

print("Laptop:")
print("CPU:", laptop1.get_cpu())
print("Memory:", laptop1.get_memory())
print("Memory Card:", laptop1.get_memory_card())
print("Computations (+):", laptop1._Computer__make_computations('+'))
print("Computations (-):", laptop1._Computer__make_computations('-'))
print("Computations (*):", laptop1._Computer__make_computations('*'))
print("Computations (/):", laptop1._Computer__make_computations('/'))
laptop1.info()
