import time
import psutil

'''
def displaySisInfo():
	print(f"CPU usage: {psutil.cpu_percent()}")
	print(f"RAM usage: {psutil.virtual_memory().percent}")

while True:
	displaySisInfo()
	time.sleep(1)
'''

def display_usage(cpu_usage, mem_usage, bars=50):
	cpu_percent = (cpu_usage / 100.0)
	mem_percent = (mem_usage / 100.0)

	cpu_bar = "█" * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
	mem_bar = "█" * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
	

	print(f"\rCPU usage: [{cpu_bar}]{cpu_usage:8.2f}% | ", end="")
	print(f"MEM usage: [{mem_bar}]{mem_usage:8.2f}%", end = "")

while True:
	display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
	time.sleep(0.5)


