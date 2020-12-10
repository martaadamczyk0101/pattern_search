#algorytm KR

#funkcja hashujaca
def H(wzorzec):
    alfabet={"a":0, "b":1, "c":2, "d":3, "e":4}
    r= 5    #rozmiar alfabetu
    q= 19   #bardzo duza liczba pierwsza
    suma= 0
    n=len(wzorzec)

    for i in range (n):
        key=wzorzec[i]
        suma= suma+ alfabet[key]*pow(r, n-i-1)

    suma=suma%q
    return suma

print("alfabet: a, b, c, d, e")
print("wzorzec: ", end="")
x=input()

print("tekst: ", end="")
tekst=input()

l=len(tekst)
licznik=0
czy=0

for i in range (0, l-len(x)+1):
    if H(tekst[i:i+len(x)]) == H(x):
        for j in range(len(x)):
            if tekst[i+j]==x[j]:
                licznik+=1
        if licznik==len(x):
            print("indeks rozpoczynajacy wystapienie wzorca: ", end="")
            print(i)
            licznik=0
            czy=1
if not czy:
    print("nie znaleziono wzorca w tekscie")
