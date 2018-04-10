#!/usr/bin/python

from Bio import SeqIO

f1 = open("outl_test.out", 'w')
f2 = open("outr_test.out", 'w')

for record in SeqIO.parse("/home/dan/bi(files)/paired_chr15_1.fastq", "fastq"):
        f1.write (record.id + "\n")

#for record in SeqIO.parse("/home/dan/bi(files)/paired_chr15_2.fastq", "fastq"):
 #       f2.write(record.id + "\n")