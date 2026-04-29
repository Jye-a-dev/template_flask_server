# config

## Tiếng Việt

Thư mục này quản lý cấu hình runtime cho server.

### File hiện có

- `env.py`: load biến môi trường từ `.env`, ép kiểu các giá trị cơ bản và expose object `config`.

### Biến môi trường đang dùng

- `HOST`: địa chỉ bind server, mặc định là `127.0.0.1`.
- `PORT`: cổng server, mặc định là `5000`.
- `DEBUG`: bật hoặc tắt debug mode, mặc định là `true`.

Thư mục này chỉ nên chứa logic cấu hình. Không nên đặt route, controller hoặc logic nghiệp vụ vào đây.

## English

This folder manages runtime configuration for the server.

### Existing file

- `env.py`: loads environment variables from `.env`, converts basic values to the right types, and exposes the `config` object.

### Environment variables

- `HOST`: server bind address, defaulting to `127.0.0.1`.
- `PORT`: server port, defaulting to `5000`.
- `DEBUG`: enables or disables debug mode, defaulting to `true`.

This folder should only contain configuration logic. Routes, controllers, and business logic should live elsewhere.
