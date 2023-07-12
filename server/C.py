import getopt
import hashlib
import json
import os
import sys
import uuid


def mkdirs(path):
    if not os.path.exists(path):
        print("mkdirs: path=" + path)
        os.makedirs(path)
    return path


def md5(param: str, len=32) -> str:
    if type(param) != 'str':
        param = json.dumps(param)
    return hashlib.md5(param.encode()).hexdigest()[0:len]


def code(len=16) -> str:
    return md5(str(uuid.uuid4()), len)


def init():
    global TOKEN
    help_info = """fast.py -t <token>"""
    argv = sys.argv[1:]
    token = None
    try:
        opts, args = getopt.getopt(argv, "ht:", ["token="])
    except getopt.GetoptError:
        print(help_info)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_info)
            sys.exit()
        elif opt in ("-t", "--token"):
            token = arg
    if not token:
        token = 'rUzf0Y861xaNJES1'
    TOKEN = token
    if not token:
        print(help_info)
    print('TOKEN', TOKEN)


def check_token(token):
    return TOKEN == token


def __load(tk=init()):
    ...


__load()
