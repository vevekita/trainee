from Pessoa import *
class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, genero: str, ra: int, periodo: int, curso: str) -> None:
        super().__init__(nome, idade, cpf, genero)
        self.ra = ra
        self.periodo = periodo
        self.curso = curso
    
    def exibirInformacoes(self) -> None:
        super().exibirInformacoes()
        print(f'\nRA: {self.ra} \nPeriodo: {self.periodo} \nCurso: {self.curso}')

    def getRA(self) -> int:
        return self.ra
    
    def getPeriodo(self) -> int:
        return self.periodo
    
    def getCurso(self) -> str:
        return self.curso

    def apresentar(self):
        print(f'Oi, meu nome é {self.getNome()} e eu sou um aluno')