# Jogo Multiplayer de Pedra, Papel e Tesoura com Análise de Rede

## Descrição do Projeto

Este projeto implementa uma versão multiplayer do clássico jogo Pedra, Papel e Tesoura em Python. A arquitetura utiliza um servidor central e múltiplos clientes, com a comunicação sendo gerenciada pela biblioteca `socket` sobre o protocolo TCP.

O `servidor.py` foi desenvolvido com `threading` para lidar com múltiplos jogadores simultaneamente, atuando como um árbitro da partida: ele recebe as jogadas de dois clientes, compara-as, e envia o resultado individualmente para cada jogador. O `cliente.py` foi adaptado para o fluxo de jogo multiplayer, comunicando-se com o servidor e aguardando o oponente para receber o resultado.

Um diferencial do projeto continua sendo a sua aplicação como ferramenta de estudo para redes. Toda a interação entre os dois clientes e o servidor pode ser capturada e analisada com o `Wireshark`, permitindo uma visualização prática de múltiplas conexões TCP simultâneas, trocas de pacotes e a lógica de sincronização gerenciada pelo servidor.

## Instruções de Instalação e Uso

Para executar e analisar o projeto, siga os passos abaixo.

### Pré-requisitos
É necessária a instalação do `Python 3` e, para a análise de tráfego, do `Wireshark`.

### 1. Executando o Jogo

Para colocar o jogo para funcionar, você precisará de três terminais abertos.

1.  **Inicie o servidor:**
    Em um terminal, execute o script do servidor. Ele ficará aguardando a conexão de dois jogadores.
    ```bash
    python servidor.py
    ```

2.  Inicie os dois jogadores:
    Abra outros dois terminais. Em cada um deles, execute o script do cliente. O primeiro a se conectar será o Jogador 1, e o segundo será o Jogador 2.
    No segundo terminal (Jogador 1)
    ```bash
    python cliente1.py
    ```
    No terceiro terminal (Jogador 2)
    ```bash
    python cliente2.py
    ```

3.  Como Jogar:
    * No terminal de cada cliente, digite sua jogada: `pedra`, `papel` ou `tesoura`. Após enviar a jogada, o cliente receberá uma mensagem de confirmação e aguardará o oponente. Assim que ambos os jogadores tiverem feito suas jogadas, o resultado da rodada será exibido em ambas as telas. Para finalizar a conexão, digite `sair`.

### 2. Analisando o Tráfego com Wireshark

Esta seção explica como "espiar" a comunicação entre os clientes e o servidor.

1.  **Inicie o `servidor.py`** conforme o passo anterior.
2.  Abra o Wireshark e selecione a interface de rede de loopback (`Adapter for loopback traffic` ou `lo0`).
3.  Inicie a captura.
4.  Agora, execute os **dois scripts `cliente.py`** em terminais separados e jogue algumas rodadas.
5.  Pare a captura no Wireshark.
6.  Para visualizar apenas o tráfego do nosso jogo, aplique o seguinte filtro:
    ```
    tcp.port == 65432
    ```
7.  Adendos:
    * Múltiplas Conexões: Você verá dois handshakes TCP distintos, um para cada cliente se conectando ao servidor.
    * Pacotes de Dados: Ao inspecionar os pacotes `[PSH, ACK]`, você poderá ver as jogadas sendo enviadas de diferentes portas de origem (os clientes) para a porta de destino `65432` (o servidor). Você também verá as respostas do servidor (mensagens de espera e resultado) sendo enviadas de volta para cada cliente.
    * Encerramento da Conexão: Pacotes com a flag `[FIN, ACK]` quando um cliente digita `sair`.

## Registro de Contribuições

Este projeto foi desenvolvido como um esforço colaborativo, com a ideia do projeto elaborada por todos os integrantes em conjunto. Abaixo, estão as responsabilidades individuais de cada integrante:

* Matheus Marinho:
    * Desenvolvimento dos códigos `servidor.py` e `cliente.py` primários.
    * Implementação da lógica de sincronização e arbitragem do jogo.
    * Configuração do socket para a comunicação TCP no lado do servidor.
      
* Gustavo Lopez:
    * Documentação do projeto no `README.md`.
    * Criação da estrutura inicial do projeto e do repositório no GitHub.
    * Atualizações nos códigos `servidor.py` e `cliente1.py` / `cliente2.py` para suportar multiplayer com auxílio de threads.
