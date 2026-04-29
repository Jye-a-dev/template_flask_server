# users

## Tiếng Việt

Đây là module demo cho API người dùng. Module này cho thấy cách chia tách route, controller, service và model trong Flask.

### Luồng xử lý

- `route.py`: khai báo Blueprint `users_bp` và các endpoint `/api/users/`, `/api/users/<id>`.
- `controller.py`: nhận request từ route, gọi service và trả JSON response.
- `service.py`: chứa dữ liệu demo trong bộ nhớ và các hàm truy vấn `list_users()`, `get_user()`.
- `model.py`: khai báo dataclass `User` và hàm chuyển dữ liệu thành dict.

### Endpoint

- `GET /api/users/`: trả danh sách user demo.
- `GET /api/users/1`: trả chi tiết user có id bằng `1`.

### Ghi chú

Những file tên dạng `users.controller.py`, `users.model.py`, `users.route.py`, `users.service.py` là placeholder cũ và đang để trống. Python import module có dấu chấm trong tên file không tiện, nên module đang chạy dùng các file `controller.py`, `model.py`, `route.py`, `service.py`.

## English

This is a demo module for user APIs. It shows how to separate route, controller, service, and model responsibilities in Flask.

### Request flow

- `route.py`: declares the `users_bp` Blueprint and the `/api/users/`, `/api/users/<id>` endpoints.
- `controller.py`: receives requests from routes, calls services, and returns JSON responses.
- `service.py`: stores demo in-memory data and provides `list_users()`, `get_user()` query functions.
- `model.py`: defines the `User` dataclass and converts it to a dictionary.

### Endpoints

- `GET /api/users/`: returns the demo user list.
- `GET /api/users/1`: returns the details of the user with id `1`.

### Notes

Files named `users.controller.py`, `users.model.py`, `users.route.py`, and `users.service.py` are old empty placeholders. Python imports are awkward with extra dots in filenames, so the running module uses `controller.py`, `model.py`, `route.py`, and `service.py`.
