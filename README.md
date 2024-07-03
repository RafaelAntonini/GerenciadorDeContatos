# Gerenciador de contatos
Este projeto é um aplicativo de Gerenciador de Contatos construído usando Python com PyQt5 para a interface gráfica e SQLite para o banco de dados. O aplicativo permite que os usuários adicionem, editem, excluam e visualizem contatos de maneira amigável.
# Funcionalidades
- Adicionar Novos Contatos: Usuários podem adicionar novos contatos com detalhes como nome, número de telefone, e-mail e endereço.
- Editar Contatos: Usuários podem atualizar as informações de contatos existentes.
- Excluir Contatos: Usuários podem remover contatos do banco de dados.
- Visualizar Contatos: Usuários podem ver uma lista de todos os contatos e buscar por contatos específicos.
# Pré-requisitos
-Python 3.x
-PyQt5
-SQLite3
# Estrutura do Projeto
- "main.py": O arquivo principal do aplicativo que executa o Gerenciador de Contatos.
- "db.py": Contém funções para interagir com o banco de dados SQLite.
- "contacts_db.db": O arquivo de banco de dados SQLite que armazena as informações dos contatos.
- "editContact.ui": O arquivo do PyQt5 Designer para a interface de edição de contatos.
- "newContact.ui": O arquivo do PyQt5 Designer para a interface de criar novos contatos.
- "viewContact.ui": O arquivo do PyQt5 Designer para a interface de visualizar os contatos.
- "removeContact.ui": O arquivo do PyQt5 Designer para a interface de remover os contatos.
- "ui.ui": O arquivo do PyQt5 Designer para a interface principal aonde pode escolher as outras opções.
# Instalação
1. Clone o repositório: git clone <url_do_repositorio>
                        cd contact-manager
2. Instale os pacotes Python necessários com o comando: pip install PyQt5
3. Execute o aplicativo: python main.py
# Uso
-  Adicionar um Contato:
Clique no botão "Adicionar".
Preencha os detalhes do contato no formulário.
Clique em "Salvar" para adicionar o contato ao banco de dados.
-  Editar um Contato:
Selecione um contato na lista.
Clique no botão "Editar".
Atualize os detalhes do contato no formulário.
Clique em "Salvar" para atualizar o contato no banco de dados.
-  Excluir um Contato:
Selecione um contato na lista.
Clique no botão "Excluir".
Confirme a exclusão.
-  Visualizar Contatos:
Todos os contatos estão listados na interface principal.
Use a barra de pesquisa para filtrar contatos por nome ou outros detalhes.
