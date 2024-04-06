from bank_system import SistemaBancario

def main():
    sistema_bancario = SistemaBancario()

    while True:
        print("\\nBem-vindo ao Sistema Bancário!")
        print("[1] Criar usuário")
        print("[2] Criar conta corrente")
        print("[3] Listar contas")
        print("[4] Login")
        print("[5] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            data_nascimento = input("Data de nascimento (dd-mm-YYYY): ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            senha = input("Senha: ")
            sistema_bancario.criar_usuario(nome, data_nascimento, cpf, endereco, senha)
        elif opcao == "2":
            cpf = input("CPF do usuário: ")
            senha = input("Senha: ")
            usuario = sistema_bancario.login(cpf, senha)
            if usuario:
                sistema_bancario.criar_conta_corrente(cpf, senha)
            else:
                print("Falha ao criar a conta. Usuário não encontrado ou senha incorreta.")
        elif opcao == "3":
            sistema_bancario.listar_contas()
        elif opcao == "4":
            cpf = input("CPF: ")
            senha = input("Senha: ")
            conta = sistema_bancario.login(cpf, senha)
            if conta:
                while True:
                    print("[1] Depositar")
                    print("[2] Sacar")
                    print("[3] Exibir Extrato")
                    print("[4] Sair")
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "1":
                        valor = float(input("Informe o valor do depósito: "))
                        conta.depositar(valor)
                    elif opcao_conta == "2":
                        valor = float(input("Informe o valor do saque: "))
                        conta.sacar(valor)
                    elif opcao_conta == "3":
                        conta.exibir_extrato()
                    elif opcao_conta == "4":
                        break
                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.")
        elif opcao == "5":
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()