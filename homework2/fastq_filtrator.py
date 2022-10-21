def length_check(read, bounds):
    if bounds == (0, 2 ** 32):
        return True
    length = len(read[1].rstrip('\n'))
    if len(bounds) == 2:
        return (length > bounds[0] and length < bounds[1])
    else:
        return (length < bounds)

def gc_check(seq, gc_bounds):
    if gc_bounds == (0, 100):
        return True
    seq = seq.rstrip('\n').upper()
    GC_count = (seq.count('G') + seq.count('C')) * 100 / len(seq)
    if len(gc_bounds) == 2:
        return (GC_count > gc_bounds[0] and GC_count < gc_bounds[1])
    else:
        return (GC_count < gc_bounds)

def quality_check(read, quality_threshold):
    if quality_threshold == 0:
        return True
    total_phred33 = 0
    for symbol in (read[3].rstrip('\n')):
        total_phred33 += (ord(symbol) - 33)
    mean_quality = total_phred33 / len(read[1])
    return (mean_quality > quality_threshold)

def write_result(read, path):
    with open(path, "a") as res:
        for row in read:
            res.write(row)

def main (input_fastq, output_file_prefix, gc_bounds = (0,100),
    length_bounds = (0, 2**32), quality_threshold = 0, save_filtered=False):
    file_name = input_fastq.split('/')[-1].split('.')[0]
    path_out_succ = output_file_prefix + file_name + '_passed.fastq'
    if save_filtered:
        path_out_fail = output_file_prefix + file_name + '_failed.fastq'
    with open(input_fastq, 'r') as input_f:
        i = 0
        read = []
        for line in input_f:
            read.append(line)
            i += 1
            if i == 4:
                i = 0
                fail = True
                if length_check(read, length_bounds):
                    if gc_check(read[1], gc_bounds):
                        if quality_check(read, quality_threshold):
                            write_result(read, path_out_succ)
                            fail = False
                if (save_filtered and fail):
                    write_result(read, path_out_fail)
                read = []