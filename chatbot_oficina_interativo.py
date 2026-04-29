# ============================================================
# CHATBOT INTERATIVO - OFICINA MECÂNICA SIMAS TURBO
# Versão para executar no Terminal
# ============================================================

# Dados iniciais do chatbot:

categorias = ["Agendamento", "Serviços", "Orçamento", "Suporte"]
comandos_sair = ["sair", "tchau", "finalizar", "encerrar", "vou me sair"]

fila_atendimento = [
    ["Julião da Doze", "Comum"],
    ["Thomas Turbano", "Premium"],
    ["Nakama Tikomo", "Comum"],
    ["Zé do Pão", "Premium"],
    ["Adiomário Pragmático", "Comum"],
    ["Zé Martinho", "Comum"],
    ["Paran Golé Doismi Lonzi", "Premium"]
]

pilha_caminho = ["Início"]

respostas = {
    "endereco": "Av. Principal, 456 - Centro",
    "telefone": "(75) 98888-0000",
    "contato": "(75) 98888-0000",
    "horario": "Segunda a Sexta, das 8h às 17h",
    "servicos": "Oferecemos revisão, troca de óleo, alinhamento, balanceamento e diagnóstico."
}

catalogo = [
    [3, "Troca de Óleo", 120.0],
    [1, "Alinhamento", 80.0],
    [4, "Balanceamento", 60.0],
    [2, "Revisão Completa", 250.0]
]

novos_servicos = []
servicos_indisponiveis = ["Lanternagem", "Retífica de Motor", "Ar Condicionado"]
mensagens_lidas = []
TAMANHO_MAX_HISTORICO = 5

# Funções auxiliares:

def pausar():
    input("\nPressione ENTER para continuar...")


def adicionar_historico(tela):
    """Simula pilha com limite de memória."""
    if len(pilha_caminho) < TAMANHO_MAX_HISTORICO:
        pilha_caminho.append(tela)
    else:
        print("\nAviso: histórico de navegação cheio!")


def mostrar_menu():
    print("\n" + "=" * 50)
    print("CHATBOT - OFICINA MECÂNICA SIMAS TURBO")
    print("=" * 50)
    print("1 - Ver categorias")
    print("2 - Ver catálogo de serviços")
    print("3 - Ordenar catálogo por preço")
    print("4 - Ordenar catálogo por nome")
    print("5 - Buscar serviço")
    print("6 - Atualizar preço de um serviço")
    print("7 - Adicionar novo serviço")
    print("8 - Consultar respostas rápidas")
    print("9 - Verificar disponibilidade de serviço")
    print("10 - Atender próximo cliente da fila")
    print("11 - Adicionar cliente na fila")
    print("12 - Ver histórico de navegação")
    print("13 - Voltar uma tela")
    print("14 - Simular mensagens do cliente")
    print("15 - Aplicar desconto em um preço")
    print("0 - Sair")
    print("=" * 50)


def ver_categorias():
    adicionar_historico("Categorias")
    print("\nCategorias disponíveis:")
    for categoria in categorias:
        print(f"- {categoria}")

    opcao = input("\nDeseja inserir Atendimento Premium no início? (s/n): ").strip().lower()
    if opcao == "s" and "Atendimento Premium" not in categorias:
        categorias.insert(0, "Atendimento Premium")
        print("Categoria adicionada com sucesso!")

    print("\nCategorias atuais:", categorias)


def exibir_catalogo(lista=None):
    adicionar_historico("Catálogo")
    if lista is None:
        lista = catalogo

    print("\nCatálogo de serviços:")
    for item in lista:
        print(f"ID: {item[0]} | Serviço: {item[1]} | Preço: R$ {item[2]:.2f}")


def ordenar_por_preco():
    adicionar_historico("Catálogo por Preço")
    catalogo.sort(key=lambda x: x[2])
    print("\nAqui estão nossas opções mais acessíveis primeiro:")
    exibir_catalogo(catalogo)


def ordenar_por_nome():
    adicionar_historico("Catálogo por Nome")
    catalogo.sort(key=lambda x: x[1])
    print("\nListagem completa de serviços em ordem alfabética:")
    exibir_catalogo(catalogo)


def buscar_servico():
    adicionar_historico("Buscar Serviço")
    catalogo.sort(key=lambda x: x[2])
    nome_procurado = input("\nDigite o nome do serviço que deseja localizar: ").strip().lower()

    encontrado = False
    for posicao, item in enumerate(catalogo):
        if item[1].lower() == nome_procurado:
            print(f"\nO serviço foi encontrado na posição {posicao} após a ordenação por preço.")
            print(f"Detalhes: ID {item[0]} | Serviço: {item[1]} | Preço: R$ {item[2]:.2f}")
            encontrado = True
            break

    if not encontrado:
        print("\nServiço não encontrado no catálogo.")


def atualizar_preco():
    adicionar_historico("Atualizar Preço")
    nome_servico = input("\nDigite o nome do serviço que deseja atualizar: ").strip().lower()

    for item in catalogo:
        if item[1].lower() == nome_servico:
            try:
                novo_preco = float(input("Digite o novo preço: R$ ").replace(",", "."))
                item[2] = novo_preco
                catalogo.sort(key=lambda x: x[2])
                print("\nPreço atualizado e catálogo reordenado com sucesso!")
                exibir_catalogo(catalogo)
                return
            except ValueError:
                print("\nPreço inválido. Digite apenas números, exemplo: 120.50")
                return

    print("\nServiço não encontrado.")


def adicionar_servico():
    adicionar_historico("Adicionar Serviço")
    nome = input("\nDigite o nome do novo serviço: ").strip()

    try:
        preco = float(input("Digite o preço do serviço: R$ ").replace(",", "."))
    except ValueError:
        print("\nPreço inválido. Serviço não cadastrado.")
        return

    novo_id = max(item[0] for item in catalogo) + 1
    catalogo.append([novo_id, nome, preco])
    novos_servicos.append(nome)

    print("\nServiço adicionado com sucesso!")
    print("Novos serviços cadastrados:", novos_servicos)


def consultar_respostas():
    adicionar_historico("Respostas Rápidas")
    print("\nEu entendo sobre estes assuntos:", list(respostas.keys()))
    duvida = input("Digite o que deseja saber: ").strip().lower()

    if duvida in respostas:
        print("\n" + respostas[duvida])
    else:
        print("\nDesculpe, não sei responder isso.")
        opcao = input("Deseja cadastrar uma resposta para essa palavra? (s/n): ").strip().lower()
        if opcao == "s":
            nova_resposta = input("Digite a resposta: ").strip()
            respostas[duvida] = nova_resposta
            print("Nova resposta cadastrada com sucesso!")


def verificar_disponibilidade():
    adicionar_historico("Disponibilidade")
    servico_pedido = input("\nQual serviço você deseja consultar? ").strip()
    esta_indisponivel = servico_pedido in servicos_indisponiveis

    if esta_indisponivel:
        print(f"O serviço '{servico_pedido}' está indisponível no momento.")
    else:
        print(f"O serviço '{servico_pedido}' está disponível ou pode ser consultado com a oficina.")

    print("Resultado booleano:", esta_indisponivel)


def atender_cliente():
    adicionar_historico("Fila de Atendimento")
    if len(fila_atendimento) == 0:
        print("\nTodos os clientes foram atendidos. Fila vazia!")
        return

    fila_atendimento.sort(key=lambda x: x[1], reverse=True)
    atendido = fila_atendimento.pop(0)

    print(f"\nChamando cliente: {atendido[0]} | Tipo: {atendido[1]}")

    if len(fila_atendimento) > 0:
        print(f"Próximo da fila: {fila_atendimento[0][0]} | Tipo: {fila_atendimento[0][1]}")
    else:
        print("Não há próximo cliente na fila.")


def adicionar_cliente_fila():
    adicionar_historico("Adicionar Cliente")
    nome = input("\nDigite o nome do cliente: ").strip()
    tipo = input("Tipo de cliente (Comum/Premium): ").strip().capitalize()

    if tipo not in ["Comum", "Premium"]:
        tipo = "Comum"

    fila_atendimento.append([nome, tipo])
    print("Cliente adicionado à fila com sucesso!")


def ver_historico():
    print("\nHistórico completo:", pilha_caminho)

    if len(pilha_caminho) > 0:
        print("Tela atual:", pilha_caminho[-1])

    historico_reverso = pilha_caminho.copy()
    historico_reverso.reverse()
    print("Histórico reverso:", historico_reverso)


def voltar_tela():
    if len(pilha_caminho) > 1:
        saindo = pilha_caminho.pop()
        print(f"\nSaindo de {saindo}... Voltando para {pilha_caminho[-1]}.")
    else:
        print("\nVocê já está no início.")


def simular_mensagens():
    adicionar_historico("Mensagens")
    buffer_mensagens = []

    print("\nDigite mensagens do cliente. Digite 'fim' para processar.")
    while True:
        msg = input("Mensagem: ").strip()
        if msg.lower() == "fim":
            break
        buffer_mensagens.append(msg)

    print("\nProcessando mensagens em ordem FIFO:")
    while len(buffer_mensagens) > 0:
        msg = buffer_mensagens.pop(0)
        mensagens_lidas.append(msg)
        print(f"Processando mensagem: {msg}")


def aplicar_desconto():
    adicionar_historico("Desconto")
    tabela_precos = [item[2] for item in catalogo]

    print("\nPreços cadastrados:")
    for indice, preco in enumerate(tabela_precos):
        print(f"{indice} - R$ {preco:.2f}")

    try:
        indice = int(input("Escolha o índice do preço para aplicar 10% de desconto: "))
        preco_com_desconto = tabela_precos[indice] * 0.9
        print(f"Preço original: R$ {tabela_precos[indice]:.2f}")
        print(f"Preço com 10% de desconto: R$ {preco_com_desconto:.2f}")
    except (ValueError, IndexError):
        print("Opção inválida.")

# Programa principal:

def iniciar_chatbot():
    print("")
    print("Bem-vindo ao chatbot da Oficina Mecânica Simas Turbo!")
    print("Digite uma opção do menu ou 'sair' para encerrar.")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao in comandos_sair or opcao == "0":
            print("\nAtendimento encerrado. Obrigado por conversar com a oficina!")
            break
        elif opcao == "1":
            ver_categorias()
        elif opcao == "2":
            exibir_catalogo()
        elif opcao == "3":
            ordenar_por_preco()
        elif opcao == "4":
            ordenar_por_nome()
        elif opcao == "5":
            buscar_servico()
        elif opcao == "6":
            atualizar_preco()
        elif opcao == "7":
            adicionar_servico()
        elif opcao == "8":
            consultar_respostas()
        elif opcao == "9":
            verificar_disponibilidade()
        elif opcao == "10":
            atender_cliente()
        elif opcao == "11":
            adicionar_cliente_fila()
        elif opcao == "12":
            ver_historico()
        elif opcao == "13":
            voltar_tela()
        elif opcao == "14":
            simular_mensagens()
        elif opcao == "15":
            aplicar_desconto()
        else:
            print("\nOpção inválida. Tente novamente.")

        pausar()


if __name__ == "__main__":
    iniciar_chatbot()
