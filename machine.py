import requests
import socket
import uuid


def get_mac_address():
	node = uuid.getnode()
	mac = uuid.UUID(int = node).hex[-12:]
	return mac

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

ip = get_host_ip()
mac = get_mac_address()
hostname = socket.gethostname()

params = {
	"machine.name":hostname,
	"machine.ip":ip,
	"machine.mac":mac
}

print(hostname,ip,mac)

url = "http://www.nct123.cn:8080/nct/nct/addmachine"

res = requests.get(url=url,params=params)

print(res.text)