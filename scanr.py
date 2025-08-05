import nmap

def scan_target(target_ip):
    scanner = nmap.PortScanner()
    print(f"🔍 Scan de {target_ip} en cours...\n")
    scanner.scan(hosts=target_ip, arguments='-p 1-1024 -T4')
    
    for host in scanner.all_hosts():
        print(f"Résultats pour {host} :")
        if scanner[host].state() == "up":
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    state = scanner[host][proto][port]['state']
                    print(f"Port {port} : {state}")

if __name__ == "__main__":
    ip = input("Entrez l'adresse IP à scanner : ")
    scan_target(ip)
