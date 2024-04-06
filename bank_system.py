from user import Usuario
from account import ContaCorrente

class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco, senha):
        if any(usuario.cpf == cpf for usuario in self.usuarios):
            print("Falha ao criar usuário. CPF já cadastrado.")
            return None
        else:
            novo_usuario = Usuario(nome, data_nascimento, cpf, endereco, senha)
            self.usuarios.append(novo_usuario)
            print(f"Usuário {nome} criado com sucesso!")
            return novo_usuario

    def criar_conta_corrente(self, cpf, senha):
        usuario = self.login(cpf, senha)
        if usuario is None:
            print("Falha ao criar conta. Usuário inválido.")
            return
        nova_conta = ContaCorrente(usuario)
        self.contas.append(nova_conta)
        print(f"Conta corrente criada para o usuário {usuario.nome} com sucesso!")
        return nova_conta

    def listar_contas(self):
        if self.contas:
            print("\nLista de contas correntes:")
            for conta in self.contas:
                print(  f"Usuário: {conta.usuario.nome},\n"
                        f"CPF: {conta.usuario.cpf},\n"
                        "==========================\n"
                        f"Agência: {conta.agencia},\n"
                        f"Número da Conta: {conta.numero_conta},\n"
                        f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Não há contas correntes cadastradas.")

    def login(self, cpf, senha):
        usuario = self.encontrar_usuario_por_cpf(cpf, senha)
        if usuario:
            conta = self.encontrar_conta(usuario)
            if conta:
                print(f"Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.")
                return conta
        return usuario

    def encontrar_usuario_por_cpf(self, cpf, senha):
        for usuario in self.usuarios:
            if usuario.cpf == cpf and usuario.verificar_senha(senha):
                return usuario
        return None

    def encontrar_conta(self, usuario):
        for conta in self.contas:
            if conta.usuario.cpf == usuario.cpf:
                return conta
        return None