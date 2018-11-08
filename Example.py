from lib.linepy import *
from collections import OrderedDict
import json,sys

with open("authToken.txt","r") as f:
    token = f.read().replace("\n","")
with open("Cmd_data.json","r",encoding="utf_8_sig") as f:
    datas = json.loads(f.read(),object_pairs_hook=OrderedDict)

cl = LineClient(authToken=token)
chcl = LineChannel(cl)
tracer = LinePoll(cl)
replyer = simplify.Simplify(cl,datas=datas)

def m_exec_thread(msg):
    try:
        if msg.toType == 0: msg.to = msg._from
        sys.stdout = open("temp.txt","w")
        exec(msg.text.replace("!exec","").replace("import os",""))
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        with open("temp.txt","r") as r:
            txt = r.read()
        cl.sendMessage(msg.to,txt)
    except Exception as e:
        txt = str(e)
        cl.sendMessage(msg.to,txt)
replyer.addFuncInterrupt("m_exec_thread",m_exec_thread)

def echoDisposer(op):
    msg = op.message
    replyer.reply(msg)
tracer.addOpInterrupt(26, echoDisposer)

while True:
    tracer.trace()
