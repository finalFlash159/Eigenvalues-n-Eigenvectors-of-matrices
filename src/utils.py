import numpy as np

def max_abs_below_diagonal(A):
    """
    Tính giá trị lớn nhất của trị tuyệt đối các phần tử dưới đường chéo chính
    của ma trận A một cách thủ công.

    Tham số:
        A (ndarray): Ma trận vuông.

    Trả về:
        float: Giá trị lớn nhất của trị tuyệt đối các phần tử dưới đường chéo chính.
    """
    n = A.shape[0]  # Kích thước ma trận
    max_val = 0.0   # Khởi tạo giá trị lớn nhất

    # Duyệt qua tất cả các phần tử dưới đường chéo chính
    for i in range(1, n):           # Bắt đầu từ hàng thứ 1 (dưới đường chéo chính)
        for j in range(i):          # Cột chỉ chạy đến trước đường chéo chính
            if abs(A[i][j]) > max_val:
                max_val = abs(A[i][j])  # Cập nhật giá trị lớn nhất nếu tìm thấy phần tử lớn hơn

    return max_val