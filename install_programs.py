import os
import subprocess
#os.system("sudo apt update")


def already_install(program_name,check_version): 
    result = subprocess.getoutput(check_version)
    print("this: ",result)
    not_found="not found"
    if(not_found in result):
        return False
    return True


#שימושית
def install_pip():
    if(not already_install("pip", "pip --version")):
        os.system("sudo apt install python3-pip")
        os.system("pip3 --version")
    else:
        print("you have pip\n")

def sounddevice():
    if(not already_install("sounddevice")):
        os.system("python3 -m pip install sounddevice --user")
        os.system("sounddevice --version")
    else:
        print("you have sounddevice\n")

def install_numpy():
    check_version='python3 -c "import numpy; print(numpy.__version__)"'
    result = subprocess.getoutput(check_version)
    print("this: ",result)
    not_found="No module named 'numpy'"
    if(not_found in result):
        os.system("pip3 install numpy")
    else:
        print("you probubly already have numpy\n")

def install_matplotlib():
    check_version="python3 -c 'import matplotlib; print(matplotlib.__version__, matplotlib.__file__)'"
    result = subprocess.getoutput(check_version)
    print("this: ",result)
    not_found="No module named"
    if(not_found in result):
        os.system("python -m pip install -U pip")
        os.system("python -m pip install -U matplotlib")
    else:
        print("you probubly already have matplotlib\n")
#install_numpy()
#put_python3_in_PATH()

install_matplotlib()



# install vscode

# vscode shortcut .code

# c++
# c
# cpp compiler
#cpp debuggerrrrrrrrrrrrrrrrr


