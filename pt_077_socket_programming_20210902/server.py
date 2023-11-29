import socket
import threading

# FROM:	https://www.youtube.com/watch?v=3QiPPX-KeSc
# 		Python Socket Programming Tutorial
# 		TechWithTim
# 		20210902

my_hostname = socket.gethostname()
my_lan_ip = socket.gethostbyname(my_hostname)

HEADER = 64
PORT = 5050
SERVER = my_lan_ip
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] -- {addr} connected.")
	connected = True

	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] -- {msg}")
			conn.send("Msg receiced".encode(FORMAT))
			
	conn.close()

def start():
	server.listen()
	print(f"[LISTENING] -- Srver is listening on {SERVER}")

	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		th_count = threading.active_count()
		print(f"[ACTIVE CONNECTIONS] -- {th_count - 1}")



print("[STARTING] -- Server is starting ...")
start()
