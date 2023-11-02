import requests

def get_requests():
    display_received_content(requests.get("https://raw.githubusercontent.com/z3r0n3br4instorm/gpt_web/main/read.zttf").text)

def display_received_content(data):
    print("Received from server:", data)

if __name__ == "__main__":
    while True:
        get_requests()