import socket

def start_client():
    # تنظیمات کلاینت
    host = '127.0.0.1'  # آدرس IP سرور
    port = 12345  # پورت سرور

    # ایجاد سوکت و اتصال به سرور
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("به سرور متصل شدید.")

    while True:
        # ارسال پیام به سرور
        message = input("کلاینت: ")
        client_socket.send(message.encode())

        # دریافت پاسخ از سرور
        data = client_socket.recv(1024).decode()
        print("سرور:", data)

    client_socket.close()

start_client()