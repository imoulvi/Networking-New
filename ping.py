import subprocess
import os
'''
servers.txt contains ip address in following format
192.168.1.1
192.168.1.2
'''
with open('cspc devices.txt', 'r') as f:
        for ip in f:
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2",    ip],stdout=f, stderr=f).wait()
            if result:
                print(ip, "inactive")
            else:
                print(ip, "active")