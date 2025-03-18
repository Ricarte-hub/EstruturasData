# Listas

## O Que São Listas?

Uma lista é uma estrutura de dados linear que consiste em uma sequência de elementos. Cada elemento pode ser acessado por sua posição, ou índice, na sequência. As listas podem ser implementadas de várias formas, sendo as mais comuns:

1. **Arrays (Vetores)**: Implementação com elementos armazenados contiguamente na memória
2. **Listas Encadeadas**: Implementação com nós ligados por referências ou ponteiros

## Características Principais

- **Ordenação sequencial**: Os elementos são ordenados em uma sequência linear
- **Acesso indexado**: Cada elemento pode ser acessado por sua posição
- **Tamanho variável**: Dependendo da implementação, pode ter tamanho fixo ou dinâmico
- **Elementos homogêneos ou heterogêneos**: Pode armazenar elementos do mesmo tipo ou tipos diferentes, dependendo da linguagem

## Tipos de Listas

### 1. Listas Baseadas em Arrays
- **Alocação contígua** de memória
- **Acesso direto** aos elementos (O(1))
- **Inserção/remoção ineficiente** no meio (O(n))
- Tamanho geralmente limitado (mas pode ser redimensionado)

### 2. Listas Encadeadas
- **Nós conectados** por referências/ponteiros
- **Inserção/remoção eficiente** em qualquer posição (O(1) após localizar)
- **Acesso sequencial** (O(n)) - sem acesso direto por índice
- Tamanho limitado apenas pela memória disponível

### 3. Listas Duplamente Encadeadas
- Cada nó tem referências para o próximo e o anterior
- Permite navegação em ambas as direções
- Mais flexível, mas consome mais memória

### 4. Listas Circulares
- O último elemento está conectado ao primeiro
- Útil para aplicações que precisam "dar a volta" na lista

## Operações Principais

1. **Inserção**: Adicionar um elemento na lista
   - No início: O(1) para listas encadeadas, O(n) para arrays
   - No fim: O(1) para arrays (com espaço disponível) e listas duplamente encadeadas, O(n) para listas encadeadas simples
   - No meio: O(n) para ambos (busca + deslocamento/reconexão)

2. **Remoção**: Remover um elemento da lista
   - No início: O(1) para listas encadeadas, O(n) para arrays
   - No fim: O(1) para arrays e listas duplamente encadeadas, O(n) para listas encadeadas simples
   - No meio: O(n) para ambos

3. **Acesso**: Recuperar um elemento da lista
   - Por índice: O(1) para arrays, O(n) para listas encadeadas
   - Por valor (busca): O(n) para ambos em listas não ordenadas

4. **Atualização**: Modificar um elemento existente
   - Por índice: O(1) para arrays, O(n) para listas encadeadas
   - Por valor: O(n) para ambos (busca + modificação)

5. **Traversal**: Percorrer todos os elementos
   - O(n) para ambos

## Aplicações Comuns

- **Histórico de navegação** em browsers
- **Lista de reprodução** em aplicativos de música
- **Gerenciamento de tarefas** em sistemas operacionais
- **Implementação de outras estruturas** como pilhas, filas, grafos
- **Manipulação de dados** onde a ordem é importante

## Implementação em Python

Python já possui uma implementação nativa de listas dinâmicas, implementadas como arrays redimensionáveis. Veja o arquivo `exemplo_lista.py` para exemplos de uso e implementação.

## Comparativo entre Arrays e Listas Encadeadas

| Operação              | Array   | Lista Encadeada |
|-----------------------|---------|-----------------|
| Acesso por índice     | O(1)    | O(n)            |
| Inserção no início    | O(n)    | O(1)            |
| Inserção no fim       | O(1)*   | O(1)**          |
| Inserção no meio      | O(n)    | O(n)            |
| Remoção no início     | O(n)    | O(1)            |
| Remoção no fim        | O(1)    | O(n)**          |
| Remoção no meio       | O(n)    | O(n)            |
| Uso de memória        | Baixo   | Alto            |

\* Amortizado, caso seja necessário redimensionar o array
\** O(1) para listas duplamente encadeadas, O(n) para listas encadeadas simples

A escolha entre implementações de listas deve considerar as operações mais frequentes na aplicação específica.
