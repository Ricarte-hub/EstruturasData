"""
Exemplo de Implementação e Uso de Listas

Este arquivo demonstra:
1. Uso das listas nativas do Python
2. Implementação de uma lista encadeada simples
3. Comparação das operações entre diferentes tipos de listas
"""

import time
import sys


def demonstrar_lista_nativa():
    """Demonstra as operações com listas nativas em Python."""
    print("\n1. LISTAS NATIVAS DO PYTHON")
    print("-" * 50)
    
    # Criação de lista
    lista = [10, 20, 30, 40, 50]
    print(f"Lista criada: {lista}")
    
    # Operações comuns
    print("\nOperações básicas:")
    
    # Acesso por índice - O(1)
    print(f"Elemento na posição 2: {lista[2]}")
    
    # Inserção no final - O(1) amortizado
    lista.append(60)
    print(f"Após append(60): {lista}")
    
    # Inserção em posição específica - O(n)
    lista.insert(2, 25)
    print(f"Após insert(2, 25): {lista}")
    
    # Remoção por valor - O(n)
    lista.remove(25)
    print(f"Após remove(25): {lista}")
    
    # Remoção por índice - O(n)
    valor_removido = lista.pop(1)
    print(f"Elemento removido com pop(1): {valor_removido}")
    print(f"Lista após pop(1): {lista}")
    
    # Busca por valor - O(n)
    indice = lista.index(40)
    print(f"Índice do valor 40: {indice}")
    
    # Verificação de pertencimento - O(n)
    existe = 30 in lista
    print(f"O valor 30 está na lista? {existe}")
    
    # Tamanho da lista - O(1)
    tamanho = len(lista)
    print(f"Tamanho da lista: {tamanho}")
    
    # Ordenação - O(n log n)
    lista.sort()
    print(f"Lista ordenada: {lista}")
    
    # Inversão - O(n)
    lista.reverse()
    print(f"Lista invertida: {lista}")
    
    print("\nObservações sobre listas em Python:")
    print("- São implementadas como arrays dinâmicos")
    print("- Oferecem acesso direto por índice O(1)")
    print("- Redimensionam automaticamente quando necessário")
    print("- Ocupam menos memória que listas encadeadas")
    print("- São mais eficientes para acesso aleatório")
    print("- Operações no meio da lista são O(n)")


class No:
    """Representação de um nó na lista encadeada."""
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
    def __str__(self):
        return str(self.dado)


class ListaEncadeada:
    """Implementação de uma lista encadeada simples."""
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return self.inicio is None
    
    def inserir_inicio(self, dado):
        """Insere um elemento no início da lista - O(1)."""
        novo_no = No(dado)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        self.tamanho += 1
    
    def inserir_fim(self, dado):
        """Insere um elemento no fim da lista - O(n)."""
        novo_no = No(dado)
        
        if self.esta_vazia():
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def inserir_posicao(self, posicao, dado):
        """Insere um elemento em uma posição específica - O(n)."""
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição inválida")
        
        if posicao == 0:
            self.inserir_inicio(dado)
            return
        
        novo_no = No(dado)
        atual = self.inicio
        contador = 0
        
        while contador < posicao - 1:
            atual = atual.proximo
            contador += 1
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1
    
    def remover_inicio(self):
        """Remove o elemento no início da lista - O(1)."""
        if self.esta_vazia():
            raise Exception("Lista vazia")
        
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        return valor
    
    def remover_fim(self):
        """Remove o elemento no fim da lista - O(n)."""
        if self.esta_vazia():
            raise Exception("Lista vazia")
        
        # Se houver apenas um elemento
        if self.inicio.proximo is None:
            valor = self.inicio.dado
            self.inicio = None
            self.tamanho -= 1
            return valor
        
        # Navegando até o penúltimo elemento
        atual = self.inicio
        while atual.proximo.proximo:
            atual = atual.proximo
        
        valor = atual.proximo.dado
        atual.proximo = None
        self.tamanho -= 1
        return valor
    
    def remover_posicao(self, posicao):
        """Remove o elemento em uma posição específica - O(n)."""
        if self.esta_vazia():
            raise Exception("Lista vazia")
        
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        
        if posicao == 0:
            return self.remover_inicio()
        
        atual = self.inicio
        contador = 0
        
        while contador < posicao - 1:
            atual = atual.proximo
            contador += 1
        
        valor = atual.proximo.dado
        atual.proximo = atual.proximo.proximo
        self.tamanho -= 1
        return valor
    
    def buscar(self, dado):
        """Busca um elemento na lista - O(n)."""
        atual = self.inicio
        posicao = 0
        
        while atual:
            if atual.dado == dado:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1  # Não encontrado
    
    def obter(self, posicao):
        """Recupera o elemento em uma posição específica - O(n)."""
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        
        atual = self.inicio
        contador = 0
        
        while contador < posicao:
            atual = atual.proximo
            contador += 1
        
        return atual.dado
    
    def imprimir(self):
        """Imprime todos os elementos da lista."""
        if self.esta_vazia():
            print("Lista vazia")
            return
        
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        
        print(" -> ".join(elementos))


def demonstrar_lista_encadeada():
    """Demonstra as operações com a lista encadeada implementada."""
    print("\n2. LISTA ENCADEADA")
    print("-" * 50)
    
    lista = ListaEncadeada()
    print("Lista encadeada criada (vazia)")
    
    # Inserções
    print("\nInserindo elementos:")
    lista.inserir_inicio(30)
    print("Após inserir_inicio(30): ", end="")
    lista.imprimir()
    
    lista.inserir_inicio(20)
    print("Após inserir_inicio(20): ", end="")
    lista.imprimir()
    
    lista.inserir_inicio(10)
    print("Após inserir_inicio(10): ", end="")
    lista.imprimir()
    
    lista.inserir_fim(40)
    print("Após inserir_fim(40): ", end="")
    lista.imprimir()
    
    lista.inserir_posicao(2, 25)
    print("Após inserir_posicao(2, 25): ", end="")
    lista.imprimir()
    
    # Acesso e Busca
    print("\nOperações de acesso e busca:")
    posicao = lista.buscar(25)
    print(f"Posição do valor 25: {posicao}")
    
    valor = lista.obter(3)
    print(f"Valor na posição 3: {valor}")
    
    # Remoções
    print("\nOperações de remoção:")
    valor = lista.remover_inicio()
    print(f"Valor removido do início: {valor}")
    print("Lista após remover_inicio(): ", end="")
    lista.imprimir()
    
    valor = lista.remover_fim()
    print(f"Valor removido do fim: {valor}")
    print("Lista após remover_fim(): ", end="")
    lista.imprimir()
    
    valor = lista.remover_posicao(1)
    print(f"Valor removido da posição 1: {valor}")
    print("Lista após remover_posicao(1): ", end="")
    lista.imprimir()
    
    print("\nObservações sobre listas encadeadas:")
    print("- Cada nó contém o dado e uma referência para o próximo nó")
    print("- Não há acesso direto por índice (sempre O(n))")
    print("- Inserções e remoções no início são O(1)")
    print("- Não precisam ser redimensionadas, crescem conforme necessário")
    print("- Ocupam mais memória devido às referências adicionais")
    print("- São mais eficientes para inserções/remoções frequentes")


def comparar_desempenho():
    """Compara o desempenho entre listas nativas e listas encadeadas."""
    print("\n3. COMPARAÇÃO DE DESEMPENHO")
    print("-" * 50)
    
    tamanho = 10000
    
    print(f"Comparando operações com {tamanho} elementos:")
    
    # Listas nativas do Python
    lista_nativa = []
    lista_encadeada = ListaEncadeada()
    
    # Inserções no início
    print("\nInserção no início:")
    
    inicio = time.time()
    for i in range(tamanho):
        lista_nativa.insert(0, i)
    fim = time.time()
    tempo_nativa = fim - inicio
    print(f"Lista nativa: {tempo_nativa:.6f} segundos")
    
    inicio = time.time()
    for i in range(tamanho):
        lista_encadeada.inserir_inicio(i)
    fim = time.time()
    tempo_encadeada = fim - inicio
    print(f"Lista encadeada: {tempo_encadeada:.6f} segundos")
    
    if tempo_nativa > tempo_encadeada:
        print(f"Lista encadeada foi {tempo_nativa/tempo_encadeada:.2f}x mais rápida para inserções no início")
    else:
        print(f"Lista nativa foi {tempo_encadeada/tempo_nativa:.2f}x mais rápida para inserções no início")
    
    # Acesso a elementos (somente para lista nativa, pois é muito lento para lista encadeada)
    print("\nAcesso a elementos aleatórios:")
    
    inicio = time.time()
    for i in range(1000):
        indice = (i * 97) % tamanho
        valor = lista_nativa[indice]
    fim = time.time()
    tempo_nativa = fim - inicio
    print(f"Lista nativa: {tempo_nativa:.6f} segundos para 1.000 acessos")
    print("Lista encadeada: tempo muito longo para executar")
    
    print("\nConclusão:")
    print("- Listas encadeadas são melhores para inserções/remoções no início")
    print("- Listas nativas (arrays) são melhores para acesso aleatório")
    print("- A escolha depende do padrão de uso da aplicação")


if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE LISTAS EM PYTHON")
    print("=" * 50)
    
    demonstrar_lista_nativa()
    demonstrar_lista_encadeada()
    comparar_desempenho()
