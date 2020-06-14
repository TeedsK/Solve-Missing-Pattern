def find_missing(sequence):
    Difference = sequence[2] - sequence[1]
    if sequence[2] - sequence[1] > sequence[1] - sequence[0]:
        Difference = sequence[1] - sequence[0]
    for x in range(1, len(sequence)):
        if sequence[x] - sequence[x-1] != Difference:
            return sequence[x] - Difference
    
        
print(find_missing([3,9]))

