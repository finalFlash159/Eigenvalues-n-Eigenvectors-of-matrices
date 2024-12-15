from src.utils import*

def power_method(A, x, TOL=1e-5, N=100):
    """
    Phương pháp lặp mũ để tìm trị riêng và vector riêng của ma trận A.

    Tham số:
        A (ndarray): Ma trận vuông.
        x (ndarray): Vector khởi tạo ban đầu.
        epsilon (float): Sai số hội tụ.
        max_iter (int): Số lần lặp tối đa.

    Trả về:
        (float, ndarray): Giá trị trị riêng lớn nhất và vector riêng tương ứng.
    """
    for i in range(N):
        y = np.dot(A, x)  # Tính tích ma trận A và vector x
        muy = np.linalg.norm(y)  # Chuẩn L2 của vector y
        
        if muy == 0:  # Kiểm tra nếu trị riêng là 0
            print("A has the eigenvalue 0, choose a different vector x and try again.")
            return None, None
        
        # Chuẩn hóa vector y và tính sai số
        error = np.linalg.norm(x - y / muy)
        x = y / muy
        
        # Kiểm tra điều kiện hội tụ
        if error < TOL:
            return muy, x
    
    # Trường hợp không hội tụ
    print("Power method did not converge after {} iterations".format(N))
    return None, None