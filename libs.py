import socket
from time import sleep

pc_name = socket.gethostname()

def welcome_message():
    style = "*" * (len(pc_name) + 10)
    print(style)
    print(f"<--> {pc_name} <-->")
    print(style)
    

def exit_program():
    print("Program akan diberhentikan...")
    sleep(1)
    print('3..')
    sleep(1)
    print('2..')
    sleep(1)
    print('1..')
    sleep(1)
    print('Bye!')


if __name__ == "__main__":
    welcome_message();
    exit_program();