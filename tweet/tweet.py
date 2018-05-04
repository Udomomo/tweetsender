import sys, tempfile, os, re
from os.path import join, dirname
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
from subprocess import call

def tweet():

    TWEET_EDITOR = os.environ.get('TWEET_EDITOR','vim') 
    initial_message = ["\n", "# Write your tweet above.\n", "# Lines starting with '#' will be ignored.\n"]

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        for msg in initial_message:
            tf.write(msg.encode('utf-8'))
        tf.flush()
        call([TWEET_EDITOR, '+set backupcopy=yes', tf.name])
        tf.flush()
        
        tf.seek(0)
        contents = ""
        for line in tf:
            decoded_line = line.decode("utf-8")
            if decoded_line != "# Write your tweet above.\n":
                contents += decoded_line
            else:
                break
        print(contents)

    params = {"status": contents}
    main(params)

def main(params):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    ck_env = os.environ.get('TWITTER_CK')
    cs_env = os.environ.get('TWITTER_CS')
    at_env = os.environ.get('TWITTER_AT')
    as_env = os.environ.get('TWITTER_AS')

    if not params["status"]:
        return "Aborted"

    twitter = OAuth1Session(ck_env, cs_env, at_env, as_env)
    req = twitter.post(url, params)

    if req.status_code == 200:
        return "Tweet has sent"
    else:
        return "Error: %d" % req.status_code

if __name__ == "__main__":
    print(tweet())