class Person:
    def __init__(self, nome: str):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def __str__(self):
        return self.__nome


class Market:
    def __init__(self, qtd_caixas: int):
        self.counters: list[Person | None] = [None for _ in range(qtd_caixas)]
        self.waiting: list[Person] = []

    def __str__(self):
        caixas_str = ", ".join(
            [str(p) if p is not None else "-----" for p in self.counters]
        )
        espera_str = ", ".join([str(p) for p in self.waiting])
        return f"Caixas: [{caixas_str}]\nEspera: [{espera_str}]"

    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        if len(self.waiting) == 0:
            print("fail: sem clientes")
            return
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return
        # pega o primeiro da fila e coloca no caixa
        person = self.waiting.pop(0)
        self.counters[index] = person

    def finish(self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return None
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None
        finished = self.counters[index]
        self.counters[index] = None
        return finished

    
def main():
    mercado = Market(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercado)
        elif args[0] == "init":
            qtd = int(args[1])
            mercado = Market(qtd)
        elif args[0] == "arrive":
            nome = args[1]
            mercado.arrive(Person(nome))
        elif args[0] == "call":
            index = int(args[1])
            mercado.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            mercado.finish(index)
main()

