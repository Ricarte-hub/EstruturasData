import time
import random
from collections import defaultdict

"""
Este programa demonstra a diferença de desempenho entre diferentes estruturas de dados
para uma tarefa comum: contar a frequência de elementos em uma coleção.

Serão comparadas três abordagens:
1. Lista + contagem linear (ineficiente)
2. Lista ordenada + busca (moderadamente eficiente)
3. Dicionário (muito eficiente)
"""

def gerar_dados(tamanho):
    """Gera uma lista de números aleatórios entre 1 e 1000."""
    return [random.randint(1, 1000) for _ in range(tamanho)]

# Abordagem 1: Lista + contagem linear (O(n²))
def contagem_com_lista(numeros):
    elementos_unicos = []
    contagem = []
    
    inicio = time.time()
    
    for num in numeros:
        if num not in elementos_unicos:
            elementos_unicos.append(num)
            contagem.append(1)
        else:
            indice = elementos_unicos.index(num)  # Busca linear: O(n)
            contagem[indice] += 1
    
    fim = time.time()
    tempo_total = fim - inicio
    
    return elementos_unicos, contagem, tempo_total

# Abordagem 2: Lista ordenada + busca binária (O(n log n))
def contagem_com_lista_ordenada(numeros):
    numeros_ordenados = sorted(numeros)  # O(n log n)
    elementos_unicos = []
    contagem = []
    
    inicio = time.time()
    
    atual = None
    for num in numeros_ordenados:
        if num != atual:
            elementos_unicos.append(num)
            contagem.append(1)
            atual = num
        else:
            contagem[-1] += 1
    
    fim = time.time()
    tempo_total = fim - inicio
    
    return elementos_unicos, contagem, tempo_total

# Abordagem 3: Dicionário (O(n))
def contagem_com_dicionario(numeros):
    contagem = {}
    
    inicio = time.time()
    
    for num in numeros:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1
    
    fim = time.time()
    tempo_total = fim - inicio
    
    return contagem, tempo_total

# Abordagem 4: defaultdict - ainda mais otimizado (O(n))
def contagem_com_defaultdict(numeros):
    contagem = defaultdict(int)
    
    inicio = time.time()
    
    for num in numeros:
        contagem[num] += 1  # Não precisa verificar se a chave existe
    
    fim = time.time()
    tempo_total = fim - inicio
    
    return dict(contagem), tempo_total

# Função principal para executar os testes
def executar_teste(tamanho):
    print(f"\nTestando com {tamanho} elementos:")
    print("-" * 50)
    
    # Geramos os mesmos dados para todos os testes
    dados = gerar_dados(tamanho)
    
    # Teste com diferentes estruturas
    print("1. Lista + contagem linear...")
    _, _, tempo1 = contagem_com_lista(dados)
    print(f"   Tempo: {tempo1:.6f} segundos")
    
    print("2. Lista ordenada...")
    _, _, tempo2 = contagem_com_lista_ordenada(dados)
    print(f"   Tempo: {tempo2:.6f} segundos")
    
    print("3. Dicionário...")
    _, tempo3 = contagem_com_dicionario(dados)
    print(f"   Tempo: {tempo3:.6f} segundos")
    
    print("4. Defaultdict...")
    _, tempo4 = contagem_com_defaultdict(dados)
    print(f"   Tempo: {tempo4:.6f} segundos")
    
    # Calculando a melhoria de desempenho
    if tempo1 > 0:
        print(f"\nComparação de desempenho:")
        print(f"- Dicionário é {tempo1/tempo3:.1f}x mais rápido que lista linear")
        print(f"- Dicionário é {tempo2/tempo3:.1f}x mais rápido que lista ordenada")
        print(f"- Defaultdict é {tempo1/tempo4:.1f}x mais rápido que lista linear")

# Executar testes com diferentes tamanhos
if __name__ == "__main__":
    print("COMPARAÇÃO DE DESEMPENHO DE ESTRUTURAS DE DADOS")
    print("=" * 50)
    print("Tarefa: Contar a frequência de elementos em uma coleção\n")
    
    # Testar com diferentes tamanhos para ver como escala
    executar_teste(1000)     # pequeno
    executar_teste(10000)    # médio
    executar_teste(50000)    # grande
    
    print("\nCONCLUSÃO:")
    print("A escolha da estrutura de dados correta (dicionário) pode fazer um ")
    print("programa rodar centenas de vezes mais rápido que uma implementação ")
    print("ineficiente (lista + busca linear), especialmente para grandes volumes de dados.")
