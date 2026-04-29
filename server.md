# server

## Tiếng Việt

Đây là thư mục gốc của backend Flask. Thư mục này chứa điểm khởi động ứng dụng, danh sách dependency, biến môi trường và toàn bộ source code chính của server.

### Thành phần chính

- `main.py`: điểm khởi động server. File này tạo Flask app từ `app.create_app()` và chạy server theo cấu hình trong `app/config/env.py`.
- `requirements.txt`: danh sách package Python cần cài để chạy project, hiện gồm Flask, Flask-CORS và python-dotenv.
- `.env`: nơi đặt biến môi trường cục bộ như `HOST`, `PORT`, `DEBUG`.
- `.gitignore`: loại trừ các file sinh ra trong quá trình chạy như `venv`, cache Python và file log.
- `run.ps1`: script chạy nhanh server trên Windows PowerShell.
- `app/`: source code chính của backend.
- `venv/`: môi trường ảo Python đã cài dependency. Không nên sửa trực tiếp và không nên commit.

### Cách chạy nhanh

```powershell
.\run.ps1
```

Server mặc định chạy tại `http://127.0.0.1:5000`.

## English

This is the root folder of the Flask backend. It contains the application entrypoint, dependency list, environment variables, and the main server source code.

### Main parts

- `main.py`: the server entrypoint. It creates the Flask app from `app.create_app()` and runs it with settings from `app/config/env.py`.
- `requirements.txt`: the Python packages required to run the project, currently Flask, Flask-CORS, and python-dotenv.
- `.env`: local environment variables such as `HOST`, `PORT`, and `DEBUG`.
- `.gitignore`: excludes generated files such as `venv`, Python cache files, and logs.
- `run.ps1`: a quick PowerShell script for running the server on Windows.
- `app/`: the main backend source code.
- `venv/`: the Python virtual environment with installed dependencies. It should not be edited directly or committed.

### Quick start

```powershell
.\run.ps1
```

By default, the server runs at `http://127.0.0.1:5000`.
