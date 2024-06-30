import subprocess

dmesg_proc = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE, text=True)
grep_proc = subprocess.Popen(["grep", "brd"], stdin=dmesg_proc.stdout, stdout=subprocess.PIPE, text=True)
output, error = grep_proc.communicate()
if error == None:
    if "brd: module loaded" in output:
        print("Found brd module loaded")
    else:
        print("brd module not loaded")
else:
    print("error occurred while running the command")
