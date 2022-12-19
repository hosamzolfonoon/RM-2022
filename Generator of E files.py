#import os
#os.system('code1 31235 100 21E50P20.in')

import subprocess
import pandas as pd

seeds = 1972
def out_code(file_name):
    syn = str(file_name) # ***
    p = subprocess.Popen(syn, stdout= subprocess.PIPE, shell=True)
    #Run the compiled code (commands)
    output,err = p.communicate()#output of run command
    output = output.decode('utf-8')
    output = output.splitlines()
    out_code_list = []
    print(output)

    for line in output:
        out_code_list.append(float(line))
    maximum_flow = out_code_list[0]
    CPU_time = out_code_list[1]
    out_code_list = [maximum_flow,CPU_time] #make a list of returns
    print('out_code_list: ', out_code_list)
    return out_code_list

#df = pd.DataFrame(columns=['time_slot','proc_time'])
'''for n in range(100,501,100):
    for p in range(20,101,20):
        df = pd.DataFrame(columns=['Num_Vertices','Prob_Arc','Max_Capacity','Max_Flow','CPU_time'])
        for r in range(100,201,20):
            file_name = 'N'+str(n)+'P'+str(p)+'R'+str(r)+'S'+str(seeds)+'.txt'
            print(file_name)
            ou=out_code(file_name)            
            df_help = pd.DataFrame({'Num_Vertices':[n],'Prob_Arc':[p],'Max_Capacity':[r],'Max_Flow':[ou[0]],'CPU_time':[ou[1]]})
            df = pd.concat([df,df_help], ignore_index=True)
        file_name_csv = 'Dinic N'+str(n)+'P'+str(p)+'.csv'
        df.to_csv(file_name_csv)
        print(df)'''
df = pd.DataFrame(columns=['Num_Vertices','Prob_Arc','Max_Capacity','Max_Flow','CPU_time'])
List_Commands = ['EK 100 ', 'MPM 100 ', 'Dinic 100 ' ]
for item in List_Commands:
    df = pd.DataFrame(columns=['Num_Vertices','Prob_Arc','Max_Capacity','Max_Flow','CPU_time'])
    for n in range(200,1001,200):
        file_name = str(item) +'N'+str(n)+'P'+str(70)+'R'+str(800)+'S'+str(seeds)+'.txt' # ***
        print(file_name)
        ou=out_code(file_name)            
        df_help = pd.DataFrame({'Num_Vertices':[n],'Prob_Arc':[70],'Max_Capacity':[800],'Max_Flow':[ou[0]],'CPU_time':[ou[1]]}) # ***
        df = pd.concat([df,df_help], ignore_index=True)
    file_name_csv = str(item[:-5])+' Ndif'+' P70'+' R800'+'.csv' # ***
    df.to_csv(file_name_csv)
    print('df-----------',df)
  
