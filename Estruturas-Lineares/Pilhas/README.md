# Pilhas (Stacks)

## O Que São Pilhas?

Uma pilha é uma estrutura de dados linear que segue o princípio **LIFO** (Last In, First Out), ou seja, o último elemento a entrar é o primeiro a sair. É semelhante a uma pilha de pratos: você adiciona e remove pratos do topo.

## Características Principais

- **Princípio LIFO**: O último elemento inserido é o primeiro a ser removido
- **Acesso restrito**: Elementos só podem ser inseridos, removidos e acessados pelo topo da pilha
- **Operações ocorrem em uma única extremidade**: Todas as operações são realizadas no topo da pilha

## Operações Básicas

1. **Empilhar (Push)**: Adiciona um elemento ao topo da pilha
   - Complexidade: O(1)

2. **Desempilhar (Pop)**: Remove o elemento do topo da pilha e o retorna
   - Complexidade: O(1)

3. **Topo (Top/Peek)**: Retorna o elemento do topo sem removê-lo
   - Complexidade: O(1)

4. **IsEmpty**: Verifica se a pilha está vazia
   - Complexidade: O(1)

5. **Tamanho (Size)**: Retorna o número de elementos na pilha
   - Complexidade: O(1)

## Implementações Comuns

### 1. Implementação baseada em Array
- **Vantagens**: Uso eficiente de memória, acesso rápido ao topo
- **Desvantagens**: Tamanho fixo ou necessidade de redimensionamento

### 2. Implementação baseada em Lista Encadeada
- **Vantagens**: Tamanho dinâmico, sem necessidade de redimensionamento
- **Desvantagens**: Maior uso de memória devido aos ponteiros/referências

## Aplicações Práticas

1. **Gerenciamento de Memória**
   - Controle de chamadas de funções (stack frame)
   - Alocação de memória em linguagens como C/C++

2. **Avaliação de Expressões**
   - Conversão de expressões infixa para pós-fixa
   - Avaliação de expressões matemáticas
   - Verificação de parênteses balanceados

3. **Navegadores Web**
   - Histórico de navegação (botão "Voltar")
   - Gerenciamento de abas

4. **Editores de Texto**
   - Funcionalidades de desfazer/refazer (undo/redo)
   - Histórico de ações

5. **Algoritmos**
   - Busca em profundidade (DFS) em grafos
   - Backtracking

6. **Compiladores**
   - Análise sintática
   - Verificação de tipos
   - Avaliação de expressões

## Complexidade de Tempo

| Operação     | Complexidade |
|--------------|--------------|
| Push         | O(1)         |
| Pop          | O(1)         |
| Peek         | O(1)         |
| IsEmpty      | O(1)         |
| Size         | O(1)         |

## Vantagens e Desvantagens

### Vantagens
- Operações principais têm complexidade O(1)
- Simples de entender e implementar
- Útil para rastrear ações em ordem inversa

### Desvantagens
- Acesso limitado (apenas ao elemento do topo)
- Não adequada para acesso aleatório ou busca
- Não adequada para processamento em ordem de chegada

## Diferenças entre Pilha e Fila

| Aspecto          | Pilha (LIFO)                    | Fila (FIFO)                     |
|------------------|----------------------------------|----------------------------------|
| Princípio        | Último a entrar, primeiro a sair | Primeiro a entrar, primeiro a sair |
| Ponto de acesso  | Uma extremidade (topo)          | Duas extremidades (frente e fundo) |
| Inserção         | Topo                            | Fim                              |
| Remoção          | Topo                            | Frente                           |
| Ordem de acesso  | Inversa à ordem de inserção      | Mesma ordem de inserção          |
| Visualização     | Pilha de pratos                  | Fila de pessoas                  |

## Implementação em Python

Python oferece várias maneiras de implementar pilhas:

1. Usando listas nativas (métodos `append()` e `pop()`)
2. Módulo `collections` com `deque`
3. Criando classes personalizadas

Veja o arquivo `exemplo_pilha.py` para exemplos de implementação e uso.
