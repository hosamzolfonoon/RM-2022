import pandas as pd

file_names = ['Dinic N1000 P70 Rdif', 'EK N1000 P70 Rdif', 'MPM N1000 P70 Rdif', 'Dinic N1000 Pdif R800', 'EK N1000 Pdif R800', 'MPM N1000 Pdif R800', 'Dinic Ndif P70 R800', 'EK Ndif P70 R800', 'MPM Ndif P70 R800']
address = "csv_data<-read.csv('C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\"
# Reading files

file_1 = open("MyFile Residual CPU Reg.txt","w")
for item in file_names[0:3]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\Residual ' + item +'.png")'+ '\n')
    file_1.write('plot(lm(csv_data$CPU_time~csv_data$Max_Capacity, data = csv_data), which=1)'+ '\n')
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

for item in file_names[3:6]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\Residual ' + item +'.png")'+ '\n')
    file_1.write('plot(lm(csv_data$CPU_time~csv_data$Prob_Arc, data = csv_data), which=1)'+ '\n')
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

for item in file_names[-3:]:
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\Residual ' + item +'.png")'+ '\n')
    file_1.write('plot(lm(csv_data$CPU_time~csv_data$Num_Vertice, data = csv_data), which=1)'+ '\n')
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

file_1.close()
