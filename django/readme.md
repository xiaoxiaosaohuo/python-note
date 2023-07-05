## Environment setup
```
python3 -m venv .
```

`python3 -m venv .` 是一个用于创建 Python 虚拟环境的命令。下面是对该命令的解释：

`python3`: 这是一个命令行工具，用于运行 Python 3 解释器。在执行该命令之前，请确保已经安装了 Python 3，并且可以通过 python3 命令来运行它。

`-m venv`: 这是 python3 命令的一个选项，用于指定要执行的模块。venv 是 Python 的标准库中的一个模块，用于创建和管理虚拟环境。

`.`: 这是命令的最后一个参数，表示当前目录。在这个命令中，它表示要在当前目录中创建虚拟环境。


### activate

```
source venv/bin/activate
```

### create web project

```
django-admin startproject web
```