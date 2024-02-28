class Funcionario:
    @staticmethod
    def formatar_nome(nome):
        if nome.strip():
            palavras = nome.split()
            palavras_formatadas = [palavra.capitalize() for palavra in palavras]
            nome_formatado = ' '.join(palavras_formatadas)
            return nome_formatado
        else:
            raise ValueError("Um nome deve ser digitado.")

    @staticmethod
    def formatar_salario(valor):
        try:
            salario_formatado = f'R${float(valor):,.2f}'
            return salario_formatado
        except ValueError:
            raise ValueError("Por favor, digite um valor numérico válido para o salário.")

    @staticmethod
    def nivel_profissional(valor):
        if valor <= 2000:
            return "Junior"
        elif 2001 <= valor <= 8000:
            return "Pleno"
        else:
            return "Sênior"

    @staticmethod
    def formatar_cpf(numero):
        if len(numero) == 11 and numero.isdigit():
            cpf_formatado = f'{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}'
            return cpf_formatado
        else:
            raise ValueError("Digite um CPF válido.")

    @staticmethod
    def validar_habilidades(habilidades):
        habilidades_lista = habilidades.split(';')
        habilidades_unicas = set(habilidades_lista)
        if len(habilidades_unicas) >= 3:
            return True
        else:
            return False


def adicionar_funcionario(lista_funcionarios):
    while True:
        try:
            nome_digitado = input("Digite o nome do funcionário: ")
            salario_digitado = input("Digite o salário: ")
            numero_cpf = input("Digite um CPF (11 dígitos): ")
            habilidades_digitadas = input("Digite as habilidades (mínimo 3, separadas por ';'): ")

            nome_formatado = Funcionario.formatar_nome(nome_digitado)
            salario_formatado = Funcionario.formatar_salario(salario_digitado)
            nivel = Funcionario.nivel_profissional(float(salario_digitado))
            cpf_formatado = Funcionario.formatar_cpf(numero_cpf)
            lista_habilidades = Funcionario.validar_habilidades(habilidades_digitadas)

            funcionario = {
                "Nome": nome_formatado,
                "Salário": salario_formatado,
                "Nível": nivel,
                "CPF": cpf_formatado,
                "Habilidades": habilidades_digitadas
            }
            lista_funcionarios.append(funcionario)

            print("\nFuncionário adicionado com sucesso!")
            opcao = input("\nDeseja adicionar outro funcionário? (1 - Sim, 2 - Voltar ao menu): ")
            if opcao != '1':
                break
        except ValueError as ve:
            print(ve)


def listar_funcionarios(lista_funcionarios):
    print("\nLista de Funcionários:")
    for i, funcionario in enumerate(lista_funcionarios, start=1):
        print(f"\nCódigo: {i}")
        for chave, valor in funcionario.items():
            print(f"{chave}: {valor}")

    if not lista_funcionarios:
        print("\nNenhum funcionário registrado.")


def apagar_funcionario(lista_funcionarios):
    codigo = int(input("\nDigite o código do funcionário que deseja apagar: ")) - 1
    if 0 <= codigo < len(lista_funcionarios):
        print("\nConfirme a exclusão do funcionário:")
        print(f"1 - Sim\n2 - Não")
        opcao = input()
        if opcao == '1':
            del lista_funcionarios[codigo]
            print("\nFuncionário removido com sucesso!")
        elif opcao == '2':
            print("\nExclusão cancelada.")
        else:
            print("\nOpção inválida.")
    else:
        print("\nCódigo de funcionário inválido.")


if __name__ == '__main__':
    lista_funcionarios = []
    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar funcionário")
        print("2 - Lista de funcionários")
        print("3 - Sair")
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == '1':
            adicionar_funcionario(lista_funcionarios)
        elif opcao_menu == '2':
            listar_funcionarios(lista_funcionarios)
            opcao_lista = input("\n1 - Apagar funcionário\n2 - Voltar ao menu\nEscolha uma opção: ")
            if opcao_lista == '1':
                apagar_funcionario(lista_funcionarios)
            elif opcao_lista != '2':
                print("\nOpção inválida.")
        elif opcao_menu == '3':
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Escolha novamente.")
