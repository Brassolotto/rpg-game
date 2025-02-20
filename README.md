# RPG Game - Aventura Interativa em Python

## Descrição

RPG em Texto é um jogo de aventura interativo desenvolvido em Python. O jogo combina mecânicas clássicas de RPG, como criação de personagens, combates por turnos, habilidades específicas para cada classe, sistema de itens/inventário, salvamento de progresso e exploração de um mundo expansível com diferentes áreas temáticas. Esta aplicação foi criada para praticar e aprimorar conceitos de programação, como orientação a objetos, manipulação de arquivos e lógica de jogo.

## Funcionalidades

- **Criação de Personagem:** Escolha entre classes como Guerreiro, Mago e Arqueiro, cada uma com atributos e bônus próprios.
- **Sistema de Combate:** Enfrente inimigos em batalhas com turno alternado, cálculo de dano e ganho de experiência.
- **Habilidades:** Use habilidades exclusivas de cada classe, que consomem energia e causam danos baseados em atributos do personagem.
- **Inventário e Itens:** Adquira e utilize itens como poções para recuperar pontos de vida e outros efeitos.
- **Salvamento:** Salve e carregue o progresso do jogo utilizando a serialização com o módulo `pickle`.
- **Mundo Expandido:** Explore diferentes áreas com descrições, chances de encontro e inimigos variados, aumentando a imersão do jogo.

## Pré-requisitos

- Python 3.7 ou superior
- Conhecimento básico de programação e lógica em Python

## Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Brassolotto/rpg-game.git
   ```

2. **Acesse a pasta do projeto:**

   ```bash
   cd rpg-game
   ```

3. **Execute o jogo:**

   ```bash
   python main.py
   ```

## Estrutura do Projeto

```plaintext
rpg-game/
├── main.py             # Ponto de entrada do jogo e loop principal
├── personagem.py       # Classe Jogador e métodos relacionados (criação, status e salvamento)
├── classes.py          # Definição das classes de personagem (Guerreiro, Mago e Arqueiro)
├── inimigos.py         # Criação de inimigos e seus templates
├── combate.py          # Sistema de combate e cálculo de dano
├── habilidades.py      # Definição das habilidades para cada classe
├── inventario.py       # Classe e funções relacionadas a itens/inventário
├── itens.py            # Exemplos de itens (ex.: Poção de Vida)
└── mundo.py            # Definição das áreas do mundo e mecânicas de exploração
```

## Como Jogar

- **Início:** Ao iniciar o jogo, você criará seu personagem escolhendo nome e classe.
- **Menu:** Utilize o menu principal para visualizar status, explorar áreas, descansar, usar itens, salvar o jogo ou sair.
- **Combate:** Durante a exploração, você enfrentará inimigos em batalhas por turnos, onde poderá atacar, usar habilidades ou tentar fugir.
- **Exploração:** Navegue entre diferentes áreas do mundo, cada uma com sua própria narrativa e desafios.
- **Progresso:** Aproveite as funções de salvamento e carregamento para continuar sua aventura em outro momento.

## Contribuição

Contribuições são muito bem-vindas! Se você deseja contribuir com novas funcionalidades, correções de bugs ou melhorias na estrutura do código, sinta-se à vontade para:

- Abrir issues detalhando as sugestões ou problemas encontrados.
- Enviar pull requests com melhorias documentadas.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

## Contato

Para dúvidas ou sugestões, entre em contato através do perfil no GitHub: [https://github.com/Brassolotto].

---

Esse README oferece uma visão geral do projeto, como instalá-lo, usá-lo e como contribuir. Sinta-se à vontade para personalizá-lo conforme suas necessidades e adicionar seções extras quando o projeto evoluir. Bom desenvolvimento!