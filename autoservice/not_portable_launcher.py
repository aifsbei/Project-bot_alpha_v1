import os, sys
import subprocess
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable


class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self): # вызывается при вызове экземпляра,
#        self.announce(self.what) # например как обработчик щелчка на кнопке
        self.run(self.where) # подклассы должны определять метод run()

    def announce(self, text): # подклассы могут переопределять метод
        print(text) # announce() вместо логики if/elif

    def run(self, cmdline):
        assert False, 'run must be defined'


class Spawn(LaunchMode):

    def run(self, cmdline):
        os.spawnv(os.P_NOWAIT, pypath, (pyfile, cmdline))


NotPortableLauncher = Spawn


#def start_this():
#    os.spawnv(os.P_DETACH)