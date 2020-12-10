#algorytm BM

s= "wyszukiwanie wzorca"
print("tekst: "+s)
wzorzec= "nie"
print("wzorzec: " +wzorzec)
last= [-1] *26
i= 0
znak= 0

for litera in wzorzec:
    if litera.isalpha():
        znak=int(ord(litera))-97
        last[znak]=i
    i+=1

m= len(wzorzec)
n= len(s)
stop= 1

pp= -1 #pozycja poczatkowa
i= 0

while i<=n-m and stop:
    j=m-1
    while j>-1 and wzorzec[j]==s[i+j]:
        j=j-1
    if j > -1:
            i = i+max(1, j-(last[ord(s[i+j])-97]))
    else:
        pp= i
        print("indeks rozpoczynajacy wystapienie wzorca: ", end="")
        print(pp)
        stop=0
        i=i+1

if pp==-1:
    print("nie znaleziono wzorca w tekscie")
