# Kiến trúc SQL Server

## Các Database khi tạo ra

### System Database
- Lưu trữ system catalog
- Thông tin cấu hình
- Thông tin các database trên instance
- Thông tin Data file
- Dữ liệu nằm ở resource database

### Model Database
- Đây là template để tạo database mới.

### TempDB Database
- Được tạo ra mỗi khi database khởi động
- Không cần recovery
- Không cần backup
- Phụ vụ chứa Temp Table
- Các công việc cần sử dụng dữ liệu tạm như SORT
- Tối ưu TEMDB thế nào
  - Tạo nhiều Temp
  - Mặc định SQL server chỉ tạo 1 Temp file, việc này gây ra nghẽn về IO
  - Ưu tiên đặt ở phân vùng có tốc độ đọc ghi cao nhất
  - Temp Table cũng có thể tối ưu bằng Index

### MSDB
- Sử dụng cho SQL server Agent service
- Sử dụng cho các service khác trong quản trị
- Ví dụ
  - Cấu hình scheduler
  - Cấu hình log shipping
  - Cấu hình Database email

### Database "Ẩn" resource Database
- Bản chất ở đây là nơi chứa các system object
- Các file store procedure, function
- DBD = 32767
- Kiểm tra xem database này lưu ở đâu
  - `SELECT 'ResourceDB' As 'Database Name', NAME as Database file, FILENAME As Database file location' FROM sys.sysatifies WHERE DBB = 3267`
- Kết quả sau khi chạy câu lệnh trên.

## Điều gì cần lưu ý
- Lưu ý thiết kế TEMPDB
- Vấn đề thường xuất hiện trong các dự án chuyển đổi
  - Chuyển database sang SQL server instance khác
  - Một số object của database cũ được lưu ở mục database instance nên không chuyển theo được khi chúng ta chuyển ở mục database
    - Login
    - Link server
    - Jobs

## Dữ liệu lưu vào đâu

### Data file
- .MDF File (Master Database file)
  - Đây là file chứa thông tin
  - Chứa thông tin INTERNAL CONFIGURATION
  - Chứa thông tin INTERNAL SYSTEM
  - Chứa thông tin vị trí đến các data file khác
  - Bắt buộc có
- .NDF File (Secondary Database File)
  - Có thể có hoặc không
  - Các data file tạo mới thì đều tính là .NDF File

### Cần lưu ý
- Nếu muốn nhóm các File theo một Logic lại với nhau
  - Filegroup
  - Mặc định hệ thống tạo ra PRIMARY FILEGROUP
    - Chứa Master Data File
  - Chúng ta có thể tự tạo ra các FILEGROUP mới
    - Khuyến cáo sử dụng với hệ thống có dữ liệu lớn
    - Sử dụng trong chiến lược quy hoạch vòng đời dữ liệu
  - Lựa chọn Default FILEGROUP
    - Không nên lưu vào PRIMARY FileGroup

### Transaction Log (phục vụ cho việc khôi phục khi có sự cố)
- Cần lưu ý
  - Chiến lược backup transaction log
