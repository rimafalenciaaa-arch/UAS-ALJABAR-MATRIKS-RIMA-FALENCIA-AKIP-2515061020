def perkalian_matriks(X, Y):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += X[i][k] * Y[k][j]

    return hasil


def transpose(X):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            hasil[j][i] = X[i][j]

    return hasil