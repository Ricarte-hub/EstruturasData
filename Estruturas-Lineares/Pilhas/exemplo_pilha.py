"""
Exemplo de Implementação e Uso de Pilhas

Este arquivo demonstra:
1. Implementação de uma pilha usando lista
2. Implementação de uma pilha usando lista encadeada
3. Uso de collections.deque como pilha
4. Aplicações práticas: verificação de parênteses balanceados, conversão de expressões e calculadora
"""

import time
from collections import deque


class PilhaLista:
    """Implementação de uma pilha usando uma lista Python."""
    
    def __init__(self):
        self.itens = []
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)  # O(1) amortizado
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens.pop()  # O(1)
    
    def topo(self):
        """Retorna o item do topo sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens[-1]
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)


class No:
    """Nó para a pilha baseada em lista encadeada."""
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class PilhaEncadeada:
    """Implementação de uma pilha usando lista encadeada."""
    
    def __init__(self):
        self.topo_no = None
        self._tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return self.topo_no is None
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        novo_no = No(item)
        novo_no.proximo = self.topo_no
        self.topo_no = novo_no
        self._tamanho += 1
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        
        valor = self.topo_no.valor
        self.topo_no = self.topo_no.proximo
        self._tamanho -= 1
        return valor
    
    def topo(self):
        """Retorna o item do topo sem removê-lo."""
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.topo_no.valor
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return self._tamanho


def demonstrar_pilha_lista():
    """Demonstra o uso da pilha implementada com lista."""
    print("\n1. PILHA USANDO LISTA")
    print("-" * 50)
    
    pilha = PilhaLista()
    print("Pilha criada (vazia)")
    
    print("\nOperações de empilhamento:")
    for i in range(1, 6):
        print(f"Empilhando {i}...")
        pilha.empilhar(i)
        print(f"Pilha: {pilha.itens} | Tamanho: {pilha.tamanho()}")
    
    print("\nOperação de consulta (topo):")
    topo = pilha.topo()
    print(f"Elemento no topo da pilha: {topo}")
    
    print("\nOperações de desempilhamento:")
    while not pilha.esta_vazia():
        valor = pilha.desempilhar()
        print(f"Desempilhado: {valor} | Pilha restante: {pilha.itens}")
    
    print("\nObservações:")
    print("- Implementação simples e eficiente")
    print("- Operações empilhar e desempilhar são O(1)")
    print("- Usa a lista nativa do Python, que já é otimizada")


def demonstrar_pilha_encadeada():
    """Demonstra o uso da pilha implementada com lista encadeada."""
    print("\n2. PILHA USANDO LISTA ENCADEADA")
    print("-" * 50)
    
    pilha = PilhaEncadeada()
    print("Pilha encadeada criada (vazia)")
    
    print("\nOperações de empilhamento:")
    valores = [10, 20, 30, 40, 50]
    for valor in valores:
        print(f"Empilhando {valor}...")
        pilha.empilhar(valor)
        print(f"Tamanho da pilha: {pilha.tamanho()}")
    
    print("\nOperação de consulta (topo):")
    topo = pilha.topo()
    print(f"Elemento no topo da pilha: {topo}")
    
    print("\nOperações de desempilhamento:")
    while not pilha.esta_vazia():
        valor = pilha.desempilhar()
        print(f"Desempilhado: {valor} | Tamanho restante: {pilha.tamanho()}")
    
    print("\nObservações:")
    print("- Todas as operações são O(1)")
    print("- Não tem limitação de tamanho fixo")
    print("- Usa mais memória devido aos ponteiros")


def demonstrar_pilha_deque():
    """Demonstra o uso do deque como uma pilha."""
    print("\n3. PILHA USANDO COLLECTIONS.DEQUE")
    print("-" * 50)
    
    pilha = deque()
    print("Pilha deque criada (vazia)")
    
    print("\nOperações de empilhamento:")
    for i in range(1, 6):
        print(f"Empilhando {i}...")
        pilha.append(i)  # O(1)
        print(f"Pilha: {list(pilha)} | Tamanho: {len(pilha)}")
    
    print("\nOperação de consulta (topo):")
    if pilha:
        print(f"Elemento no topo da pilha: {pilha[-1]}")
    
    print("\nOperações de desempilhamento:")
    while pilha:
        valor = pilha.pop()  # O(1)
        print(f"Desempilhado: {valor} | Pilha restante: {list(pilha)}")
    
    print("\nObservações:")
    print("- Implementação mais eficiente em Python para pilhas")
    print("- Todas as operações são O(1)")
    print("- É uma estrutura otimizada para operações em ambas as extremidades")
    print("- Recomendada para uso em produção")


def verificar_parenteses_balanceados(expressao):
    """
    Verifica se uma expressão tem parênteses, colchetes e chaves balanceados.
    Retorna True se estiverem balanceados, False caso contrário.
    """
    pilha = []
    mapeamento = {')': '(', '}': '{', ']': '['}
    
    for char in expressao:
        # Se é um abre-parênteses, empilha
        if char in '({[':
            pilha.append(char)
        # Se é um fecha-parênteses
        elif char in ')}]':
            # Se a pilha está vazia, não há correspondência
            if not pilha:
                return False
            # Verifica se o topo corresponde ao fecha-parênteses atual
            if pilha.pop() != mapeamento[char]:
                return False
    
    # Retorna True se a pilha estiver vazia (todos os símbolos foram pareados)
    return len(pilha) == 0


def aplicacao_verificar_parenteses():
    """Demonstra a aplicação de pilhas para verificar expressões balanceadas."""
    print("\n4. APLICAÇÃO: VERIFICAÇÃO DE PARÊNTESES BALANCEADOS")
    print("-" * 50)
    
    expressoes = [
        "( )",
        "( ) [ ] { }",
        "( [ { } ] )",
        "( [ ) ]",
        "{ [ ( ] ) }",
        "( ( ( ) ) )",
        "]",
        "[ { ( ) } ] )",
        "{ } [ ] ) ("
    ]
    
    for expressao in expressoes:
        resultado = verificar_parenteses_balanceados(expressao)
        print(f"Expressão: {expressao}")
        if resultado:
            print("✓ Parênteses balanceados")
        else:
            print("✗ Parênteses desbalanceados")
        print()
    
    print("Esta aplicação demonstra:")
    print("- Uso de pilha para rastrear símbolos de abertura")
    print("- Verificação do símbolo mais recente primeiro (LIFO)")
    print("- Aplicação comum em compiladores e análise sintática")


def infixa_para_posfixa(expressao):
    """
    Converte uma expressão infixa para notação pós-fixa (polonesa reversa).
    Exemplo: "A + B * C" -> "A B C * +"
    """
    # Definindo a precedência dos operadores
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    pilha = []  # Para operadores
    resultado = []  # Para a expressão pós-fixa
    
    # Remover espaços
    expressao = expressao.replace(" ", "")
    
    for token in expressao:
        # Se for um operando (letra ou dígito)
        if token.isalnum():
            resultado.append(token)
        
        # Se for um parêntese de abertura
        elif token == '(':
            pilha.append(token)
        
        # Se for um parêntese de fechamento
        elif token == ')':
            while pilha and pilha[-1] != '(':
                resultado.append(pilha.pop())
            
            # Remover o '(' da pilha
            if pilha and pilha[-1] == '(':
                pilha.pop()
        
        # Se for um operador
        else:
            while pilha and pilha[-1] != '(' and (
                    pilha[-1] not in precedencia or
                    precedencia.get(token, 0) <= precedencia.get(pilha[-1], 0)):
                resultado.append(pilha.pop())
            pilha.append(token)
    
    # Desempilha os operadores restantes
    while pilha:
        resultado.append(pilha.pop())
    
    return ''.join(resultado)


def avaliar_posfixa(expressao):
    """
    Avalia uma expressão em notação pós-fixa (polonesa reversa).
    Exemplo: "AB+C*" -> (A + B) * C
    """
    pilha = []
    
    for token in expressao:
        # Se for um operando (dígito)
        if token.isdigit():
            pilha.append(int(token))
        
        # Se for um operador
        elif token in '+-*/^':
            # Precisa de pelo menos dois operandos
            if len(pilha) < 2:
                raise ValueError("Expressão inválida")
            
            b = pilha.pop()  # Segundo operando
            a = pilha.pop()  # Primeiro operando
            
            # Realizar a operação
            if token == '+':
                pilha.append(a + b)
            elif token == '-':
                pilha.append(a - b)
            elif token == '*':
                pilha.append(a * b)
            elif token == '/':
                pilha.append(a / b)
            elif token == '^':
                pilha.append(a ** b)
    
    # O resultado deve ser o único valor na pilha
    if len(pilha) != 1:
        raise ValueError("Expressão inválida")
    
    return pilha[0]


def aplicacao_calculadora():
    """Demonstra a aplicação de pilhas para converter e avaliar expressões matemáticas."""
    print("\n5. APLICAÇÃO: CALCULADORA DE EXPRESSÕES")
    print("-" * 50)
    
    expressoes_infixas = [
        "3 + 4",
        "5 * 2 + 1",
        "( 5 + 3 ) * 2",
        "5 + 3 * 2",
        "( 7 - 2 ) * 3 + 4"
    ]
    
    print("Conversão de notação infixa para pós-fixa:")
    for expressao in expressoes_infixas:
        posfixa = infixa_para_posfixa(expressao)
        print(f"Infixa: {expressao}")
        print(f"Pós-fixa: {posfixa}")
        print()
    
    print("\nAvaliação de expressões pós-fixas:")
    expressoes_posfixas = ['34+', '52*1+', '53+2*', '532*+', '72-3*4+']
    for expressao in expressoes_posfixas:
        try:
            resultado = avaliar_posfixa(expressao)
            print(f"Expressão: {expressao}")
            print(f"Resultado: {resultado}")
            print()
        except ValueError as e:
            print(f"Erro ao avaliar {expressao}: {e}")
            print()
    
    print("Esta aplicação demonstra:")
    print("- Uso de pilhas para converter entre notações matemáticas")
    print("- Uso de pilhas para avaliar expressões")
    print("- Aplicação em compiladores, calculadoras e sistemas de álgebra computacional")


def simulacao_chamadas_funcao():
    """Demonstra como as pilhas são usadas para rastrear chamadas de função."""
    print("\n6. APLICAÇÃO: SIMULAÇÃO DE CHAMADAS DE FUNÇÃO")
    print("-" * 50)
    
    pilha_chamadas = PilhaLista()
    
    def simular_chamada(nome_funcao, params=None):
        """Simula uma chamada de função, empilhando o frame na pilha de chamadas."""
        if params is None:
            params = {}
        
        # Registra o frame na pilha
        frame = {"funcao": nome_funcao, "parametros": params, "variaveis_locais": {}}
        pilha_chamadas.empilhar(frame)
        print(f"CHAMADA: {nome_funcao}({', '.join([f'{k}={v}' for k, v in params.items()])})")
        print(f"Pilha de chamadas: {pilha_chamadas.tamanho()} frame(s)")
        print(f"Topo da pilha: {pilha_chamadas.topo()['funcao']}")
        print()
    
    def simular_retorno(valor_retorno=None):
        """Simula o retorno de uma função, desempilhando o frame."""
        if pilha_chamadas.esta_vazia():
            print("ERRO: Pilha de chamadas vazia")
            return
        
        frame = pilha_chamadas.desempilhar()
        print(f"RETORNO: {frame['funcao']} -> {valor_retorno}")
        
        if not pilha_chamadas.esta_vazia():
            print(f"Pilha de chamadas: {pilha_chamadas.tamanho()} frame(s)")
            print(f"Topo da pilha (retornando para): {pilha_chamadas.topo()['funcao']}")
        else:
            print("Pilha de chamadas vazia (programa terminou)")
        print()
    
    # Simulação de um programa com chamadas de função
    print("Iniciando simulação de chamadas de função:")
    print("main() chama fatorial(5), que chama a si mesmo recursivamente.\n")
    
    simular_chamada("main", {})
    simular_chamada("fatorial", {"n": 5})
    simular_chamada("fatorial", {"n": 4})
    simular_chamada("fatorial", {"n": 3})
    simular_chamada("fatorial", {"n": 2})
    simular_chamada("fatorial", {"n": 1})
    
    # Retornos (em ordem inversa às chamadas)
    simular_retorno(1)  # fatorial(1) -> 1
    simular_retorno(2)  # fatorial(2) -> 2
    simular_retorno(6)  # fatorial(3) -> 6
    simular_retorno(24)  # fatorial(4) -> 24
    simular_retorno(120)  # fatorial(5) -> 120
    simular_retorno(None)  # main() -> None
    
    print("Observações:")
    print("- A pilha rastreia a ordem das chamadas de função")
    print("- O retorno ocorre na ordem inversa (LIFO)")
    print("- É assim que seu programa de fato funciona na memória do computador!")
    print("- Se a pilha ficar muito grande, você pode ter um 'stack overflow'")


if __name__ == "__main__":
    print("DEMONSTRAÇÃO DE PILHAS EM PYTHON")
    print("=" * 50)
    
    demonstrar_pilha_lista()
    demonstrar_pilha_encadeada()
    demonstrar_pilha_deque()
    aplicacao_verificar_parenteses()
    aplicacao_calculadora()
    simulacao_chamadas_funcao()
