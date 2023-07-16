def to_rna(dna_strand):
    
    dna_chain = "GCTA"
    rna_chain = "CGAU"

    rna_strand = ""
    for nucleotid in dna_strand:
        index = dna_chain.index(nucleotid)
        rna_strand = rna_strand + rna_chain[index]

    return rna_strand

print(to_rna(""))               # ""
print(to_rna("C"))              # "G"
print(to_rna("G"))              # "C"
print(to_rna("T"))              # "A"
print(to_rna("A"))              # "U"
print(to_rna("ACGTGGTCTTAA"))   # "UGCACCAGAAUU"