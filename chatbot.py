# ============================================================
# CHATBOT - OFICINA MECÂNICA SIMAS TURBO
# ============================================================

# 1. Categorias
categorias = ["Agendamento","Serviços", "Orçamento", "Suporte"]
print(categorias)
categorias.sort()
print(categorias)
categorias.sort(reverse=True)
print(categorias)

# 2. Comandos de saída
comandos_sair = ["sair","tchau","finalizar","encerrar","vou me sair"]

# 3. Fila de espera
fila_atendimento = ["Julião da Doze", "Thomas Turbano", "Nakama Tikomo", "Zé do Pão", "Adiomário Pragmático", "Zé Martinho", "Paran Golé Doismi Lonzi"]
cliente_atendido = fila_atendimento.pop(0)

# 4. Histórico de navegação
pilha_caminho = ["Inicio", "Menu_Servicos", "Orçamento"]
ultima_tela = pilha_caminho.pop()

# 5. Base de respostas rápidas (dicionário)
respostas = {
    "endereco": "Av. Principal, 456 - Centro",
    "telefone": "(75) 98888-0000",
    "contato": "(75) 98888-0000",
    "horario": "Segunda a Sexta, das 8h às 17h",
    "servicos": "Oferecemos revisão, troca de óleo, alinhamento e diagnóstico"
}

# 6. Catálogo de itens
catalogo = [
    [3, "Troca de Óleo", 120.0],
    [1, "Alinhamento", 80.0],
    [4, "Balanceamento", 60.0],
    [2, "Revisão Completa", 250.0]
]

# Ordenação de catálago:
catalogo.sort(key=lambda x: x[2])

print("Aqui estão nossas opções mais acessíveis primeiro:")
for item in catalogo:
    print(f"ID: {item[0]} | Serviço: {item[1]} | Preço: R$ {item[2]}")


# Sincronização de Índices:
nome_procurado = input("Digite o nome do serviço que deseja localizar: ")

encontrado = False

for posicao, item in enumerate(catalogo):
    if item[1] == nome_procurado:
        print(f"O serviço foi encontrado na posição {posicao}.")
        print(f"Detalhes: ID {item[0]}, Serviço {item[1]}, Preço R$ {item[2]}")
        encontrado = True

if encontrado == False:
    print("Serviço não encontrado no catálogo.")

# Atualização Real    
for item in catalogo:
    if item[1] == "Balanceamento":
        item[2] = 100.0

catalogo.sort(key=lambda x: x[2])

print("Catálogo após atualização e reordenação:")
for item in catalogo:
    print(f"ID: {item[0]} | Serviço: {item[1]} | Preço: R$ {item[2]}")

# 7. Inserção Dinâmica de Novos Serviços/produtos (Append)
novos_servicos = []

novos_servicos.append("Troca de Filtro")
novos_servicos.append("Diagnóstico Eletrônico")
novos_servicos.append("Limpeza de Bicos")

# 8. Vetor de Preços e Tipos Numéricos (Float/Int)
tabela_precos = [150.0, 280.0, 450.0]

print(tabela_precos[1] * 0.9)  # desconto de 10%

# 9. Inserção em Posição Específica
categorias.insert(0, "Atendimento Premium")
print(f"Categorias atualizadas: {categorias}")

# 10. Verificação de Disponibilidade
servicos_indisponiveis = ["Lanternagem", "Retífica de Motor", "Ar Condicionado"]

servico_pedido = input("Qual serviço você deseja consultar? ")

# O operador 'in' retorna True se o item estiver na lista e False se não estiver
esta_indisponivel = servico_pedido in servicos_indisponiveis

print(f"O serviço '{servico_pedido}' está indisponível? {esta_indisponivel}")

# 11. Verificação de Topo sem Remover (Peek)
def verificar_ultima_acao(pilha):
    # Retorna o último elemento sem removê-lo
    return pilha[-1]

pilha_navegacao = ["Menu Principal", "Ordens de Serviço", "Cadastro de Cliente"]

topo = verificar_ultima_acao(pilha_navegacao)

print(f"Você está atualmente em: {topo}")
print(f"Histórico completo: {pilha_navegacao}")

#Histórico reverso:
pilha_navegacao.reverse()
print(f"Histórico reverso: {pilha_navegacao}")

# 12. Limitação de Memória (Stack Overflow Simulado)
TAMANHO_MAX = 3

if len(pilha_navegacao) < TAMANHO_MAX:
    pilha_navegacao.append("Pagamento")
else:
    print("Erro: Historico de navegacao cheio!")

# 13. Rastro de Desfazer (Undo Progressivo)
while len(pilha_navegacao) > 0:
    saindo = pilha_navegacao.pop()
    print(f"Saindo de {saindo}... Voltando ao nivel anterior.")

#14 Prioridade de Atendimento (Gestão da Cabeça)
#A fila de ouro para clientes premium
fila_atendimento = [
    ["Julião da Doze", "Comum"], 
    ["Thomas Turbano", "Premium"], 
    ["Nakama Tikomo", "Comum"], 
    ["Zé do Pão", "Premium"], 
    ["Adiomário Pragmático", "Comum"], 
    ["Zé Martinho", "Comum"], 
    ["Paran Golé Doismi Lonzi", "Premium"]
]

fila_atendimento.sort(key=lambda x: x[1], reverse=True)

atendido = fila_atendimento.pop(0) # Remove o primeiro (indice 0)

print(f"Chamando cliente: {atendido}")
print(f"Proximo da fila agora e: {fila_atendimento[0]}")


# 15. Fila Vazia e Segurança de Acesso
if len(fila_atendimento) > 0:
    fila_atendimento.pop(0)
else:
    print("Todos os clientes foram atendidos. Fila vazia!")

# 16. Simulação de Buffer de Mensagens

buffer_mensagens = ["Oi", "Quero o preco", "Tchau", "Qual o horario?", "Obrigado!", "Quero orçamento", "Preço troca de óleo"]
mensagens_lidas = []

while len(buffer_mensagens) > 0:
    msg = buffer_mensagens.pop(0)
    mensagens_lidas.append(msg)
    print(f"Processando mensagem: {msg}")


# 17. Acesso Específico a Atributos (Células)

# Nome do segundo serviço
nome = catalogo[1][1]
print("Nome do segundo serviço:", nome)

# Preço do terceiro serviço
preco = catalogo[2][2]
print("Preço do terceiro serviço:", preco)

# 18. Atualização de Dados na Matriz

catalogo[0][2] = catalogo[0][2] + 5.0
print("Novo preço do primeiro item:", catalogo[0][2])

# 19. Percorrimento Completo (Caminhamento)

for item in catalogo:
    print(f"Serviço: {item[1]} - Valor: R$ {item[2]}")

# 20. Verificação de Existência de Chave
duvida = input("O que deseja saber? ").strip().lower()

if duvida in respostas:
    print(respostas[duvida])
else:
    print("Desculpe, não sei responder isso.")

# 21. Adição e Remoção Dinâmica de Chaves
respostas["promocao"] = "Desconto de 20% nas quartas-feiras!"

respostas.pop("telefone") # Remove a chave telefone

# 22. Extração de Metadados (Keys e Values)
print("Eu entendo sobre estes assuntos:", list(respostas.keys()))
print("Minhas respostas cadastradas sao:", list(respostas.values()))
