from webserver import keep_alive
import requests

channelID = 998487725915254854
headers = {
    "authorization":
    "OTk4NDg4MjI4ODQxNjY4NjE4.G5D9HJ.X-DLCxk9wnzWW2lF3jQ81td9bmBWIVXtLkopic"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
