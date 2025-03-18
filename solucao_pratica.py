class Paciente:
    """
    Classe para representar um paciente no sistema hospitalar.
    
    Atributos:
        nome (str): Nome do paciente
        prioridade (int): Nível de prioridade do atendimento (1: emergência, 2: urgência, 3: pouco urgente)
        hora_chegada (int): Hora de chegada (usada como critério de desempate)
    """
    
    def __init__(self, nome, prioridade, hora_chegada):
        self.nome = nome
        self.prioridade = prioridade
        self.hora_chegada = hora_chegada
    
    def __str__(self):
        prioridade_texto = {
            1: "EMERGÊNCIA",
            2: "URGÊNCIA",
            3: "POUCO URGENTE"
        }
        return f"Paciente: {self.nome} | Prioridade: {prioridade_texto[self.prioridade]} | Chegada: {self.hora_chegada}"


class FilaPrioridade:
    """
    Implementação de uma fila de prioridade para o sistema de atendimento hospitalar.
    Os pacientes são organizados primeiro pela prioridade e depois pela hora de chegada.
    """
    
    def __init__(self):
        self.fila = []
    
    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.fila) == 0
    
    def inserir(self, paciente):
        """
        Insere um paciente na fila de acordo com sua prioridade.
        Pacientes com a mesma prioridade são organizados por ordem de chegada.
        """
        # Encontramos a posição correta para inserir o paciente
        posicao = 0
        while (posicao < len(self.fila) and 
               (self.fila[posicao].prioridade < paciente.prioridade or 
                (self.fila[posicao].prioridade == paciente.prioridade and 
                 self.fila[posicao].hora_chegada < paciente.hora_chegada))):
            posicao += 1
        
        # Inserimos o paciente na posição encontrada
        self.fila.insert(posicao, paciente)
        print(f"Paciente {paciente.nome} adicionado à fila.")
    
    def proximo_paciente(self):
        """Retorna o próximo paciente a ser atendido sem removê-lo da fila."""
        if self.esta_vazia():
            return None
        return self.fila[0]
    
    def atender(self):
        """Remove e retorna o próximo paciente a ser atendido."""
        if self.esta_vazia():
            print("Não há pacientes na fila.")
            return None
        
        paciente = self.fila.pop(0)
        print(f"Atendendo paciente: {paciente.nome}")
        return paciente
    
    def mostrar_fila(self):
        """Mostra a fila atual de pacientes."""
        if self.esta_vazia():
            print("A fila está vazia.")
            return
        
        print("\n=== FILA DE ATENDIMENTO ===")
        for i, paciente in enumerate(self.fila, 1):
            print(f"{i}. {paciente}")
        print("===========================\n")


# Demonstração do funcionamento
if __name__ == "__main__":
    fila_hospital = FilaPrioridade()
    
    # Simulando a chegada de pacientes
    fila_hospital.inserir(Paciente("João", 3, 1))  # Pouco urgente, chegou primeiro
    fila_hospital.mostrar_fila()
    
    fila_hospital.inserir(Paciente("Maria", 1, 2))  # Emergência, chegou depois
    fila_hospital.mostrar_fila()
    
    fila_hospital.inserir(Paciente("Pedro", 2, 3))  # Urgência
    fila_hospital.mostrar_fila()
    
    fila_hospital.inserir(Paciente("Ana", 1, 4))  # Outra emergência
    fila_hospital.mostrar_fila()
    
    fila_hospital.inserir(Paciente("Carlos", 3, 5))  # Outro caso pouco urgente
    fila_hospital.mostrar_fila()
    
    # Simulando o atendimento
    print("\n=== INICIANDO ATENDIMENTOS ===\n")
    
    # Atendendo pacientes por ordem de prioridade
    for _ in range(5):
        proximo = fila_hospital.proximo_paciente()
        if proximo:
            print(f"Próximo paciente: {proximo}")
            fila_hospital.atender()
            fila_hospital.mostrar_fila()
