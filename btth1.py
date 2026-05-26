
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# * INPUT/OUTPUT:
#   - Input: Thao tác lựa chọn menu (int: 1-5).
#     + Chức năng 1: Username, Title, Description, Hashtags (string).
#     + Chức năng 3: Hashtag cần kiểm tra (string).
#     + Chức năng 4: Từ khóa tìm kiếm và từ khóa thay thế (string).
#   - Output: Thông tin video đã xử lý, kết quả chuẩn hóa/kiểm tra/thay thế hoặc thông báo lỗi tương ứng.

# * ĐỀ XUẤT GIẢI PHÁP:
#   - Sử dụng vòng lặp `while True` và cấu trúc `match-case` để điều hướng menu.
#   - Sử dụng các phương thức xử lý chuỗi: `.strip()`, `.split()`, `.title()`, `.lower()`, `.upper()`, `.replace()`, `.count()`, `.isalnum()`, `len()`.
#   - Ràng buộc logic: Kiểm tra rỗng bằng `.strip()`, kiểm tra thứ tự thực hiện hàm (chức năng 2, 4 yêu cầu chức năng 1 chạy trước).

# * THIẾT KẾ THUẬT TOÁN :
#   Khởi tạo biến toàn cục (username, title, description, hashtags_list)
#   Vòng lặp vô hạn:
#       Hiển thị MENU -> Nhập choice
#       Chọn choice:
#           Case 1: Nhập data -> Nếu trống thì báo lỗi & `continue` -> Xử lý & in chuỗi theo định dạng.
#           Case 2: Nếu chưa có username -> Báo lỗi. Ngược lại -> Thêm '@' + viết thường username.
#           Case 3: Nhập hashtag -> Kiểm tra điều kiện (rỗng, bắt đầu '#', khoảng trắng, độ dài, ký tự đặc biệt) -> Hợp lệ thì thêm vào list.
#           Case 4: Nếu chưa có description -> Báo lỗi. Ngược lại -> Nhập từ khóa -> Kiểm tra tồn tại bằng `in` -> Thay thế và đếm số lần xuất hiện.
#           Case 5: In thông báo thoát -> `break`.
#           Case khác: Báo lỗi nhập lại.


# (2) Triển khai code
username = ""
title = ""
description = ""
hashtags_list = []

while True:
    print("+==============================================+")
    print("|          HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK    |")
    print("+==============================================+")
    print("|  1. Nhập và phân tích thông tin video        |")
    print("|  2. Chuẩn hóa tên tài khoản                  |")
    print("|  3. Kiểm tra tính hợp lệ của hashtag         |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong mô tả |")
    print("|  5. Thoát chương trình                       |")
    print("+==============================================+")
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    match choice:
        case '1':
            raw_username = input("Nhập tên tài khoản: ")
            raw_title = input("Nhập tiêu đề video: ")
            raw_description = input("Nhập mô tả video: ")
            raw_hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            
            if not raw_username.strip():
                print("Tên tài khoản không được rỗng")
                continue
            if not raw_description.strip():
                print("Mô tả video không được rỗng")
                continue
            
            username = raw_username.strip()
            title = raw_title.strip()
            description = raw_description.strip()
            hashtags_list = []
            for i in raw_hashtags.split(","):
                clean_h = i.strip()
                if clean_h != '':
                    hashtags_list.append(clean_h)
            
            print("+==============================================+")
            print(f"- Tên tài khoản (loại bỏ khoảng trắng): {username}")
            print(f"- Tiêu đề chuẩn hóa (viết hoa chữ đầu): {title.title()}")
            print(f"- Mô tả video: '{description}'")
            print(f"- Độ dài mô tả video: {len(description)} ký tự")
            print(f"- Số lượng từ trong mô tả: {len(description.split())} từ")
            print(f"- Danh sách hashtag: {hashtags_list}")
            print(f"- Số lượng hashtag: {len(hashtags_list)}")
            print(f"- Mô tả dạng chữ thường: {description.lower()}")
            print(f"- Mô tả dạng chữ hoa: {description.upper()}")
            print("+==============================================+")
            
        case '2':
            if not username:
                print("Cảnh báo: Vui lòng thực hiện Chức năng 1 để nhập dữ liệu trước.")
                continue
            normalized_username = f'@{username.lower()}'
            print("+==============================================+")
            print(f"- Tên tài khoản ban đầu: {username}")
            print(f"- Tên tài khoản sau chuẩn hóa: {normalized_username}")
            print("+==============================================+")
            
        case '3':
            if not username:
                print("Cảnh báo: Vui lòng thực hiện Chức năng 1 trước khi quản lý hashtag.")
                continue
                
            test_hashtag = input("Nhập một hashtag: ").strip()
            if test_hashtag == '':
                print("Hashtag không được rỗng")
            elif test_hashtag[0] != "#":
                print("Hashtag phải bắt đầu bằng ký tự #")
            elif " " in test_hashtag:
                print("Hashtag không được chứa khoảng trắng")
            elif len(test_hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
            else:
                body_hashtag = test_hashtag[1:]
                if not body_hashtag.replace('_', 'a').isalnum():
                    print("Thất bại: Hashtag chỉ được dùng chữ cái, chữ số hoặc dấu gạch dưới!")
                else:
                    print("Thông báo: Hashtag hợp lệ!")
                    hashtags_list.append(test_hashtag)
                    print(f"-> Đã thêm vào danh sách thành công. Danh sách hiện tại: {hashtags_list}")
                    
        case '4':
            if not description:
                print("Cảnh báo: Vui lòng thực hiện Chức năng 1 để nhập mô tả video trước.")
                continue
            search_keyword = input("Nhập từ khóa cần tìm: ")
            replace_keyword = input("Nhập từ khóa thay thế: ")
            
            if search_keyword in description:
                count_appearances = description.count(search_keyword)
                description = description.replace(search_keyword, replace_keyword)
                print("\n --- KẾT QUẢ THAY THẾ ---")
                print(f"- Mô tả video sau khi thay thế: {description}")
                print(f"- Số lần xuất hiện và đã thay thế: {count_appearances} lần")
            else:
                print(f"Thông báo: Không tìm thấy từ khóa '{search_keyword}' trong mô tả.")
                
        case '5':
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ, yêu cầu nhập lại từ 1 đến 5!")