import datetime

usuario_salvo = {}
categorias = ["Trabalho", "Alimentacao", "Transporte", "Moradia", "Lazer"]
transacoes = []



def ler_inteiro_limitado(mensagem, max_digitos):
    """Impede letras e limita a quantidade máxima de números inteiros."""
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("[ERRO] O campo não pode ser vazio.")
            continue
        if not entrada.isdigit():
            print("[ERRO] Entrada inválida! Digite apenas números (letras e símbolos não são permitidos).")
            continue
        if len(entrada) > max_digitos:
            print(f"[ERRO] Limite excedido! Este campo só permite no máximo {max_digitos} números.")
            continue
        return int(entrada)


def ler_decimal_limitado(mensagem, max_digitos):
    """Impede letras e limita a quantidade total de dígitos numéricos para valores monetários."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        if not entrada:
            print("[ERRO] O campo não pode ser vazio.")
            continue
            
    
        partes = entrada.split('.')
        if len(partes) > 2:
            print("[ERRO] Formato numérico inválido. Use apenas um ponto ou vírgula para os centavos.")
            continue
            
        apenas_digitos = "".join(partes)
        if not apenas_digitos.isdigit():
            print("[ERRO] Entrada inválida! Digite apenas números (letras não são permitidas).")
            continue
            
        if len(apenas_digitos) > max_digitos:
            print(f"[ERRO] Limite excedido! Este campo permite no máximo {max_digitos} dígitos numéricos.")
            continue
            
        valor = float(entrada)
        if valor < 0:
            print("[ERRO] O valor não pode ser negativo.")
            continue
        return valor


def ler_texto_apenas_numeros(mensagem, max_digitos, exato=False):
    """Valida campos de texto que aceitam apenas números (como CPF e Telefone)."""
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("[ERRO] O campo não pode ser vazio.")
            continue
        if not entrada.isdigit():
            print("[ERRO] Entrada inválida! Digite apenas números (letras não são permitidas).")
            continue
        if exato and len(entrada) != max_digitos:
            print(f"[ERRO] Entrada inválida! Este campo precisa ter exatamente {max_digitos} números.")
            continue
        if len(entrada) > max_digitos:
            print(f"[ERRO] Limite excedido! Este campo permite no máximo {max_digitos} números.")
            continue
        return entrada


def cadastrar_perfil():
    print("\n----- Cadastrar Perfil -----")
    usuario = {}
    
    usuario["nome"]             = input("Nome: ").strip()
    
    # Aplicação dos impedimentos e limites de números
    usuario["idade"]            = ler_inteiro_limitado("Idade (máx 3 números): ", max_digitos=3)
    usuario["cpf"]              = ler_texto_apenas_numeros("CPF (exatamente 11 números): ", max_digitos=11, exato=True)
    usuario["telefone"]         = ler_texto_apenas_numeros("Telefone com DDD (máx 11 números): ", max_digitos=11)
    
    usuario["salario"]          = ler_decimal_limitado("Salario (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["cartao_credito"]   = ler_decimal_limitado("Limite do cartao de credito (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["caixinha_reserva"] = ler_decimal_limitado("Caixinha/Reserva (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["alimentacao"]      = ler_decimal_limitado("Gasto com alimentacao (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["transporte"]       = ler_decimal_limitado("Gasto com transporte (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["moradia"]          = ler_decimal_limitado("Gasto com moradia (máx 10 dígitos): R$ ", max_digitos=10)
    usuario["lazer"]            = ler_decimal_limitado("Gasto com lazer (máx 10 dígitos): R$ ", max_digitos=10)

    global usuario_salvo
    usuario_salvo = usuario

    print("\n========================================")
    print("[SUCESSO] Perfil finalizado com sucesso!")
    print("========================================")
    print("Nome        :", usuario["nome"])
    print("Idade       :", usuario["idade"])
    print("CPF         :", usuario["cpf"])
    print("Salario     : R$", f"{usuario['salario']:.2f}")
    
    input("\nEnter para voltar...")


def ver_perfil():
    print("\n----- Perfil do Usuario -----")
    if not usuario_salvo:
        print("[AVISO] Nenhum perfil cadastrado ainda.")
    else:
        gastos_fixos = (usuario_salvo["alimentacao"] + usuario_salvo["transporte"] + 
                        usuario_salvo["moradia"] + usuario_salvo["lazer"])
        saldo_livre = usuario_salvo["salario"] - gastos_fixos

        print("Nome        :", usuario_salvo["nome"])
        print("Idade       :", usuario_salvo["idade"])
        print("CPF         :", usuario_salvo["cpf"])
        print("Telefone    :", usuario_salvo["telefone"])
        print("Salario     : R$", f"{usuario_salvo['salario']:.2f}")
        print("Cartao      : R$", f"{usuario_salvo['cartao_credito']:.2f}")
        print("Reserva     : R$", f"{usuario_salvo['caixinha_reserva']:.2f}")
        print("Alimentacao : R$", f"{usuario_salvo['alimentacao']:.2f}")
        print("Transporte  : R$", f"{usuario_salvo['transporte']:.2f}")
        print("Moradia     : R$", f"{usuario_salvo['moradia']:.2f}")
        print("Lazer       : R$", f"{usuario_salvo['lazer']:.2f}")
        print("Saldo livre : R$", f"{saldo_livre:.2f}")
        
    input("\nEnter para voltar...")


def cadastrar_categoria():
    print("\n----- Cadastrar Categoria -----")
    nome_categoria = input("Nome da categoria: ").strip().capitalize()
    if not nome_categoria:
        print("[ERRO] O nome não pode ser vazio.")
        input("Enter para voltar...")
        return
    if nome_categoria in categorias:
        print("[ERRO] Esta categoria já existe.")
        input("Enter para voltar...")
        return
        
    categorias.append(nome_categoria)
    
    print("\n===========================================")
    print(f"[SUCESSO] Categoria '{nome_categoria}' finalizada com sucesso!")
    print("===========================================")
    input("\nEnter para voltar...")


def listar_categorias():
    print("\n----- Categorias -----")
    for i, cat in enumerate(categorias, 1):
        print(f"  {i}. {cat}")
    input("\nEnter para voltar...")


def registrar_transacao():
    print("\n----- Registrar Transacao -----")
    print("Categorias disponíveis:")
    for i, cat in enumerate(categorias, 1):
        print(f"  {i}. {cat}")

    transacao = {}
    

    idx_cat = ler_inteiro_limitado("\nNumero da categoria (0 para cancelar): ", max_digitos=3)
    if idx_cat == 0:
        return
    if idx_cat < 1 or idx_cat > len(categorias):
        print("[ERRO] Categoria inválida.")
        input("Enter para voltar...")
        return
        
    transacao["categoria"] = categorias[idx_cat - 1]

    while True:
        tipo = input("Tipo (E=Entrada / S=Saida): ").upper().strip()
        if tipo in ['E', 'S']:
            transacao["tipo"] = tipo
            break
        print("[ERRO] Tipo inválido. Digite 'E' ou 'S'.")
        
    transacao["descricao"] = input("Descricao: ").strip()
    if not transacao["descricao"]:
        transacao["descricao"] = "Sem descrição"
    
    transacao["valor"] = ler_decimal_limitado("Valor (R$) (máx 10 dígitos): ", max_digitos=10)
    
    data_input = input("Data (DD/MM/AAAA) [Enter = hoje]: ").strip()
    if not data_input:
        transacao["data"] = datetime.date.today().strftime("%d/%m/%Y")
    else:
        try:
            datetime.datetime.strptime(data_input, "%d/%m/%Y")
            transacao["data"] = data_input
        except ValueError:
            print("[AVISO] Formato inválido. Definindo para a data de hoje.")
            transacao["data"] = datetime.date.today().strftime("%d/%m/%Y")

    transacoes.append(transacao)
    tipo_label = "Entrada" if transacao["tipo"] == "E" else "Saida"

    print("\n===========================================")
    print("[SUCESSO] Transação finalizada com sucesso!")
    print("===========================================")
    print("Categoria :", transacao["categoria"])
    print("Tipo      :", tipo_label)
    print("Descricao :", transacao["descricao"])
    print("Valor     : R$", f"{transacao['valor']:.2f}")
    print("Data      :", transacao["data"])
    input("\nEnter para voltar...")


def listar_transacoes():
    print("\n----- Transacoes -----")
    if not transacoes:
        print("[AVISO] Nenhuma transação registrada ainda.")
    else:
        for t in transacoes:
            tipo_label = "Entrada" if t["tipo"] == "E" else "Saida"
            print(f"{t['data']} - {t['descricao']}: R$ {t['valor']:.2f} ({tipo_label}) [{t['categoria']}]")
    input("\nEnter para voltar...")


def ver_saldo():
    print("\n----- Saldo Consolidado -----")
    saldo = {"entradas": 0.00, "saidas": 0.00, "total": 0.00}
    
    for t in transacoes:
        if t["tipo"] == "E":
            saldo["entradas"] += t["valor"]
        elif t["tipo"] == "S":
            saldo["saidas"] += t["valor"]
    
    saldo["total"] = saldo["entradas"] - saldo["saidas"]
        
    print(f"Entradas : R$ {saldo['entradas']:.2f}")
    print(f"Saidas   : R$ {saldo['saidas']:.2f}")
    print(f"Saldo    : R$ {saldo['total']:.2f}")
    input("\nEnter para voltar...")


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
            print("\nSessão encerrada. Ate logo!")
            break
        else:
            print("[ERRO] Opcao invalida. Tente novamente.")

menu()
