import random
import colorama
from colorama import Fore, Back, Style

import ecdsa
import base58
import requests
from Crypto.Hash import keccak


def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_adder = b"\x41" + keccak256(pub_key)[-20:]
    Addr = base58.b58encode_check(primitive_adder)
    return Addr


count = 0
print(Fore.CYAN + "Please Wait..." + Style.RESET_ALL)
while True:
    raw = bytes(random.sample(range(0, 256), 32))
    key = get_signing_key(raw)
    Wallet = verifying_key_to_addr(key.get_verifying_key()).decode()
    HexAdd = base58.b58encode_check(Wallet.encode()).hex()
    publickey = key.get_verifying_key().to_string().hex()
    privatekey = raw.hex()

    count += 1
    print(str(count)+" | "+privatekey+" | "+Wallet)

   # print(str(count) + " Add = " + Wallet + " " + "| Pk = " + privatekey+"  "+str(balances)+"  "+str(txid))
    f=open("trxKey.txt","a")
    f.write(privatekey+'\n')
    f.close()
    f1=open("trxAdd.txt","a")
    f1.write(Wallet+'\n')
    f1.close()


