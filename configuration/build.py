from utils import Guide
from utils import Executor
from utils import Config

guide = Guide("..","build")
guide.make_build()
guide.cd_build()

cfg = Config()
ide = cfg.get_ide()

Executor.run(["conan", "install", guide.root_dir])
Executor.run(["cmake", guide.root_dir, '-G', ide])