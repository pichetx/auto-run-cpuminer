import os, time, json




def banner():
	os.system("clear")
	print("\033[1;34;40m")
	os.system("figlet -f big CPUminer")
	os.system("figlet -f digital http-server")
	print("\033[00m\n")
	print("\033[95mDeveloper by PICHET SAENGTEWAN\033[0m")
	print("\033[36m\033[0m")

def setip():


    banner()
    try:
        print("ตัวอย่าง:  \033[93m192.168.1.28:\033[00m""\033[32m8080\033[00m")
        ip = input("   ip :  ")
        print("\033[35m-----------------------------------------\033[0m")
        
        
        if ip == "":
            raise Exception()
    except:
        os.system("@cls||clear")
        print("\033[32mเกิดข้อผิดพลาดโปรดตั้งค่าใหม่\033[00m")
        time.sleep(3)
        os.system("python3 addip.py")

    push = {
        'ip': ip
    }
    with open("setip/ip.json", "w") as set:
        json.dump(push, set, indent=4)


while True:
    banner()
    setip()
    with open("setip/ip.json",encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        ip = loads['ip']
        	
        print("\033[36m")
        print("ip address ที่บันทึก")
        print("ip  =",ip)
        print("\033[0m\n")
        print("\033[31mโปรดตรวจสอบการตั้งค่า ถ้าถูกต้อง ให้ใช้คำสั่ง  run-miner  เพื่อเปิดขุด\033[0m")
    break




