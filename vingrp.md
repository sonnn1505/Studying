### Java core:
    -  vòng đời của Java :
        - code/text 
            - ---> Java complier (bytecode)  
              - --> Class loader (load file bytoce lên RAM) 
                - --> Java Verifier ( very file lại Bytecode, đảm bảo file hợp lệ , không có rủi ro bảo mật)
                  - -->Iterprefer (dịch qua mã máy thực hiện chương trình)
    - các thuật ngữ trong Java:
      - Class
        - Object
          - Method
            - Instance Varible
    - Java collection:
      - Array
  
### Array
    - Nhanh
        - Trực tiếp
    - Tập hợp dữ liệu thông tin có cùng kiểu & ở cạnh nhau

        |0|1|2|3|4|5|6|7|8|9|10|
        |4|8|14|18|
        |4byte| --> 32 bit
        |8byte| --> 64 bit
        vị trí [i] = (địa chỉ bắt đầu + i) * 32 bit (4 byte)
    - Nhược điểm :
        - kích thước cố định và có giới hạn
        - Cấp phát liên tục gần nhau --> cần cấp phát bộ nhớ lên tục
        - CR(UD--> thêm xóa ở cuối --> Nhanh)
### LinkList :
    - chứa dữ liệu , 
    - Linh hoạt : 
    - Node( datas, liên kết)


