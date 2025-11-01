class Cliente:
    def __init__(self, nome : str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"
    
class Market:
    def __init__(self, num_caixas : int):
        self.caixas = [None] * num_caixas
        self.fila = []
    
    def __str__(self):
        caixas_str = ", ".join(map(lambda p: p.getNome() if p else "-----", self.caixas))
        fila_str = ", ".join(map(lambda p: p.getNome(), self.fila))
        return f"Caixas: [{caixas_str}]\nEspera: [{fila_str}]"