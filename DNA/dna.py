def nucleotides_count():
    with open("DNA/rosalind_dna.txt", "r") as file:
        dna = file.read().strip()
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for nucleotide in dna:
            counts[nucleotide] += 1

    return counts["A"], counts["C"], counts["G"], counts["T"]
