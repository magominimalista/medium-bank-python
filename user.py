import re
import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco, senha):
        self.nome = nome
        try:
            self.data_nascimento = self.validar_data(data_nascimento)
        except ValueError as e:
            print(e) 
        self.cpf = cpf
        self.endereco = endereco
        self.senha = senha

        if not self.validar_cpf():
            raise ValueError("CPF inválido")
        if not self.validar_senha():
            raise ValueError("Senha inválida. A senha deve ter pelo menos 8 caracteres e incluir pelo menos uma letra minúscula, uma letra maiúscula, um dígito e um caractere especial (@, $, !, %, *, ?, &, #).")

    def validar_data(self, data):
        try:
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato dd-mm-YYYY.")
        
    def validar_cpf(self):
        # Validação básica do CPF
        if len(self.cpf) != 11 or not self.cpf.isdigit():
            return False
        # Adicione aqui a lógica para validar os dígitos verificadores do CPF
        return True
    
    def validar_senha(self):
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$", self.senha):
            return True
        return False

    def verificar_senha(self, senha):
        return self.senha == senha

# Testando o código
# usuario = Usuario("João", "10-10-1990", "12345678901", "Rua 1, 123", "Abc123!1")

# if usuario.validar_cpf():
#     print("CPF válido")
# else:
#     print("CPF inválido")

# if usuario.validar_senha():
#     print("Senha válida")
# else:
#     print("Senha inválida")

# if usuario.verificar_senha("Abc123!"):
#     print("Senha correta")
# else:
#     print("Senha incorreta")
