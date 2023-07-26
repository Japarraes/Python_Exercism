TRASLATION = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine",       "UUG": "Leucine",
    "UCU": "Serine",        "UCC": "Serine",        "UCA": "Serine",    "UCG": "Serine",
    "UAU": "Tyrosine",      "UAC": "Tyrosine",      "UGU": "Cysteine",  "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",          "UAG": "STOP",          "UGA": "STOP",
}

def proteins(strand):
    
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    chain_protein = []
    
    for codon in codons:
        if TRASLATION.get(codon) == "STOP":
            break

        chain_protein.append(TRASLATION.get(codon))

    return chain_protein


# value = "UGG"                   # expected = ["Tryptophan"]
# value = "UGA"                   # expected = []
# value = "UUUUUU"                # expected = ["Phenylalanine", "Phenylalanine"]
# value = "UUAUUG"                # expected = ["Leucine", "Leucine"]
# value = "AUGUUUUGG"             # expected = ["Methionine", "Phenylalanine", "Tryptophan"]
# value = "UAGUGG"                # expected = []
# value = "UGGUAG"                # expected = ["Tryptophan"]
# value = "AUGUUUUAA"             # expected = ["Methionine", "Phenylalanine"]
# value = "UGGUAGUGG"             # expected = ["Tryptophan"]
value = "UGGUGUUAUUAAUGGUUU"    # expected = ["Tryptophan", "Cysteine", "Tyrosine"]
print(proteins(value))