class Person:
    def __init__(self, nome : str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return self.__nome
    
class Market:
    def __init__(self, counterCount : int):
        self.counters = [None] or counterCount
        self.queue = []

    def v_Index(self, index : int) -> bool:
        return 0 <= index < len(self.counters)
    
    def arrive(self, person : Person):
        self.queue.append(person)

    def call(self, index: int) -> bool:
        if not self.v_Index(index):
            print("fail: caixa inexistente")
            return False
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return False

        if not self.queue:
            print("fail: sem clientes")
            return False

        person = self.queue.pop(0)
        self.counters[index] = person
        return True
    
    def finish(self, index : int):
        if not self.v_Index(index):
            print("fail: caixa inexistente")
            return None
        
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None

        person = self.counters[index]
        self.counters[index] = None
        return person
    
    def __str__(self):
        caixas = [str(p) if p is not None else "-----, -----" for p in self.counters]
        espera = [str(p) for p in self.queue]
        return f"Caixas: [{', '.join(caixas)}]\nEspera: [{', '.join(espera)}]"
    
def main():
    mercado = Market("")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercado)
        elif args[0] == "init":
            mercado = Market(int(args[1]))
        elif args[0] == "arrive":
            nome = args[1]
            mercado.arrive(Person(nome))
        elif args[0] == "call":
            index = int(args[1])
            mercado.call(index)
main()

