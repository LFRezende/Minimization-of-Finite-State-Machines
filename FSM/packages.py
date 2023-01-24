from random import sample
from math import factorial as f, log2


def arrange(n, p):
    a = f(n)/(f(n-p))
    return int(a)


def combination(n, p):
    c = arrange(n, p)/f(p)
    return int(c)


def signal():
    '''
    Produces all of the possible bit combinations for the inputs.
    LFRezende - Instituto Tecnológico de Aeronáutica, ELE-24
    :return: indexes:
    '''
    logsign = int(input('Type in the number of inputs.'))
    signals = 2**logsign
    indexes = []
    index = ''
    for v in range(0, logsign + 1):
        count = 0
        index = '0'*(logsign - v) + '1'* v
        while True:
            index = ''.join(sample(index, len(index)))
            if index not in indexes:
                indexes.append(index)
                count += 1
            if count == combination(logsign, v):
                break
        indexes = sorted(indexes)
    return indexes


def states():
    '''
    Receives a .txt file for state manipulation and creation of the minimization table.
    LFRezende, Instituto Tecnológico de Aeronáutica, ELE-24.
    :return:
    '''
    ns = int(input('How many states does your finite states machine has?'))
    data = str(input('Type in the name of the text file (no .txt) which contains the stable states table'))
    data = data + '.txt'
    nbits = log2(ns)
    arq = open(data, 'rt')
    table = []
    for v in arq:
        next_states = v.split(';')
        for k, x in enumerate(next_states):
            if '\n' in x:
                next_states[k] = x.replace('\n', '')
        table.append(next_states)
    print(table)
    arq.close()
    return table


def compatibility(table):
    compatible = []
    hold = []
    # First roller through the states table
    for n, state in enumerate(table):
        # Second roller through the states table, for comparing
        for k, v in enumerate(table):
            if n < k: # Correction: For not repeating loops.
                # If the states are identical, they're immediately compatible.
                if state[1:] == v[1:]:
                    compatible.append([state[0], v[0]])
                # Otherwise, we need to re-study the system.
                else:
                    for key, letter in enumerate(state[1:]):
                        # For every discrepancy of states, it needs to be accounted.
                        if state[1:][key] != v[1:][key]:
                            # Pair of states are "hung" because of "this" combination.
                            hold.append([f'{state[0]} to {v[0]}', f'{state[1:][key]} - {v[1:][key]}'])
    # Eliminating double representations on hold.
    hold = noDoubles(hold)[:]
    print(hold)
    #hold = pairToDependents(hold)[:]
    print(hold)
    return hold, compatible


def noDoubles(hold):
    newhold = []
    for v in hold:
        if v not in newhold:
            newhold.append(v)
    return newhold


# PRECISAMOS CONSERTAR ******
def pairToDependents2(hold):
    newhold = []
    for key, element in enumerate(hold):
        newhold.append([element[0], ''])
        for k, v in enumerate(hold):
            if v[0] == element[0] and v[1] != element[1]:
                newhold[key][1] += (element[1] + ' ')
    return newhold

def writeCompatible(hold, compatible):
    arq_h = open('hold.txt', 'wt+')
    arq_c = open('compatible.txt',  'wt+')
    arq_h.write('--- Compatible State-Pair Table ---\n')
    for v in hold:
        arq_h.write(f'{v[0]} --> ({v[1]})\n')
    for v in compatible:
        arq_c.write(f'{v[0]} is compatible to {v[1]}\n')


'''
def bitDiff(indexes):

    Reorganizes crescent bit list into 1 bit differentials, for Karnaugh Map usability.
    This function assumes indexes already ordered, crescent form.
    LFRezende - Instituto Tecnológico de Aeronáutica, ELE-24
    :param indexes:
    :return:

    l = len(indexes)
    kMap = []
    for k in range(0, l):
        i1 = ''
        i2 = ''
        if k % 4 == 2:
            if indexes[k] not in kMap:
                i1 = indexes[k]
                i2 = indexes[k+1]
                kMap.append(i2)
                kMap.append(i1)
        else:
            if indexes[k] not in kMap:
                kMap.append(indexes[k])
    print(kMap)


def bitDiff2(indexes):

    Reorganizes crescent bit list into 1 bit differentials, for Karnaugh Map usability.
    This function assumes indexes already ordered, crescent form.
    LFRezende - Instituto Tecnológico de Aeronáutica, ELE-24
    :param indexes:
    :return:
    '''
