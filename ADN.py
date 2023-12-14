import sys
import re
import argparse

#Isolement des séquences et des variants à partir du fichier fasta
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

parser = argparse.ArgumentParser(description='Some description.')
#parser.add_argument('--help',help="message d'aide")
parser.add_argument('--match-score',default=1,help="valeur associé quand le variant correspond à la séquence")
parser.add_argument('--mismatch-score',default=-1,help="valeur associé quand le variant ne correspond pas à la séquence")
parser.add_argument('--indel-score',default=-2,help="valeur associé quand il y a une insertion ou un nucléotide manquant")
parser.add_argument('--log-file',default=None,help="chemin pour le fichier")
parser.add_argument('--verbose',default=0,help="niveau de verbeux")
args = parser.parse_args()

#fonction pour remplir le tableau pour une séquence et son variant
def remplir_tableau(seq,var,args):
    tab=[[0 for k in range(len(var))] for k in range(len(seq))]
    chemin=[['' for k in range(len(var))] for k in range(len(seq))]
    for k in range(len(tab)):
        for i in range(len(tab[0])):
            if k==0:
                tab[k][i]=i*args.indel_score
                chemin[k][i]='LEFT'
            elif i==0:
                tab[k][i]=k*args.indel_score
                chemin[k][i]='UP'
            else:
                diag=0
                haut=tab[k-1][i]+args.indel_score
                bas=tab[k][i-1]+args.indel_score
                if seq[k]==var[i]:
                    diag=tab[k-1][i-1]+args.match_score
                else:
                    diag=tab[k-1][i-1]+args.mismatch_score
                tab[k][i]=max(diag,haut,bas)
                if tab[k][i]==diag:
                    chemin[k][i]='DIAG'
                elif tab[k][i]==haut:
                    chemin[k][i]='UP'
                else:
                    chemin[k][i]='LEFT'
    return chemin

def trouver_chemin(chemin):
    l_chemin=[]
    col=-1
    ligne=-1
    while col!=-len(chemin[0])+1 and ligne!=-len(chemin)+1:
        a=chemin[ligne][col]
        l_chemin.append(a)
        if chemin[ligne][col]=='DIAG':
            col-=1
            ligne-=1
        elif chemin[ligne][col]=='UP':
            ligne-=1
        else:
            col-=1
    return l_chemin



def alignement(seq,var,chemin):
    seq_align=seq[-1]
    var_align=var[-1]
    indseq=-1
    indvar=-1
    for k in range(0,len(chemin),-1):
        if chemin[k]=='DIAG':
            indseq-=1
            indvar-=1
            seq_align+=seq[indseq]
            var_align+=var[indvar]
        elif chemin[k]=='UP':
            indseq-=1
            seq_align+=seq[indseq]
            var_align+='-'
        else:
            indvar-=1
            seq_align+='-'
            var_align+=var[indvar]
    print(seq_align,var_align)



