import requests
import json
import time
def get_requests():
    display_received_content(requests.get("https://github.com/z3r0n3br4instorm/gpt_web/blob/main/read.zttf").text)

def display_received_content(data):
    time.sleep(5)
    try:
        print("Received from server:", json.loads(data)["payload"]["blob"]["rawLines"][0])
    except:
        print("An unexpected error occured !")
if __name__ == "__main__":
    while True:
        get_requests()