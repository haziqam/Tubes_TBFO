Prod = {

}

def CYKParse(w):
    # n adalah banyak simbol terminal yang akan di-parse
    n = len(w)

    # inisialisasi tabel CYK
    Tab = [[set([]) for j in range(n-i)] for i in range(n)]

    # isi baris paling bawah tabel CYK -> basis
    for i in range(n):
        if(isinstance(w[i], list)):
            temp = len(w[i])
            Tab[i][0] = CYKParse(w[i])
        else:
            for l, r in Prod.items():
                for deriv in r:
                    if((len(deriv) == 1) and (deriv[0] == w[i])):
                        Tab[i][0].add(l)    # terminal terdapat dalam produksi, tambahkan variabel produksi

    # pengisian tabel CYK
    for i in range(1,n):
        for j in range(n-i):
            for k in range(i):
                for l, r in Prod.items():
                    for deriv in r:
                        if((len(deriv) == 2) and (deriv[0] in Tab[j][k]) and (deriv[1] in Tab[j+1+k][i-k-1])):
                            Tab[i][j].add(l)

    # Return variabel yang menghasilkan w; V *-> w
    return Tab[0][n-1]