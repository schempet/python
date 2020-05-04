import paramiko
import time
import sys, os, string, threading

outlock = threading.Lock()

def print_std(stdout):
    for line in stdout:
       print(line.strip('\n'))


def workon(ssh, cmd):
    for i in range(1,10):
      print(ssh, i)
      stdin, stdout, stderr = ssh.exec_command('whoami')
      print_std(stdout)
      stdin, stdout, stderr = ssh.exec_command(cmd)
      print_std(stdout)
      time.sleep(1)

def session(host, username, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=passwd)
    return ssh
   

def main():
        threads = []
        machine1='localhost'
        ssh1 = session(machine1, 'schempet', 'cisco123')
        t = threading.Thread(target=workon, args=(ssh1,'pwd'))
        t.start()
        threads.append(t)
        machine2='localhost'
        ssh2 = session(machine2, 'snisha', 'snisha123')
        t = threading.Thread(target=workon, args=(ssh2, 'ping -c 2 localhost'))
        t.start()
        threads.append(t)
        for t in threads:
           t.join() 

main()

