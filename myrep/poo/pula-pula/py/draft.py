class Kid:
    def __init__(self, nome : str, idade : int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def __str__(self) -> str:
        return f"{self.__nome}:{self.__idade}"
    
class Trampoline:
    def __init__(self):
        self.playing = []
        self.waiting = []
    
    def arrive(self, kid):
        self.waiting.insert(0, kid)

    def enter(self):
        if self.waiting:
            kid = self.waiting.pop()
            self.playing.insert(0, kid)

    def leave(self):
        if self.playing:
            kid = self.playing.pop()
            self.waiting.insert(0, kid)

    def remove(self, name):
        for i, kid in enumerate(self.waiting):
            if kid.getNome() == name:
                del self.waiting[i]
                return
        for i, kid in enumerate(self.playing):
            if kid.getNome() == name:
                del self.playing[i]
                return
        print(f"fail: {name} nao esta no pula-pula")

    def __str__(self):
        saida = "["
        for i in range(len(self.waiting)):
            saida += str(self.waiting[i])
            if i < len(self.waiting) - 1:
                saida += ", "
        saida += "] => ["
        for i in range(len(self.playing)):
            saida += str(self.playing[i])
            if i < len(self.playing) - 1:
                saida += ", "
        saida += "]"
        return saida



def main():
    pula = Trampoline()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "arrive":
            name = args[1]
            age = int(args[2])
            kid = Kid(name, age)
            pula.arrive(kid)
        elif args[0] == "show":
            print(pula)
        elif args[0] == "enter":
            pula.enter()
        elif args[0] == "leave":
            pula.leave()
        elif args[0] == "remove":
            name = args[1]
            pula.remove(name)



main()
    