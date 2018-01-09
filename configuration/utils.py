import os
import sys
import platform
import shutil
import subprocess
import configparser

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
        self.root_dir = os.path.realpath(os.path.join(self.current_dir, root_dir))
        self.build_dir = os.path.realpath(os.path.join(self.root_dir, build_dir))

    def make_build(self):
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)

    def check_same(self):
        cur = os.path.dirname(os.path.realpath(__file__))
        cwd = os.getcwd()
        if cur == cwd:
            err_msg = "Current directory and executor path has the same paths:" + cur 
            os.sys.exit(err_msg)

    def cd_build(self, dir = None):
        os.chdir(self.build_dir if dir is None else dir)

    def deploy(dir, files = []):
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        for file in files:
            filename = os.path.basename(file)
            destpath = os.path.join(target_directory, filename)
            shutil.move(file, destpath)

class Config:
    __name = "cfg.ini"

    def __init__(self):
        if not os.path.isfile(self.__name):
            file = open(self.__name, 'w')
            file.write("[IDE]\n")
            file.write("Windows = Visual Studio 15 2017 Win64\n")
            file.write("Darwin = Xcode\n")
            file.write("Linux = KDevelop3")

            file.close()

    def get_ide(self):
        config = configparser.ConfigParser()
        config.read(self.__name)
        operation_system = platform.system()
        return config['IDE'][operation_system]
