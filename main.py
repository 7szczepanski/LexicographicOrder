'''

Created by Mateusz Szczepanski 19.04.2017
    Lexicographic Order

'''

vals = [0,1,2,3,4,5]
finished = False

def swap(array,i, j):
    temp = array[i]
    array[i]=array[j]
    array[j] = temp

while finished==False:
    print (vals)
    largestI = -1
    for i in range(len(vals)-1):
        if(vals[i]<vals[i+1]):
            largestI = i

    if largestI == -1:
        finished = True

    largestJ = -1
    for j in range(0,len(vals)):
        if (vals[largestI]<vals[j]):
            largestJ = j

    swap(vals,largestI,largestJ)

    endArray = vals[largestI+1:]
    endArray.reverse()
    for en in endArray:
        vals.pop()
    vals = vals+endArray

