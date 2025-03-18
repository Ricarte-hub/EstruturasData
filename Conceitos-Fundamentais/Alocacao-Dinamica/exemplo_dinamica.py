"""
Exemplo de Alocação Dinâmica em Python

Este script demonstra o conceito de alocação dinâmica de memória usando Python.
Embora Python gerencie automaticamente a memória, os exemplos ilustram o comportamento
e vantagens da alocação dinâmica.
"""

import sys
import time
import random


class No:
    """
    Classe que representa um nó em uma lista encadeada.
    Cada nó é alocado dinamicamente na memória.
    """
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def __str__(self):
        return str(self.valor)


class ListaEncadeada:
    """
    Implementação simples de uma lista encadeada.
    Demonstra a alocação dinâmica de memória à medida que novos nós são adicionados.
    """
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def esta_vazia(self):
        return self.cabeca is None
    
    def inserir_inicio(self, valor):
        """Insere um novo nó no início da lista."""
        novo_no = No(valor)  # Alocação dinâmica de memória para o novo nó
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1
    
    def inserir_fim(self, valor):
        """Insere um novo nó no fim da lista."""
        novo_no = No(valor)  # Alocação dinâmica de memória para o novo nó
        
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def remover(self, valor):
        """Remove um nó com o valor especificado."""
        if self.esta_vazia():
            return False
        
        # Caso especial: remover o primeiro nó
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo  # A memória do nó removido será coletada pelo garbage collector
            self.tamanho -= 1
            return True
        
        # Procurar pelo nó a ser removido
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        
        # Se encontrou o nó
        if atual.proximo:
            atual.proximo = atual.proximo.proximo  # Desreferencia o nó, que será coletado pelo garbage collector
            self.tamanho -= 1
            return True
        
        return False
    
    def imprimir(self):
        """Imprime todos os elementos da lista."""
        if self.esta_vazia():
            print("Lista vazia")
            return
        
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        print(" -> ".join(elementos))


def demonstrar_lista_redimensionavel():
    """
    Demonstra como as listas em Python são dinamicamente redimensionáveis,
    um exemplo claro de alocação dinâmica de memória.
    """
    print("\n1. LISTA DINAMICAMENTE REDIMENSIONÁVEL")
    print("-" * 50)
    
    lista = []
    tamanhos = []
    
    print("Adicionando elementos a uma lista vazia:")
    for i in range(10):
        print(f"Inserindo elemento {i+1}...")
        lista.append(i)
        tamanhos.append(sys.getsizeof(lista))
        print(f"Lista: {lista} | Tamanho em bytes: {tamanhos[-1]}")
    
    print("\nObserve como o tamanho da lista muda:")
    for i in range(1, len(tamanhos)):
        if tamanhos[i] != tamanhos[i-1]:
            print(f"Ao adicionar o elemento {i}, a lista foi redimensionada de {tamanhos[i-1]} para {tamanhos[i]} bytes")
    
    print("\nEm Python, as listas são redimensionadas automaticamente para acomodar novos elementos.")
    print("Isso é um exemplo de alocação dinâmica: a quantidade de memória é ajustada conforme necessário.")


def demonstrar_lista_encadeada():
    """
    Demonstra o uso da lista encadeada, onde cada nó é alocado dinamicamente.
    """
    print("\n2. LISTA ENCADEADA (CADA NÓ É ALOCADO DINAMICAMENTE)")
    print("-" * 50)
    
    lista = ListaEncadeada()
    
    print("Adicionando elementos à lista encadeada:")
    for i in range(1, 6):
        lista.inserir_fim(i * 10)
        print(f"Inserido: {i * 10} | ", end="")
        lista.imprimir()
    
    print("\nRemovendo elementos:")
    for valor in [30, 10, 50]:
        if lista.remover(valor):
            print(f"Removido: {valor} | ", end="")
        else:
            print(f"Valor {valor} não encontrado | ", end="")
        lista.imprimir()
    
    print("\nA lista encadeada é um exemplo perfeito de alocação dinâmica:")
    print("- Cada nó é alocado individualmente quando necessário")
    print("- A lista pode crescer conforme necessário, sem limitações predefinidas")
    print("- A memória é liberada (pelo garbage collector em Python) quando um nó é removido")


def comparar_com_arrays_estaticos():
    """
    Compara listas dinâmicas com arrays estáticos em termos de flexibilidade.
    """
    print("\n3. COMPARAÇÃO: ARRAYS ESTÁTICOS VS LISTAS DINÂMICAS")
    print("-" * 50)
    
    # Simulação de um array estático (em Python seria um array de tamanho fixo usando numpy)
    tamanho_fixo = 5
    print(f"1. Array 'estático' de tamanho {tamanho_fixo}:")
    array_estatico = [0] * tamanho_fixo  # Simulando um array de tamanho fixo
    
    # Preenchendo o array até sua capacidade
    for i in range(tamanho_fixo):
        array_estatico[i] = i + 1
        print(f"   Inserido: {i+1} | Array: {array_estatico}")
    
    print("\n   Problema: se precisarmos adicionar mais elementos, precisaríamos criar um novo array")
    print("   e copiar todos os elementos existentes para ele.\n")
    
    # Lista dinâmica (alocada dinamicamente)
    print("2. Lista dinâmica (sem tamanho predefinido):")
    lista_dinamica = []
    
    # Adicionando elementos
    for i in range(8):  # Adicionamos mais que o tamanho do array estático
        lista_dinamica.append(i + 1)
        print(f"   Inserido: {i+1} | Lista: {lista_dinamica}")
    
    print("\n   Vantagem: a lista cresce automaticamente conforme necessário, sem necessidade")
    print("   de realocar e copiar manualmente os elementos.")


def demonstrar_aplicacao_pratica():
    """
    Demonstra uma aplicação prática onde a alocação dinâmica é essencial.
    """
    print("\n4. APLICAÇÃO PRÁTICA: PROCESSANDO DADOS DE TAMANHO DESCONHECIDO")
    print("-" * 50)
    
    print("Imagine um sistema que processa transações financeiras.")
    print("O número de transações varia diariamente e não é conhecido antecipadamente.\n")
    
    # Simulando a chegada de transações (número aleatório a cada execução)
    num_transacoes = random.randint(5, 15)
    print(f"Hoje chegaram {num_transacoes} transações para processar.")
    
    # Em um sistema real, estas transações viriam de uma fonte externa (arquivo, banco de dados, etc.)
    transacoes = []  # Lista dinamicamente alocada
    
    # Processando cada transação
    valor_total = 0
    for i in range(num_transacoes):
        # Gerando uma transação aleatória entre R$10 e R$1000
        valor = round(random.uniform(10, 1000), 2)
        transacoes.append(valor)
        valor_total += valor
    
    # Mostrando as transações processadas
    print("\nTransações processadas:")
    for i, valor in enumerate(transacoes, 1):
        print(f"Transação {i}: R$ {valor:.2f}")
    
    print(f"\nValor total: R$ {valor_total:.2f}")
    print(f"Valor médio: R$ {valor_total/num_transacoes:.2f}")
    
    print("\nNeste exemplo, a alocação dinâmica permite processar qualquer número de transações")
    print("sem precisar definir um limite máximo antecipadamente.")


if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE ALOCAÇÃO DINÂMICA DE MEMÓRIA EM PYTHON")
    print("=" * 70)
    print("Nota: Python gerencia automaticamente a alocação dinâmica de memória,")
    print("mas estes exemplos ilustram os conceitos e benefícios da alocação dinâmica.")
    
    demonstrar_lista_redimensionavel()
    demonstrar_lista_encadeada()
    comparar_com_arrays_estaticos()
    demonstrar_aplicacao_pratica()
    
    print("\nCONCLUSÃO:")
    print("A alocação dinâmica de memória permite que programas utilizem memória")
    print("de maneira eficiente, alocando apenas o necessário conforme a execução avança.")
    print("Isso é particularmente importante para estruturas de dados cujo tamanho")
    print("não pode ser determinado em tempo de compilação, como listas encadeadas,")
    print("árvores, grafos, e para processamento de dados de tamanho desconhecido.")
