### This file contains examples from week 1

# First, create a string variable called ori that is equal to the Vibrio cholerae ori. Don't forget to enclose your string in quotes!
vibrioCholeraeOri = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

# Then, print the length of ori
print(len(vibrioCholeraeOri))

## Counting words
"ACAACTATGCATACTATCGGGAACTATCCT".count("ACTAT") # => 3
# notice that this solution doesn't work properly in overlapping case
"CGATATATCCATAG".count("ATA") # => 2 (but should return 3!)

# Let's fix the algorithm
# My implementation:
def pattern_count(pattern, text):
    if len(text) < len(pattern):
        return 0

    count = 0
    i = 0
    while i < (len(text) - len(pattern) + 1):
        # start index is inclusive
        substring_start = i
        # end index is exclusive!
        substring_end = i + len(pattern)
        if text[substring_start:substring_end] == pattern:
            print "start: %s, end: %s" % (substring_start, substring_end)
            count = count + 1
        i = i + 1
    return count

pattern_count("ATA", "CGATATATCCATAG") # => 2 (but should return 3!)
