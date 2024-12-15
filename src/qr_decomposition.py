from src.utils import*

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

        # Tạo ma trận xoay P (Givens rotation)
        P = np.eye(n)
        P[i-1, i-1] = c
        P[i, i] = c
        P[i-1, i] = s
        P[i, i-1] = -s
        
        # Cập nhật R và Q
        R = P @ R  # Xoay hàng
        R = np.round(R, decimals=10) # do code tự làm tròn lên nên kết quả có thể sẽ là một số rất nhỏ mà không đúng là 0
        Q = Q @ P.T  # Xoay cột tích lũy vào Q
    return Q, R


def qr_algorithm_tridiagonal(A, TOL=1e-2, N=20):
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
    
    # Bước 2: Lặp cho đến khi k > N
    while k <= N:
        # Bước 2.1: Phân rã QR
        Q, R = qr_tridiagonal(Ak)
        
        # Bước 2.2: Cập nhật ma trận A(k) = RQ
        Ak = R @ Q
        
        # Bước 2.3: Tính M là giá trị lớn nhất của các phần tử dưới đường chéo chính
        M = np.max(np.abs(np.tril(Ak, k=-1)))
        
        # Bước 2.4: Kiểm tra điều kiện hội tụ
        if M <= TOL:
            print("Thuật toán hội tụ sau", k, "vòng lặp.")
            return np.diag(Ak)  # Trị riêng là đường chéo chính của Ak
        
        # Bước 2.5: Tăng k
        k += 1
    
    # Bước 3: Thuật toán thất bại
    print("Thuật toán thất bại sau", N, "vòng lặp.")
    return None