nt_string = 'GGGGACCACTTTGTACAAGAAAGCTGGGTCTAGCAGTGGCCGGAGGAGGCGAG'
k = 15

mers = []

for i in range(len(nt_string) - k + 1):
    mers.append(nt_string[i:(i+k)])

file = open('kmer_output.fasta', 'w')
for i in range(len(mers)):
    #file.write('>' + 'k_mer ' + i + 'of:' + nt_string + '\n')
    file.write('>k_mer {0} of:{1}\n'.format(i, nt_string))
    file.write(mers[i])
    file.write('\n\n')

file.close()



