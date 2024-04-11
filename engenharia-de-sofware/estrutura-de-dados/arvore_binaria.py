class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no.direita)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(valor, no.esquerda)
        else:
            return self._buscar_recursivo(valor, no.direita)

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)

print("Busca por 2:", arvore.buscar(2))
print("Busca por 6:", arvore.buscar(6))
