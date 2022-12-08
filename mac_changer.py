#! /usr/bin/env python
#beta file not finished yet

'''Md Delwar Hossain Dipu
    Saudi Arabia'''
import subprocess
intf1 = "wlan0"
intf2 = "eth0"

print("[0] Changing MAC address for "+intf1+" ?")
print("[1] Changing MAC address for "+intf2+" ?")

select1 = int(input("Choice number 0/1 : "))
if select1 == 0:
    print("\t You select --> "+intf1)
    print("\n")
    new_mac = str(input("Enter new MAC address useing 00:**:**... "))
    print("Your new MAC is "+new_mac)
    confirem = str(input("Are you agree to change Y/N \n"))
    if confirem == "Y" or confirem == "y":
        subprocess.call("ifconfig "+intf1+" down",shell=True)
        subprocess.call("ifconfig "+intf1+" hw ether "+new_mac,shell=True)
        subprocess.call("ifconfig "+intf1+" up",shell=True)
        print("\t Congratulation  your new MAC address is : "+new_mac)
        print("\t Have a nice day ")
        status=str(input("\tAre you want to check "+intf1+" status Y/N :"))
        if status == "y" or status == "Y":
            subprocess.call("ifconfig "+intf1,shell=True)
        else:
            exit()

    else:
        exit()
elif select1 == 1:
    print("\t You select --> "+intf2)
    print("\n")
    new_mac = str(input("Enter new MAC address useing 00:**:**... "))
    print("Your new MAC is "+new_mac)
    confirem = str(input("Are you agree to change Y/N \n"))
    if confirem == "Y" or confirem == "y":
        subprocess.call("ifconfig "+intf2+" down",shell=True)
        subprocess.call("ifconfig "+intf2+" hw ether "+new_mac,shell=True)
        subprocess.call("ifconfig "+intf2+" up",shell=True)
        print("\t Congratulation  your new MAC address is : "+new_mac)
        print("\t Have a nice day ")
        status = str(input("\tAre you want to check "+intf2+" status Y/N :"))
        if status == "y" or status == "Y":
            subprocess.call("ifconfig "+intf2,shell=True)
        else:
            exit()
    else:
        exit()
else:
    exit()
