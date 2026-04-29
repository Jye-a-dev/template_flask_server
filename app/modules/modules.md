# modules

## Tiếng Việt

Thư mục này chứa các module nghiệp vụ theo domain. Mỗi module nên độc lập tương đối và có route, controller, service, model riêng.

### Module hiện có

- `users/`: module demo quản lý API người dùng.

### Cấu trúc đề xuất cho mỗi module

- `route.py`: tạo Blueprint và khai báo URL của module.
- `controller.py`: nhận request, gọi service và trả response.
- `service.py`: xử lý logic nghiệp vụ.
- `model.py`: khai báo cấu trúc dữ liệu hoặc model database.

Sau khi tạo module mới, đăng ký blueprint của module đó trong `app/routes.py`.

## English

This folder contains domain-based business modules. Each module should be relatively independent and have its own route, controller, service, and model files.

### Existing module

- `users/`: a demo module for user-related APIs.

### Suggested structure for each module

- `route.py`: creates the Blueprint and declares the module URLs.
- `controller.py`: receives requests, calls services, and returns responses.
- `service.py`: handles business logic.
- `model.py`: defines data structures or database models.

After creating a new module, register its blueprint in `app/routes.py`.
