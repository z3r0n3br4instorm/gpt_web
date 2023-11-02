import requests
import os

def push_it():
    os.system("rm read.zttf")
    os.system("git add .")
    os.system('git commit -m "updated data"')
    os.system("git push origin")

def write_stuff(data):
    os.system("rm read.zttf")
    command = "echo '"+data+"' > read.zttf"
    push_it()
    os.system(command)
    push_it()

def write_to_server():
    get_data = input("Enter Prompt :")
    write_stuff(get_data)

if __name__ == "__main__":
    while True:
        write_to_server()