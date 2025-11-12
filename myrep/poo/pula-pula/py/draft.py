class Client:
    def __init__(self, id, phone):
        self.id = id
        self.phone = phone

    def __str__(self):
        return f"{self.id}:{self.phone}"


class Theater:
    def __init__(self, num_seats=0):
        self.seats = [None] * num_seats

    def reserve(self, id, phone, index):
        if not self._verify_index(index):
            raise Exception("cadeira nao existe")
        if self.seats[index] is not None:
            raise Exception("cadeira ja esta ocupada")
        if self._search(id) != -1:
            raise Exception("cliente ja esta no cinema")
        self.seats[index] = Client(id, phone)

    def cancel(self, id):
        index = self._search(id)
        if index == -1:
            raise Exception("cliente nao esta no cinema")
        self.seats[index] = None

    def _search(self, id):
        for i, seat in enumerate(self.seats):
            if seat and seat.id == id:
                return i
        return -1

    def _verify_index(self, index):
        return 0 <= index < len(self.seats)

    def __str__(self):
        if not self.seats:
            return "[]"
        parts = [str(seat) if seat else "-" for seat in self.seats]
        return "[" + " ".join(parts) + "]"


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
        elif args[0] == "init":



main()
    