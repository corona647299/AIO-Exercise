def levenshtein_distance(s, t):
    # Khởi tạo bảng lưu kết quả, ban đầu toàn là 0
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    # Khởi tạo giá trị ban đầu cho trường hợp cơ sở (khoảng cách của chuỗi rỗng)
    for i in range(len(s) + 1):
        dp[i][0] = i
    for j in range(len(t) + 1):
        dp[0][j] = j
    
    # Tính toán khoảng cách Levenshtein
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,        # Xoá một ký tự từ chuỗi s
                           dp[i][j - 1] + 1,        # Thêm một ký tự vào chuỗi s
                           dp[i - 1][j - 1] + substitution_cost)  # Thay thế một ký tự

    # Trả về khoảng cách Levenshtein giữa hai chuỗi
    return dp[len(s)][len(t)]
\
if __name__ == "__main__":
    # Ví dụ 
    s1 = "yu"
    s2 = "you"
    print(f"Levenshtein distance between '{s1}' and '{s2}' is: {levenshtein_distance(s1, s2)}")