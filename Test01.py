import subprocess
import pandas as pd
syn = str('EK 100 '+'N10R20P60S5.txt')

p = subprocess.Popen(syn, stdout= subprocess.PIPE, shell=True)
#Run the compiled code (commands)
output,err = p.communicate()#output of run command
output = output.decode('utf-8')
output = output.splitlines()
print(output)
out_code_list = []
for line in output:
    out_code_list.append(float(line))
print(out_code_list)
'''for line in output:
    out_code_list.append(line)
print(out_code_list)
maximum_flow = float(out_code_list[0])
CPU_time = float(out_code_list[3])
out_code_list = [maximum_flow,CPU_time] #make a list of returns'''
