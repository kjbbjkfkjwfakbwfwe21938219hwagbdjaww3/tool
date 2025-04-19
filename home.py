import requests, sys
from time import sleep
from datetime import datetime, timedelta
import time
import os
# import socket
# import platform
# import subprocess


# # Cấu hình Tool 2
# TOOL2_HOST = '127.0.0.1'
# TOOL2_PORT = 5001
# TOOL2_ENDPOINT = '/receive_info'

# def get_wifi_ssid():
#     ssid = "Không xác định"
#     try:
#         system = platform.system()
#         if system == "Linux": # Giữ nguyên cho Linux
#             output = subprocess.check_output(["iwgetid", "-r"]).decode("utf-8").strip()
#             if output:
#                 ssid = output
#         elif system == "Windows": # Giữ nguyên cho Windows
#             output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8")
#             for line in output.splitlines():
#                 if "SSID" in line:
#                     ssid = line.split(":")[1].strip()
#                     break
#         elif system == "Darwin": # Giữ nguyên cho macOS
#             output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]).decode("utf-8")
#             for line in output.splitlines():
#                 if "SSID:" in line:
#                     ssid = line.split(":")[1].strip()
#                     break
#         elif system == "Android": # Thêm xử lý cho Android
#             output = subprocess.check_output(["dumpsys", "wifi"]).decode("utf-8")
#             for line in output.splitlines():
#                 if "SSID: " in line:
#                     ssid = line.split("SSID: ")[1].strip()
#                     if ssid == "<unknown ssid>": # Xử lý trường hợp SSID unknown
#                         ssid = "Không kết nối WiFi" # hoặc giá trị phù hợp
#                     break

#     except Exception as e:
#         print(f"Lỗi khi lấy tên WiFi: {e}")
#     return ssid

# def is_rooted():
#     rooted = False
#     try:
#         if platform.system() == "Linux" or platform.system() == "Android":
#             if os.geteuid() == 0:
#                 rooted = True
#             else: # Thêm kiểm tra su binary cho Android (có thể không chính xác 100%)
#                 process = subprocess.Popen(['su', '-c', 'id'],
#                                            stdout=subprocess.PIPE,
#                                            stderr=subprocess.PIPE)
#                 stdout, stderr = process.communicate()
#                 if process.returncode == 0:
#                     rooted = True
#     except Exception as e:
#         print(f"Lỗi khi kiểm tra root: {e}")
#     return rooted

# def get_network_operator():
#     operator = "Không xác định"
#     # (Như trước, việc lấy nhà mạng rất phức tạp, có thể cần Android API)
#     return operator

# def get_battery_info():
#     battery_percentage = "Không xác định"
#     battery_status = "Không xác định"
#     try:
#         system = platform.system()
#         if system == "Windows": # Giữ nguyên cho Windows
#             output = subprocess.check_output(["wmic", "path", "Win32_Battery", "Get", "BatteryStatus,EstimatedChargeRemaining"]).decode("utf-8")
#             lines = output.strip().splitlines()
#             if len(lines) > 1:
#                 parts = lines[1].split()
#                 if len(parts) == 2:
#                     battery_status_code = parts[0]
#                     battery_percentage = parts[1]

#                     status_messages = {
#                         '1': 'Không xác định',
#                         '2': 'Đang sạc',
#                         '3': 'Đang xả',
#                         '4': 'Thấp',
#                         '5': 'Cao',
#                         '6': 'Lỗi',
#                         '7': 'Đang sạc một phần',
#                         '8': 'Đang sạc đầy'
#                     }
#                     battery_status = status_messages.get(battery_status_code, 'Không rõ')

#         elif system == "Linux": # Giữ nguyên cho Linux
#             battery_dir = ""
#             for entry in os.listdir("/sys/class/power_supply/"):
#                 if entry.startswith("BAT"):
#                     battery_dir = os.path.join("/sys/class/power_supply/", entry)
#                     break
#             if battery_dir:
#                 try:
#                     with open(os.path.join(battery_dir, "capacity"), "r") as f:
#                         battery_percentage = f.readline().strip() + "%"
#                     with open(os.path.join(battery_dir, "status"), "r") as f:
#                         battery_status = f.readline().strip()
#                 except FileNotFoundError:
#                     pass

#         elif system == "Darwin": # Giữ nguyên cho macOS
#             output = subprocess.check_output(["ioreg", "-r", "-c", "AppleSmartBattery", "-w0"]).decode("utf-8")
#             for line in output.splitlines():
#                 if '"CurrentCapacity" =' in line:
#                     battery_percentage = line.split("=")[1].strip()
#                     battery_percentage = str(round(int(battery_percentage)/100*100)) + "%"
#                 if '"BatteryHealth" =' in line:
#                     battery_status = line.split("=")[1].strip().strip('"')
#         elif system == "Android": # Thêm xử lý cho Android (tương tự Linux)
#             battery_dir = ""
#             for entry in os.listdir("/sys/class/power_supply/"):
#                 if entry.startswith("battery") or entry.startswith("BAT"): # Thường là "battery" hoặc "BATx"
#                     battery_dir = os.path.join("/sys/class/power_supply/", entry)
#                     break
#             if battery_dir:
#                 try:
#                     with open(os.path.join(battery_dir, "capacity"), "r") as f:
#                         battery_percentage = f.readline().strip() + "%"
#                     with open(os.path.join(battery_dir, "status"), "r") as f:
#                         battery_status = f.readline().strip()
#                 except FileNotFoundError:
#                     pass


#     except Exception as e:
#         print(f"Lỗi khi lấy thông tin pin: {e}")
#     return battery_percentage, battery_status

# def get_bluetooth_status():
#     bluetooth_connected = "Không xác định"
#     try:
#         system = platform.system()
#         if system == "Windows": # Giữ nguyên cho Windows
#             output = subprocess.run(["powershell", "-Command", "Get-PnpDevice -Class Bluetooth | Where-Object {$_.Status -eq 'OK'}"], capture_output=True, text=True)
#             if output.stdout:
#                 bluetooth_connected = "Có"
#             else:
#                 bluetooth_connected = "Không"

#         elif system == "Linux": # Giữ nguyên cho Linux
#             output = subprocess.run(["bluetoothctl", "show"], capture_output=True, text=True)
#             if "Powered: yes" in output.stdout:
#                 bluetooth_connected = "Có"
#             else:
#                 bluetooth_connected = "Không"

#         elif system == "Darwin": # Giữ nguyên cho macOS
#             output = subprocess.check_output(["system_profiler", "SPBluetoothDataType"]).decode("utf-8")
#             if "State: On" in output:
#                 bluetooth_connected = "Có"
#             else:
#                 bluetooth_connected = "Không"
#         elif system == "Android": # Thêm xử lý cho Android
#             output = subprocess.check_output(["dumpsys", "bluetooth_manager"]).decode("utf-8")
#             if "state=ON" in output or "enabled: true" in output: # Kiểm tra trạng thái ON hoặc enabled
#                 bluetooth_connected = "Có"
#             else:
#                 bluetooth_connected = "Không"


#     except Exception as e:
#         print(f"Lỗi khi lấy trạng thái Bluetooth: {e}")
#     return bluetooth_connected


# def send_info_to_tool2():
#     server_hostname = socket.gethostname()
#     device_name = platform.platform()
#     server_ip = socket.gethostbyname(server_hostname)

#     wifi_ssid = get_wifi_ssid()
#     rooted_status = is_rooted()
#     network_operator = get_network_operator()
#     battery_percentage, battery_status = get_battery_info()
#     bluetooth_connected = get_bluetooth_status()

#     data_to_send = {
#         'ip': server_ip,
#         'hostname': server_hostname,
#         'device_name': device_name,
#         'wifi_ssid': wifi_ssid,
#         'rooted': rooted_status,
#         'network_operator': network_operator,
#         'battery_percentage': battery_percentage,
#         'battery_status': battery_status,
#         'bluetooth_connected': bluetooth_connected
#     }

#     try:
#         response = requests.post(f'http://{TOOL2_HOST}:{TOOL2_PORT}{TOOL2_ENDPOINT}', json=data_to_send)
#         if response.status_code == 200:
#             print("Thông tin (máy, pin, Bluetooth...) đã được gửi thành công đến Tool 2.")
#         else:
#             print(f"Lỗi khi gửi thông tin đến Tool 2. Status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"Lỗi kết nối đến Tool 2: {e}")

# if __name__ == '__main__':
#     send_info_to_tool2()


try:
    import requests, colorama, prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"

# Thời điểm tool start
t= time.localtime(time.time())
localtime = time.asctime(t)
str = "Tool bất đầu lúc: " + time.asctime(t)

colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
def get_public_ip():
    try:
        # Gửi yêu cầu đến dịch vụ ipify để lấy địa chỉ IP công cộng
        response = requests.get('https://api64.ipify.org?format=json')
        # Trích xuất và in ra địa chỉ IP từ phản hồi JSON
        ip_address = response.json().get('ip')
        return ip_address
    except requests.RequestException as e:
        return None
def notify_user_ip():
    ip = get_public_ip()
    if ip:
        print(f"    Your IP address: {ip}")
    else:
        print("    không check được ip! vui lòng kết nối mạng !")
os.system("clear")
t= time.localtime(time.time())
localtime = time.asctime(t)
str = "    Time Start: " + time.asctime(t)
banner = """
\033[1;33m╔════════════════════════════════════════╗
\033[1;33m║\033[1;35m██╗░░██╗░░░░░░██████╗░███████╗██╗░░░██╗\033[1;33m ║
\033[1;33m║\033[1;39m██║░██╔╝░░░░░░██╔══██╗██╔════╝██║░░░██║\033[1;33m ║
\033[1;33m║\033[1;36m█████═╝░█████╗██║░░██║█████╗░░╚██╗░██╔╝\033[1;33m ║
\033[1;33m║\033[1;32m██╔═██╗░╚════╝██║░░██║██╔══╝░░░╚████╔╝░\033[1;33m ║
\033[1;33m║\033[1;34m██║░╚██╗░░░░░░██████╔╝███████╗░░╚██╔╝░░\033[1;33m ║
\033[1;33m║\033[1;33m╚═╝░░╚═╝░░░░░░╚═════╝░╚══════╝░░░╚═╝░░░\033[1;33m ║
\033[1;33m╠════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ Phiên bản bạn đang sử dụng : \033[1;35m0.0.1    \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mfb.com/LunarKrystal.Dev    \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35m0345451805 [Lương Trường Khôi] \033[1;33m║
\033[1;33m║\033[1;34m▶ Ngày tạo tool: 11/09/2024   ㅤ        \033[1;33m║
\033[1;33m║\033[1;34m▶ Nếu Có Lỗi Hãy Báo Qua Facebook Nhé   \033[1;33m║
\033[1;33m╚════════════════════════════════════════╝"""
print(banner)
print("\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print("\033[1;39m┌───────────────── By.LTK ───────────────┐")
print("\033[1;32mㅤㅤㅤㅤㅤㅤ\033[1;32mPython \033[1;39mVERSION\033[1;32m 3.13\033[1;32m")
print("\033[1;32m    TELEGRAM: t.me/TrKhoi_Media")
print("\033[1;35m    FACEBOOK: Lương Trường Khôi")
print("\033[1;32m    ZALO: 0345451805\033[1;31m")
notify_user_ip()
print(str)
print("\033[1;32m    \033[1;39mCopyright: Lương Trường Khôi\033[1;32m")
print("\033[1;39m└────────────────────────────────────────┘")
print("\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;34m")   
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mSPAM SMS/CALL   \033[1;32m║')
print('\033[1;39m└───────────────────┘')
# print('\033[1;33m Ngừng hoạt động')
print('\033[1;31m<\033[1;37m/\033[1;31m> \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Spam SMS (mượt)')
print('\033[1;31m<\033[1;37m/\033[1;31m> \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTool Spam SMS / CALL (ổn định)')
print('\033[1;31m────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39m    SCAN        \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m<\033[1;37m/\033[1;31m> \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mScan VNC VPS (BETA)')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mTiện Ích     \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m👾\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m0\033[1;31m] \033[1;32mThoát Tool')

#Tiến hành chọn chức năng
try:
    while True:
        chon = input('\033[1;31m[\033[1;37m✨\033[1;31m] \033[1;37m=> \033[1;32mNHẬP\033[1;37m =>: \033[1;33m')
        if chon == "1":
            exec(requests.get('https://raw.githubusercontent.com/kjbbjkfkjwfakbwfwe21938219hwagbdjaww3/tool/refs/heads/main/scripts/spam.py').text)
        elif chon == "1.1":
            exec(requests.get("https://raw.githubusercontent.com/kjbbjkfkjwfakbwfwe21938219hwagbdjaww3/tool/refs/heads/main/scripts/spamsms.py").text)
        elif chon == "2":
            os.system("cls") if os.name == "nt" else os.system("clear")
            exec(requests.get("https://raw.githubusercontent.com/kjbbjkfkjwfakbwfwe21938219hwagbdjaww3/tool/refs/heads/main/scripts/scanvps.py").text)
        elif chon == "0":  # Chỉ thoát nếu nhập đúng "0"
            print("Cảm ơn đã sử dụng tools. Hẹn gặp lại 💝")
            sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            break
        else:
            print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")
except KeyboardInterrupt:
    print("\n\033[1;31m[🌌] Tiến hành thoát tool..")
    sleep(1)
    os.system("cls") if os.name == "nt" else os.system("clear")

