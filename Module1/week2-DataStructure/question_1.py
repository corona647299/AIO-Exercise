from collections import deque


def max_sliding_window(num_list, k):

    result = []
    dq = deque()

    for i in range(len(num_list)):
        # Loại bỏ các phần tử ngoài phạm vi của cửa sổ hiện tại
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Loại bỏ các phần tử có giá trị nhỏ hơn phần tử mới
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()

        # Thêm chỉ số của phần tử hiện tại vào hàng đợi
        dq.append(i)

        # Nếu chỉ số hiện tại đủ để hình thành một cửa sổ, thêm giá trị lớn nhất vào kết quả
        if i >= k - 1:
            result.append(num_list[dq[0]])

    return result


if __name__ == "__main__":

    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3

    print(max_sliding_window(num_list, k))









