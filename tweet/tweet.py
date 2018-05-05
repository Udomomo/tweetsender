import sys, tempfile, os, re
from getpass import getpass
from os.path import join, dirname
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv, set_key
from subprocess import call

def config(dotenv_path = join(dirname(__file__), '.env')):
    CK = input("CONSUMER_KEY: ")
    CS = getpass("CONSUMER_SECRET: ")
    AT = input("ACCESS_TOKEN: ")
    AS = getpass("ACCESS_TOKEN_SECRET: ")

    set_key(dotenv_path, "TWITTER_CK", CK)
    set_key(dotenv_path, "TWITTER_CS", CS)
    set_key(dotenv_path, "TWITTER_AT", AT)
    set_key(dotenv_path, "TWITTER_AS", AS)
    print("API keys has been set.")

def tweet(dotenv_path = join(dirname(__file__), '.env')):
    load_dotenv(dotenv_path)

    TWEET_EDITOR = os.getenv('TWEET_EDITOR','vim') 
    initial_message = ["\n", "# Write your tweet above.\n"]

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

    params = {"status": contents}
    if not params["status"] or params["status"] == "\n":
        print("Aborted")
        return

    send_tweet(params)

def parse_error(res):
    return res["errors"][0]['message']

def send_tweet(params):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    
    # dotenv_path = join(dirname(__file__), '.env')
    # load_dotenv(dotenv_path)

    ck_env = os.getenv('TWITTER_CK')
    cs_env = os.getenv('TWITTER_CS')
    at_env = os.getenv('TWITTER_AT')
    as_env = os.getenv('TWITTER_AS')

    twitter = OAuth1Session(ck_env, cs_env, at_env, as_env)
    req = twitter.post(url, params)
    
    if req.status_code == 200:
        print("Tweet has successfully sent.")
    else:
        res = req.json()
        err = parse_error(res)
        print("Error: " + err)

if __name__ == "__main__":
    tweet()