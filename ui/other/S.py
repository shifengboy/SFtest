import subprocess

# code, re = subprocess.getstatusoutput('dir')
#
# print(re)
# print(code)

s = subprocess.Popen('python', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
s.stdin.write(b'print(1123123) \n')
out, erro = s.communicate()
print(out)
subprocess.run()