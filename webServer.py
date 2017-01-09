from flask import Flask
from flask import request
from gmusicapi import Musicmanager
import subprocess

mm = Musicmanager()
mm.login()
try:
    mm.login()
except Exception as e:
    print(e)
    mm.perform_oauth()

with open('log','a') as logFile:
    logFile.write("App launched\n")

app = Flask(__name__)

@app.route('/new/ako/zrt/')
def hello_world():
    with open('log','a') as logFile:
        logFile.write(str(request))
    try:
        url = request.args.get('url').strip()
    except Exception as e:
        return "URL not correct"
    try:
        title = request.args.get('title').strip()
    except Exception as e:
        return "Title not correct"
    uid=url[-12:]
    command=["youtube-dl"]
    command.append("--download-archive")
    command.append("catalogDownloaded.txt")
    command.append("--extract-audio")
    command.append("--audio-format")
    command.append("mp3")
    command.append("-o")
    command.append("%(id)s.%(ext)s")
    command.append(uid)
    with open('log','a') as logFile:
        logFile.write(str(command))
        logFile.write("uid/"+str(uid)+"/")
    subprocess.check_call(command)
    mm.upload("./"+str(uid)+".mp3")
    return "SUCCESS,"+str(title)+".mp3 uploaded"
