class Client:
    def __init__(self, id, phone):
        self.id = id
        self.phone = phone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def __str__(self):
        return f"{self.id}:{self.phone}"


class Theater:
    def __init__(self, num_seats=0):
        self.seats = [None for _ in range(num_seats)]

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

    def getSeats(self):
        return self.seats.copy()

    def __str__(self):
        if not self.seats:
            return "[]"
        result = []
        for seat in self.seats:
            if seat is None:
                result.append("-")
            else:
                result.append(str(seat))
        return "[" + " ".join(result) + "]"

    def _search(self, name):
        for i, seat in enumerate(self.seats):
            if seat is not None and seat.get_id() == name:
                return i
        return -1

    def _verify_index(self, index):
        return 0 <= index < len(self.seats)


def main():
    cinema = Theater()  # começa vazio
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
        print("$" + line)
        args = line.split()
        cmd = args[0]

        try:
            if cmd == "end":
                break
            elif cmd == "show":
                print(cinema)
            elif cmd == "init":
                cinema = Theater(int(args[1]))
            elif cmd == "reserve":
                cinema.reserve(args[1], args[2], int(args[3]))
            elif cmd == "cancel":
                cinema.cancel(args[1])
        except Exception as e:
            print(f"fail: {e}")


main()
