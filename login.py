import datetime, os, sys
from time import sleep
try:
    import requests
    from pystyle import Center, Anime, Colors, Colorate
except:
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install pystyle')
    import requests
    from pystyle import Center, Anime, Colors, Colorate
    from time import sleep

# Định nghĩa các màu
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
reset = "\033[0m"
bold = "\033[1m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"
luc = '\033[1;32m'  # Xanh lá
vang = '\033[1;33m'
reset = '\033[0m'
# Đánh Dấu Bản Quyền
LK_tool = "trang + trang + [do + +_+ trang ] => "
tkhoi = "trang + trang + [do + ÷_+ trang ] => "
krystal = "trang + trang + '-------------------------------------------------------------------------'"

# Hàm xóa màn hình
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lấy ngày giờ hiện tại
def get_current_datetime():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    return date, time

# Lấy địa chỉ IP công cộng
def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_info = response.json()
        return ip_info['ip']
    except requests.exceptions.RequestException as e:
        print("Error fetching IP address:", e)
        return None

# Lấy thông tin vị trí (nơi ở) từ IP
def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        location_info = response.json()
        return location_info
    except requests.exceptions.RequestException as e:
        print("Error fetching location:", e)
        return None

# Lấy thời tiết từ OpenWeatherMap
def get_weather(city_name):
    try:
        weather_url = f'https://keyherlyswar.x10.mx/Apidocs/weather.php?q={city_name}'
        response = requests.get(weather_url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data["0"]["current"]["temperature"]
            weather_description = weather_data["0"]["current"]["winddisplay"]
            return f"{temperature}°C, {weather_description}"
        else:
            return "Không thể lấy thông tin thời tiết."
    except requests.exceptions.RequestException as e:
        return "Lỗi khi kết nối tới API thời tiết."

# Function to display banner with dynamic data
def display_banner():
    # Lấy ngày giờ, IP, vị trí và thời tiết
    current_date, current_time = get_current_datetime()
    ip_address = get_ip_address()
    if ip_address:
        location_info = get_location(ip_address)
        if location_info:
            city = location_info.get("city", "Không xác định")
            region = location_info.get("region", "Không xác định")
            country = location_info.get("country", "Không xác định")
            location = f"{city}, {region}, {country}"
        else:
            location = "Không thể lấy vị trí"
    else:
        location = "Không thể lấy địa chỉ IP"


    weather_info = get_weather(city)

    # Banner với thông tin động
    banner = f"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░████░██░█░▄▄▀█░▄▄▀█░▄▄▀██░█▀▄█░▄▄▀█░██░█░▄▄█▄░▄█░▄▄▀█░███
██░████░██░█░██░█░▀▀░█░▀▀▄██░▄▀██░▀▀▄█░▀▀░█▄▄▀██░██░▀▀░█░███
██░▀▀░██▄▄▄█▄██▄█▄██▄█▄█▄▄██░██░█▄█▄▄█▀▀▀▄█▄▄▄██▄██▄██▄█▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  

            Ａｕｔｈｏｒ: Lương Trường Khôi
            Ｇｉｔｈｕｂ: LunarKrystal
            Ｆａｃｅｂｏｏｋ: Lương Trường Khôi (LunarKrystal)

            ---------------------------
            Ngày: {reset} {current_date}
            Giờ: {reset} {current_time}
            Địa chỉ IP: {reset} {ip_address}
            Vị trí: {reset} {location}
            Thời tiết: {reset} {weather_info}
            ---------------------------
            ENTER ĐỂ VÀO TOOL 😋
            """

    # Hiển thị banner
    Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)

# Hàm chính
def main():
    clear_screen()
    display_banner()

if __name__ == "__main__":
    main()


print(f"{luc}Welcome Home{reset}, {vang}Admin {do}LunarKrystal")
sleep(2)
os.system("cls") if os.name == "nt" else os.system("clear")

#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""{vang}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░████░██░█░▄▄▀█░▄▄▀█░▄▄▀██░█▀▄█░▄▄▀█░██░█░▄▄█▄░▄█░▄▄▀█░███
██░████░██░█░██░█░▀▀░█░▀▀▄██░▄▀██░▀▀▄█░▀▀░█▄▄▀██░██░▀▀░█░███
██░▀▀░██▄▄▄█▄██▄█▄██▄█▄█▄▄██░██░█▄█▄▄█▀▀▀▄█▄▄▄██▄██▄██▄█▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)

urlkey = "https://raw.githubusercontent.com/LunarKrystal/-/refs/heads/main/%3F.txt"
# =======================[RUN]=======================#
while True:
    try:
        os.system("cls") if os.name == "nt" else os.system("clear")
        banner()
    
        print("\033[1;31m[\033[1;39m1\033[1;31m] \033[1;39mNhập Key Để Vào Tool Nhé ")
    
        chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mNhập Số\033[1;39m]\033[1;39m: \033[1;32m')
        
        response = requests.get(urlkey)
        remote_data = response.text.strip()
        if chon == remote_data:
            print(dev+" \033[1;39mĐang Vào Tool...")
            sleep(2)
            os.system("python3 home.py")
            # print("?")
            # exec(requests.get('https://run.mocky.io/v3/a74e88ba-070e-4cf3-a358-9f8013c49427').text)
            break
                # exec(requests.get('ok').text)
    except requests.exceptions.ConnectionError:
            print(dev+" \033[1;39mServer Đang Bảo Trì!")
            exit()
    except KeyboardInterrupt:
        print(dev+" \033[1;39mNhập Sai Rồi Nhập Lại Đi!")
        exit()