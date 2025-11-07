class Grafite:
    def __init__(self, calibre : float, dureza : str, tamanho : int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgaste(self) -> int:
        return{
            "HB" : 1,
            "2B" : 2,
            "4B" : 4,
            "6B" : 6
        }.get(self.dureza, 1)
    
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    
class Lapiseira:
    def __init__(self, calibre : float):
        self.calibre = calibre
        self.bico : Grafite | None = None
        self.tambor : list[Grafite] = []

    def insert(self, grafite = Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if not self.tambor:
            print("fail: nao existe grafite no tambor")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        gasto = self.bico.desgaste()
        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        if self.bico.tamanho - gasto < 10:
            self.bico.tamanho = 10
            print("fail: folha incompleta")
            return
        self.bico.tamanho -= gasto


    def __str__(self):
        bico_str = f"[{self.bico}]" if self.bico else "[]"
        tambor_str = "".join([f"[{g}]" for g in self.tambor])
        return f"calibre: {self.calibre}, bico: {bico_str}, tambor: <{tambor_str}>"

def main():
    lapiseira = Lapiseira(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
        elif args[0] == "insert":
            grafite = Grafite(float(args[1]), args[2], int(args[3]))
            lapiseira.insert(grafite)
        elif args[0] == "pull":
            lapiseira.pull()
        elif args[0] == "remove":
            lapiseira.remove()
        elif args[0] == "write":
            lapiseira.write()

main()

        