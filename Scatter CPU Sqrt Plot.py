import pandas as pd

df = pd.read_csv(r'C:\Users\hosam\Documents\assignment\code\Coefficients CPU.csv')
file_names = ['Dinic N1000 P70 Rdif', 'EK N1000 P70 Rdif', 'MPM N1000 P70 Rdif', 'Dinic N1000 Pdif R800', 'EK N1000 Pdif R800', 'MPM N1000 Pdif R800', 'Dinic Ndif P70 R800', 'EK Ndif P70 R800', 'MPM Ndif P70 R800']
address = "csv_data<-read.csv('C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\"
# Reading files
df.set_index('E', inplace=True)

file_1 = open("MyFile Sqrt CPU Reg.txt","w")
for item in file_names[0:3]:
    a = df.loc[item,'a']
    b = df.loc[item,'b']
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\' + item +'.png")'+ '\n')
    file_1.write('plot(x = csv_data$Max_Capacity, y = csv_data$CPU_time, xlab = "Max_Capacity", ylab = "CPU_time", col = "blue", pch = 19, main = "'+ item + '")'+ '\n')
    file_1.write('curve(('+str(a)+'+'+str(b)+'*x)^2, 0, 1100,col ="red", add=TRUE)'+ '\n')   
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

for item in file_names[3:6]:
    a = df.loc[item,'a']
    b = df.loc[item,'b']
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\' + item +'.png")'+ '\n')
    file_1.write('plot(x = csv_data$Prob_Arc, y = csv_data$CPU_time, xlab = "Prob_Arc", ylab = "CPU_time", col = "blue", pch = 19, main = "'+ item + '")'+ '\n')
    file_1.write('curve(('+str(a)+'+'+str(b)+'*x)^2, 0, 100,col ="red", add=TRUE)'+ '\n')   
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

for item in file_names[-3:]:
    a = df.loc[item,'a']
    b = df.loc[item,'b']
    file_1.write(address + item + '.csv'+"'"+')' + '\n')
    file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\' + item +'.png")'+ '\n')
    file_1.write('plot(x = csv_data$Num_Vertices, y = csv_data$CPU_time, xlab = "Num_Vertices", ylab = "CPU_time", col = "blue", pch = 19, main = "'+ item + '")'+ '\n')
    file_1.write('curve(('+str(a)+'+'+str(b)+'*x)^2, 0, 1100,col ="red", add=TRUE)'+ '\n')   
    file_1.write('dev.off()' + '\n')
    file_1.write('\n')

file_1.close()
