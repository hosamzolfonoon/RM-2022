import pandas as pd
import numpy as np


file_names = ['Dinic N1000 P70 Rdif', 'EK N1000 P70 Rdif', 'MPM N1000 P70 Rdif', 'Dinic N1000 Pdif R800', 'EK N1000 Pdif R800', 'MPM N1000 Pdif R800', 'Dinic Ndif P70 R800', 'EK Ndif P70 R800', 'MPM Ndif P70 R800']
address = "csv_data<-read.csv('C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\"
# Reading files

file_1 = open("Linear Coefficient.txt","w")
for item in file_names[0:3]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Max_Capacity, data = csv_data))$coefficients[1,1]' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Max_Capacity, data = csv_data))$coefficients[2,1]' + '\n')

for item in file_names[3:6]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Prob_Arc, data = csv_data))$coefficients[1,1]' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Prob_Arc, data = csv_data))$coefficients[2,1]' + '\n')

for item in file_names[-3:]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Num_Vertices, data = csv_data))$coefficients[1,1]' + '\n')
    file_1.write('summary(lm(csv_data$Max_Flow~csv_data$Num_Vertices, data = csv_data))$coefficients[2,1]' + '\n')

file_1.close()
