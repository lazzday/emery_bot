# emerybot for /r/Gunners
# Answers "Good ebening" to any detected greeting string (e.g. "hello")

import praw
import secret

reddit = praw.Reddit(client_id=secret.CLIENT_ID,
                     client_secret=secret.CLIENT_SECRET,
                     username=secret.USERNAME,
                     password=secret.PASSWORD,
                     user_agent='Created by /u/lazzday')

subreddit = reddit.subreddit('Gunners')

keyphrase = ['good afternoon',
             'good evening',
             'good day',
             'good morning',
             'hello'
             ]

response = 'Good ebening!'

for comment in subreddit.stream.comments():
    if any(x in comment.body.lower() for x in keyphrase):
        with open("ids.txt", "r+") as sub_id:
            ids = sub_id.read().split()
            if comment.id not in ids:
                try:
                    comment.reply(response)
                    print('post success:', comment.id, ":", comment.body)
                    sub_id.write(' ' + comment.id)
                except:
                    print('post failed:', comment.id, ":", comment.body)
            else:
                print("Comment", comment.id, "already responded to.")
            sub_id.close()
print("Script end")