from utils import Executor
from utils import Guide

guide = Guide("..","build")
guide.make_build()
guide.cd_build()

Executor.run(["conan", "install", guide.root_dir])
Executor.run(["cmake", guide.root_dir])