# 1. API import metadata thay vì scan
# 2. bussiness metadata/ techncial meta data mapping
# 3. access control / permission grant (group)
# 4. data linage
# 5.data classification: PII
# 6. approval workflow (data owner/ data steward)
 

## 3. Sử dụng AWS Glue APIs
### Tạo cơ sở dữ liệu:

import boto3

client = boto3.client('glue')

### Tạo database
response = client.create_database(
    DatabaseInput={
        'Name': 'my_database',
        'Description': 'My database description'
    }
)


### Tạo table:

response = client.create_table(
    DatabaseName='my_database',
    TableInput={
        'Name': 'my_table',
        'StorageDescriptor': {
            'Columns': [
                {'Name': 'column1', 'Type': 'string'},
                {'Name': 'column2', 'Type': 'int'}
            ],
            'Location': 's3://my-bucket/my-folder/'
        }
    }
)

### connection

response = client.create_connection(
    ConnectionInput={
        'Name': 'my_connection',
        'ConnectionType': 'JDBC',
        'ConnectionProperties': {
            'JDBC_CONNECTION_URL': 'jdbc:mysql://my-database-url',
            'USERNAME': 'my-username',
            'PASSWORD': 'my-password'
        }
    }
)
#
