from pypresence import Presence
import time


def run():
    start_time = time.time()
    client_id = "931833854069714974"
    rpc = Presence(client_id)
    rpc.connect()

    while True:
        data = open('lyrics.txt', 'r')
        c = 0
        for line in data:
            c += 1
            rpc.update(
                state="^ Line: ^", 
                details=f"{line}", 
                large_image="rr", 
                large_text="Rick Astley", 
                small_text="FusionSid", 
                small_image="fs", 
                buttons=[
                    {
                        "label":"not a rick roll", 
                        "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    }, 
                    {
                        "label":"my shitty bot", 
                        "url":"https://discord.com/api/oauth2/authorize?client_id=896932646846885898&permissions=8&scope=bot%20applications.commands"
                    }
                ], 
                party_size=[c, 60], 
                start=start_time)
                
            time.sleep(15)
            
run()
