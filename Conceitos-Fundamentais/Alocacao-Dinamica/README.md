# Alocação Dinâmica de Memória

## O que é Alocação Dinâmica?

A alocação dinâmica de memória ocorre quando o espaço de memória é alocado durante a execução do programa, e não durante a compilação. Isso permite que o programa solicite memória conforme necessário, com base nas necessidades que surgem durante sua execução.

## Características Principais

1. **Determinada em tempo de execução**: O espaço é alocado somente quando necessário, durante a execução do programa
2. **Tamanho flexível**: A quantidade de memória pode ser definida com base em dados de entrada ou outras condições em tempo de execução
3. **Localização no heap (monticulo)**: A memória alocada dinamicamente fica no heap, não na pilha
4. **Acesso indireto**: Normalmente acessada através de ponteiros ou referências
5. **Desalocação manual ou automática**: Dependendo da linguagem, a memória deve ser liberada manualmente ou é gerenciada automaticamente (garbage collection)

## Exemplos de Alocação Dinâmica

Em Python, C# ou Java, a alocação dinâmica ocorre em:

- Objetos criados com `new` (em C#, Java)
- Praticamente todos os objetos em Python (listas, dicionários, objetos customizados)
- Arrays redimensionáveis (listas em Python)
- Estruturas de dados como listas encadeadas, árvores, grafos

## Vantagens da Alocação Dinâmica

1. **Flexibilidade**: Aloca exatamente a quantidade de memória necessária
2. **Eficiência de espaço**: Evita desperdício de memória
3. **Estruturas de tamanho variável**: Permite criar e manipular estruturas cujo tamanho não é conhecido em tempo de compilação
4. **Compartilhamento de dados**: Facilita o compartilhamento de dados entre diferentes partes do programa

## Desvantagens da Alocação Dinâmica

1. **Overhead de gerenciamento**: Requer tempo adicional para gerenciar a alocação e desalocação
2. **Acesso mais lento**: Geralmente mais lento que o acesso a memória alocada estaticamente
3. **Fragmentação da memória**: Pode levar à fragmentação do heap
4. **Vazamentos de memória**: Se não for gerenciada corretamente, pode causar vazamentos (em linguagens sem garbage collector)
5. **Complexidade adicional**: Requer mais cuidado na implementação

## Exemplos de Uso Prático

- Listas encadeadas, árvores e grafos
- Arrays redimensionáveis (como as listas em Python)
- Leitura de dados de tamanho desconhecido (como linhas de um arquivo)
- Objetos criados durante a execução do programa

## Onde é usada em Estruturas de Dados

- Listas encadeadas (simples, duplas, circulares)
- Árvores (binárias, AVL, B, B+, etc.)
- Grafos
- Tabelas hash com redimensionamento dinâmico
- Pilhas e filas de tamanho dinâmico

O arquivo `exemplo_dinamica.py` demonstra o uso de alocação dinâmica em Python.
