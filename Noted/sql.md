# MySQL
## Index
### 1. Normal index (chỉ mục thông thường) or Single column Index
      => Normal Index
      => CREATE INDEX idx_username ON users(username);
### 2. Unique Index ( Chỉ mục duy nhất)
      => Unique Index
      => CREATE UNIQUE INDEX idx_email ON users(email);
### 3. Primary key Index (chỉ mục khóa chính)
     => Primary key Index
     => PRIMARY KEY (id)
### 4. Full Text Index ( Chỉ mục toàn văn)
    => FULLTEXT Index
    => CREATE FULLTEXT INDEX idx_fulltext_username ON  users(username);
### 5. Composite Index ( Chỉ mục tổng hợp) - Nguyên tắc sử dụng
    => CREATE INDEX idx_username_email ON users(username, email);
    => Quy tắc ngoài cùng bên trái
    => Type 
          - all: Tất cả toàn bộ truy vấn hoặc chỉ mục không hợp lệ 
          - system: một phần dữ liệu trong bảng được truy vấn
          - const: cho biết các truy vấn hiện tại được thực hiện có thể sử dụng index
          - range:
          - ref: 
          - index: chỉ mục phụ đang sử dụng
      => Tuyệt chiêu sắp xếp INDEX : 
          - Trường nào giống nhau nhiều về giá trị không nên dùng index
          - Công thức đặt trường nào bên trái, trường nào bên phải.
            Select
                  count(DISTINCT coloumn1)/ count(1) as column1_cnt ,
                  count(DISTINCT column2)/count(1) as column2_cnt
            from table;
            => số nào cao thì nằm ngoài cùng bên trái.
          
### cách chọn chỉ mục hợp lệ: 
