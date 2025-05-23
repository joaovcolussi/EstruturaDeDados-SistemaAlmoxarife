# Sistema de Almoxarifado Simples em Python

## Integrantes

- **João Victor Colussi** - RA: 2003753  
- **Alexandre Gomes** - RA: 1986088 
- **Cristian Heber Pires da Silva** - RA: 2019595


---

## 1. Requisitos de Execução

- **Python 3.x**: Desenvolvido e testado na versão 3.6 ou superior.
- **Sem dependências externas**: Utiliza apenas módulos padrão do Python (`datetime`).

### Como Executar:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo foi salvo.
3. Execute o comando:

```bash
python SistemaAlmoxarife.py
```

### Funcionalidades do Sistema
Sistema de console para gerenciamento de almoxarifado com menu interativo.

### Cadastro de Produtos
Adicionar produtos informando:

Nome

Descrição

Categoria

ID gerado automaticamente (ex: P001, P002).

Criação automática de novas categorias se não existirem.

## Controle de Estoque
Estoque inicial de cada produto é zero.

Quantidade é atualizada a cada entrada/saída.

## Operações Disponíveis
### Gerenciamento de Produtos:

#### Cadastrar Novos Produtos:

Permite registrar novos produtos fornecendo nome, descrição e categoria.

Os IDs dos produtos são gerados automaticamente pelo sistema (ex: P001, P002) para identificação única.

#### Gerenciar Categorias de Produtos:

Permite adicionar novas categorias de produtos dinamicamente durante o cadastro, caso a categoria informada não exista.

É possível listar todas as categorias de produtos existentes no sistema.

### Gerenciamento de Estoque:

#### Controlo de Estoque Individual:

Cada produto cadastrado possui um controlo de estoque associado, que é inicializado em zero.

O sistema mantém e atualiza a quantidade atual de cada produto disponível.

#### Consultar Estoque de Produto Específico:

Permite visualizar os detalhes completos (ID, nome, descrição, categoria) e a quantidade em estoque de um produto específico, pesquisando pelo seu ID.

Listar Todos os Produtos e Estoques:

Exibe uma lista de todos os produtos cadastrados, incluindo ID, nome, categoria e a respetiva quantidade em estoque.

### Operações de Almoxarifado:

#### Movimentação de Estoque:

Registrar Entrada no Estoque: Aumentar a quantidade de um produto específico no estoque, atualizando o saldo.

Registrar Saída do Estoque: Diminuir a quantidade de um produto do estoque, com verificação para não permitir saídas que excedam o saldo disponível.

### Monitorização e Alertas:

#### Alertas de Reestoque:

Quando a quantidade de um produto em estoque atinge um limite mínimo predefinido, um alerta é automaticamente gerado.

O ID do produto em alerta é adicionado a uma fila de alertas pendentes.

Visualizar Alertas Pendentes: Permite ao utilizador ver quais produtos estão atualmente na fila de alertas de reestoque, indicando baixo estoque.

Processar Alertas de Reestoque: Permite ao utilizador "processar" um alerta (o mais recente adicionado à fila). No contexto deste sistema simplificado, processar significa remover o alerta da fila de visualização, indicando que foi visto ou que a ação de reestoque está a ser tratada.

#### Auditoria e Histórico:

Ver Histórico de Operações: Apresenta um log cronológico detalhado de todas as operações significativas realizadas no sistema. Isto inclui cadastros de produtos, entradas e saídas de estoque, e a criação ou processamento de alertas.

### Justificativa da Escolha de Cada Estrutura de Dados

Para construir nosso sistema de almoxarifado, pensamos com carinho em como organizar as informações. A ideia era usar as ferramentas certas para cada tarefa, e aqui explicamos o porquê de cada escolha:

#### Dicionários (`dict`): Nossos Coringas pra Achar Tudo Rápido
 A gente usou dicionários pra duas paradas chave:
* `produtos_cadastrados`: Pensa nisso como um fichário onde cada produto tem sua pasta, identificada por um ID único. Se preciso achar os detalhes de um produto, vou direto na pasta dele pelo ID. Sem estresse, sem procurar um por um. É agilidade pura pra cadastrar, consultar ou atualizar as infos.
* `estoque`: Aqui, o dicionário é tipo o painel de controle das quantidades. Cada ID de produto aponta pra quantos itens dele a gente tem. Entrou mercadoria? Saiu? A gente atualiza o número ali e pronto. Pra controlar entrada e saída, não tem nada mais direto.

#### Listas (`list`): O Histórico Organizado dos Acontecimentos
* A `historico_operacoes` é, basicamente, o nosso log de tudo que rolou: quem cadastrou o quê, o que entrou, o que saiu, qual alerta pintou. Cada evento vira uma linha nesse "caderno". Listas são boas pra isso porque a gente vai adicionando as novas informações no final, e tudo fica na ordem certinha, do mais antigo pro mais novo.

#### Tuplas (`tuple`): Registros que Não Mudam, pra Confiança Total
* Cada "linha" do nosso histórico (`historico_operacoes`) é uma tupla. Uma tupla é tipo um registro selado: uma vez que você anota as informações lá (data, tipo da operação, produto, detalhes), elas não podem ser alteradas. Isso é fundamental pro histórico, porque dá a segurança de que ninguém vai mexer nos registros do passado. É a integridade dos dados em primeiro lugar.

#### Conjuntos (`set`): Garantindo que Cada Categoria Seja Única, Sem Repetição
* Pras `categorias_disponiveis`, a gente foi de `set`. A lógica é simples: num conjunto, não tem essa de item repetido. Se a gente tentar adicionar "Eletrônicos" e já existir "Eletrônicos", ele simplesmente não duplica. Isso evita bagunça e garante que cada categoria é única. Fora que pra adicionar uma nova ou checar se ela já tá lá, é muito rápido.

#### Listas Encadeadas (Simples): Uma Fila Flexível pros Alertas de Estoque Baixo
* A `fila_alertas_reestoque` é onde a gente coloca os produtos que tão quase acabando e precisam de atenção. Usamos uma lista encadeada aqui pra mostrar como ela se adapta bem quando a gente precisa adicionar e remover itens direto – que é o caso dos alertas, que surgem e são resolvidos. No nosso esquema, o último produto que entrou na "fila" de alerta é o primeiro que a gente olha pra resolver. Pensa numa pilha de tarefas: você geralmente pega a que tá no topo, né? É essa a ideia.
