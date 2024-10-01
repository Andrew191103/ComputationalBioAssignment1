
codon_table = {
    'UUU': ('Phe', 'F'), 'UUC': ('Phe', 'F'), 'UUA': ('Leu', 'L'), 'UUG': ('Leu', 'L'),
    'UCU': ('Ser', 'S'), 'UCC': ('Ser', 'S'), 'UCA': ('Ser', 'S'), 'UCG': ('Ser', 'S'),
    'UAU': ('Tyr', 'Y'), 'UAC': ('Tyr', 'Y'), 'UAA': ('Stop', 'Stop'), 'UAG': ('Stop', 'Stop'),
    'UGU': ('Cys', 'C'), 'UGC': ('Cys', 'C'), 'UGA': ('Stop', 'Stop'), 'UGG': ('Trp', 'W'),
    'CUU': ('Leu', 'L'), 'CUC': ('Leu', 'L'), 'CUA': ('Leu', 'L'), 'CUG': ('Leu', 'L'),
    'CCU': ('Pro', 'P'), 'CCC': ('Pro', 'P'), 'CCA': ('Pro', 'P'), 'CCG': ('Pro', 'P'),
    'CAU': ('His', 'H'), 'CAC': ('His', 'H'), 'CAA': ('Gln', 'Q'), 'CAG': ('Gln', 'Q'),
    'CGU': ('Arg', 'R'), 'CGC': ('Arg', 'R'), 'CGA': ('Arg', 'R'), 'CGG': ('Arg', 'R'),
    'AUU': ('Ile', 'I'), 'AUC': ('Ile', 'I'), 'AUA': ('Ile', 'I'), 'AUG': ('Met', 'M'),
    'ACU': ('Thr', 'T'), 'ACC': ('Thr', 'T'), 'ACA': ('Thr', 'T'), 'ACG': ('Thr', 'T'),
    'AAU': ('Asn', 'N'), 'AAC': ('Asn', 'N'), 'AAA': ('Lys', 'K'), 'AAG': ('Lys', 'K'),
    'AGU': ('Ser', 'S'), 'AGC': ('Ser', 'S'), 'AGA': ('Arg', 'R'), 'AGG': ('Arg', 'R'),
    'GUU': ('Val', 'V'), 'GUC': ('Val', 'V'), 'GUA': ('Val', 'V'), 'GUG': ('Val', 'V'),
    'GCU': ('Ala', 'A'), 'GCC': ('Ala', 'A'), 'GCA': ('Ala', 'A'), 'GCG': ('Ala', 'A'),
    'GAU': ('Asp', 'D'), 'GAC': ('Asp', 'D'), 'GAA': ('Glu', 'E'), 'GAG': ('Glu', 'E'),
    'GGU': ('Gly', 'G'), 'GGC': ('Gly', 'G'), 'GGA': ('Gly', 'G'), 'GGG': ('Gly', 'G')
}


def isValid(dna):
    return all(base in 'ATCG' for base in dna) and len(dna) % 3 == 0


def complement(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_map[base] for base in dna)


def toMrna(dna):
    return dna.replace('T', 'U')


def toAminoAcid(mrna):
    amino_acids = []
    for i in range(0, len(mrna), 3):
        codon = mrna[i:i+3]
        if codon_table[codon][1] == 'Stop':
            break
        amino_acids.append(f"{codon_table[codon][0]} ({codon_table[codon][1]})")
    return ' - '.join(amino_acids)


def showStepsToAminoAcid(dna):
    if not isValid(dna):
        return "Invalid DNA sequence. Please provide a sequence that is a multiple of 3 and contains only 'A', 'T', 'C', 'G'."
    
    complement_dna = complement(dna)
    mrna = toMrna(complement_dna)
    amino_acids = toAminoAcid(mrna)
    
    print(f"Input DNA = {dna}")
    print(f"Complement = {complement_dna}")
    print(f"mRNA = {mrna}")
    print(f"Amino Acid = {amino_acids}")


dna_sequence = input("Input a valid DNA sequence: ").strip()


showStepsToAminoAcid(dna_sequence)
