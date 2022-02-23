
import random
import time
import requests
from colorama import Fore , Style, ansi

print('Start')
with open("trxAdd.txt","r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1

print("Total Address Loaded This File Import  "+Fore.YELLOW+str(line_count)+Style.RESET_ALL)
mylist = []

with open('trxAdd.txt', newline='',encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

count = 0
remaining = line_count
for i in range(0, len(mylist)):
    trxadd = mylist[i]
    blocs = requests.get('https://apilist.tronscan.org/api/account?address='+trxadd)
    ress = blocs.json()
    TXS = dict(ress)["totalTransactionCount"]
    bal = dict(ress)["balance"]
    count += 1
    remaining -= 1
    print(str(count),Fore.CYAN,'|','TRON Address',Style.RESET_ALL,'',Fore.BLUE,'->',Style.RESET_ALL,'',Fore.MAGENTA,trxadd,Style.RESET_ALL, Fore.RED,' | ',Style.RESET_ALL, Fore.YELLOW,'','TXID No. -> ',Fore.RED,str(TXS),Style.RESET_ALL,' ')
    if int(TXS) > 0 :
        print(Fore.GREEN,'Save Information Wallet This Location File name : Winner.txt ')
        print('==================== M M D R Z A . C O M ====================')
        time.sleep(5)
        f = open("Winner.txt","a")
        f.write("\nWIN ADD => "+trxadd+"  "+"TX => "+str(TXS)+" BAL => "+str(bal))
        f.close()
        time.sleep(1)

        print(Fore.RED,'Save in the file name "Winner.TXT" can you check this file root folder')
        time.sleep(1)
        print(Fore.GREEN,'Now i run procces check your file and countine work')
        print(Fore.CYAN,'==================== M M D R Z A . C O M ====================',Style.RESET_ALL)
        time.sleep(1)

        continue
