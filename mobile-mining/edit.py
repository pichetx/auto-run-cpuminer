import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ตัวอย่าง:")
       print(" \033[93mstratum+tcp://allium.sea.mine.zpool.ca:6433\033[00m")
       print(" \033[93mstratum+tcp://yescrypt.asia.mine.zergpool.com:6233\033[00m")
       pool = input(" pool : ")
       print("\033[35m-----------------------------------------\033[0m")

       print("ตัวเลือก: \033[93m")
       print("scrypt scrypt:N scrypt-jane:N sha256d allium")
       print("axiom bastion bitcore blake blake2s blake2b")
       print("bmw cryptonight cryptonight-ligth decred dmd-gr")
       print("fresh geek groestl jha lbry lyra2RE lyra2REv2")
       print("lyra2REv3 myr-gr neoscrypt nist5 pentablake")
       print("pluck quark qubit skein skein2 s3 sia sib")
       print("timetravel tribus vanilla veltor xavan x11evo")
       print("x11 x12 x13 x14 x15 x16r x16rv2 x16s x17 x20r")
       print("0x10 yespower yespowerR16 yespowerIC yespowerLITB")
       print("yespowerIOTS yespowerITC yespowerMGPC")
       print("yespowerSUGAR yespowerTIDE yespowerURX")
       print("yescrypt yescryptR8 yescryptR16 yescryptR32 zr5")
       print("\033[00m")
       algo = input("algo: ")
       print("\033[35m-----------------------------------------\033[0m")
        
       print("ตัวอย่าง: \033[93mDCYiQottcGcnmzkp9KqqJwowc3ifEZUxm1\033[00m")
       wallet = input("wallet: ")
       print("\033[35m-----------------------------------------\033[0m")

       print("ตัวอย่าง:")
       print("  \033[93mc=DOGE (zergpoolไม่ต้องใส่ id=ชื่อ ระบบจะเพิ่มให้เอง)\033[00m")
       password = input("password : ")
       print("\033[35m-----------------------------------------\033[0m")

       if pool == "" or wallet == "":
          raise Exception()
       if password == "":
          raise Exception()
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("edit-miner")   
   push = {
         'pool': pool,
         'wallet': wallet,
         'pass': password
          }
   with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)

        print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
        name = input("[-n]: ")
        print("\033[35m-----------------------------------------\033[0m")
        
        print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
        cpu = int(input("[-t]: "))
        print("\033[35m-----------------------------------------\033[0m")
        
        if name == "":
            name = "x"
        if cpu == "":
            cpu = 1
        
        push = {
                 'name': name,
                 'cpu': cpu
               }
        with open("set-miner/offline.json", "w") as set:
             json.dump(push, set, indent=4)
             
while True:
  banneredit()
  OffMiner()
  os.system("run-miner")     
  break
