matrice=[]
n=int(input('introdu nuumarul de linii (2<=n<=10):'))
if ((n>=2)and(n<=10)):
    print("introdu elementele matricei:")
    for linie in range(0,n):
        linie=[]
        for element in range(0,n):
            element=int(input())
            linie.append(element)
        matrice.append(linie)
    print(matrice)
    d_principala=[]
    d_secundara=[]
    msus_principala=[]
    mjos_principala=[]
    msus_secundara=[]
    mjos_secundara=[]
    for i in range(len(matrice)):
        for k in range(len(matrice[0])):
            if i==k:
                d_principala.append(matrice[i][k])
            if(i+k)==(len(matrice)-1):
                d_secundara.append(matrice[i][k])
            if i<k:
                msus_principala.append(matrice[i][k])
            if i>k:
                mjos_principala.append(matrice[i][k])
            if (i+k)<(len(matrice)-1):
                msus_secundara.append(matrice[i][k])
            if (i+k)>(len(matrice)-1):
                mjos_secundara.append(matrice[i][k])
    print('suma elementelor diagonale principale=',sum(d_principala))
    print('suma elementelor diagonale secundare=',sum(d_secundara))
    print('suma elementelor mai sus de diagonala principala=',sum(msus_principala))
    print('suma elementelor mai jos de diagonala principala=',sum(mjos_principala))
    print('suma elementelor mai sus de diagonala secundara=',sum(msus_secundara))
    print('suma elementelor mai jos de diagonala secundara=',sum(mjos_secundara))


    