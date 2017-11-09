import os
import platform
import subprocess

class Executor:
    def run(commands = [], *args):
        child = subprocess.Popen(commands, stdout=subprocess.PIPE)
        while child.poll() is None:
            output_line = child.stdout.readline()
            if (output_line):
                print(output_line.decode("utf-8")[:-1])
        code = child.returncode
        if (code):
            os.sys.exit(code)

class Guide:
    root_dir = ".."
    build_dir = "build"
    current_dir = ""

    def __init__(self, root_dir, build_dir):
        self.current_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
        self.root_dir = os.path.realpath(os.path.join(self.current_dir, self.root_dir))
        self.build_dir = os.path.realpath(os.path.join(self.root_dir, self.build_dir))

    def make_build(self):
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)

    def check_same(self):
        cur = os.path.dirname(os.path.realpath(__file__))
        cwd = os.getcwd()
        if cur == cwd:
            err_msg = "Current directory and executor path has the same paths:" + cur 
            os.sys.exit(err_msg)

    def cd_build(self):
        os.chdir(self.build_dir)