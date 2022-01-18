from pypresence import Presence
import time

start_time = time.time()
client_id = "931833854069714974"
rpc = Presence(client_id)
rpc.connect()
rpc.update(state="rick rolling you", large_image="rr", small_image="fs", buttons=[{"label":"not a rick roll", "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"label":"my shitty bot", "url":"https://discord.com/api/oauth2/authorize?client_id=896932646846885898&permissions=8&scope=bot%20applications.commands"}], start=time.time())

data = open('/Users/siddheshzantye/Desktop/Coding/Python/Presence/lyrics.txt', 'r')

while True:
    for i in data:
        time.sleep(15)
        rpc.update(state="rick rolling you", details=f"{i}", large_image="rr", small_image="fs", buttons=[{"label":"not a rick roll", "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"label":"my shitty bot", "url":"https://discord.com/api/oauth2/authorize?client_id=896932646846885898&permissions=8&scope=bot%20applications.commands"}], start=start_time)
        
