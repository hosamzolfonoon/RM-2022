import pandas as pd

file_names = ['Dinic', 'EK', 'MPM']
x_labels = ['CPU_time', 'Max_Flow']
Nuber_Bins = 5

address = "csv_data<-read.csv('C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\"

file_1 = open("Histogram Codes.txt","w")
for label_1 in x_labels:
    for name_1 in file_names:
        file_1.write(address + name_1 + '.csv'+"'"+')' + '\n')
        file_1.write('png(filename="C:\\\\Users\\\\hosam\\\\Documents\\\\assignment\\\\code\\\\' + name_1 + ' ' + label_1 +'.png")'+ '\n')
        file_1.write('hist(csv_data$'+ label_1 + ', breaks=seq(min(csv_data$'+label_1+'),max(csv_data$'+label_1+'),l=6), col='+"'blue'"+', xlab='+"'"+label_1+"'"+', border='+"'black'"+', prob=TRUE, main = "'+ label_1 + ' Histogram for ' + name_1 + ' Algorithm' + '")'+ '\n')
        file_1.write('lines(density(csv_data$'+ label_1 + '), col = "red", lwd = 2)'+ '\n')
        #file_1.write('hist(csv_data$'+ label_1 + ', breaks=5, col='+"'blue'"+', xlab='+"'"+label_1+"'"+', ylim=c(0,50), border='+"'black'"+', freq=TRUE, main = "'+ label_1 + ' Histogram for ' + name_1 + ' Algorithm' + '")'+ '\n')

        file_1.write('options(scipen=999)'+ '\n')
        file_1.write('dev.off()' + '\n')
        file_1.write('\n')

file_1.close()
