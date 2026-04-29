# app

## Tiếng Việt

Đây là thư mục source chính của ứng dụng Flask. Thư mục này là nơi ghép app factory, route tổng, middleware, helper và các module nghiệp vụ.

### Vai trò

- `__init__.py`: tạo Flask app bằng hàm `create_app()`, bật CORS, đăng ký route và error handler.
- `routes.py`: khai báo các route cấp ứng dụng như `/`, `/health` và gắn các blueprint module.
- `config/`: đọc và chuẩn hóa biến môi trường.
- `helpers/`: chứa các hàm tiện ích dùng chung, ví dụ định dạng response JSON.
- `middlewares/`: chứa handler xử lý lỗi và logic nằm giữa request/response.
- `modules/`: chứa các module theo domain, hiện có module `users`.

### Nguyên tắc mở rộng

Khi thêm tính năng mới, nên tạo module riêng trong `modules/<tên_module>/` gồm route, controller, service và model. Sau đó import blueprint vào `routes.py` để gắn module đó vào app.

## English

This is the main source folder of the Flask application. It connects the app factory, top-level routes, middleware, helpers, and business modules.

### Responsibilities

- `__init__.py`: creates the Flask app through `create_app()`, enables CORS, and registers routes plus error handlers.
- `routes.py`: defines application-level routes such as `/` and `/health`, then attaches module blueprints.
- `config/`: reads and normalizes environment variables.
- `helpers/`: shared utility functions, for example JSON response formatting.
- `middlewares/`: error handlers and request/response lifecycle logic.
- `modules/`: domain-based modules, currently including `users`.

### Extension guideline

When adding a new feature, create a dedicated module in `modules/<module_name>/` with route, controller, service, and model files. Then import its blueprint into `routes.py` to attach it to the app.
