class Kid:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"


class Trampoline:
    def __init__(self):
        self.waiting = []   # fila de espera
        self.playing = []   # crianças dentro do pula-pula

    def arrive(self, nome, idade):
        self.waiting.insert(0, Kid(nome, idade))

    def enter(self):
        if len(self.waiting) > 0:
            kid = self.waiting.pop()
            self.playing.insert(0, kid)

    def leave(self):
        if len(self.playing) > 0:
            kid = self.playing.pop()
            self.waiting.insert(0, kid)

    def remove(self, nome):

        # primeiro tenta remover do playing
        for i, k in enumerate(self.playing):
            if k.nome == nome:
                self.playing.pop(i)
                return

        # depois tenta remover do waiting
        for i, k in enumerate(self.waiting):
            if k.nome == nome:
                self.waiting.pop(i)
                return

        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        # CORREÇÃO: a fila deve aparecer na ordem natural (sem reversed)
        w = "[" + ", ".join(str(k) for k in self.waiting) + "]"
        p = "[" + ", ".join(str(k) for k in self.playing) + "]"
        return f"{w} => {p}"


def main():
    tramp = Trampoline()
    while True:
        line = input().strip()

        if line == "":
            continue

        print(f"${line}")  # exigido pelos testes

        parts = line.split()
        cmd = parts[0]

        if cmd == "arrive":
            tramp.arrive(parts[1], int(parts[2]))

        elif cmd == "enter":
            tramp.enter()

        elif cmd == "leave":
            tramp.leave()

        elif cmd == "remove":
            tramp.remove(parts[1])

        elif cmd == "show":
            print(tramp)

        elif cmd == "end":
            break


if __name__ == "__main__":
    main()

