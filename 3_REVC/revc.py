def dna_complement():
    base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    with open("rosalind_revc.txt", "r") as file:
        dna = file.read().strip()
        reverse_dna = dna[::-1]

        complement = []
        for nucleotide in reverse_dna:
            complement.append(base_pairs[nucleotide])

    result = ''.join(complement)
    print(result)
    return result
