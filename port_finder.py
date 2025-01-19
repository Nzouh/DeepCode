"""Author: Abdelhamid Sabir
   Date: 18 Jan 2025
"""


import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(domain, port, timeout=0.1):
    """Scan a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((domain, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None

def scan_ports(domain, ports, timeout=0.5, max_threads=10):
    """Scan multiple ports in parallel."""
    open_ports = []
    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, domain, port, timeout) for port in ports]
        for future in futures:
            result = future.result()
            if result is not None:
                open_ports.append(result)
    return open_ports


domain = "" #add domain variable here
ports_to_scan = [22, 53, 80, 88, 135, 139, 389, 443, 445, 1433, 3000, 3268, 8080]  # list of ports to check
open_ports = scan_ports(domain, ports_to_scan)
print(f"Open ports on {domain}: {open_ports}")