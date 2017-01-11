from gmusicapi import Musicmanager
import subprocess
import sys
import glob
import os
from time import sleep

class Uploader():
    def __init__(self):
         self.mm = Musicmanager()
         try:
             self.mm.login()
         except Exception as e:
             print(e)
             self.mm.perform_oauth()
         pass
    def check(self):
        while True:
             files=glob.glob("./music/*.mp3")
             print("Found :"+str(files))
             for music in files:
                  code=self.uploadFile(music)
                  print(code)
                  if len(code[0])==1:
                      try:
                          os.remove(music)
                      except OSError:
                          pass
             sleep(30)

    def uploadFile(self,path):
        try:
            return self.mm.upload(path)
        except Exception as e:
            print(e)

def main():
    u=Uploader()
    u.check()

if __name__ == "__main__":
    main()
