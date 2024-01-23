
### Etapas do Smash Forecast App

# Passo 1: Planejamento e Preparação

- Compreender os Requisitos: 
    - Desenvolver um web app que permite múltiplos usuários fazerem palpites (picks) para diversas rodadas em um torneio de tênis. 
    - Os picks começam nas quartas de final.
    - Computação de Pontos: A seleção dos jogadores e pontuação começa a partir da quartas de final
    - Ranking de pontuação: Apresentação dos usuários e seus respectivos pontos em uma tabela classificatória.
- Definir as Personas dos Usuários: Entusiastas de tênis e participantes em geral interessados em fazer palpites em resultados de torneios.
- Escolher Tecnologias: tecnologias a serem usadas (Python, Flask, SQLite, HTML, CSS, Javascript).
- Configurar Ambiente de Desenvolvimento:
    - VS Code: Usar o VS Code para o desenvolvimento do projeto na fase local, com auxílio do GitHub copilot.
    - Framework Web: Flask para gerenciar as rotas, interações com o banco de dados e lógica de negócios.

# Passo 2: Funcionalidades do Web App

- [ ] Autenticação de usuários.
- [X] Seleção de palpites (picks).
- [ ] Submissão e armazenamento de palpites.
- [ ] Cálculo de pontos e exibição do ranking.

# Passo 3: Design e Prototipagem

- [ ] Esboçar as Telas: Crie wireframes para as páginas principais (Tela Chave do Torneio e Tela de Resultado).
- [ ] Design de Interface: Desenvolva o design detalhado, incluindo esquema de cores, tipografia e elementos de UI.
- [ ] Revisão e Ajustes: Valide o design com usuários potenciais e faça ajustes conforme necessário.

# Passo 4: Estrutura do projeto

- [ ] Backend
    - [X] Arquivo Python principal (app.py) para a lógica do servidor Flask.
    - [X] Pasta para modelos do banco de dados SQLite.
    - [X] Pasta para rotas do Flask que lidam com requisições e respostas HTTP.
- [ ] Frontend
    - [X] Arquivos HTML para as páginas da interface do usuário.
    - [ ] Arquivos CSS para estilização.
    - [X] Arquivos JavaScript para lógica do front-end.
- [ ] Testes
    - [ ] Pasta para os scripts de teste.

# Passo 5: Passos iniciais

- [X] Configurar o ambiente de desenvolvimento.
- [X] Instalar Flask, SQLite e outras dependências necessárias.
- [X] Inicializar um repositório Git para versionamento do projeto

# Passo 6: Desenvolvimento

- [ ] Back-end:
    - [X] Configurar o servidor Flask.
- [ ] Modelagem de dados:
    - [ ] Usuários
    - [ ] Torneios
    - [X] Jogos
    - [X] Jogadores
- [X] Configurar a conexão com o banco de dados SQLite.
- [ ] Front-end:
    - [X] Criar páginas básicas em HTML.
    - [ ] Adicionar estilos CSS.
    - [ ] Implementar funcionalidades básicas em JavaScript.
- [X] Rota POST para `submitPicks`:
    - [X] Receber o JSON `submitPicks` do frontend.
    - [X] Validar e processar os dados para gerar objetos `Game`.
    - [X] Salvar os objetos `Game` na base de dados.
- [ ] Criação da Classe `User`:
    - [ ] Representa um usuário no sistema.
    - [ ] Adicionar campos como `id`, `username`, `email`, `password_hash`.
    - [ ] Relacionamento com a classe `Picks`.
    - [ ] Implementar métodos para representação e segurança (e.g., `__repr__`, `set_password`, `check_password`).
- [ ] Sistema de Autenticação:
    - [ ] Uso de Flask-Login para gerenciamento de sessões de usuário.
    - [ ] Implementar funções `load_user` e `user_loader`.
    - [ ] Uso de Flask-WTF para formulários seguros de login e registro.
- [ ] Rotas de Autenticação:
    - [ ] Rota de Registro de Usuários:
  - [ ] Formulário de registro com validação.
  - [ ] Hashing de senha antes de salvar no banco de dados.
- [ ] Rota de Login de Usuários:
  - [ ] Formulário de login com validação.
  - [ ] Autenticação de usuário e início de sessão.
- [ ] Rota de Logout:
  - [ ] Encerramento da sessão do usuário.
- [ ] Recuperação de Senha (Opcional):
    - [ ] Implementar funcionalidade de redefinição de senha.
    - [ ] Enviar e-mail com link de redefinição de senha.
- [ ] Interface do Usuário:
    - [ ] Páginas HTML para registro, login, e logout.
    - [ ] Barra de navegação para acesso fácil a diferentes seções do aplicativo.
    - [ ] Melhorias no front-end para suportar autenticação.
- [ ] Segurança e Privacidade:
    - [ ] Garantir que as senhas nunca sejam armazenadas em texto puro.
    - [ ] Proteção contra vulnerabilidades comuns (e.g., CSRF).
- [ ] Testes e Depuração:
    - [ ] Escrever testes para validar o registro, login e logout.
    - [ ] Testar a segurança e integridade da autenticação.
- [ ] Cálculo de Pontos:
    - [ ] Criar função para calcular pontos com base nas `Picks` dos usuários e nos resultados reais dos jogos.
    - [ ] Implementar testes para garantir a correta atribuição de pontos.
- [ ] Exibição do Ranking:
    - [ ] Desenvolver lógica para ordenar usuários com base nos pontos calculados.
    - [ ] Criar rota e página para exibir o ranking dos usuários.
- [ ] Atualização do Front-end para mostrar Resultados e Ranking:
    - [ ] Atualizar a interface para exibir as escolhas dos usuários, os resultados dos jogos e o ranking.
    - [ ] Implementar interatividade para permitir que os usuários vejam como suas escolhas se comparam com os resultados reais e o desempenho de outros usuários.

# Passo 7: Testes

    - [ ] Escrever testes unitários para as funções do back-end.
    - [ ] Testes de integração para as rotas do Flask.
    - [ ] Testes Unitários: Escreva testes para as funções individuais e modelos de dados.
    - [ ] Testes de Integração: Verifique se as diferentes partes do sistema (frontend, backend, banco de dados) funcionam juntas.
    - [ ] Testes de Usabilidade: Realize testes com usuários para identificar problemas na navegação e interação.

# Passo 8: Deploy e Lançamento

- [ ] Configurar Ambiente de Produção: Prepare o servidor de produção ou serviço de hospedagem.
- [ ] Deploy: Publique o aplicativo no ambiente de produção.
- [ ] Monitoramento: Monitore o desempenho e erros para garantir a estabilidade do sistema.

# Passo 9: Revisão e Iteração

- [ ] Coletar Feedback: Receba feedback dos usuários e stakeholders.
- [ ] Ajustes e Melhorias: Faça as melhorias necessárias no design, usabilidade e funcionalidades.
- [ ] Refatoração: Otimizar o código para melhor manutenção e desempenho.

# Passo 10: Manutenção e Atualização

- [ ] Suporte Contínuo: Forneça suporte técnico e responda a feedbacks e problemas dos usuários.
- [ ] Atualizações Regulares: Continue desenvolvendo novas funcionalidades e melhorias.
