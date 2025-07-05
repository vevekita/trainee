class Cliente:
    def __init__(self, nome: str, email: str, telefone: str) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibirInformacoes(self) -> None:
        print(f'\nNome: {self.nome} \nEmail: {self.email} \nTelefone: {self.telefone}')

    def getNome(self) -> str:
        return self.nome
    
    def setNome(self, novo_nome: str) -> None:
        self.nome = novo_nome

    def getEmail(self) -> str:
        return self.email
    
    def setEmail(self, novo_email: str) -> None:
        self.email = novo_email

    def getTelefone(self) -> str:
        return self.telefone

    def setTelefone(self, novo_telefone: str) -> None:
        self.telefone = novo_telefone 