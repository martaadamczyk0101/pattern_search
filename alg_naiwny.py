#algorytm naiwny

tekst = "wyszukiwanie wzorca nie nie nienie"
print("tekst: "+tekst)
wzorzec = "nie"
print("wzorzec: "+wzorzec)
licznik=0
czy=0

for i in range (len(tekst)):
    if tekst[i]==wzorzec[0]:
        g=i+1
        for j in range (1,len(wzorzec)):
            if tekst[g]==wzorzec[j]:
                licznik=licznik+1
                g+=1
            else:
                break
        if licznik+1==len(wzorzec):
            print("pozycja rozpoczynajaca wystapienie wzorca: ", end="" )
            print(i)
            licznik=0
            czy=1

if not czy:
    print("nie znaleziono wzorca")
