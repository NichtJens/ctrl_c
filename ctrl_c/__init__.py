import sys, signal

# http://tldp.org/LDP/abs/html/exitcodes.html

def ctrl_c(ret_value=128 + signal.SIGINT):
    signal.signal(signal.SIGINT, lambda x,y: sys.exit(ret_value))

ctrl_c()

