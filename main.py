import praw
from time import sleep

def invert(m):
    return ' '.join(list(map(lambda x: x[::-1], m.split())))

reddit = praw.Reddit(
    client_id="ID CLIENT",
    client_secret="SECRET CLIENT",
    user_agent="<console:MQS_BOT:1.0>",
    username="REDDIT USERNAME", 
    password="REDDIT PASSWORD",
)

while True:

    subreddit = reddit.subreddit("copypasta_es")
    
    for submission in subreddit.new(limit=1):
        x = submission

    with open("keys.txt", "r") as f:
  
       readfile = f.read()

       if str(x) in readfile:
           pass

       else:

           with open("keys.txt", "a") as k:

            print(f"Se agrego el post [{x}] a la lista.")
            k.write(f"{str(x)} ")
            k.close()

            submission = reddit.submission(id=x)
            submission.reply(invert(submission.selftext))
            sleep(20)

    
