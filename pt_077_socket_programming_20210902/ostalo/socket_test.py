import socket
import threading

my_hostname = socket.gethostname()
my_lan_ip = socket.gethostbyname(my_hostname)

print(f"{my_hostname}\n{my_lan_ip}")

  