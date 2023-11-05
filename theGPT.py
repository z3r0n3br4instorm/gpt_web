from gpt4all import GPT4All
import time
import os
def debug(string):
    print("[DEBUGGER]",string)

def push_it():
    os.system("git add .")
    os.system('git commit -m "updated data"')
    os.system("git push origin")

def write_stuff(data):
    os.system("client_read.zttf")
    command = "echo '"+data+"' > client_read.zttf"
    push_it()
    os.system(command)
    push_it()

model = GPT4All('mistral-7b-openorca.Q4_0.gguf')
while True:
    try:
        prompt = open("gpt_write.zttf","r").read()
        with model.chat_session():
            response1 = model.generate(prompt=prompt, temp=0)
            print(model.current_chat_session)
            __forClient = model.current_chat_session
            write_stuff(__forClient)
    except:
        debug("I/O failiure...")