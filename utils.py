import shutil
import subprocess
import sys

# print notices in green
def notice(msg):
    print("\033[32m" + msg + "\033[0m")

# print warnings in yellow
def warning(msg):
    print("\033[33m" + msg + "\033[0m")

# print error in red and exit
def error(msg):
    print("\033[31m" + msg + "\033[0m")
    sys.exit(1)

def verify_command_available(cmd):
    if shutil.which(cmd) == None:
        error(f"the '{cmd}' command was not found, please install it")
    # TODO: do the analog of this in ReleaseTools bash script:
    # command -v curl >/dev/null 2>&1 ||
    #     error "the 'curl' command was not found, please install it"

# check for uncommitted changes
def verify_git_clean():
    res = subprocess.call(["git", "update-index", "--refresh"])
    if res == 0:
        res = subprocess.call(["git", "diff-index", "--quiet", "HEAD", "--"])
    if res != 0:
        error("uncommitted changes detected")

# download file at the given URL to path `dst`
# TODO: check at startup if `curl is present`
def download(url, dst):
    res = subprocess.call(["curl", "-L", "-C", "-", "-o", dst, url])
    if res != 0:
        error('failed downloading ' + url)
