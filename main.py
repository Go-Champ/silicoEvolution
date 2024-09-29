# this is the main file to create the individuals and run the simulation 

class population:
    def __init__(self, freq_A, freq_a):
        allele_freq_A = freq_A
        allele_freq_a = freq_a
        genotype_freq_AA = allele_freq_A*allele_freq_A
        genotype_freq_Aa = 2*allele_freq_A*allele_freq_a
        genotype_freq_aa = allele_freq_a*allele_freq_a
        print("A -> ", allele_freq_A, '/n',
            "a -> ", allele_freq_a, '/n',
            "Genotype AA -> ", genotype_freq_AA, '/n,'
            "Genotype Aa -> ", genotype_freq_Aa, '/n,'
            "Genotype aa -> ", genotype_freq_aa)
        
population (0.7, 0.3)