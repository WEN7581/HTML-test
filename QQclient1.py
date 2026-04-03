import socket
import threading
import json
import time
import sys

# 数据包类
class OICQPacket:
    def __init__(self, cmd, sender, receiver, content):
        self.cmd = cmd
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = time.time()

    def to_json(self):
        return json.dumps(self.__dict__).encode('utf-8')

class OICQClient:
    def __init__(self, my_nickname, server_ips=None, server_port=8000):
        self.nickname = my_nickname
        
        # 配置服务器列表
        if server_ips is None:
            self.server_ips = ['192.168.2.3', '192.168.43.195']
        else:
            self.server_ips = server_ips
            
        self.server_port = server_port
        self.is_running = True
        self.sock = None
        self.connected = False
        
        # 尝试连接服务器
        self.connect_to_server()
        
        if self.connected:
            # 启动接收线程
            self.recv_thread = threading.Thread(target=self.receive_loop)
            self.recv_thread.daemon = True
            self.recv_thread.start()
            
            # 发送登录包
            self.send_to_server("LOGIN", "ALL", "我上线了")
            
            # 进入命令行输入循环
            self.run_input_loop()
        else:
            print("无法连接服务器，程序退出。")

    def connect_to_server(self):
        print(f"[系统] 正在为您 ({self.nickname}) 寻找服务器...")
        
        for ip in self.server_ips:
            try:
                print(f"[系统] 尝试连接 {ip}:{self.server_port}...")
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(2)
                self.sock.connect((ip, self.server_port))
                self.sock.settimeout(None)
                
                self.connected = True
                print(f"[系统] 成功连接到服务器: {ip}")
                return
                
            except Exception as e:
                print(f"[系统] 连接 {ip} 失败: {e}")
                if self.sock:
                    self.sock.close()
                self.sock = None
        
        print("[错误] 所有服务器地址均无法连接！")

    def send_to_server(self, cmd, receiver, content):
        if not self.connected or not self.sock:
            print("[错误] 未连接到服务器")
            return

        packet = OICQPacket(cmd, self.nickname, receiver, content)
        data = packet.to_json()
        
        try:
            self.sock.sendall(data)
        except Exception as e:
            print(f"[错误] 发送失败: {e}")
            self.connected = False

    def send_message(self, msg):
        if not msg:
            return
        
        # 简单的逻辑：如果是 Pony 就发给 Tony
        target_user = "C2"
        
        print(f"我 -> {target_user}: {msg}")
        self.send_to_server("MSG", target_user, msg)

    def receive_loop(self):
        while self.is_running and self.connected:
            try:
                data = self.sock.recv(1024)
                if not data:
                    print("\n[系统] 服务器断开连接")
                    break
                
                packet_data = json.loads(data.decode('utf-8'))
                self.handle_packet(packet_data)
            except Exception as e:
                # print(f"[错误] 接收数据出错: {e}")
                break
        
        self.connected = False
        # 如果连接断开，可以通过设置标志位通知主线程退出（这里简化处理）

    def handle_packet(self, data):
        cmd = data.get('cmd')
        sender = data.get('sender')
        content = data.get('content')

        if cmd == "MSG":
            # 打印接收到的消息，\r 用于回到行首，\n 用于换行
            # 这样可以避免消息和输入提示符混在一起太乱
            print(f"\r{sender}: {content}")
            # 重新打印提示符
            print(f"{self.nickname} > ", end="", flush=True)

    def run_input_loop(self):
        print(f"\n--- {self.nickname} 已上线 ---")
        print("输入消息并回车发送。输入 'exit' 或 'quit' 退出程序。")
        
        while self.is_running and self.connected:
            try:
                # 显示提示符
                msg = input(f"{self.nickname} > ")
                
                if msg.lower() in ['exit', 'quit']:
                    self.logout()
                    break
                
                self.send_message(msg)
            except (EOFError, KeyboardInterrupt):
                # 捕获 Ctrl+D 或 Ctrl+C
                print("\n正在退出...")
                self.logout()
                break

    def logout(self):
        self.is_running = False
        if self.connected:
            self.send_to_server("LOGOUT", "ALL", "我下线了")
        if self.sock:
            self.sock.close()
        print("已下线。")

if __name__ == "__main__":
    # 在这里修改启动的昵称
    # 如果要测试两个客户端，请打开两个终端窗口，分别修改这里的名字运行
    NICKNAME = "C1" 
    
    # 也可以通过命令行参数指定: python client.py Tony
    if len(sys.argv) > 1:
        NICKNAME = sys.argv[1]

    client = OICQClient(NICKNAME)