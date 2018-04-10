#!/usr/bin/python

from Bio import SeqIO

f1 = open("outl.out", 'w')
f2 = open("outr.out", 'w')

for record in SeqIO.parse("/home/dan/bi(files)/human_chr15/chr15_1.fastq", "fastq"):
        f1.write (record.id + "\n")

for record in SeqIO.parse("/home/dan/bi(files)/human_chr15/chr15_2.fastq", "fastq"):
        f2.write(record.id + "\n")

          GNU nano 2.7.1                                                                                  File: length_test.py                                                                                             

from Bio import SeqIO

counter = 0
print (counter)

print("before")
angira = SeqIO.parse("mapped.fastq", "fastq")
print("after")
for record in angira:
        counter += 1
        print(counter)
        if len(record.seq) > len(record.quality):
                print("seq")
        elif len(record.seq) < len(record.quality):
                print("QUALITY")
        else :
                print ("eeeeqqqqqqqqquuuuuuuuuuuuuuuuaaaaaaaaaallllllll")