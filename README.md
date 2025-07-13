# PdA-Redes

## Descrição do Projeto

Este projeto implementa o clássico jogo Pedra, Papel e Tesoura em Python, utilizando uma arquitetura cliente-servidor para a comunicação. O projeto faz uso da biblioteca `socket` para estabelecer uma conexão TCP, onde o `servidor.py` gerencia a lógica do jogo e o `cliente.py` envia as jogadas do usuário.

Um diferencial deste projeto é sua aplicação como ferramenta de estudo para redes de computadores. Toda a interação entre o cliente e o servidor,desde o estabelecimento da conexão até o envio de cada jogada e resultado, pode ser capturada e analisada em tempo real com a ferramenta `Wireshark`. Isso permite uma visualização prática do handshake TCP, da troca de pacotes de dados e do encerramento da conexão.

## Instruções de Instalação e Uso

Para executar e analisar o projeto, siga os passos abaixo.

### Pré-requisitos
É necessária a instalação do `Python 3` e do `Wireshark`.

### 1. Executando o Jogo

Para colocar o jogo para funcionar, você precisará de dois terminais abertos.

1.  Inicie o servidor:
    Em um terminal, execute o script do servidor. Ele ficará aguardando uma conexão.
    ```bash
    python servidor.py
    ```

2.  Inicie o cliente:
    Em um segundo terminal, execute o script do cliente para se conectar ao servidor.
    ```bash
    python cliente.py
    ```

3.  Como Jogar:
    No terminal do cliente, digite sua jogada: `pedra`, `papel` ou `tesoura`. Em seguida, o resultado da rodada será exibido na tela. Para finalizar, digite `sair`.

### 2. Analisando o Tráfego com Wireshark

Esta seção explica como "espiar" a comunicação entre o cliente e o servidor.

1.  **Inicie o `servidor.py`** conforme o passo anterior.
2.  Abra o Wireshark. Na tela inicial, selecione a interface de rede de loopback. Geralmente, ela tem o nome **`Adapter for loopback traffic`** (no Windows) ou **`lo0`** (no macOS/Linux).
3.  Inicie a captura clicando no ícone de barbatana de tubarão azul.
4.  Agora, execute o **`cliente.py`** e jogue algumas rodadas.
5.  Pare a captura no Wireshark.
6.  Para visualizar apenas o tráfego do nosso jogo, aplique o seguinte filtro na barra de exibição e pressione Enter:
    ```
    tcp.port == 65432
    ```
7.  **O que observar:**
    * **Handshake TCP:** Os três primeiros pacotes (`[SYN]`, `[SYN, ACK]`, `[ACK]`) que estabelecem a conexão.
    * **Pacotes de Dados:** Pacotes com a flag `[PSH, ACK]`. Clique neles e, no painel de detalhes, expanda a seção "Data" para ver as jogadas (`pedra`, `papel`) e os resultados enviados como texto simples.
    * **Encerramento da Conexão:** Pacotes com a flag `[FIN, ACK]` que aparecem quando você digita `sair` no cliente.

## 🧑‍💻 Registro de Contribuições

Este projeto foi desenvolvido como um esforço colaborativo. Abaixo estão as responsabilidades de cada integrante:

  Matheus Marinho:
    * Desenvolvimento dos códigos `servidor.py` e `cliente.py`.
    * Configuração do socket para a comunicação TCP no lado do servidor.

  Gustavo Lopez:
    * Documentação do projeto no `README.md` e realização dos testes de análise com o Wireshark.
    * Criação da estrutura inicial do projeto e do repositório no GitHub.
