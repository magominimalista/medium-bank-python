class ContaCorrente:
    numero_conta_sequencial = 1

    def __init__(self, usuario):
        self.agencia = "0001"
        self.numero_conta = ContaCorrente.numero_conta_sequencial
        ContaCorrente.numero_conta_sequencial += 1
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.limite_saque = 500
        
    def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                self.extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite_saque:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self.limite_saque:.2f}.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    def exibir_extrato(self):
        print("\\n================ EXTRATO ================")
        print(self.extrato or "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")