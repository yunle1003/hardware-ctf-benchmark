#!/usr/bin/env python3
import socket, threading, json, os, sys, logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def forward_data(src, dst):
    try:
        while True:
            data = src.recv(4096)
            if not data: break
            dst.send(data)
    except: pass
def handle_client(client_socket, target_host, target_port, client_addr):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((target_host, target_port))
        t1 = threading.Thread(target=forward_data, args=(client_socket, server_socket), daemon=True)
        t2 = threading.Thread(target=forward_data, args=(server_socket, client_socket), daemon=True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except Exception as e:
        logger.error(f"Error: {e}")
def start_proxy_listener(listen_port, target_host, target_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', listen_port))
    server.listen(100)
    logger.info(f"Listening {listen_port} -> {target_host}:{target_port}")
    def accept_loop():
        while True:
            try:
                client_socket, client_addr = server.accept()
                t = threading.Thread(target=handle_client, args=(client_socket, target_host, target_port, client_addr), daemon=True)
                t.start()
            except Exception as e:
                logger.error(f"Accept: {e}")
    threading.Thread(target=accept_loop, daemon=True).start()
def main():
    gateway_map = json.loads(os.environ.get('CYBERBENCH_GATEWAY_MAP', '{}'))
    if not gateway_map:
        logger.error("Empty map")
        sys.exit(1)
    for listen_port_str, target_info in gateway_map.items():
        listen_port = int(listen_port_str)
        target_host = target_info.get('host')
        target_port = target_info.get('port')
        if target_host and target_port:
            start_proxy_listener(listen_port, target_host, target_port)
    try:
        while True:
            threading.Event().wait(1)
    except KeyboardInterrupt:
        sys.exit(0)
if __name__ == '__main__':
    main()
