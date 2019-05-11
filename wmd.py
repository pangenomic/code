

def write_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string """
    out=open("k_mers.txt","w")
    for i in range(len(s) - k +1):
        if 'N' not in s[i:i+k]:
            out.write(s[i:i+k])

def get_kmers(s, k):
    """ This function return the set of k-mers that occur in a given string """
    kmers = set()
    for i in range(len(s) - k +1):
        if 'N' not in s[i:i + k]:
            kmers.add(s[i:i+k])
    return kmers

str = open('caeJap1.fa', 'r').read() #apre il file
genome = '\n'.join(str.split('\n')[1:])  #toglie l'indentazione del file fasta
genome=genome.replace('\n', '')
genome=genome.upper()

k=get_kmers(genome, 14)

