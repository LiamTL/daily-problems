def DNA_strand(dna):
    better_dna_UwU =""
    for nucleus_part in dna:
        if nucleus_part =="A":
            better_dna_UwU +="T"
            
        elif nucleus_part =="T":
            better_dna_UwU +="A"
            
        elif nucleus_part =="G":
            better_dna_UwU +="C"
            
        elif nucleus_part == "C":
            better_dna_UwU +="G"
            
    return better_dna_UwU