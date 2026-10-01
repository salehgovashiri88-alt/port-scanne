import socket
import sys

def scan(host, start, end):
    print(f"Scanning {host} ports {start}-{end}...")
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, port)) == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    print("Done.")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan(host, 1, 1024)
  
