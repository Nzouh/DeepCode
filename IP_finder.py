import socket
import ipaddress

# Define non-routable IP ranges
NON_ROUTABLE_RANGES = [
    ipaddress.IPv4Network("127.0.0.0/8"),     # Loopback addresses
    ipaddress.IPv4Network("10.0.0.0/8"),      # Private network
    ipaddress.IPv4Network("172.16.0.0/12"),   # Private network
    ipaddress.IPv4Network("192.168.0.0/16"),  # Private network
    ipaddress.IPv4Network("169.254.0.0/16"),  # Link-local addresses
]

def is_routable(ip):
    """Check if an IP address is routable."""
    ip_obj = ipaddress.IPv4Address(ip)
    return not any(ip_obj in range_ for range_ in NON_ROUTABLE_RANGES)

def resolve_domain(domain):
    """Resolve a domain to an IP address and filter non-routable IPs."""
    try:
        ip = socket.gethostbyname(domain)
        if is_routable(ip):
            return ip  # Return the routable IP
        else:
            return f"Excluded (Non-routable): {ip}"
    except socket.gaierror:
        return "Unresolved"

# List of domains to check
domains = ["google.com"] #add domain variable here

# Check each domain
results = {domain: resolve_domain(domain) for domain in domains}

# Display results
for domain, status in results.items():
    print(f"{domain}: {status}")
