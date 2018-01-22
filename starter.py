from alignment import alignment

#load genes and make dictionary from gene and they name
inf = open("BioProjectFiles/Marburg_Genes.fasta", "r")
input = inf.read()
lines = input.split("\n")

RNA = ""
gene_name = ""
s = dict()
if lines[0].startswith(">"):
    gene_name = lines[0].replace(">", "").replace("\r", "")

for line in lines:
    line = line.replace('\r', "")
    if line.startswith(">") or line.__len__() == 0:
        if RNA.__len__() > 1:
            s[gene_name] = RNA
            gene_name = line.replace(">", "")
        RNA = ""
    else:
        RNA = RNA + line

inf = open("BioProjectFiles/Bundibugyo_Genome.fasta", "r")
