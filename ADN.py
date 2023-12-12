import sys
import re


seqid=False
varid=False
seq=[]
var=[]
for line in sys.stdin:
    if re.match("[A,T,C,G]+",line) ==None:
        if seqid==True and varid==True:
            seqid,varid=False,False
    else:
        if varid==False:
            if seqid==False:
                seq.append(line.strip())
                seqid=True
            else:
                var.append(line.strip())
                varid=True
        else:
            var[-1]=var[-1]+line.strip()
print(seq,var)

