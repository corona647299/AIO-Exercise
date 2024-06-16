import string


def count_words_from_file(file_path):

    word_count = {}

    # Mở tệp và đọc nội dung
    with open(file_path, 'r') as file:
        for line in file:
            # Chuyển thành chữ thường
            line = line.lower()
            # Tách chuỗi thành các từ
            words = line.split()
            # Đếm số lần xuất hiện của từng từ
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1       

    return word_count


if __name__ == "__main__":    
    file_path = r"C:\Users\ADMIN\Downloads\P1_data.txt"
