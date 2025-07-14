import socket
import time

HOST = '127.0.0.1'
PORTA = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORTA))
print(f"Conectado ao servidor em {HOST}:{PORTA}")
time.sleep(1)

mensagem_inicial = server.recv(1024)
print(mensagem_inicial.decode('utf-8'))
time.sleep(1)

while True:
    jogada = input("\nEscolha sua jogada (pedra, papel, tesoura) ou 'sair' para terminar: ").lower()

    if jogada == 'sair':
        break

    if jogada not in ['pedra', 'papel', 'tesoura']:
        print("Jogada inválida. Tente novamente.")
        continue

    server.sendall(jogada.encode('utf-8'))

    dados_servidor_espera = server.recv(1024)
    print(dados_servidor_espera.decode('utf-8'))

    print("Aguardando o resultado final da rodada...")
    dados_servidor_final = server.recv(1024)

    time.sleep(1)
    print('\nResultado:', dados_servidor_final.decode('utf-8'))
    time.sleep(2)

print("Conexão encerrada.")
server.close()