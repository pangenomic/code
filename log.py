import math

str = open('p_pacificus.fa', 'r').read() #apre il file
genome = '\n'.join(str.split('\n')[1:])  #toglie l'intestazione del file fasta
l=len(genome)

LOG=math.log(l,4)  #log in base 4
print(LOG)
