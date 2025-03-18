# Alocação Estática de Memória

## O que é Alocação Estática?

A alocação estática de memória ocorre quando o espaço necessário para armazenar variáveis é alocado durante a compilação, antes da execução do programa. O compilador determina quanto espaço reservar com base nas declarações de variáveis no código.

## Características Principais

1. **Determinada em tempo de compilação**: O espaço é reservado antes da execução do programa
2. **Tamanho fixo**: O tamanho da memória alocada não pode ser alterado durante a execução
3. **Localização na pilha (stack)**: Geralmente, as variáveis estaticamente alocadas são armazenadas na pilha de memória
4. **Acesso rápido**: Geralmente mais rápido que a alocação dinâmica
5. **Desalocação automática**: A memória é liberada automaticamente quando sai do escopo

## Exemplos de Alocação Estática

Em Python, C# ou Java, a alocação estática ocorre principalmente em:

- Variáveis primitivas locais (inteiros, floats, booleanos)
- Arrays de tamanho fixo (em algumas linguagens)
- Variáveis de classe estáticas
- Constantes

## Vantagens da Alocação Estática

1. **Eficiência**: Acesso mais rápido à memória
2. **Previsibilidade**: Comportamento mais previsível do programa
3. **Simplicidade**: Não é necessário gerenciar manualmente a liberação de memória
4. **Evita vazamentos de memória**: A desalocação é automática

## Desvantagens da Alocação Estática

1. **Inflexibilidade**: O tamanho não pode ser ajustado durante a execução
2. **Desperdício potencial**: Se você alocar mais espaço do que o necessário, o excesso será desperdiçado
3. **Limitações**: Não adequada para estruturas de dados cujo tamanho não é conhecido antecipadamente

## Exemplos de Uso Prático

- Arrays de tamanho fixo
- Buffers de tamanho conhecido
- Armazenamento de dados temporários de tamanho constante
- Variáveis locais em funções

## Onde é usada em Estruturas de Dados

- Arrays estáticos
- Matrizes de tamanho fixo
- Pilhas e filas de tamanho predefinido
- Tabelas hash com número fixo de buckets

O arquivo `exemplo_estatica.py` demonstra o uso de alocação estática em Python.
