#we need socket library to comunicate to another machines, using UDP and TCP protocols
import socket
import termcolor
import pyfiglet
#it performs the scan for each port that user entered, by looping through the range of ports
def scan(target, ports):
	print('\n' +' Starting Scan For ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)

#the for loop from the scan() function passes the ip address of the target and the port, if the port is opened and the program manages to connect it prints out "port open" and it closes the socket object
def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass
		#print("[-] Port Closed " + str(port))

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)
#Asks the user to input target or multiple targets separted by comma		
targets = input("[*] Enter Targets To Scan(split them by ,): ")
#Ask the user to enter how many ports wants to scan
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
#It checks the user input, if there are mupltiple or single ip address, and than it passes the values to the scan function
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ipaddr in targets.split(','):
		scan(ipaddr.strip(' '), ports)
else:
	scan(targets, ports)
	