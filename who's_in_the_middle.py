w1 = int(input())
w2 = int(input())
w3 = int(input())


if(w1 < w2 and w2 < w3):
    m = w2
elif(w1 < w2 and w2 > w3):
    if(w1 > w3):
        m = w1
    else:
        m = w3
elif(w1 > w2 and w2 < w3):
    if(w1 > w3):
        m = w3
    else:
        m = w1
elif(w1 > w2 and w2 > w3):
    m = w2