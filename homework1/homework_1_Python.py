def transcribe(sequence):
    if NA_type == 'RNA':
        return ('Error, RNA to RNA transcription is not supported, try again')
    trans_seq = (sequence.replace('T', 'U')).replace('t', 'u')
    return (trans_seq)

def reverse(sequence):
    return (sequence[::-1])

def complement(sequence):
    compl_dic = {'A': 'T', 'T': 'A', 'U': 'A', 'G': 'C', 'C': 'G'}
    compl_seq = ''
    if NA_type == 'RNA':
        compl_dic['A'] = 'U'
    for nucl in sequence:
        if nucl.islower():
            nucl = nucl.upper()
            compl_seq += compl_dic[nucl].lower()
        else:
            compl_seq += compl_dic[nucl]
    return (compl_seq)

def reverse_complement(sec):

    return (reverse(complement(sec)))

functions = {'transcribe':transcribe, 'reverse':reverse,
             'complement':complement, 'reverse complement':rev_com, 'exit':''}

while True:
    print('Type your command here:')
    command = str(input())
    if command not in functions.keys():
        print ('Invalid command, try again.')
        continue
    if command == 'exit':
        print('Good Bye! May Omnissiah directs your footsteps along the path of knowledge.')
        break
    print('Type your sequence here:')
    seq = str(input())
    letters = ['A','T','U','G','C']
    alph_check=seq.upper()
    NA_type = 'DNA'
    if 'U' in alph_check:
        NA_type = 'RNA'
    TU_error = ('T' in alph_check and NA_type == 'RNA')
    for i in letters:
        alph_check = alph_check.replace(i,'')
    if len(alph_check)>0 or TU_error:
        print('Invalid alphabet, try again!')
    else:
        print (functions[command](seq))