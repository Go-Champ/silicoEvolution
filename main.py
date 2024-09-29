# this is the main file to create the individuals and run the simulation 

class population:
    def __init__(self, freq_A, freq_a):
        allele_freq_A = freq_A
        allele_freq_a = freq_a
        genotype_freq_AA = allele_freq_A*allele_freq_A
        genotype_freq_Aa = 2*allele_freq_A*allele_freq_a
        genotype_freq_aa = allele_freq_a*allele_freq_a

    def show_freq(self):
        print (genotype_freq_AA)

population(0.7, 0.3)
