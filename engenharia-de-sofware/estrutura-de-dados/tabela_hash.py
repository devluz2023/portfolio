class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                return

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None

# Exemplo de uso:
tabela = TabelaHash(10)
tabela.inserir('a', 1)
tabela.inserir('b', 2)
tabela.inserir('c', 3)

print("Valor associado à chave 'a':", tabela.buscar('a'))
print("Valor associado à chave 'b':", tabela.buscar('b'))
print("Valor associado à chave 'c':", tabela.buscar('c'))

tabela.remover('b')
print("Após remover a chave 'b', o valor associado à chave 'b':", tabela.buscar('b'))
