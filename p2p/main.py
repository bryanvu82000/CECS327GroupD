import time

import server
import socket
import client
#print(socket.gethostbyname(socket.gethostname()))


savedIP =["192.168.254.133","192.168.254.132"]
# savedIP = []
# becomeServer is a flag for when the file does not get transfered.


def listen():
    while True:
        becomeServer = False
        prevTime = 0
        prevSize = 0
        try:
            #, prevTime, prevSize, becomeServer
            privateIP, becomeServer = client.receive()
            if savedIP.__contains__(privateIP) == False:
                #print("Prev all IP's: " + str(savedIP))
                savedIP.append(privateIP)
                print("ALL IPS: " + str(savedIP))
        except:
            print("")

        if(becomeServer):
            break
        time.sleep(5)
def main():
    while True:
        listen()
        server.run(savedIP, "Pokemon Diamond.zip")


main()