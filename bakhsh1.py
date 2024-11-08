import socket

def start_server():
    # تنظیمات سرور
    host = '127.0.0.1'  # آدرس IP لوکال (localhost)
    port = 12345  # پورت دلخواه

    # ایجاد سوکت و تنظیمات آن
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # انتظار برای یک کلاینت

    print("سرور در حال گوش دادن است...")

    conn, addr = server_socket.accept()
    print("اتصال از طرف:", addr)

    while True:
        # دریافت پیام از کلاینت
        data = conn.recv(1024).decode()
        if not data:
            break
        print("کلاینت:", data)

        # ارسال پاسخ به کلاینت
        message = input("سرور: ")
        conn.send(message.encode())

    conn.close()

start_server()