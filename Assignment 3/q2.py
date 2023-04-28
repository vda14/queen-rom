window = []
n = int(input(""))
for i in range(n):
    w = int(input(""))
    window = window + [w]

def maxsubsum(window):
    sumlist = []
    for i in range(len(window)):
        for j in range(i, len(window)):
            sumlist.append(sum(window[i:j+1]))
    return max(sumlist)
            
print(maxsubsum(window))
