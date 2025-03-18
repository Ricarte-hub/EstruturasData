# Definição e Importância das Estruturas de Dados

## Estruturas de Dados Lineares vs. Não Lineares

### Estruturas Lineares

As estruturas de dados lineares organizam os elementos em uma sequência, onde cada elemento tem um único predecessor e um único sucessor (exceto o primeiro e o último elemento).

**Exemplos de Estruturas Lineares:**

1. **Arrays (Vetores)**: Coleção de elementos do mesmo tipo armazenados em posições contíguas de memória.
2. **Listas Encadeadas**: Sequência de nós onde cada nó contém dados e uma referência ao próximo nó.
3. **Pilhas (Stacks)**: Seguem o princípio LIFO (Last In, First Out) - o último elemento inserido é o primeiro a ser removido.
4. **Filas (Queues)**: Seguem o princípio FIFO (First In, First Out) - o primeiro elemento inserido é o primeiro a ser removido.
5. **Deques (Double Ended Queues)**: Permitem inserção e remoção de elementos em ambas as extremidades.

**Características:**
- Cada elemento tem uma posição única na sequência
- Linearmente ordenados
- Acesso sequencial (em alguns casos, também acesso direto)

### Estruturas Não Lineares

As estruturas de dados não lineares não organizam os elementos em uma sequência linear. Um elemento pode ter vários predecessores e sucessores.

**Exemplos de Estruturas Não Lineares:**

1. **Árvores**: Estruturas hierárquicas com um nó raiz e nós filhos.
   - **Árvore Binária**: Cada nó tem no máximo dois filhos
   - **Árvore AVL**: Árvore binária de busca auto-balanceada
   - **Árvore B**: Otimizada para sistemas de armazenamento que leem e escrevem blocos grandes de dados
   
2. **Grafos**: Conjunto de vértices (nós) conectados por arestas (conexões).
   - **Grafo Direcionado**: As arestas têm direção
   - **Grafo Não-Direcionado**: As arestas não têm direção
   - **Grafo Ponderado**: As arestas têm pesos associados

3. **Tabelas Hash**: Estruturas que mapeiam chaves para valores usando uma função hash.

**Características:**
- Elementos podem ter múltiplas conexões
- Organização não sequencial
- Representam relações complexas

## Impacto no Desempenho de Programas

A escolha da estrutura de dados correta é fundamental para o desempenho de um programa, afetando diretamente:

### 1. Tempo de Execução (Complexidade Temporal)
- Uma busca em uma lista não ordenada tem complexidade O(n)
- Uma busca em uma árvore binária balanceada tem complexidade O(log n)
- Uma busca em uma tabela hash bem implementada pode ter complexidade O(1)

### 2. Uso de Memória (Complexidade Espacial)
- Arrays usam memória contígua e têm baixa sobrecarga
- Listas encadeadas precisam de espaço adicional para armazenar referências
- Árvores e grafos requerem memória para nós e conexões

### 3. Facilidade de Implementação e Manutenção
- Estruturas mais simples são mais fáceis de implementar e depurar
- Estruturas mais complexas podem exigir algoritmos avançados para operações básicas

### 4. Escalabilidade
- Algumas estruturas, como árvores de busca balanceadas, mantêm bom desempenho mesmo com grandes volumes de dados
- Outras, como arrays simples, podem degradar rapidamente com o aumento de dados

A diferença entre usar a estrutura certa e errada pode significar um programa que executa em milissegundos versus um que leva horas para completar a mesma tarefa.

O arquivo `exemplo_performance.py` demonstra como a escolha da estrutura de dados impacta diretamente no desempenho do código.
