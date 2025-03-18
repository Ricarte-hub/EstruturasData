"""
Exemplo de Alocação Estática em Python

Embora Python gerencie automaticamente a memória, podemos demonstrar o conceito
de alocação estática usando arrays de tamanho fixo e variáveis locais.
"""

import sys
import numpy as np  # Para arrays de tamanho fixo
import time


def demonstrar_variaveis_estaticas():
    """Demonstra o uso de variáveis com alocação estática."""
    print("\n1. VARIÁVEIS COM ALOCAÇÃO ESTÁTICA")
    print("-" * 50)
    
    # Variáveis primitivas (alocadas estaticamente na pilha)
    inteiro = 42               # 4 bytes (tipicamente)
    flutuante = 3.14159        # 8 bytes (tipicamente)
    booleano = True            # 1 byte
    caractere = 'A'            # 1-4 bytes dependendo da codificação
    
    # Mostrando o tamanho na memória
    print(f"Tamanho de um inteiro: {sys.getsizeof(inteiro)} bytes")
    print(f"Tamanho de um float: {sys.getsizeof(flutuante)} bytes")
    print(f"Tamanho de um booleano: {sys.getsizeof(booleano)} bytes")
    print(f"Tamanho de um caractere: {sys.getsizeof(caractere)} bytes")
    
    # Quando a função termina, essas variáveis são automaticamente desalocadas


def demonstrar_array_estatico():
    """Demonstra o uso de arrays com tamanho fixo."""
    print("\n2. ARRAYS COM TAMANHO FIXO (ALOCAÇÃO ESTÁTICA)")
    print("-" * 50)
    
    # Usando numpy para criar um array de tamanho fixo
    # Este é mais próximo de um array estático em C/C++
    tamanho = 10
    array_estatico = np.zeros(tamanho, dtype=np.int32)
    
    print(f"Array estático criado com tamanho fixo de {tamanho} elementos")
    print(f"Tamanho do array: {array_estatico.size} elementos")
    print(f"Tipo de dados: {array_estatico.dtype}")
    print(f"Tamanho em bytes: {array_estatico.nbytes} bytes")
    
    # Preenchendo o array
    for i in range(tamanho):
        array_estatico[i] = i * 10
    
    print(f"Array preenchido: {array_estatico}")
    
    # Tentativa de adicionar mais elementos (erro em um array estático real)
    try:
        print("Tentando adicionar um elemento além do tamanho fixo...")
        array_estatico[tamanho] = 100  # Isso gerará um erro em um array estático
    except IndexError as e:
        print(f"Erro: {e} - Não é possível expandir um array estático!")


def comparar_acesso():
    """Compara o tempo de acesso entre alocações estáticas e dinâmicas."""
    print("\n3. COMPARAÇÃO DE DESEMPENHO: ESTÁTICO VS DINÂMICO")
    print("-" * 50)
    
    tamanho = 1000000
    repeticoes = 100
    
    # Criar array estático usando numpy (mais próximo de arrays estáticos em C)
    print(f"Criando array estático de {tamanho} inteiros...")
    array_estatico = np.zeros(tamanho, dtype=np.int32)
    
    # Criar lista dinâmica em Python (que usa alocação dinâmica)
    print(f"Criando lista dinâmica de {tamanho} inteiros...")
    lista_dinamica = [0] * tamanho
    
    # Medir tempo de acesso para array estático
    print("\nTestando acesso aleatório:")
    
    inicio = time.time()
    for _ in range(repeticoes):
        indice = np.random.randint(0, tamanho)
        valor = array_estatico[indice]
    tempo_estatico = time.time() - inicio
    
    # Medir tempo de acesso para lista dinâmica
    inicio = time.time()
    for _ in range(repeticoes):
        indice = np.random.randint(0, tamanho)
        valor = lista_dinamica[indice]
    tempo_dinamico = time.time() - inicio
    
    # Mostrar resultados
    print(f"Tempo para {repeticoes} acessos a array estático: {tempo_estatico:.6f} segundos")
    print(f"Tempo para {repeticoes} acessos a lista dinâmica: {tempo_dinamico:.6f} segundos")
    
    if tempo_estatico < tempo_dinamico:
        diferenca_percentual = (tempo_dinamico / tempo_estatico - 1) * 100
        print(f"Array estático foi {diferenca_percentual:.2f}% mais rápido!")
    else:
        diferenca_percentual = (tempo_estatico / tempo_dinamico - 1) * 100
        print(f"Lista dinâmica foi {diferenca_percentual:.2f}% mais rápida!")
    
    print("\nNota: Em Python, mesmo as 'listas dinâmicas' podem ser otimizadas pelo interpretador,")
    print("mas em linguagens de mais baixo nível, a diferença seria mais significativa.")


def demonstrar_limitacoes():
    """Demonstra as limitações da alocação estática."""
    print("\n4. LIMITAÇÕES DA ALOCAÇÃO ESTÁTICA")
    print("-" * 50)
    
    # 1. Tamanho fixo
    tamanho_fixo = 5
    print(f"1. Uma vez definido o tamanho ({tamanho_fixo}), não pode ser alterado")
    array_fixo = np.zeros(tamanho_fixo, dtype=np.int32)
    print(f"   Array: {array_fixo}")
    
    # 2. Desperdício de memória
    tamanho_grande = 10
    elementos_usados = 3
    print(f"\n2. Desperdício de memória se não usar todos os elementos")
    print(f"   Array de tamanho {tamanho_grande}, mas apenas {elementos_usados} elementos usados")
    array_grande = np.zeros(tamanho_grande, dtype=np.int32)
    for i in range(elementos_usados):
        array_grande[i] = i + 1
    print(f"   Array: {array_grande}")
    print(f"   Bytes alocados: {array_grande.nbytes}")
    print(f"   Bytes efetivamente usados: {elementos_usados * 4}")  # 4 bytes por int32
    
    # 3. Não ideal para dados de tamanho desconhecido ou variável
    print(f"\n3. Não adequado para dados de tamanho desconhecido/variável")
    print(f"   Exemplo: leitura de um arquivo com número desconhecido de linhas")
    print(f"   ou processamento de entrada do usuário de tamanho variável.")


if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE ALOCAÇÃO ESTÁTICA DE MEMÓRIA EM PYTHON")
    print("=" * 70)
    print("Nota: Python gerencia automaticamente a alocação de memória,")
    print("mas este exemplo ilustra os conceitos de alocação estática.")
    
    demonstrar_variaveis_estaticas()
    demonstrar_array_estatico()
    comparar_acesso()
    demonstrar_limitacoes()
    
    print("\nCONCLUSÃO:")
    print("A alocação estática é útil quando o tamanho dos dados é conhecido")
    print("antecipadamente e não precisa mudar durante a execução do programa.")
    print("Oferece melhor desempenho, mas menos flexibilidade que a alocação dinâmica.")
