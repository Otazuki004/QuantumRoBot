def PyRun(code):
    #Import Some Items For Development Friendly
    from root.__main__ import bot
    import time
    import os
    exec(code)


def RUN(code):
    from subprocess import getoutput as run
    OUTPUT = run(code)
    print(OUTPUT)
    
