def cadastrar_perfil():
    print("\n----- Cadastrar Perfil -----")
    usuario = {}
    try:
        usuario["nome"]             = input("Nome: ")
        usuario["idade"]            = int(input("Idade: "))
        usuario["cpf"]              = input("CPF: ")
        usuario["telefone"]         = input("Telefone: ")
        usuario["salario"]          = float(input("Salario: "))
        usuario["cartao_credito"]   = float(input("Limite do cartao de credito: "))
        usuario["caixinha_reserva"] = float(input("Caixinha/Reserva: "))
        usuario["alimentacao"]      = float(input("Gasto com alimentacao: "))
        usuario["transporte"]       = float(input("Gasto com transporte: "))
        usuario["moradia"]          = float(input("Gasto com moradia: "))
        usuario["lazer"]            = float(input("Gasto com lazer: "))
    except ValueError:
        print("Erro: idade e valores devem ser numeros.")
        input("Enter para voltar...")
        return

    print("\nDados informados:")
    print("Nome      :", usuario["nome"])
    print("Idade     :", usuario["idade"])
    print("CPF       :", usuario["cpf"])
    print("Telefone  :", usuario["telefone"])
    print("Salario   : R$", usuario["salario"])
    print("Cartao    : R$", usuario["cartao_credito"])
    print("Reserva   : R$", usuario["caixinha_reserva"])
    print("Alimentacao : R$", usuario["alimentacao"])
    print("Transporte  : R$", usuario["transporte"])
    print("Moradia     : R$", usuario["moradia"])
    print("Lazer       : R$", usuario["lazer"])
    print("\n[Em desenvolvimento — dados ainda nao salvos]")
    input("Enter para voltar...")


def ver_perfil():
    print("\n----- Perfil do Usuario -----")
    print("Nome      : -")
    print("Idade     : -")
    print("CPF       : -")
    print("Telefone  : -")
    print("Salario   : R$ 0.00")
    print("Cartao    : R$ 0.00")
    print("Reserva   : R$ 0.00")
    print("Alimentacao : R$ 0.00")
    print("Transporte  : R$ 0.00")
    print("Moradia     : R$ 0.00")
    print("Lazer       : R$ 0.00")
    print("Saldo livre : R$ 0.00")
    print("\n[Em desenvolvimento]")
    input("Enter para voltar...")

def cadastrar_categoria():
    print("\n----- Cadastrar Categoria -----")
    categoria = {}
    try:
        categoria["nome"] = input("Nome da categoria: ")
        if not categoria["nome"]:
            raise ValueError("Nome nao pode ser vazio.")
    except ValueError as e:
        print("Erro:", e)
        input("Enter para voltar...")
        return
    print("Categoria informada:", categoria["nome"])
    print("\n[Em desenvolvimento — categoria ainda nao salva]")
    input("Enter para voltar...")


def listar_categorias():
    print("\n----- Categorias -----")
    print("  1. Trabalho")
    print("  2. Alimentacao")
    print("  3. Transporte")
    print("  4. Moradia")
    print("  5. Lazer")
    print("\n[Em desenvolvimento]")
    input("Enter para voltar...")

def registrar_transacao():
    print("\n----- Registrar Transacao -----")
    print("Categorias:")
    print("  1. Trabalho")
    print("  2. Alimentacao")
    print("  3. Transporte")

    transacao = {}
    try:
        transacao["categoria"] = int(input("Numero da categoria (0 para cancelar): "))
    except ValueError:
        print("Erro: digite o numero da categoria.")
        input("Enter para voltar...")
        return

    if transacao["categoria"] == 0:
        return

    try:
        transacao["tipo"]      = input("Tipo (E=Entrada / S=Saida): ").upper()
        transacao["descricao"] = input("Descricao: ")
        transacao["valor"]     = float(input("Valor (R$): ").replace(",", "."))
        transacao["data"]      = input("Data (DD/MM/AAAA) [Enter = hoje]: ")
    except ValueError:
        print("Erro: valor deve ser um numero.")
        input("Enter para voltar...")
        return

    if not transacao["data"]:
        transacao["data"] = "hoje"

    tipo_label = "Entrada" if transacao["tipo"] == "E" else "Saida"

    print("\nTransacao informada:")
    print("Categoria :", transacao["categoria"])
    print("Tipo      :", tipo_label)
    print("Descricao :", transacao["descricao"])
    print("Valor     : R$", transacao["valor"])
    print("Data      :", transacao["data"])
    print("\n[Em desenvolvimento — transacao ainda nao salva]")
    input("Enter para voltar...")


def listar_transacoes():
    print("\n----- Transacoes -----")
    print("01/06/2026 - Salario: R$ 1800.00 (Entrada) [Trabalho]")
    print("05/06/2026 - Mercado: R$ 250.00 (Saida) [Alimentacao]")
    print("07/06/2026 - Internet: R$ 100.00 (Saida) [Transporte]")
    print("\n[Em desenvolvimento]")
    input("Enter para voltar...")

def ver_saldo():
    print("\n----- Saldo Consolidado -----")
    saldo = {}
    try:
        saldo["entradas"] = 0.00
        saldo["saidas"]   = 0.00
        saldo["total"]    = saldo["entradas"] - saldo["saidas"]
    except Exception as e:
        print("Erro ao calcular saldo:", e)
        input("Enter para voltar...")
        return
    print("Entradas : R$", saldo["entradas"])
    print("Saidas   : R$", saldo["saidas"])
    print("Saldo    : R$", saldo["total"])
    print("\n[Em desenvolvimento]")
    input("Enter para voltar...")

def menu():
    while True:
        print("\n===== FINANCAS PESSOAIS =====")
        print("1. Cadastrar perfil")
        print("2. Ver perfil")
        print("3. Cadastrar categoria")
        print("4. Listar categorias")
        print("5. Registrar transacao")
        print("6. Listar transacoes")
        print("7. Ver saldo consolidado")
        print("0. Sair")

        try:
            opcao = input("\nEscolha uma opcao: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAte logo!")
            break

        if opcao == "1":
            cadastrar_perfil()
        elif opcao == "2":
            ver_perfil()
        elif opcao == "3":
            cadastrar_categoria()
        elif opcao == "4":
            listar_categorias()
        elif opcao == "5":
            registrar_transacao()
        elif opcao == "6":
            listar_transacoes()
        elif opcao == "7":
            ver_saldo()
        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


menu()