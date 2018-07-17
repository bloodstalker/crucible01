#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import argparse
import code
import readline
import signal
import sys

def SigHandler_SIGINT(signum, frame):
    print()
    sys.exit(0)

class Argparser(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--string", type=str, help="string")
        parser.add_argument("--bool", action="store_true", help="bool", default=False)
        parser.add_argument("--dbg", action="store_true", help="debug", default=False)
        self.args = parser.parse_args()

# write code here
def premain(argparser):
    signal.signal(signal.SIGINT, SigHandler_SIGINT)
    #here
    log = open("./log", "r")
    new_log = open("./log.h", "w")
    new_log.write("typedef struct {\n\tint x;\n\tint y;\n}co_t;\n")
    new_log.write("co_t co[] = {")
    size = 0
    for line in log:
        pos = line.find("--")
        #print("{" + line[0:pos] + "," + line[pos+2:-1] + "},")
        new_log.write("{" + line[0:pos] + "," + line[pos+2:-1] + "},")
        size+=1
    new_log.write("};\n")
    new_log.write("int co_size = " + str(size) + ";\n")

def main():
    argparser = Argparser()
    if argparser.args.dbg:
        try:
            premain(argparser)
        except Exception as e:
            print(e.__doc__)
            if e.message: print(e.message)
            variables = globals().copy()
            variables.update(locals())
            shell = code.InteractiveConsole(variables)
            shell.interact(banner="DEBUG REPL")
    else:
        premain(argparser)

if __name__ == "__main__":
    main()
