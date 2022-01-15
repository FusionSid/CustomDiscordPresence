from pypresence import Presence
import time

client_id = "931833854069714974"
rpc = Presence(client_id)
rpc.connect()
rpc.update(state="rick rolling you", large_image="rr", buttons=[{"label":"not a rick roll", "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}], start=time.time())

while True:
    pass