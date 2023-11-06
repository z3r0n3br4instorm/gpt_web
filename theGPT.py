from gpt4all import GPT4All
import time
import os
def debug(string):
    print("[DEBUGGER]",str(string))

def push_it():
    os.system("git add .")
    os.system('git commit -m "updated data"')
    os.system("git push origin")

def write_stuff(data):
    os.system("rm client_read.zttf")
    push_it()
    command = "echo '"+str(data)+"' > client_read.zttf"
    os.system(command)
    push_it()
prompt2 = ""
model = GPT4All('mistral-7b-openorca.Q4_0.gguf')
while True:
    if True:
        prompt = open("gpt_write.zttf","r").read()
        if prompt == prompt2:
            print("skip")
        else:
            with model.chat_session():
                response1 = model.generate(prompt=prompt, temp=0)
                print(model.current_chat_session)
                __forClient = model.current_chat_session
                write_stuff(__forClient)
                debug(__forClient)
                prompt2 = prompt
    time.sleep(1)
#    except:
#        debug("I/O failiure...")
