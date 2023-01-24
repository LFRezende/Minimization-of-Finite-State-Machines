from FSM import *
# Assumes crescent binary association with the states in the text file.
# first column: the state.

table = states()
hc = compatibility(table)
writeCompatible(hc[0], hc[1])
'''inputs = signal()
print(inputs)
bitDiff(inputs)'''