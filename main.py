import Rima020

print("Masukkan Matriks X")
X = [list(map(float, input().split())) for _ in range(3)]

print("Masukkan Matriks Y")
Y = [list(map(float, input().split())) for _ in range(3)]

print("\n1. Perkalian Matriks")
print("2. Transpose Matriks")

pilih = input("Pilih menu: ")

if pilih == "1":
    print("\nHasil Perkalian:")
    print(Rima020.perkalian_matriks(X, Y))

elif pilih == "2":
    print("\nHasil Transpose:")
    print(Rima020.transpose(X))

else:
    print("Pilihan tidak valid")