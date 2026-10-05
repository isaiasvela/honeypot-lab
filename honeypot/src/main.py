import json
import socket
from datetime import datetime, timezone
from pathlib import Path

import paramiko


HOST = "0.0.0.0"
PORT = 2222

BASE_DIR = Path(__file__).resolve().parent.parent
HOST_KEY_PATH = BASE_DIR / "keys" / "host_key"

def save_event(event):



    with open(BASE_DIR / "data/events.jsonl", "a") as file:
        file.write(event+'\n')


class HoneypotServer(paramiko.ServerInterface):
    def __init__(self, source_ip: str):
        self.source_ip = source_ip
    

    def check_auth_password(self, username: str, password: str) -> int:
    
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source_ip": self.source_ip,
            "event_type": "login_attempt",
            "username": username,
            "password": password,
        }
            
        json_event = json.dumps(event)

        save_event(json_event)

        print(json_event, flush=True) 
        
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username: str) -> str:
        return "password"


def main() -> None:
    host_key = paramiko.RSAKey.from_private_key_file(HOST_KEY_PATH)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(100)

    print(f"[+] Honeypot listening on {HOST}:{PORT}", flush=True)

    while True:
        client_socket, client_address = server_socket.accept()
        source_ip, source_port = client_address

        print(
            f"[+] Connection from {source_ip}:{source_port}",
            flush=True,
        )

        transport = paramiko.Transport(client_socket)
        transport.add_server_key(host_key)

        server = HoneypotServer(source_ip)

        try:
            transport.start_server(server=server)
            transport.accept(10)
        except paramiko.SSHException as exc:
            print(f"[-] SSH error from {source_ip}: {exc}", flush=True)
        finally:
            transport.close()


if __name__ == "__main__":
    main()
