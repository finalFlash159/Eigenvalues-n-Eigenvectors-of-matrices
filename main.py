from src.power_method import power_method
from src.qr_decomposition import qr_algorithm_tridiagonal
import numpy as np

def main():

    # Phương pháp lặp mũ
    print("Power method\n")

    A = np.array([[-4, 14, 0], [-5, 13, 0], [-1, 0, 2]])
    x_0 = np.array([1, 1, 1])
    TOL = 1e-2
    N = 20
    value, vector = power_method(A, x_0, TOL, N)

    print("Trị riêng lớn nhất:", value)
    print("Vector riêng tương ứng:", vector)

    # Phân rã QR
    print("\nQR algorithm\n")

    A = np.array([[3, 1, 0],
              [1, 3, 1],
              [0, 1, 3]], dtype=float)
    TOL = 1e-2
    N = 20
    eigenvalues = qr_algorithm_tridiagonal(A, TOL, N)
    print("Các trị riêng của ma trận A:", eigenvalues)



if __name__ == "__main__":
    main()