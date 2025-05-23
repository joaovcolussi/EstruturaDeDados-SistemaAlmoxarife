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

Gerenciar Categorias de Produtos:

Permite adicionar novas categorias de produtos dinamicamente durante o cadastro, caso a categoria informada não exista.

É possível listar todas as categorias de produtos existentes no sistema.

### Gerenciamento de Estoque:

#### Controlo de Estoque Individual:

Cada produto cadastrado possui um controlo de estoque associado, que é inicializado em zero.

O sistema mantém e atualiza a quantidade atual de cada produto disponível.

Consultar Estoque de Produto Específico:

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
