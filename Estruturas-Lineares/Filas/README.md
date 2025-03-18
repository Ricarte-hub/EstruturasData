# Filas (Queues)

## O Que São Filas?

Uma fila é uma estrutura de dados linear que segue o princípio **FIFO** (First In, First Out), ou seja, o primeiro elemento a entrar é o primeiro a sair. É semelhante a uma fila de pessoas em um banco ou supermercado: quem chega primeiro é atendido primeiro.

## Características Principais

- **Princípio FIFO**: O primeiro elemento inserido é o primeiro a ser removido
- **Duas operações principais**: Enfileirar (inserir) e Desenfileirar (remover)
- **Acesso restrito**: Elementos só podem ser acessados pela frente da fila
- **Inserção e remoção em extremidades opostas**: Inserção no final, remoção no início

## Operações Básicas

1. **Enfileirar (Enqueue)**: Adiciona um elemento ao final da fila
   - Complexidade: O(1)

2. **Desenfileirar (Dequeue)**: Remove o elemento do início da fila e o retorna
   - Complexidade: O(1)

3. **Frente (Front/Peek)**: Retorna o elemento do início da fila sem removê-lo
   - Complexidade: O(1)

4. **IsEmpty**: Verifica se a fila está vazia
   - Complexidade: O(1)

5. **Tamanho (Size)**: Retorna o número de elementos na fila
   - Complexidade: O(1)

## Tipos de Filas

### 1. Fila Simples
- Implementação básica do princípio FIFO
- Elementos são adicionados ao final e removidos do início

### 2. Fila Circular
- Usa um array circular para implementação eficiente
- Evita o deslocamento de elementos ao desenfileirar
- Útil quando há um tamanho máximo conhecido para a fila

### 3. Fila de Prioridade
- Elementos possuem prioridades associadas
- Elementos com maior prioridade são desenfileirados primeiro
- Normalmente implementada com Heap ou Lista Ordenada

### 4. Fila de Duas Pontas (Deque)
- Permite inserção e remoção em ambas as extremidades
- Combina características de filas e pilhas

## Implementações Comuns

### 1. Implementação baseada em Array
- **Vantagens**: Acesso rápido aos elementos
- **Desvantagens**: Tamanho fixo ou necessidade de redimensionamento

### 2. Implementação baseada em Lista Encadeada
- **Vantagens**: Tamanho dinâmico, sem necessidade de redimensionamento
- **Desvantagens**: Maior uso de memória devido aos ponteiros

## Aplicações Práticas

1. **Gerenciamento de Recursos**
   - Escalonamento de CPU em sistemas operacionais
   - Buffers para impressoras e dispositivos de E/S

2. **Sincronização**
   - Transferência de dados entre threads (consumidor-produtor)
   - Gerenciamento de pedidos em sistemas online

3. **Algoritmos de Busca e Travessia**
   - Busca em Largura (BFS) em grafos
   - Travessia em nível em árvores

4. **Sistemas em Tempo Real**
   - Gerenciamento de eventos e interrupções
   - Processamento de solicitações em ordem cronológica

5. **Aplicações Práticas Cotidianas**
   - Filas de atendimento em serviços
   - Sistemas de reserva (hotéis, voos, etc.)
   - Gerenciamento de tarefas em ordem de chegada

## Complexidade de Tempo

| Operação     | Complexidade |
|--------------|--------------|
| Enfileirar   | O(1)         |
| Desenfileirar| O(1)         |
| Peek         | O(1)         |
| IsEmpty      | O(1)         |
| Size         | O(1)         |

## Vantagens e Desvantagens

### Vantagens
- Simples de entender e implementar
- Eficiente para processamento em ordem de chegada
- Operações principais têm complexidade O(1)

### Desvantagens
- Acesso limitado (apenas ao elemento da frente)
- Não adequada para acesso aleatório ou busca
- Não eficiente para remoção de elementos arbitrários

## Implementação em Python

Python oferece várias maneiras de implementar filas:

1. Módulo `queue` com a classe `Queue` (thread-safe)
2. Módulo `collections` com `deque` (mais eficiente para filas)
3. Usando listas (menos eficiente para filas grandes)

Veja o arquivo `exemplo_fila.py` para exemplos de implementação e uso.
