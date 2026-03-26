# 1. Sử dụng Python bản nhẹ (slim)
FROM python:3.10-slim

# 2. Cài đặt FFmpeg trực tiếp vào hệ điều hành của Container
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# 3. Thiết lập thư mục làm việc trong container
WORKDIR /

# 4. Copy file requirements và cài đặt thư viện Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code vào container
COPY . .

# 6. Tạo thư mục downloads để lưu file tạm
RUN mkdir -p downloads

# 7. Chạy app bằng Gunicorn (thay vì app.run của Flask để ổn định hơn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "600", "app.main:create_app()"]