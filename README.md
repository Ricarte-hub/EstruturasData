# Estruturas de Dados

Repositório criado para a disciplina de Estruturas de Dados I da UDF - 3º semestre, por:
- Arthur Oliveira Lima
- Arthur Fernandes Franco Ricarte
- Luara Vitória Nunes Cardoso

## Problema Prático: Sistema de Atendimento de Emergência Hospitalar

### Descrição do Problema

Um hospital precisa gerenciar o atendimento de pacientes na emergência baseado na gravidade dos casos. Os pacientes devem ser atendidos por ordem de prioridade, e não por ordem de chegada.

Casos muito graves (emergências) devem ser atendidos imediatamente, casos moderadamente graves (urgências) devem ser atendidos assim que possível, e casos menos graves (pouco urgentes) devem aguardar enquanto houver casos mais sérios.

### Estrutura de Dados Escolhida: Fila de Prioridade

Para resolver este problema, escolhemos a **Fila de Prioridade** (implementada como uma lista ordenada). Esta estrutura nos permite:

1. Inserir pacientes em qualquer posição da fila, baseado na gravidade do caso
2. Garantir que o próximo paciente a ser atendido seja sempre o mais prioritário
3. Reorganizar a fila automaticamente quando novos pacientes chegam

A fila de prioridade é ideal neste cenário porque combina a lógica FIFO (First In, First Out) das filas tradicionais com a capacidade de ordenar elementos por prioridade.

### Implementação

A implementação da solução está disponível no arquivo `solucao_pratica.py`.
