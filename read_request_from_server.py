import requests
import json

def get_requests():
    display_received_content(requests.get("https://github.com/z3r0n3br4instorm/gpt_web/blob/main/read.zttf").text)

def display_received_content(data):
    print("Received from server:", json.loads(data)["payload"]["blob"]["rawLines"][0])

if __name__ == "__main__":
    while True:
        get_requests()