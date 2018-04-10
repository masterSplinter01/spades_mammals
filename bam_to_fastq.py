import pysam
samfile = pysam.AlignmentFile("sorted_mapped.bam", "rb")
for read in samfile.fetch(until_eof=True): 
        print len((read.query_qualities))
        print len("".join((chr(x + 33) for x in read.query_qualities)))
