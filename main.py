# this is the main file to create the individuals and run the simulation 

# importing libraries 
import csv

class population:
    def __init__(self, freq, domoinant = True):
        if domoinant:
            self.allele_freq_A = freq
        else:
            self.allele_freq_A = 1-freq
        self.allele_freq_a = 1-self.allele_freq_A
        self.genotype_freq_AA = self.allele_freq_A*self.allele_freq_A
        self.genotype_freq_Aa = 2*self.allele_freq_A*self.allele_freq_a
        self.genotype_freq_aa = self.allele_freq_a*self.allele_freq_a
        print ("A -> ", self.allele_freq_A)
        print ("a -> ", self.allele_freq_a)
        print ("Genotype AA -> ", self.genotype_freq_AA)
        print ("Genotype Aa -> ", self.genotype_freq_Aa)
        print ("Genotype aa -> ", self.genotype_freq_aa)

    mean_fitness = 1
    def set_fitness(self, fit_AA, fit_Aa, fit_aa):
        self.mean_fitness = self.genotype_freq_AA*fit_AA + \
                            self.genotype_freq_Aa*fit_Aa + \
                            self.genotype_freq_aa*fit_aa
        print("Mean fitness ", self.mean_fitness)


## MAIN ##        
pop1 = population(0.7, domoinant=False)

# defining generations 
total_generations = 100
fitness_AA = 1
fitness_Aa = 0.4
fitness_aa = 0.2

# opening file to store data


# assinging the fitness values to pop1
pop1.set_fitness(fitness_AA, fitness_Aa, fitness_aa)

# simulating generations
for generation in range(total_generations):
    pop1.genotype_freq_AA = pop1.genotype_freq_AA*fitness_AA
    pop1.genotype_freq_Aa = pop1.genotype_freq_Aa*fitness_Aa
    pop1.genotype_freq_aa = pop1.genotype_freq_aa*fitness_aa
    current_A = (pop1.genotype_freq_AA/pop1.mean_fitness)+(pop1.genotype_freq_Aa/2*pop1.mean_fitness)
    current_a = (pop1.genotype_freq_aa/pop1.mean_fitness)+(pop1.genotype_freq_Aa/2*pop1.mean_fitness)

    data = [generation, current_A, current_a, pop1.genotype_freq_AA, pop1.genotype_freq_Aa, pop1.genotype_freq_aa]
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
    generation = generation+1
