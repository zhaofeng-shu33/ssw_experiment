import time,datetime,os

def timer():
    return datetime.datetime.now().strftime('%H:%M:%S.%f') #%Z %Y.%m.%d %H:%M:%S

f=open('log.txt','w')
f.write(timer())
f.write("\n")

count=0
for i in range(1,42):
    for j in range(i,42):
        cmd="./ssw_test -pl proteinPartitions/partition%d.fasta proteinPartitions/partition%d.fasta  ./BLOSUM62 -o 10 -e 1"%(i,j)
        f.write("run partition%d.fasta partition%d.fasta"%(i,j))
        output=os.popen(cmd)
        print(output.read().strip())
        count+=1
        f.write(timer())
        f.write("\n")
f.write("Finish\n")
f.write(timer())
f.write("\n")
f.close()
print(count)


