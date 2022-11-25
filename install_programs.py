import os
import subprocess
#os.system("sudo apt update")


def install(program_name,check_is_installed,not_found, installation_command): 
    check_if_installed_already = subprocess.getoutput(check_is_installed)
    if(not_found in check_if_installed_already):
        os.system(installation_command)
    else:
        print("you probubly have ", program_name," \n")


#שימושית
install("pip", "pip3 --version", "not found", "sudo apt install python3-pip")
install("sounddevice", "sounddevice --version", "not found", "python3 -m pip install sounddevice --user")
install("numpy", 'python3 -c "import numpy; print(numpy.__version__)"', "No module named 'numpy'", "pip3 install numpy")
os.system("python -m pip install -U pip")
install("matplotlib", "python3 -c 'import matplotlib; print(matplotlib.__version__, matplotlib.__file__)'", "No module named", "python -m pip install -U matplotlib")



############################################################### enviroment ###############################################################
install("zsh", "zsh --version", "not found", "sudo apt install zsh")
install("oh-my-zsh", "cd ~/oh-my-zsh", "no such file or directory: ", 'sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
install("vim", "vim --version",  "not found","sudo apt-get install vim" )
install("zip", "zip --version",  "not found","sudo apt-get install zip" )
install("gzip", "gzip --version",  "not found","sudo apt-get install gzip" )
install("tar", "tar --version",  "not found","sudo apt-get install tar" )


# install vscode

# vscode shortcut .code

# c++
# c
# cpp compiler
#cpp debuggerrrrrrrrrrrrrrrrr


