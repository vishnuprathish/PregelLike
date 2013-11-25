#convpy.py 
#vish
#    Source format
#	20 Berlin Frankfurt
#	50 Berlin Munich
#	20 Frankfurt Berlin
#	10 Frankfurt Munich
#	 
#
#    Destination Format:
#
#    	Berlin\tFrankfurt:20\tMunich:50
#    	Frankfurt\tBerlin:20\tMunich:10
#    	Munich
import sys



file = open(sys.argv[1]);

Dics=dict()
words=list()

for line in file:
    #print line
    words=line.split()
    if Dics.get(words[1])==None:
        Dics[words[1]]=words[1]+"\t"+str(words[2])+":"+str(words[0])
    else:
        Dics[words[1]]=Dics[words[1]]+"\t"+str(words[2])+":"+str(words[0])
    Dics[words[2]]=words[2]

    
for line in Dics:
    print Dics[line]
