possibilities = {
    'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'], 'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'], 'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'C': ['UGU', 'UGC'],
    'W': ['UGG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG']
}

def isValid(codons):
    return all(amino in possibilities for amino in codons)


def countRNACodons(rna):
    codon_count = {}
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1
    print("Codon Frequencies:")
    for codon, count in codon_count.items():
        print(f"{codon} = {count}")


def recurse(codons, rna=""):
    if not codons:
        countRNACodons(rna)
        return
    for codon in possibilities[codons[0]]:
        recurse(codons[1:], rna + codon)


def main():
    input_amino_acids = input("Enter the amino acid sequence (max 3 amino acids): ")
    if isValid(input_amino_acids):
        recurse(input_amino_acids)
    else:
        print("Invalid input. Please enter valid amino acid symbols.")


main()
