# ctrl_c
A small Python module that allows to cleanly exit a script by pressing Ctrl+C, i.e., no more Traceback for KeyboardInterrupt

---

Pressing Ctrl+C while a Python script is running usually leads to output like this:

    ^CTraceback (most recent call last):
      File "...", line ..., in <module>
        ...
    KeyboardInterrupt

Sometimes one might rather not see this traceback, but mimic the behavior of a shell script. Simply importing this module via

    import ctrl_c

hooks up the signal SIGINT with sys.exit() including the correct return value according to [the LDP](http://tldp.org/LDP/abs/html/exitcodes.html "Exit Codes With Special Meanings").


Furthermore, calling the contained function with an argument, i.e., 

    ctrl_c.ctrl_c(ret_value)

 will use this as the return value instead.


