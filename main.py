import socket

def get_ip_address(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def main():
    url = input("Введите URL: ")
    ip_address = get_ip_address(url)
    print(f"IP адрес для {url}: {ip_address}")

if __name__ == "__main__":
    main()
