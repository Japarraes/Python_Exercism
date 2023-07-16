DNA_RNA_TRANSCRIBE = str.maketrans('CGAT', 'GCUA')

def to_rna(dna):
	"""Turns a DNA sequence into an RNA sequence.

	dna (str): the DNA sequence to change. 

	returns: the RNA sequence.  If any non-DNA nucleotides are present, returns the empty
	string instead.
	"""
	if any(c not in 'CGAT' for c in dna):
		return ''
	return dna.translate(DNA_RNA_TRANSCRIBE)


print(to_rna(""))               # ""
print(to_rna("C"))              # "G"
print(to_rna("G"))              # "C"
print(to_rna("T"))              # "A"
print(to_rna("A"))              # "U"
print(to_rna("ACGTGGTCTTAA"))   # "UGCACCAGAAUU"