class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.nome = "teste"
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes: {vingadores.likes}')

office = Serie('the office', 2004, 11)
office.dar_like()
print(f'Nome: {office.nome} - Ano: {office.ano} - Temporadas: {office.temporadas} Temporadas - Likes: {office.likes}')