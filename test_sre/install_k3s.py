import os
import subprocess

def install_k3s():
    subprocess.run(["sudo", "apt-get", "update", "-y"])
    subprocess.run(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "curl"])
    subprocess.run(["curl", "-sfL", "https://get.k3s.io", "-o", "k3s_install.sh"])
    subprocess.run(["sudo", "bash", "k3s_install.sh"])
    subprocess.run(["sudo", "kubectl", "get", "nodes"])

if __name__ == "__main__":
    install_k3s()
