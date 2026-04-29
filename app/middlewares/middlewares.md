# middlewares

## Tiếng Việt

Thư mục này chứa logic xử lý nằm quanh vòng đời request/response của Flask.

### File hiện có

- `error_handler.py`: đăng ký handler cho lỗi HTTP và lỗi không mong muốn, sau đó trả về response JSON thống nhất.
- `error.middleware.py`: file placeholder cũ, hiện chưa dùng trong luồng chạy vì tên file có dấu chấm không thuận tiện cho import Python thông thường.

### Mục đích

Middleware và error handler giúp tách logic xử lý lỗi khỏi controller. Controller chỉ cần `abort()` hoặc để exception nổi lên, còn thư mục này phụ trách format lỗi trả về cho client.

## English

This folder contains logic around Flask's request/response lifecycle.

### Existing files

- `error_handler.py`: registers handlers for HTTP errors and unexpected errors, then returns a consistent JSON response.
- `error.middleware.py`: an old placeholder file. It is currently not used because filenames with extra dots are inconvenient for normal Python imports.

### Purpose

Middleware and error handlers keep error formatting separate from controllers. Controllers can call `abort()` or let exceptions bubble up, while this folder formats the error response for the client.
