#!/usr/bin/env python3
import subprocess

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell = True, text = True).strip()
    except:
        return f"Error running: {cmd}"

def cpu_info():
    return run("lscpu | grep 'Model name'")

def memory_info():
    return run("free -h")

def disk_info():
    return run("df -h --total | grep total")

def ip_info():
    return run("ip -4 addr show | grep inet")

def uptime():
    return run("uptime -p")

if __name__ == "__main__":
    print("========CPU============================")
    print(cpu_info(), "\n")

    print("=========MEMORY========================")
    print(memory_info(), "\n")

    print("=======DISK============================")
    print(disk_info(),"\n")

    print("=======IP ADDRESS======================")
    print(ip_info(),"\n")

    print("========UPTIME=========================")
    print(uptime(),"\n")


