import subprocess

proc = subprocess.Popen(['python', '-u', 'Y11-13_SoOswinStockMarket.py'],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        bufsize=1
                        )
f = open('testcase.txt', 'r')
testInput = f.read()
f = open('testoutput.txt', 'r')
testOutput = f.read().split()
f.close()
stdoutdata = proc.communicate(testInput)[0].split()
print(stdoutdata)
print(testOutput)
if(stdoutdata == testOutput):
	print("Correct!")