# aws-serverless-khai-data-processor
"Ứng dụng web Serverless trên AWS thu thập dữ liệu người dùng, sử dụng Lambda, API Gateway, S3 Hosting và DynamoDB.
Luồng Dữ liệu (Data Flow):
Giao diện: Người dùng truy cập giao diện web tĩnh được host trên Amazon S3 Static Website Hosting.
Kích hoạt API: Dữ liệu được gửi qua yêu cầu POST/GET đến điểm cuối Amazon API Gateway (REST API).
Xử lý Logic: API Gateway kích hoạt hàm AWS Lambda để thực thi logic nghiệp vụ, xác thực dữ liệu đầu vào.
Lưu trữ Kép:
Dữ liệu cấu trúc được lưu vào Amazon DynamoDB .
Bản sao dữ liệu thô (raw data) được lưu trữ vào Amazon S3 Bucket
