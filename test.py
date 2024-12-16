import numpy as np

def qr_tridiagonal(A):
    """
    Phân rã QR cho ma trận đối xứng ba đường chéo A.
    Đầu vào: A - Ma trận đối xứng ba đường chéo (kích thước n x n)
    Đầu ra: Q - Ma trận trực giao, R - Ma trận tam giác trên
    """
    n = A.shape[0]  # Kích thước ma trận A
    Q = np.eye(n)   # Ma trận trực giao ban đầu (ma trận đơn vị)
    R = A.copy()    # Sao chép ma trận A để biến đổi

    for i in range(1, n):
        # Tính toán cos và sin dành cho xoay Givens
        a = R[i-1, i-1]     # Phần tử trên đường chéo
        b = R[i, i-1]       # Phần tử dưới đường chéo (cần triệt tiêu)
        r = np.sqrt(a**2 + b**2)  # Chuẩn hóa
        c = a / r
        s = b / r
        print(f"a{i} = {a}, b{i+1} = {b}, c{i+1} = {c}, s{i+1} = {s}")

        # Tạo ma trận xoay P (Givens rotation)
        P = np.eye(n)
        P[i-1, i-1] = c
        P[i, i] = c
        P[i-1, i] = s
        P[i, i-1] = -s
        print(f"Ma trận xoay P{i+1}:\n{np.round(P, 4)}")
        print (f"Ma trận R{i+1}:\n{ np.round(np.round(P @ R, decimals=10),4)}")
        
        # Cập nhật R và Q
        R = P @ R  # Xoay hàng
        R = np.round(R, decimals=10) # do code tự làm tròn lên nên kết quả có thể sẽ là một số rất nhỏ mà không đúng là 0
        Q = Q @ P.T  # Xoay cột tích lũy vào Q

    print(f"Ma trận Q:\n{np.round(Q,4)}")
    return Q, R, P




def qr_algorithm_tridiagonal(A, TOL=1e-2, N=6):
    """
    Thuật toán QR để tìm các trị riêng của ma trận ba đường chéo đối xứng.

    Tham số:
        A (ndarray): Ma trận đối xứng ba đường chéo.
        TOL (float): Sai số hội tụ.
        N (int): Số vòng lặp tối đa.

    Trả về:
        Các trị riêng của ma trận A hoặc thông báo thuật toán thất bại.
    """
    # Bước 1: Khởi tạo
    k = 1
    Ak = A.copy()  # A(k) = A
    print(f"Ma trận A0 = \n{np.round(Ak, 4)}\n")
    
    # Bước 2: Lặp cho đến khi k > N
    while k <= N:
        print(f"\nLẦN LẶP THỨ {k-1}\n")
        # Bước 2.1: Phân rã QR
        Q, R, _ = qr_tridiagonal(Ak)
        
        # Bước 2.2: Cập nhật ma trận A(k) = RQ
        Ak = R @ Q
        print(f"Ma trận A{k} = \n{np.round(Ak, 4)}\n")
        
        # Bước 2.3: Tính M là giá trị lớn nhất của các phần tử dưới đường chéo chính
        M = np.max(np.abs(np.tril(Ak, k=-1)))
        k += 1
        
    return np.diag(Ak)  # Trị riêng là đường chéo chính của Ak
        

# Ma trận A (test case)
A = np.array([[5, -1, 0, 0, 0],
              [-1, 4.5, 0.2, 0, 0],
              [0, 0.2, 1, -0.4, 1],
              [0, 0, -0.4, 3, 1],
              [0, 0, 0, 1, 3],
              ], dtype=float)


qr_algorithm_tridiagonal(A)