import socket
import requests

def main():
	hostname = socket.gethostname()
	local_ip_addres = socket.gethostbyname(hostname)
	public_ip_addres1 = requests.get('https://api.ipify.org').text
	# public_ip_addres2 = requests.get('https://api.bigdatacloud.net/data/client-ip').text
	# returns json -> must extract just an IP!


	print("{:<15} {}".format('hostname:', hostname))
	print("{:<15} {}".format('my local IP:', local_ip_addres))
	print("{:<15} {}".format('my public IP1:', public_ip_addres1))
	# print("{:<15} {}".format('my public IP2:', public_ip_addres2))

if __name__ == '__main__':
	main()
