class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, genero: str):
        self.__nome = nome #aqui todas são públicas, se houvesse um _ antes do atributo seria privado e com dois __ seria privado.
        self.__idade = idade
        self.__cpf = cpf
        self.__genero = genero

    def exibirInformacoes(self) -> None:
        print('Nome:', self.__nome)
        print(f'Idade: {self.__idade}')
        print(f'CPF: {self.__cpf}')
        print(f'Gênero: {self.__genero}')

    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, novo_nome: str) -> None:
        self.__nome = novo_nome
    
    def getIdade(self) -> int:
        return self.__idade
    
    def setIdade(self, nova_idade: int) -> None:
        if nova_idade >= 0:
            self.__idade = nova_idade
            print('Idade alterada')
        else:
            print('Idade inválida')

    def getCpf(self) -> str:
        return self.__cpf
    
    def setCpf(self, novo_cpf: str) -> None:
        self.__cpf = novo_cpf
    
    def getGenero(self) -> str:
        return self.__genero
    
    def setGenero(self, novo_genero: str) -> None:
        self.__genero = novo_genero
    
    def apresentar(self) -> None:
        print(f'Oi, meu nome é {self.getNome()} e eu sou uma pessoa.')
