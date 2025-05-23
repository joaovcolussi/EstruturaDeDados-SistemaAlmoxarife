import datetime

#Lista Encadeada Simples:
class LinkedListSimples:
    def __init__(self, dados):
        self.dados = dados
        self.next = None

    def __repr__(self):
        return str(self.dados)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def esta_vazia(self):
        return self.head is None

    def adicionar_no_inicio(self, dados):
        novo_no = LinkedListSimples(dados)
        novo_no.next = self.head
        self.head = novo_no
        self.size += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            return None
        no_removido = self.head
        self.head = self.head.next
        self.size -= 1
        return no_removido.dados

    def __repr__(self):
        nos = []
        no_atual = self.head
        while no_atual:
            nos.append(str(no_atual.dados))
            no_atual = no_atual.next
        return " -> ".join(nos) if nos else "Lista vazia"

    def __len__(self):
        return self.size

#Estrutura de Dados Global

#1. DICIONÁRIO: Para armazenar produtos cadastrados.

produtos_cadastrados = {}  #Ex: {"P001": {"nome": "Caneta Azul", "descricao": "Caneta esferográfica azul", "categoria": "Escritório"}}

#2. DICIONÁRIO: Para armazenar o estoque.
estoque = {}  # Ex: {"P001": 100}

#3. LISTA (atuando como log): Para histórico das operações.
historico_operacoes = []  # Ex: [("2024-05-23 10:00:00", "CADASTRO", "P001", "Novo produto cadastrado")]

#4. SET: Para armazenar categorias de produtos únicas.
categorias_disponiveis = {"Escritório", "Automotivo", "Informática"}

#5. LISTA ENCADEADA: Para uma fila de alertas de reestoque.
fila_alertas_reestoque = LinkedList()
LIMITE_MINIMO_ESTOQUE = 10

    # Funções do Sistema

def gerar_id_produto():
    # Gera um ID único para um novo produto
    return f"P{len(produtos_cadastrados) + 1:03d}"

def registrar_log(tipo_operacao, id_produto, detalhes):
    # Registra uma operação no histórico.
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (timestamp, tipo_operacao, id_produto, detalhes)
    historico_operacoes.append(log_entry)

def cadastrar_produto():
    # Cadastra um novo produto no sistema
    print("\n Cadastro de Novo Produto ")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    
    print("Categorias disponíveis:", ", ".join(categorias_disponiveis) if categorias_disponiveis else "Nenhuma categoria cadastrada")
    categoria = input(f"Categoria do produto (ou digite nova para adicionar): ")

    if categoria.lower() == "nova":
        nova_categoria = input("Digite o nome da nova categoria: ")
        categorias_disponiveis.add(nova_categoria)
        categoria = nova_categoria
        print(f"Categoria '{categoria}' adicionada.")
    elif categoria not in categorias_disponiveis:
        print(f"Categoria '{categoria}' não existe. Adicionando automaticamente.")
        categorias_disponiveis.add(categoria)

    id_produto = gerar_id_produto()
    #Armazenando detalhes do produto.
    produtos_cadastrados[id_produto] = {"nome": nome, "descricao": descricao, "categoria": categoria}
    estoque[id_produto] = 0  # Inicializa o estoque do novo produto como 0.
    
    registrar_log("CADASTRO", id_produto, f"Produto '{nome}' cadastrado.")
    print(f"Produto '{nome}' cadastrado com ID: {id_produto}")

def registrar_entrada_estoque():
    #Registra a entrada do produto no estoque.
    print("\nRegistrar Entrada no Estoque")
    id_produto = input("ID do produto: ").upper()
    if id_produto not in produtos_cadastrados:
        print(f"Erro: Produto com ID {id_produto} não encontrado.")
        return
    
    try:
        quantidade = int(input("Quantidade a adicionar: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser positiva.")
            return
    except ValueError:
        print("Erro: Quantidade inválida.")
        return

    #Atualizando a quantidade em estoque.
    estoque[id_produto] += quantidade
    registrar_log("ENTRADA", id_produto, f"Adicionadas {quantidade} unidades. Novo total: {estoque[id_produto]}.")
    print(f"Estoque do produto {produtos_cadastrados[id_produto]['nome']} atualizado para {estoque[id_produto]}.")

    #Verifica se o produto estava na fila de alertas e remove se o estoque normalizou
    no_atual = fila_alertas_reestoque.head
    anterior = None
    removido_alerta = False
    while no_atual:
        if no_atual.dados == id_produto and estoque[id_produto] > LIMITE_MINIMO_ESTOQUE:
            if anterior:
                anterior.next = no_atual.next
            else:
                fila_alertas_reestoque.head = no_atual.next
            fila_alertas_reestoque.size -=1
            print(f"Produto {id_produto} removido da fila de alertas de reestoque.")
            removido_alerta = True
            break
        anterior = no_atual
        no_atual = no_atual.next
    if removido_alerta:
         registrar_log("ALERTA_REMOVIDO", id_produto, f"Alerta de reestoque removido. Estoque: {estoque[id_produto]}.")


def registrar_saida_estoque():
    #Registra a saída de produtos do estoque
    print("\nRegistrar Saída do Estoque")
    id_produto = input("o produto: ").upper()
    if id_produto not in produtos_cadastrados:
        print(f"Erro: Produto com ID {id_produto} não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade a remover: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser positiva.")
            return
    except ValueError:
        print("Erro: Quantidade inválida.")
        return

    if estoque[id_produto] >= quantidade:
        estoque[id_produto] -= quantidade
        registrar_log("SAIDA", id_produto, f"Removidas {quantidade} unidades. Novo total: {estoque[id_produto]}.")
        print(f"Estoque do produto {produtos_cadastrados[id_produto]['nome']} atualizado para {estoque[id_produto]}.")

        #Adiciona à fila de alertas se o estoque ficar baixo e não estiver lá.
        if estoque[id_produto] <= LIMITE_MINIMO_ESTOQUE:
            #Verificar se já não está na fila
            presente_na_fila = False
            no_atual = fila_alertas_reestoque.head
            while no_atual:
                if no_atual.dados == id_produto:
                    presente_na_fila = True
                    break
                no_atual = no_atual.next
            
            if not presente_na_fila:
                fila_alertas_reestoque.adicionar_no_inicio(id_produto)
                registrar_log("ALERTA_CRIADO", id_produto, f"Produto com estoque baixo ({estoque[id_produto]}). Adicionado à fila de alertas.")
                print(f"ALERTA: Estoque baixo para {produtos_cadastrados[id_produto]['nome']}! Adicionado à fila de reestoque.")
    else:
        print(f"Erro: Quantidade insuficiente em estoque. Disponível: {estoque[id_produto]}.")

def consultar_estoque_produto():
    #Consulta o estoque de um produto pelo ID
    print("\nConsultar Estoque de Produto")
    id_produto = input("ID do produto: ").upper()
    if id_produto in produtos_cadastrados:
        produto = produtos_cadastrados[id_produto]
        quantidade = estoque[id_produto]     
        print(f"Produto: {produto['nome']} (ID: {id_produto})")
        print(f"Descrição: {produto['descricao']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade em estoque: {quantidade}")
    else:
        print(f"Erro: Produto com ID {id_produto} não encontrado.")

def listar_todos_produtos():
    #Lista todos os produtos cadastrados e seus estoques.
    print("\nLista de Todos os Produtos")
    if not produtos_cadastrados:
        print("Nenhum produto cadastrado.")
        return
    #Iterando sobre as chaves do dicionário (que podem ser convertidas para uma lista)
    for id_produto, info_produto in produtos_cadastrados.items():
        print(f"ID: {id_produto}, Nome: {info_produto['nome']}, Categoria: {info_produto['categoria']}, Estoque: {estoque.get(id_produto, 0)}")

def listar_categorias():
    #Lista todas as categorias de produtos disponíveis.
    print("\nCategorias de Produtos")
    if not categorias_disponiveis: #Verificando se o conjunto está vazio.
        print("Nenhuma categoria cadastrada.")
        return
    for i, categoria in enumerate(categorias_disponiveis):
        print(f"{i+1}. {categoria}")

def ver_historico_operacoes():
    #Exibe o histórico de todas as operações.
    print("\nHistórico de Operações")
    if not historico_operacoes: #Verificando se a lista está vazia.
        print("Nenhuma operação registrada.")
        return
    for timestamp, tipo, id_p, detalhes in historico_operacoes:
        nome_produto = produtos_cadastrados.get(id_p, {}).get('nome', id_p)
        print(f"[{timestamp}] [{tipo}] Produto: {nome_produto} - {detalhes}")

def ver_alertas_reestoque():
    #Exibe a fila de produtos que precisam de reestoque.
    print("\nAlertas de Reestoque Pendentes")
    if fila_alertas_reestoque.esta_vazia(): #Verificando se está vazia.
        print("Nenhum alerta de reestoque pendente.")
        return
    print("Produtos que necessitam de reestoque (do mais recente para o mais antigo):")
    
    no_atual = fila_alertas_reestoque.head
    while no_atual:
        id_produto = no_atual.dados
        nome_produto = produtos_cadastrados.get(id_produto, {}).get('nome', 'Desconhecido')
        quant_estoque = estoque.get(id_produto, 'N/A')
        print(f"- ID: {id_produto}, Nome: {nome_produto}, Estoque Atual: {quant_estoque}")
        no_atual = no_atual.next

def processar_proximo_alerta():
    #Processa (remove) o alerta de reestoque mais antigo da fila.
    print("\nProcessar Alerta de Reestoque")
    if fila_alertas_reestoque.esta_vazia():
        print("Nenhum alerta para processar.")
        return
    id_produto_alertado = fila_alertas_reestoque.remover_do_inicio()
    if id_produto_alertado:
        nome_produto = produtos_cadastrados.get(id_produto_alertado, {}).get('nome', id_produto_alertado)
        registrar_log("ALERTA_PROCESSADO", id_produto_alertado, f"Alerta para '{nome_produto}' processado/reconhecido.")
        print(f"Alerta para o produto '{nome_produto}' (ID: {id_produto_alertado}) foi processado e removido da fila de visualização.")
        print(f"Lembre-se de registrar a entrada de estoque para este produto se necessário.")
    else:
        print("Não foi possível processar o alerta.")


#Menu Principal
def menu_principal():
    #Exibe o menu principal
    opcoes_menu = {
        "1": "Cadastrar Novo Produto",
        "2": "Registrar Entrada no Estoque",
        "3": "Registrar Saída do Estoque",
        "4": "Consultar Estoque de Produto",
        "5": "Listar Todos os Produtos",
        "6": "Listar Categorias",
        "7": "Ver Histórico de Operações",
        "8": "Ver Alertas de Reestoque",
        "9": "Processar Próximo Alerta de Reestoque",
        "0": "Sair"
    }
    while True:
        print("\n Sistema de Almoxarifado ")
        for chave, valor in opcoes_menu.items():
            print(f"{chave}. {valor}")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            registrar_entrada_estoque()
        elif escolha == '3':
            registrar_saida_estoque()
        elif escolha == '4':
            consultar_estoque_produto()
        elif escolha == '5':
            listar_todos_produtos()
        elif escolha == '6':
            listar_categorias()
        elif escolha == '7':
            ver_historico_operacoes()
        elif escolha == '8':
            ver_alertas_reestoque()
        elif escolha == '9':
            processar_proximo_alerta()
        elif escolha == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()