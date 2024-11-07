import boto3
import json

# Khởi tạo client cho AWS Glue
glue_client = boto3.client('glue', region_name='us-west-2')  # Thay đổi thành vùng của bạn

def create_database(database_name):
    try:
        response = glue_client.create_database(
            DatabaseInput={
                'Name': database_name,
                'Description': 'Database cho dữ liệu từ Lambda function'
            }
        )
        print(f"Tạo database '{database_name}' thành công.")
        return response
    except glue_client.exceptions.AlreadyExistsException:
        print(f"Database '{database_name}' đã tồn tại.")

def create_table(database_name, table_name):
    try:
        response = glue_client.create_table(
            DatabaseName=database_name,
            TableInput={
                'Name': table_name,
                'Description': 'Table chứa metadata dữ liệu của bạn',
                'StorageDescriptor': {
                    'Columns': [
                        {'Name': 'id', 'Type': 'int'},
                        {'Name': 'name', 'Type': 'string'},
                        {'Name': 'age', 'Type': 'int'}
                    ],
                    'Location': 's3://your-bucket/your-path/',  # Thay đổi thành đường dẫn S3 của bạn
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        'Parameters': {
                            'field.delim': ','
                        }
                    }
                },
                'TableType': 'EXTERNAL_TABLE'
            }
        )
        print(f"Tạo table '{table_name}' thành công.")
        return response
    except glue_client.exceptions.AlreadyExistsException:
        print(f"Table '{table_name}' đã tồn tại.")



def update_table_properties(database_name, table_name, record_count):
  try:
      # Lấy thông tin bảng hiện tại
      table = glue_client.get_table(DatabaseName=database_name, Name=table_name)
      
      # Cập nhật thuộc tính record_count
      table_input = table['Table']
      table_input['Parameters'] = table_input.get('Parameters', {})
      table_input['Parameters']['record_count'] = str(record_count)  # Chuyển số liệu sang chuỗi

      # Gọi API để cập nhật bảng
      response = glue_client.update_table(
          DatabaseName=database_name,
          TableInput={
              'Name': table_name,
              'StorageDescriptor': table_input['StorageDescriptor'],  # Sao chép cấu hình StorageDescriptor
              'Parameters': table_input['Parameters']
          }
      )
      
      print(f"Updated table properties for '{table_name}' in Glue Data Catalog.")
      
  except glue_client.exceptions.EntityNotFoundException:
      print(f"Table '{table_name}' không tồn tại trong Glue Data Catalog.")
  except Exception as e:
      print(f"Lỗi khi cập nhật Table properties: {e}")

def count_records_from_s3(bucket_name, file_key):
  # Đọc tệp CSV từ S3
  obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
  data = pd.read_csv(obj['Body'])
  return len(data)



def lambda_handler(event, context):
  # Tên database và table
  database_name = 'my_python_database'
  table_name = 'my_table'
  
  # Tạo database và table
  create_database(database_name)
  create_table(database_name, table_name)
  
  return {
      'statusCode': 200,
      'body': json.dumps(f"Database '{database_name}' và Table '{table_name}' đã được tạo hoặc đã tồn tại.")
  }
