from Bio.SeqIO.QualityIO import FastqGeneralIterator


input_file = "/home/dan/bi(files)/human_chr15/chr15_1.fastq"
id_file = "/home/dan/Dropbox/AU/bi/common.out"
output_file = "/home/dan/bi(files)/paired_chr15_1.fastq"
count = 0


with open(id_file) as id_handle:
    # Taking first word on each line as an identifer
    wanted = set(line.rstrip("\n").split(None,1)[0] for line in id_handle)
print("Found %i unique identifiers in %s" % (len(wanted), id_file))

with open(input_file) as in_handle:
    with open(output_file, "w") as out_handle:
        for title, seq, qual in FastqGeneralIterator(in_handle):
            # The ID is the first word in the title line (after the @ sign):
            if title.split(None, 1)[0] in wanted:
                # This produces a standard 4-line FASTQ entry:
                out_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
                count += 1
print("Saved %i records from %s to %s" % (count, input_file, output_file))
if count < len(wanted):
    print("Warning %i IDs not found in %s" % (len(wanted) - count, input_file))
