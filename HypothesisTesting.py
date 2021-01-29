def combine(p, r):
    h = 1
    m = p-r
    for j in range(m):
        h = h * (p - j) / (j + 1)
    return h

def Count(pr, I, up, po):
    hasil = 1
    qr = 1 - pr
    if I == 0:
        for i in range(po):
            hasil = hasil * qr
        print(I, " ", hasil)
        return hasil
    if I == po:
        for i in range(po):
            hasil = hasil * pr
        print(I, " ", hasil)
        return hasil
    hasil = combine(po, I)
    for i in range(I):
        hasil = hasil * pr
    temp=po-I
    for i in range(temp):
        hasil = hasil * qr
    if up:
        print(I, " ", hasil)
        return hasil + Count(pr, I+1, up, po)
    print(I, " ", hasil)
    return hasil + Count(pr, I-1, up, po)

def OneTail(p, pop, x, s, hi):
    print("X   Probability")
    sum = Count(p, x, hi, pop)
    print("sum", sum)
    sum=int(sum*100000)
    sum=float(sum/1000)
    if sum<s:
        print(sum, "% <", s, "%. Therefore, reject h0 and accept h1")
    else:
        print(sum, "% >", s, "%. Therefore, accept h0 and reject h1")

naik = False
print("\nPlease input p in a per b, N, x, and significant level")
a = int(input("a = "))
b = int(input("b = "))
sample = int(input("N = "))
eks = int(input("X = "))
sl = float(input("significant level (in percent) = "))
prob = float(a/b)
if float(eks/sample)>prob:
    naik=True
OneTail(prob, sample, eks, sl, naik)