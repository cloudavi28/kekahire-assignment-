  - required pyhton script  that reads data from S3 and pushes it to RDS or Glue Database

   python
   import boto3
   import pymysql

   def read_from_s3(bucket_name, file_name):
       s3 = boto3.client('s3')
       response = s3.get_object(Bucket=bucket_name, Key=file_name)
       data = response['Body'].read().decode('utf-8')
       return data

   def push_to_rds(data, rds_endpoint, username, password, database):
       connection = pymysql.connect(host=rds_endpoint,
                                    user=username,
                                    password=password,
                                    database=database)
       cursor = connection.cursor()
       cursor.execute("INSERT INTO your_table (data) VALUES (%s)", (data,))
       connection.commit()
       cursor.close()
       connection.close()

   if __name__ == "__main__":
       bucket_name = 'your-s3-bucket'
       file_name = 'your-file-name'
       rds_endpoint = 'your-rds-endpoint'
       username = 'your-username'
       password = 'your-password'
       database = 'your-database'

       data = read_from_s3(bucket_name, file_name)
       push_to_rds(data, rds_endpoint, username, password, database)
   

4. *Create requirements.txt:*
   - List the Python packages your application depends on.

   text
   boto3
   pymysql
   
