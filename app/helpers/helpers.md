# helpers

## Tiếng Việt

Thư mục này chứa các hàm tiện ích dùng chung trong nhiều phần của backend.

### File hiện có

- `response.py`: chuẩn hóa response JSON thành hai dạng `success_response()` và `error_response()`.

### Mục đích

Helper giúp route và controller trả về API response đồng nhất:

- response thành công có `success`, `message`, `data`;
- response lỗi có `success`, `message` và tùy chọn `details`.

Khi thêm helper mới, nên giữ logic nhỏ, rõ ràng và không phụ thuộc ngược vào module nghiệp vụ.

## English

This folder contains shared utility functions used across the backend.

### Existing file

- `response.py`: standardizes JSON responses through `success_response()` and `error_response()`.

### Purpose

Helpers keep API responses consistent across routes and controllers:

- successful responses include `success`, `message`, and `data`;
- error responses include `success`, `message`, and optional `details`.

When adding a new helper, keep it small, clear, and independent from business modules.
