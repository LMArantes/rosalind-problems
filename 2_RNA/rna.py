def transcription():
    with open("rosalind_rna.txt", "r") as file:
        dna = file.read().strip()

    rna = dna.replace("T", "U")
    return rna
