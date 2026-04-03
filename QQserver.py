import socket
import json
import threading

class OICQServer:
    def __init__(self, host='0.0.0.0', port=8000):
        # 修改为 TCP 协议 (SOCK_STREAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        # 开启监听，允许最大挂起连接数为 5
        self.server_socket.listen(5)
        
        # 存储用户信息: {nickname: socket}
        self.online_users = {}
        
        print(f"[系统] OICQ TCP 服务器启动成功，监听端口: {port}...")
        print("[系统] 等待用户连接...")

    def start(self):
        while True:
            try:
                # 接受新的客户端连接 (阻塞直到有连接)
                client_socket, client_addr = self.server_socket.accept()
                print(f"[连接] 新客户端连接来自: {client_addr}")
                
                # 为每个客户端创建一个独立的线程进行处理
                threading.Thread(target=self.handle_client, args=(client_socket, client_addr)).start()
            except Exception as e:
                print(f"[错误] {e}")

    def handle_client(self, client_socket, client_addr):
        # 持续接收该客户端的消息
        while True:
            try:
                # 接收数据 (TCP 是流式传输，recv 指定缓冲区大小)
                data = client_socket.recv(1024)
                
                # 如果接收到空数据，说明客户端断开了连接
                if not data:
                    break
                
                packet = json.loads(data.decode('utf-8'))
                self.process_packet(packet, client_socket)
                
            except Exception as e:
                print(f"[错误] 处理客户端 {client_addr} 时出错: {e}")
                break
        
        # 清理断开连接的用户
        self.cleanup_user(client_socket)
        client_socket.close()
        print(f"[断开] 客户端 {client_addr} 已断开")

    def process_packet(self, packet, client_socket):
        cmd = packet.get('cmd')
        sender = packet.get('sender')
        content = packet.get('content')

        if cmd == "LOGIN":
            self.online_users[sender] = client_socket
            print(f"[登录] {sender} 上线了")
            
        elif cmd == "MSG":
            receiver = packet.get('receiver')
            
            if receiver in self.online_users:
                target_socket = self.online_users[receiver]
                # 使用 send 发送数据，而不是 sendto
                target_socket.send(json.dumps(packet).encode('utf-8'))
                print(f"[转发] {sender} -> {receiver}: {content}")
            else:
                print(f"[失败] {sender} 试图发送消息给不在线的用户: {receiver}")

        elif cmd == "LOGOUT":
            print(f"[登出] {sender} 主动下线了")
            self.cleanup_user(client_socket)

    def cleanup_user(self, client_socket):
        # 根据 socket 对象反向查找并删除用户
        to_remove = []
        for nickname, sock in self.online_users.items():
            if sock == client_socket:
                to_remove.append(nickname)
        
        for nickname in to_remove:
            del self.online_users[nickname]

if __name__ == "__main__":
    server = OICQServer()
    server.start()