import requests,os
from time import strftime,sleep
banner = """
          \033[1;36m████████╗░█████╗░████████╗
          \033[1;34m╚══██╔══╝██╔══██╗ ╚══██╔══╝
          \033[1;35m   ██║   ██║  ╚═╝    ██║
          \033[1;36m   ██║   ██║  ██     ██║
          \033[1;32m   ██║   ╚█████╔╝    ██║
          \033[1;34m   ╚═╝    ╚════╝     ╚═╝

                      \033[1;36m████████╗  ████╗  █████╗ ██╗
                      \033[1;35m╚══██╔══╝██╔══██╗██╔══██╗██║
                      \033[1;33m   ██║   ██║  ██║██║  ██║██║
                      \033[1;32m   ██║   ██║  ██║██║  ██║██║
                      \033[1;34m   ██║   ╚█████╔╝╚█████╔╝███████╗
                      \033[1;36m   ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[1;34m═════════════════════════════════════════════════════════════
\033[1;35mCOPYRIGHT : \033[1;36mThành Chần ♥
\033[1;35mZalo : \033[1;36m0335021778 ♥
\033[1;35mNhóm Xàm xí,Báo lỗi : \033[1;36mhttps://zalo.me/g/drghio579 ♥
\033[1;34m═════════════════════════════════════════════════════════════"""
def taobox(text):
  m = len(text)
  dai = m + 4
  print("\033[1;32m╔" + "═" * dai + "╗")
  print("║  " + "\033[1;33m"+text + "\033[1;32m  ║" )
  print("╚" + "═" * dai + "╝")
def taonv(text):
  dai = len(text) + 8
  #print("\033[1;32m┏" + "━" * dai + "┓")
  print(f"\033[1;36m{text}")
  #print("\033[1;32m┗" + "━" * dai + "┛")
def key():
  try:
    ma = open("keytool.txt","x")
  except:
    pass
  ngay=int(strftime('%d'))
  key1=str(ngay*124656646+2388472%3)
  key = 'tct'+key1
  url = 'https://layskeytool.000webhostapp.com/key.html?key='+key
  ma = open("keytool.txt","r")  
  testkey = ma.read()
  if testkey != key:
    for i in range(3,-1,-1):
      print("                                               ",end = "\r")
      for j in ["",".","..","..."]:
        print(f"\033[1;36mBạn sẽ đc chuyển đến web lấy mã sau {i} giây{j}",end = "\r")
        sleep(1/4)
    print("                                                    ",end = "\r")
    os.system(f"termux-open-url {url}")
    testkey = input("\033[1;35mNhập Key : ") 
    for i in range(1,101):
      print("                              ",end = "\r")
      if(i < 10):
        print(f"\033[1;33mĐang check key {i}%",end = "\r")
        sleep(0.1)
      else:
        print(f"\033[1;33mĐang check key {i}%",end = "\r")
        sleep(0.01)
    sleep(1)    
    if testkey != key:
      print(f"\033[1;31mKey sai hãy vượt link and nhập lại đe")
      quit()
    else:
      ma = open("keytool.txt","w")
      ma.write(testkey)
      ma.close()
      print("\033[1;36mKey đúng gòi bạn sài tool vui vẻ nhé:)))")
      sleep(1)
os.system("clear")      
print(banner)      
#key()       
os.system("clear")
print(banner)
taobox("Tool Golike ★")
print("\033[1;36m[>🍓<] => \033[1;33mNhập Số [1] ► Follow Tiktok")
print("\033[1;36m[>🍓<] => \033[1;33mNhập Số [2] ► Like Tiktok")
print("\033[1;36m[>🍓<] => \033[1;33mNhập Số [3] ► Follow Instagram")
print("\033[1;34m═════════════════════════════════════════════════════════════")
while True:
  try:
    select = int(input("\033[1;35mChọn nhiệm vụ bạn mún làm (12 để vừa fl vừa like) : "))
    if select not in [1,2,3,12]:
      print("\033[1;33mNhiệm vụ này không có trong danh sách!!!")
      continue
    break
  except:
    print("\033[1;31mSai định dạng!!!")
try:
  sl = open("luachon.txt","x")
except:
  pass
sl = open("luachon.txt","w")
sl.write(str(select))
sl.close()
if select in [1,2,12]:
  response = requests.get("https://raw.githubusercontent.com/thanhbtm1/golike/main/goliketiktok.py")
  path = "/storage/emulated/0/Download/goliketiktokv1.py"
  with open(path, "wb") as file:
    file.write(response.content)
  os.system("cd /sdcard/download && python goliketiktokv1.py")  
elif select == 3:
  response = requests.get("https://raw.githubusercontent.com/thanhbtm1/golike/main/golikeins.py")
  path = "/storage/emulated/0/Download/golikeinsv1.py"
  with open(path, "wb") as file:
    file.write(response.content)
  os.system("cd /sdcard/download && python golikeinsv1.py")  hihi