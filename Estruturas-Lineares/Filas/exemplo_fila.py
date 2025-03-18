"""
Exemplo de Implementação e Uso de Filas

Este arquivo demonstra:
1. Implementação de uma fila usando uma lista
2. Implementação de uma fila usando uma lista encadeada
3. Uso do módulo collections.deque para filas eficientes
4. Implementação de uma fila circular
5. Implementação de uma fila de prioridade
6. Aplicações práticas
"""

import time
from queue import Queue, PriorityQueue
from collections import deque
import random


class FilaLista:
    """Implementação de uma fila usando uma lista Python."""
    
    def __init__(self):
        self.itens = []
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.itens.pop(0)  # O(n) - precisa deslocar todos os elementos
    
    def frente(self):
        """Retorna o item do início sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.itens[0]
    
    def tamanho(self):
        """Retorna o número de itens na fila."""
        return len(self.itens)


class No:
    """Nó para a fila baseada em lista encadeada."""
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    """Implementação de uma fila usando lista encadeada."""
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0
    
    def esta_vazia(self):
        return self.inicio is None
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        novo_no = No(item)
        
        if self.esta_vazia():
            self.inicio = novo_no
        else:
            self.fim.proximo = novo_no
        
        self.fim = novo_no
        self._tamanho += 1
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
        
        self._tamanho -= 1
        return valor
    
    def frente(self):
        """Retorna o item do início sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.inicio.valor
    
    def tamanho(self):
        """Retorna o número de itens na fila."""
        return self._tamanho


class FilaCircular:
    """Implementação de uma fila circular usando um array."""
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self._tamanho = 0
    
    def esta_vazia(self):
        return self._tamanho == 0
    
    def esta_cheia(self):
        return self._tamanho == self.capacidade
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        if self.esta_cheia():
            raise Exception("Fila cheia")
        
        self.itens[self.fim] = item
        self.fim = (self.fim + 1) % self.capacidade
        self._tamanho += 1
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        
        valor = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self._tamanho -= 1
        return valor
    
    def frente(self):
        """Retorna o item do início sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.itens[self.inicio]
    
    def tamanho(self):
        """Retorna o número de itens na fila."""
        return self._tamanho


def demonstrar_fila_lista():
    """Demonstra o uso da fila implementada com lista."""
    print("\n1. FILA USANDO LISTA")
    print("-" * 50)
    
    fila = FilaLista()
    print("Fila criada (vazia)")
    
    print("\nOperações de enfileiramento:")
    for i in range(1, 6):
        print(f"Enfileirando {i}...")
        fila.enfileirar(i)
        print(f"Fila: {fila.itens} | Tamanho: {fila.tamanho()}")
    
    print("\nOperação de consulta (frente):")
    frente = fila.frente()
    print(f"Elemento na frente da fila: {frente}")
    
    print("\nOperações de desenfileiramento:")
    while not fila.esta_vazia():
        valor = fila.desenfileirar()
        print(f"Desenfileirado: {valor} | Fila restante: {fila.itens}")
    
    print("\nObservações:")
    print("- Implementação simples, mas ineficiente para filas grandes")
    print("- Operação desenfileirar é O(n) devido ao deslocamento de elementos")


def demonstrar_fila_encadeada():
    """Demonstra o uso da fila implementada com lista encadeada."""
    print("\n2. FILA USANDO LISTA ENCADEADA")
    print("-" * 50)
    
    fila = FilaEncadeada()
    print("Fila encadeada criada (vazia)")
    
    print("\nOperações de enfileiramento:")
    valores = [10, 20, 30, 40, 50]
    for valor in valores:
        print(f"Enfileirando {valor}...")
        fila.enfileirar(valor)
        print(f"Tamanho da fila: {fila.tamanho()}")
    
    print("\nOperação de consulta (frente):")
    frente = fila.frente()
    print(f"Elemento na frente da fila: {frente}")
    
    print("\nOperações de desenfileiramento:")
    while not fila.esta_vazia():
        valor = fila.desenfileirar()
        print(f"Desenfileirado: {valor} | Tamanho restante: {fila.tamanho()}")
    
    print("\nObservações:")
    print("- Implementação mais eficiente para filas grandes")
    print("- Todas as operações são O(1)")
    print("- Usa mais memória devido aos ponteiros")


def demonstrar_fila_deque():
    """Demonstra o uso do deque como uma fila eficiente."""
    print("\n3. FILA USANDO COLLECTIONS.DEQUE")
    print("-" * 50)
    
    fila = deque()
    print("Fila deque criada (vazia)")
    
    print("\nOperações de enfileiramento:")
    for i in range(1, 6):
        print(f"Enfileirando {i}...")
        fila.append(i)  # O(1)
        print(f"Fila: {list(fila)} | Tamanho: {len(fila)}")
    
    print("\nOperação de consulta (frente):")
    if fila:
        print(f"Elemento na frente da fila: {fila[0]}")
    
    print("\nOperações de desenfileiramento:")
    while fila:
        valor = fila.popleft()  # O(1)
        print(f"Desenfileirado: {valor} | Fila restante: {list(fila)}")
    
    print("\nObservações:")
    print("- Implementação mais eficiente em Python para filas")
    print("- Todas as operações são O(1)")
    print("- É uma fila de duas pontas (deque), permitindo operações em ambas as extremidades")
    print("- Recomendada para uso em produção")


def demonstrar_fila_circular():
    """Demonstra o uso da fila circular."""
    print("\n4. FILA CIRCULAR")
    print("-" * 50)
    
    capacidade = 5
    fila = FilaCircular(capacidade)
    print(f"Fila circular criada com capacidade {capacidade}")
    
    print("\nOperações de enfileiramento:")
    for i in range(1, 6):
        print(f"Enfileirando {i}...")
        fila.enfileirar(i)
        print(f"Fila: {fila.itens} | Início: {fila.inicio} | Fim: {fila.fim}")
    
    print("\nTentativa de enfileirar em uma fila cheia:")
    try:
        fila.enfileirar(6)
    except Exception as e:
        print(f"Erro: {e}")
    
    print("\nDesenfileirando alguns elementos:")
    for _ in range(3):
        valor = fila.desenfileirar()
        print(f"Desenfileirado: {valor} | Fila: {fila.itens} | Início: {fila.inicio} | Fim: {fila.fim}")
    
    print("\nEnfileirando novos elementos (demonstrando a circularidade):")
    for i in range(6, 9):
        try:
            fila.enfileirar(i)
            print(f"Enfileirado: {i} | Fila: {fila.itens} | Início: {fila.inicio} | Fim: {fila.fim}")
        except Exception as e:
            print(f"Erro ao enfileirar {i}: {e}")
    
    print("\nDesenfileirando todos os elementos restantes:")
    while not fila.esta_vazia():
        valor = fila.desenfileirar()
        print(f"Desenfileirado: {valor} | Fila: {fila.itens} | Início: {fila.inicio} | Fim: {fila.fim}")
    
    print("\nObservações:")
    print("- Evita o desperdício de espaço usando uma abordagem circular")
    print("- Útil quando a fila tem um tamanho máximo conhecido")
    print("- Todas as operações são O(1)")


def demonstrar_fila_prioridade():
    """Demonstra o uso da fila de prioridade."""
    print("\n5. FILA DE PRIORIDADE")
    print("-" * 50)
    
    fila = PriorityQueue()
    print("Fila de prioridade criada (vazia)")
    
    print("\nEnfileirando elementos com prioridades:")
    elementos = [
        (3, "Tarefa com prioridade normal"),
        (1, "Tarefa urgente"),
        (5, "Tarefa de baixa prioridade"),
        (2, "Tarefa importante"),
        (4, "Tarefa regular")
    ]
    
    for prioridade, tarefa in elementos:
        print(f"Enfileirando: Prioridade {prioridade} - {tarefa}")
        fila.put((prioridade, tarefa))
    
    print("\nDesenfileirando elementos (sempre o de maior prioridade primeiro):")
    while not fila.empty():
        prioridade, tarefa = fila.get()
        print(f"Desenfileirado: Prioridade {prioridade} - {tarefa}")
    
    print("\nObservações:")
    print("- Sempre retorna o elemento com maior prioridade (menor número)")
    print("- Implementada internamente com um heap, operações são O(log n)")
    print("- Útil para escalonamento de tarefas e algoritmos de busca")


def aplicacao_simulacao_atendimento():
    """Demonstra uma aplicação prática: simulação de uma fila de atendimento."""
    print("\n6. APLICAÇÃO PRÁTICA: SIMULAÇÃO DE ATENDIMENTO")
    print("-" * 50)
    
    # Parâmetros da simulação
    duracao_simulacao = 60  # minutos
    tempo_medio_chegada = 5  # minutos entre clientes
    tempo_medio_atendimento = 8  # minutos por cliente
    
    # Contadores
    tempo_total_espera = 0
    clientes_atendidos = 0
    clientes_na_fila = 0
    
    # Fila de atendimento
    fila_clientes = deque()
    
    # Tempo atual e tempo do próximo evento
    tempo_atual = 0
    proximo_cliente = random.expovariate(1.0 / tempo_medio_chegada)
    fim_atendimento = float('inf')  # Nenhum cliente sendo atendido inicialmente
    
    print(f"Simulando {duracao_simulacao} minutos de atendimento")
    print(f"Tempo médio entre chegadas: {tempo_medio_chegada} minutos")
    print(f"Tempo médio de atendimento: {tempo_medio_atendimento} minutos")
    print("\nIniciando simulação...\n")
    
    while tempo_atual < duracao_simulacao:
        # Determina o próximo evento
        if proximo_cliente < fim_atendimento:
            # Próximo evento: chegada de cliente
            tempo_atual = proximo_cliente
            tempo_chegada = tempo_atual
            
            # Agenda próxima chegada
            proximo_cliente = tempo_atual + random.expovariate(1.0 / tempo_medio_chegada)
            
            # Enfileira o cliente com seu tempo de chegada
            fila_clientes.append(tempo_chegada)
            clientes_na_fila += 1
            
            print(f"Tempo {tempo_atual:.1f} min: Cliente chegou. Clientes na fila: {clientes_na_fila}")
            
            # Se não há cliente sendo atendido, inicia o atendimento
            if fim_atendimento == float('inf'):
                # Desenfileira o cliente
                tempo_chegada = fila_clientes.popleft()
                clientes_na_fila -= 1
                
                # Calcula tempo de espera
                tempo_espera = tempo_atual - tempo_chegada
                tempo_total_espera += tempo_espera
                
                # Agenda fim do atendimento
                duracao_atendimento = random.expovariate(1.0 / tempo_medio_atendimento)
                fim_atendimento = tempo_atual + duracao_atendimento
                
                print(f"Tempo {tempo_atual:.1f} min: Iniciando atendimento. Tempo de espera: {tempo_espera:.1f} min")
        else:
            # Próximo evento: fim de atendimento
            tempo_atual = fim_atendimento
            clientes_atendidos += 1
            
            print(f"Tempo {tempo_atual:.1f} min: Atendimento concluído. Total atendidos: {clientes_atendidos}")
            
            # Se há mais clientes na fila, inicia próximo atendimento
            if fila_clientes:
                # Desenfileira o próximo cliente
                tempo_chegada = fila_clientes.popleft()
                clientes_na_fila -= 1
                
                # Calcula tempo de espera
                tempo_espera = tempo_atual - tempo_chegada
                tempo_total_espera += tempo_espera
                
                # Agenda fim do atendimento
                duracao_atendimento = random.expovariate(1.0 / tempo_medio_atendimento)
                fim_atendimento = tempo_atual + duracao_atendimento
                
                print(f"Tempo {tempo_atual:.1f} min: Iniciando próximo atendimento. Tempo de espera: {tempo_espera:.1f} min")
            else:
                # Sem mais clientes na fila
                fim_atendimento = float('inf')
    
    print("\nFim da simulação")
    print(f"Total de clientes atendidos: {clientes_atendidos}")
    
    if clientes_atendidos > 0:
        tempo_medio_espera = tempo_total_espera / clientes_atendidos
        print(f"Tempo médio de espera: {tempo_medio_espera:.2f} minutos")
    
    print(f"Clientes restantes na fila: {len(fila_clientes)}")


if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE FILAS EM PYTHON")
    print("=" * 50)
    
    demonstrar_fila_lista()
    demonstrar_fila_encadeada()
    demonstrar_fila_deque()
    demonstrar_fila_circular()
    demonstrar_fila_prioridade()
    aplicacao_simulacao_atendimento()
