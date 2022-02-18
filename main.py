from pypresence import Presence
import time
from subprocess import run

start_time = time.time()
client_id = "931833854069714974"
rpc = Presence(client_id)
rpc.connect()

def get_current_app():
    output = run([f"osascript", "get_app.scpt"], capture_output=True).stdout.decode()
    output = output.replace(".app:", "")
    output = output.split(":")
    return output[2]

while True:
    data = open('lyrics.txt', 'r')
    for line in data:
        rpc.update(
            state=f"Active app: `{get_current_app()}`", 
            details=f"{line}", 
            large_image="rr", 
            large_text="Rick Astley", 
            small_text="FusionSid", 
            small_image="fs", 
            buttons=[
                {
                    "label":"Totally not a rick roll", 
                    "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                }, 
                {
                    "label":"my shitty bot", 
                    "url":"https://discord.com/api/oauth2/authorize?client_id=896932646846885898&permissions=8&scope=bot%20applications.commands"
                }
            ], 
            start=start_time)
            
        time.sleep(15)
        
