
# Etapas para implementação do Smash Picks App

## Passo 1: Especificação do App

- O aplicativo web "Palpites do Torneio de Tênis" é uma plataforma inovadora desenvolvida para hospedar um bolão de apostas em torneios de tênis, permitindo que múltiplos usuários façam 15 palpites em um torneio de tenis. 
- O torneio de 128 jogadores funciona da seguinte forma:
    - Na primeira rodada, são realizados 64 jogos. Os vencedores avançam para a segunda rodada, onde há 32 jogos. 
    - Na terceira rodada, restam 16 jogadores e 16 jogos. 
    - A quarta rodada tem 8 jogos, levando às quartas de final com 4 jogos. 
    - As semifinais contam com apenas 2 jogos, e a final decide o campeão. 
    - Este é um torneio progressivo, onde os jogadores enfrentam eliminatórias até que apenas um permaneça como vencedor.
- O aplicativo foca em três etapas-chave de um torneio de tênis: Quartas de Final (QF), Semifinais (SF) e Final (F).
    - Dessa forma, os usuários devem escolher 8 jogadores para as QF, 4 para a SF, 2 finalistas e 1 campeão
- Durante o torneio, será calculada a pontuação dos usuários, iniciando a partir das Quartas de Final (QF). 
- Após cada partida, haverá uma atualização do total de pontos possíveis para cada participante. 
- O sistema de pontuação adotado é baseado em pesos atribuídos a cada fase do torneio: 1 ponto para as QF, 2 pontos para as Semifinais (SF), 3 pontos para a Final (F) e 4 pontos para acertar o campeão. 
- Portanto, a pontuação máxima possível é de 26 pontos, calculada como 8 (QF) * 1 + 4 (SF) * 2 + 2 (F) * 3 + 1 (Campeão) * 4.
- Por exemplo, considere um usuário que tenha escolhido os seguintes vencedores para um torneio:
    - QF: Djokovic vence Fritz, Sinner vence De Minaur, Medvedev vence Hurkacz, Zverev vence Alvaraz.
    - SF: Djokovic vence Sinner, Medvedev vence Hurkacz.
    - F: Djokovic vence Medvedev.
- Todos os usuários começam o torneio com 0 pontos ganhos e 26 pontos possíveis.
- Se, na primeira rodada, Fritz for derrotado conforme a escolha do usuário, este manterá 0 pontos ganhos, mas terá agora 25 pontos possíveis.
- No entanto, se Djokovic for eliminado antes das QF, o usuário terá 0 pontos e perderá a possibilidade de ganhar 10 pontos (1+2+3+4), restando apenas 16 pontos possíveis.
- O leaderboard do aplicativo incluirá gráficos de barras empilhados mostrando os pontos ganhos e possíveis para cada usuário, com atualizações após cada jogo.
- Este recurso visual permite aos usuários acompanhar facilmente seu desempenho e compará-lo com o dos outros participantes ao longo do torneio.

### Tecnologia

- Tecnologias usadas: Python, Flask, SQLite, HTML, CSS, Javascript.
- Configurar Ambiente de Desenvolvimento:
    - VS Code: Usar o VS Code para o desenvolvimento do projeto na fase local, com auxílio do GitHub copilot.
    - Framework Web: Flask para gerenciar as rotas, interações com o banco de dados e lógica de negócios.

## Passo 2: Funcionalidades do Web App

- [ ] Autenticação de usuários.
- [X] Seleção de palpites (picks).
- [X] Submissão e armazenamento de palpites.
- [ ] Cálculo de pontos e exibição do ranking.
- [ ] Acompanhanento em tempo real do ranking por meio de apis (ex: https://api-tennis.com/)

## Passo 3: Design e Prototipagem

- [X] Esboçar as Telas: Crie wireframes para as páginas principais (Tela Chave do Torneio e Tela de Resultado).
- [ ] Design de Interface: Desenvolva o design detalhado, incluindo esquema de cores, tipografia e elementos de UI.
- [ ] Revisão e Ajustes: Valide o design com usuários potenciais e faça ajustes conforme necessário.

## Passo 4: Estrutura do projeto

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

## Passo 5: Passos iniciais

- [X] Configurar o ambiente de desenvolvimento.
- [X] Instalar Flask, SQLite e outras dependências necessárias.
- [X] Inicializar um repositório Git para versionamento do projeto

## Passo 6: Desenvolvimento

- [ ] Back-end:
    - [X] Configurar o servidor Flask.
- [ ] Modelagem de dados:
    - [X] Usuários
    - [ ] Torneios
    - [X] Jogos
    - [X] Jogadores
- [X] Configurar a conexão com o banco de dados SQLite.
- [ ] Front-end:
    - [X] Criar páginas básicas em HTML.
    - [X] Adicionar estilos CSS.
    - [X] Implementar funcionalidades básicas em JavaScript.
- [X] Rota POST para `submitPicks`:
    - [X] Receber o JSON `submitPicks` do frontend.
    - [X] Validar e processar os dados para gerar objetos `Game`.
    - [X] Salvar os objetos `Game` na base de dados.
- [ ] Criação da Classe `User` sem autenticação:
    - [X] Representa um usuário no sistema.
    - [X] Adicionar campos como `id`, `username`
    - [X] Relacionamento com a classe `Picks`.
- [ ] Cálculo de Pontos:
    - [ ] Incluir rotina de atualização dos vencedores a cada rodada
    - [ ] Criar função para calcular os pontos possíveis e ganhos com base reais dos jogos.
- [ ] Exibição do Ranking:
    - [ ] Desenvolver lógica para ordenar usuários com base nos pontos calculados.
    - [ ] Criar rota e página para exibir o ranking dos usuários.
- [ ] Atualização do Front-end para mostrar Resultados e Ranking:
    - [ ] Atualizar a interface para exibir as escolhas dos usuários, os resultados dos jogos e o ranking.
    - [ ] Implementar interatividade para permitir que os usuários vejam como suas escolhas se comparam com os resultados reais e o desempenho de outros usuários.
- [ ] Sistema de Autenticação:
    - [ ] Uso de Flask-Login para gerenciamento de sessões de usuário.
    - [ ] Implementar funções `load_user` e `user_loader`.
    - [ ] Uso de Flask-WTF para formulários seguros de login e registro.
    - [ ] Rota de Registro de Usuários:
    - [ ] Formulário de registro com validação.
    - [ ] Hashing de senha antes de salvar no banco de dados.
    - [ ] Formulário de login com validação.
    - [ ] Autenticação de usuário e início de sessão.
    - [ ] Encerramento da sessão do usuário.
    - [ ] Implementar funcionalidade de redefinição de senha.
    - [ ] Enviar e-mail com link de redefinição de senha.
    - [ ] Páginas HTML para registro, login, e logout.
    - [ ] Barra de navegação para acesso fácil a diferentes seções do aplicativo.
    - [ ] Melhorias no front-end para suportar autenticação.
    - [ ] Garantir que as senhas nunca sejam armazenadas em texto puro.
    - [ ] Proteção contra vulnerabilidades comuns (e.g., CSRF).


## Passo 7: Testes

- [ ] Escrever testes unitários para as funções do back-end.
- [ ] Testes de integração para as rotas do Flask.
- [ ] Testes Unitários: Escreva testes para as funções individuais e modelos de dados.
- [ ] Testes de Integração: Verifique se as diferentes partes do sistema (frontend, backend, banco de dados) funcionam juntas.
- [ ] Testes de Usabilidade: Realize testes com usuários para identificar problemas na navegação e interação.

## Passo 8: Deploy e Lançamento

- [ ] Configurar Ambiente de Produção: Prepare o servidor de produção ou serviço de hospedagem.
- [ ] Deploy: Publique o aplicativo no ambiente de produção.
- [ ] Monitoramento: Monitore o desempenho e erros para garantir a estabilidade do sistema.

## Passo 9: Revisão e Iteração

- [ ] Coletar Feedback: Receba feedback dos usuários e stakeholders.
- [ ] Ajustes e Melhorias: Faça as melhorias necessárias no design, usabilidade e funcionalidades.
- [ ] Refatoração: Otimizar o código para melhor manutenção e desempenho.

## Passo 10: Manutenção e Atualização

- [ ] Suporte Contínuo: Forneça suporte técnico e responda a feedbacks e problemas dos usuários.
- [ ] Atualizações Regulares: Continue desenvolvendo novas funcionalidades e melhorias.
