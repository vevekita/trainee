from Aluno import *
from Cliente import *
from Produto import *

def main() -> None:
    p1 = Pessoa('João', 20, '12345678900', 'M')
    p1.exibirInformacoes()

    p1.setIdade(12)
    print(p1.getIdade())
    p1.exibirInformacoes()
    p1.apresentar()
    p1.setCpf('98765432100')
    print(p1.getCpf())


    a1 = Aluno('Verônica', 17, '80064409990', 'Feminino', 145096, 1, 'Ciência da Computação')
    a1.exibirInformacoes()
    a1.apresentar()

    c1 = Cliente('Jujuba', 'jujuba.gomets@gmail.com', '44998077100')
    c1.exibirInformacoes()
    c1.setTelefone('44999708174')
    print('O novo telefone inserido é', c1.getTelefone())
    
    prod1 = Produto('Bolo', 'Bolo de chocolate com morango', 22.9)
    prod1.exibirInformacoes()
    prod1.setPreco(20.0)
    print('O novo preço do produto é', prod1.getPreco())

if __name__ == '__main__':
    main() 