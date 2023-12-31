def PyRun(code):
    exec(code)


def RUN(code):
    from subprocess import getoutput as run
    OUTPUT = run(code)
    print(OUTPUT)
    
def SRUN(code):
    from subprocess import getoutput as run
    OUTPUT = run(code)
    print(OUTPUT)
    exit()
