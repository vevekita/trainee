class Produto:
    def __init__(self, nome: str, descricao: str, preco: float) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def exibirInformacoes(self) -> None:
        print(f'\nNome do produto: {self.nome} \nDescrição do produto: {self.descricao} \nPreço do produto: {self.preco}')

    def getNome(self) -> str:
        return self.nome
    
    def setNome(self, novo_nome: str) -> None:
        self.nome = novo_nome

    def getDescricao(self) -> str:
        return self.descricao
    
    def setDescricao(self, nova_descricao: str) -> None:
        self.descricao = nova_descricao

    def getPreco(self) -> float:
        return self.preco

    def setPreco(self, novo_preco: float) -> None:
        self.preco = novo_preco