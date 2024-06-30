import subprocess

cmd = "ls"
option = "-lh"
directory = input("Enter the dir path:")

args = []
args.append(cmd)
args.append(option)

for d in directory.split():
    args.append(d)

output = subprocess.run(args, capture_output=True)
print('-------------------')
print('Return code: ', output.returncode)
print('Output:\n', output.stdout.decode("utf-8"))