import sys, signal

# http://tldp.org/LDP/abs/html/exitcodes.html
RET_VALUE = 128 + signal.SIGINT

def ctrl_c(ret_value=RET_VALUE):
    signal.signal(signal.SIGINT, lambda x, y: exit(ret_value))

def exit(ret_value):
    print
    sys.exit(ret_value)

ctrl_c()

