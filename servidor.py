import threading
import time
import socket

# --- Variáveis para controlar o jogo entre as threads ---
jogadores = []
jogadas = {}
lock = threading.Lock()  # Um "cadeado" para evitar confusão entre as threads

HOST = '0.0.0.0'
PORTA = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORTA))
server.listen(2)  # Prepara o servidor para aceitar até 2 jogadores

print(f"Servidor escutando em {HOST}:{PORTA}")
print("Aguardando 2 jogadores se conectarem...")

# --- Aceita as conexões dos dois jogadores ---
while len(jogadores) < 2:
    conn, addr = server.accept()
    jogadores.append(conn)
    print(f"Jogador {len(jogadores)} conectado de {addr}")
    time.sleep(1)

# Envia uma mensagem inicial para ambos os jogadores começarem
jogadores[0].sendall(b"Voce e o Jogador 1. O jogo vai comecar!")
jogadores[1].sendall(b"Voce e o Jogador 2. O jogo vai comecar!")
time.sleep(1)


def thread_jogo(conn, player_id):
    """
    Esta é a função que cada jogador executará em sua própria thread.
    A lógica aqui é muito parecida com o seu 'while True' original.
    """
    while True:
        # Recebe os dados do cliente (a jogada)
        mensagem_cliente = conn.recv(1024)
        if not mensagem_cliente:
            # Se não receber dados, o cliente desconectou
            break

        # Decodifica os bytes recebidos para string
        mao_cliente = mensagem_cliente.decode('utf-8')
        print(f"Jogador {player_id} jogou: {mao_cliente}")

        # O 'lock' garante que apenas uma thread mexa no dicionário 'jogadas' por vez
        with lock:
            jogadas[player_id] = mao_cliente

        conn.sendall(b"Jogada recebida. Aguardando o oponente...")

        # Loop para esperar o outro jogador
        while len(jogadas) < 2:
            time.sleep(0.5)

        # --- Apenas uma das threads vai executar esta parte ---
        with lock:
            # Verifica se as jogadas já foram processadas por outra thread
            if len(jogadas) < 2:
                continue

            print("\nAmbos jogaram. Processando o resultado...")
            time.sleep(1)

            # Lógica do jogo (adaptada para jogador vs jogador)
            mao_p1 = jogadas[1]  # Jogada do jogador 1
            mao_p2 = jogadas[2]  # Jogada do jogador 2

            print("1..")
            time.sleep(1)
            print("2..")
            time.sleep(1)
            print("3..")
            time.sleep(1)

            print(f"Jogador 1 ({mao_p1}) vs Jogador 2 ({mao_p2})!\n")

            resultado_p1 = ""
            resultado_p2 = ""

            if mao_p1 == mao_p2:
                resultado_p1 = f"Empate! Ambos jogaram {mao_p1}.\n"
                resultado_p2 = f"Empate! Ambos jogaram {mao_p2}.\n"

            elif (mao_p1 == 'pedra' and mao_p2 == 'tesoura') or \
                    (mao_p1 == 'tesoura' and mao_p2 == 'papel') or \
                    (mao_p1 == 'papel' and mao_p2 == 'pedra'):
                resultado_p1 = f"Voce ganhou! Sua {mao_p1} vence a {mao_p2} do oponente.\n"
                resultado_p2 = f"Voce perdeu! Sua {mao_p2} perde para a {mao_p1} do oponente.\n"
            else:
                resultado_p2 = f"Voce ganhou! Sua {mao_p2} vence a {mao_p1} do oponente.\n"
                resultado_p1 = f"Voce perdeu! Sua {mao_p1} perde para a {mao_p2} do oponente.\n"

            # Envia o resultado de volta para cada cliente
            jogadores[0].sendall(resultado_p1.encode('utf-8'))
            jogadores[1].sendall(resultado_p2.encode('utf-8'))

            # Limpa o dicionário de jogadas para a próxima rodada
            jogadas.clear()

            time.sleep(1)
            print("Aguardando nova rodada...")


# Cria e inicia as threads para cada jogador
thread_p1 = threading.Thread(target=thread_jogo, args=(jogadores[0], 1))
thread_p2 = threading.Thread(target=thread_jogo, args=(jogadores[1], 2))

thread_p1.start()
thread_p2.start()

# Mantém o programa principal rodando enquanto as threads estiverem ativas
thread_p1.join()
thread_p2.join()

print("Fim de jogo.")