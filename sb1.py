from Dhenza7.linepy import *
from Dhenza7.akad.ttypes import Message
from Dhenza7.akad.ttypes import ContentType as Type
from Dhenza7.akad.ttypes import ChatRoomAnnouncementContents
from Dhenza7.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
import pyimgflip
from gtts import gTTS
from googletrans import Translator
#Bot Line v.10
#Creator: DHENZA TBP
listApp = [
	"CHROMEOS\t2.1.5\tdhenza\t0.18.1660.143.0"
	#"DESKTOPWIN\t5.9.2\tdhenza\t11.2.5", 
	#"DESKTOPMAC\t5.9.2\tdhenza\t11.2.5", 
	#"IOSIPAD\t8.14.2\tdhenza\t11.2.5", 
	#"WIN10\t5.5.5\tdhenza\t11.2.5"
]
try:
    for app in listApp:
        try:
            try:
                with open("authToken.txt", "r") as token:
                    authToken = token.read().replace("\n","")
                    if not authToken:
                        ririn = LINE()
                        with open("authToken.txt","w") as token:
                            token.write(cl.authToken)
                        continue
                    ririn = LINE(authToken, appName=app)
                break
            except Exception as error:
                print(error)
        except Exception as error:
            print(error)
except Exception as error:
    print(error