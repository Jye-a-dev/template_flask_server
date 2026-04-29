# Flask Server Template

## Clone repo này

```bash
git clone https://github.com/Jye-a-dev/template_flask_server
```

Template khởi tạo cho backend REST API bằng Python Flask theo hướng module rõ ràng, dùng:

- Python + Flask
- Flask built-in development server cho dev nhanh
- App factory bằng `create_app()`
- Routing qua Flask route và Blueprint
- Controller, service, model tách riêng
- Middleware/error handler dùng chung
- Helper response JSON dùng chung
- CORS bằng Flask-CORS
- Cấu hình runtime qua `.env`
- Placeholder cho config, modules, routes, middlewares, services, helpers
- File `.md` song ngữ trong từng folder chính để giải thích vai trò thư mục

Template này phù hợp khi bạn muốn bắt đầu nhanh với một REST API server Flask nhỏ gọn, rõ cấu trúc, dễ học, dễ copy module và không muốn bắt đầu bằng một framework quá nặng.

## 1. Project này đang setup theo kiểu nào?

Repo hiện tại là kiểu:

```text
Python Flask + REST API + app factory + blueprint + controller/service/model
```

Đây là setup phù hợp cho:

- REST API backend nhỏ hoặc vừa
- Backend cho React, Vue, Next hoặc mobile app
- Dự án học backend căn bản bằng Python
- Dự án cần hiểu rõ luồng request đi qua từng file
- API đơn giản chưa cần framework lớn hơn
- Prototype nhanh trước khi nâng cấp sang FastAPI, Django hoặc kiến trúc lớn hơn
- Team muốn code Flask rõ tầng route/controller/service/model
- Project muốn tự kiểm soát routing, response và cấu trúc module

Hiện tại repo có module `users` làm ví dụ thật. Module này đã có route, controller, service, model và endpoint đọc dữ liệu cơ bản.

## 2. Khi nào nên dùng từng kiểu setup Python backend?

### Flask kiểu controller/service/model

Đây là kiểu setup của repo này.

Dùng khi:

- muốn học rõ bản chất backend Python
- muốn REST API nhỏ, ít dependency
- muốn chạy nhanh bằng Flask development server
- muốn hiểu route, controller, service, model hoạt động như thế nào
- muốn template dễ copy và dễ chỉnh
- muốn cấu trúc nhẹ hơn Django

### FastAPI

Dùng khi:

- cần API hiện đại, type hint mạnh
- muốn validation tự động bằng Pydantic
- muốn OpenAPI/Swagger tự sinh
- cần async endpoint hoặc performance tốt hơn cho API
- team quen Python type hint

### Django hoặc Django REST Framework

Dùng khi:

- dự án lớn hơn
- cần authentication, admin panel, ORM, migration đầy đủ
- cần cấu trúc production mạnh hơn
- team đã quen Django
- cần nhiều tính năng có sẵn thay vì tự ghép

### Node.js Express hoặc NestJS

Nên dùng Node.js backend khi:

- team quen JavaScript hoặc TypeScript hơn Python
- cần realtime nhiều
- frontend và backend muốn dùng cùng ngôn ngữ
- cần ecosystem npm

Nên dùng Flask khi:

- team quen Python
- API đơn giản
- muốn setup nhanh
- muốn code ít dependency
- muốn dễ deploy trên VPS, Docker hoặc cloud Python runtime

## 3. Cài và chạy project

### Yêu cầu

- Python 3.10 trở lên
- `pip`
- Virtual environment, project hiện đã có folder `venv`

Kiểm tra Python:

```bash
python --version
```

### Cài dependency nếu chưa có `venv`

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Windows CMD:

```bat
venv\Scripts\activate.bat
pip install -r requirements.txt
```

macOS/Linux:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Chạy môi trường dev

Tại folder `server`:

```powershell
.\run.ps1
```

Hoặc chạy trực tiếp:

```powershell
.\venv\Scripts\python.exe main.py
```

Sau đó mở:

```text
http://127.0.0.1:5000
```

## 4. URL mặc định

Sau khi chạy server, app mặc định chạy tại:

```text
http://127.0.0.1:5000
```

Các API hiện có:

```text
GET http://127.0.0.1:5000/
GET http://127.0.0.1:5000/health
GET http://127.0.0.1:5000/api/users/
GET http://127.0.0.1:5000/api/users/1
```

Ví dụ response root:

```json
{
  "success": true,
  "message": "Server is running",
  "data": {
    "service": "server",
    "status": "running",
    "docs": {
      "health": "/health",
      "users": "/api/users"
    }
  }
}
```

Ví dụ response users:

```json
{
  "success": true,
  "message": "Users fetched successfully",
  "data": [
    {
      "id": 1,
      "name": "Demo User",
      "email": "demo@example.com"
    }
  ]
}
```

## 5. Cấu trúc thư mục hiện tại

```text
server/
├─ server.md
├─ README.md
├─ .env
├─ .gitignore
├─ main.py
├─ requirements.txt
├─ run.ps1
├─ app/
│  ├─ app.md
│  ├─ __init__.py
│  ├─ routes.py
│  ├─ config/
│  │  ├─ config.md
│  │  ├─ __init__.py
│  │  └─ env.py
│  ├─ helpers/
│  │  ├─ helpers.md
│  │  ├─ __init__.py
│  │  └─ response.py
│  ├─ middlewares/
│  │  ├─ middlewares.md
│  │  ├─ __init__.py
│  │  ├─ error_handler.py
│  │  └─ error.middleware.py
│  └─ modules/
│     ├─ modules.md
│     ├─ __init__.py
│     └─ users/
│        ├─ users.md
│        ├─ __init__.py
│        ├─ route.py
│        ├─ controller.py
│        ├─ service.py
│        ├─ model.py
│        ├─ users.controller.py
│        ├─ users.model.py
│        ├─ users.route.py
│        └─ users.service.py
└─ venv/
```

Ý nghĩa chính:

- `app/`: source code chính của Flask app
- `app/config/`: cấu hình runtime và biến môi trường
- `app/helpers/`: helper dùng chung như JSON response
- `app/middlewares/`: xử lý lỗi và logic request/response dùng chung
- `app/modules/`: module nghiệp vụ theo domain
- `app/modules/users/`: module users mẫu
- `main.py`: entrypoint chạy server
- `run.ps1`: script chạy nhanh trên Windows PowerShell
- `.env`: biến môi trường
- `requirements.txt`: dependency Python
- `README.md`: tài liệu tổng quan của project
- `*.md`: tài liệu mô tả vai trò từng folder bằng English và tiếng Việt
- `venv/`: môi trường ảo Python, không nên commit

## 6. Luồng chạy hiện tại của app

Luồng cơ bản:

1. Server chạy từ `main.py`.
2. `main.py` gọi `create_app()` trong `app/__init__.py`.
3. `create_app()` tạo Flask app, bật CORS, đăng ký route và error handler.
4. Route cấp app được đăng ký trong `app/routes.py`.
5. `app/routes.py` gắn blueprint `users_bp` vào prefix `/api/users`.
6. Request vào `/api/users/` được xử lý trong `app/modules/users/route.py`.
7. Route gọi function tương ứng trong `controller.py`.
8. Controller gọi `service.py`.
9. Service đọc dữ liệu từ `model.py` hoặc nguồn dữ liệu sau này.
10. Controller trả JSON bằng helper trong `app/helpers/response.py`.

Tóm tắt:

```text
main.py
-> app/create_app
-> app/routes.py
-> users/route.py
-> users/controller.py
-> users/service.py
-> users/model.py
-> success_response
```

## 7. Cách tạo một module mới theo style của repo này

Với cấu trúc hiện tại, mỗi entity nên nằm trong một folder riêng dưới `app/modules/`.

Ví dụ module products:

```text
app/modules/products/
├─ __init__.py
├─ products.md
├─ route.py
├─ controller.py
├─ service.py
└─ model.py
```

Sau đó đăng ký blueprint vào:

```text
app/routes.py
```

Ý nghĩa từng phần:

- `route.py`: ánh xạ HTTP method và path tới controller
- `controller.py`: nhận HTTP request, gọi service, trả response
- `service.py`: xử lý business logic chính
- `model.py`: đại diện dữ liệu, xử lý dữ liệu hoặc truy vấn database
- `<module>.md`: giải thích vai trò module bằng tiếng Việt và English

Ví dụ prefix route:

```python
app.register_blueprint(products_bp, url_prefix="/api/products")
```

## 8. Quy tắc đặt tên đang dùng

### Folder

Folder dùng chữ thường:

```text
app
config
helpers
middlewares
modules
users
```

### File Python

File Python dùng snake_case hoặc tên ngắn theo vai trò:

```text
route.py
controller.py
service.py
model.py
error_handler.py
response.py
```

### Function

Function dùng snake_case:

```python
create_app()
register_routes()
success_response()
error_response()
list_users()
get_user()
```

### Class

Class dùng PascalCase:

```python
Config
User
```

### Endpoint

Endpoint nên dùng plural noun:

```text
/api/users
/api/products
/api/orders
```

## 9. Response format trong repo này

Response JSON được trả qua helper:

```python
return success_response(data, "Users fetched successfully")
```

Helper nằm ở:

```text
app/helpers/response.py
```

Mục tiêu:

- response thống nhất
- luôn trả JSON
- có format chung cho success và error
- dễ thay đổi response format ở một nơi
- hỗ trợ tiếng Việt qua JSON UTF-8 mặc định của Flask

Response thành công:

```json
{
  "success": true,
  "message": "OK",
  "data": {}
}
```

Response lỗi:

```json
{
  "success": false,
  "message": "User not found"
}
```

## 10. Cấu hình `.env` trong repo này

Cấu hình runtime nằm ở:

```text
.env
```

File đọc cấu hình:

```text
app/config/env.py
```

Biến môi trường hiện có:

```env
HOST=127.0.0.1
PORT=5000
DEBUG=true
```

Ý nghĩa:

- `HOST`: địa chỉ server bind
- `PORT`: cổng chạy server
- `DEBUG`: bật hoặc tắt debug mode

Khi lên production, nên đặt:

```env
DEBUG=false
```

## 11. Database trong repo này

Hiện tại project chưa có database connection thật. Module `users` đang dùng dữ liệu mẫu trong bộ nhớ:

```text
app/modules/users/service.py
```

Khi muốn thêm database, có thể bắt đầu bằng một trong các hướng:

- SQLite cho dev nhẹ
- PostgreSQL cho API production
- MySQL/MariaDB nếu hosting hoặc team đang dùng sẵn
- SQLAlchemy nếu muốn ORM
- psycopg hoặc mysql-connector nếu muốn query trực tiếp

Gợi ý cấu trúc khi thêm database:

```text
app/database/
├─ database.md
├─ __init__.py
└─ connection.py
```

Hoặc nếu dùng repository:

```text
app/modules/users/
├─ repository.py
├─ service.py
└─ model.py
```

## 12. CORS trong repo này

CORS được bật trong:

```text
app/__init__.py
```

Hiện tại dùng:

```python
CORS(app)
```

Trong dev, cấu hình này giúp frontend gọi API dễ hơn.

Khi lên production, nên giới hạn origin cụ thể, ví dụ:

```python
CORS(app, origins=["https://your-frontend.com"])
```

## 13. Error handling trong repo này

Error handler nằm ở:

```text
app/middlewares/error_handler.py
```

Hiện tại error handling gồm:

- lỗi HTTP như 404 trả JSON thống nhất
- lỗi không mong muốn trả HTTP 500
- log exception bằng `app.logger.exception()`

Ví dụ lỗi user không tồn tại:

```json
{
  "success": false,
  "message": "User not found"
}
```

Khi project lớn hơn, có thể thêm:

```text
app/exceptions/
app/validators/
```

Gợi ý exception:

```text
NotFoundError
BadRequestError
UnauthorizedError
ForbiddenError
ValidationError
```

## 14. Validation trong repo này

Hiện tại project chưa có validation layer riêng.

Với Flask, có thể validate trong controller hoặc tách helper/service riêng:

```text
app/helpers/validation.py
```

Khi thêm `POST /api/users`, nên kiểm tra:

- `name` bắt buộc
- `email` bắt buộc
- `email` đúng format
- dữ liệu không vượt quá độ dài cho phép

Không nên để dữ liệu request đi thẳng vào service/model mà chưa validate.

## 15. Auth và Security trong repo này

Project hiện chưa có auth.

Khi cần auth, có thể thêm:

- JWT access token
- refresh token
- password hashing bằng `werkzeug.security`
- middleware hoặc decorator kiểm tra `Authorization` header
- current user helper/service
- role và permission

Gợi ý cấu trúc:

```text
app/modules/auth/
├─ auth.md
├─ route.py
├─ controller.py
├─ service.py
└─ model.py
```

Không nên tự lưu plain text password. Luôn dùng hashing:

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

## 16. Quy tắc tổ chức code nên giữ

- Route chỉ match URL và gọi controller
- Controller chỉ nhận request, gọi service và trả response
- Service chứa business logic
- Model đại diện dữ liệu hoặc xử lý truy vấn dữ liệu
- Helper chỉ chứa utility nhỏ dùng chung
- Middleware chỉ xử lý request/response dùng chung
- Config chỉ chứa cấu hình, không chứa nghiệp vụ
- Không nhồi business logic vào `main.py`
- Không để controller chứa nhiều query phức tạp
- Không commit secret thật trong `.env`
- Không trả lỗi raw hoặc stack trace ở production
- Mỗi folder nên giữ file `.md` để giải thích vai trò folder

## 17. Cách scale project khi API lớn hơn

Khi app tăng độ phức tạp, có thể thêm:

- `repositories/`
- `dtos/`
- `validators/`
- `exceptions/`
- `database/`
- `auth/`
- `migrations/`
- `logs/`
- `storage/`
- `tests/`

Ví dụ scale theo module:

```text
app/modules/
├─ auth/
├─ users/
├─ products/
├─ orders/
└─ payments/
```

Ví dụ scale theo tầng trong từng module:

```text
route.py
controller.py
service.py
repository.py
model.py
schema.py
validator.py
```

Với project học hoặc API nhỏ, cấu trúc hiện tại là đủ. Khi service và model bắt đầu nhiều query hơn, nên thêm repository.

## 18. Khi nào nên tách repository hoặc DTO?

Repository nên tách riêng khi:

- model bắt đầu có nhiều query database
- nhiều service cùng cần truy xuất một bảng
- muốn service không phụ thuộc trực tiếp database driver
- muốn test business logic dễ hơn
- muốn đổi database ít ảnh hưởng tầng service

DTO hoặc schema nên thêm riêng khi:

- request body phức tạp
- response không giống model
- cần ẩn field nhạy cảm
- cần format dữ liệu trước khi trả về client
- nhiều endpoint dùng cùng một kiểu dữ liệu

Ví dụ:

```text
app/modules/users/
├─ dto.py
├─ repository.py
├─ service.py
└─ model.py
```

Không cần tạo quá nhiều abstraction nếu API vẫn rất nhỏ.

## 19. Chạy project trong VS Code

Mở folder:

```bash
code .
```

Chạy server:

```powershell
.\run.ps1
```

Dừng server:

```text
Ctrl + C trong terminal
```

Nếu port bị chiếm trên Windows:

```powershell
netstat -ano | Select-String ':5000'
Stop-Process -Id <PID>
```

Thay `<PID>` bằng số ở cột cuối.

## 20. Test API nhanh

Dùng browser cho GET endpoint:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/health
http://127.0.0.1:5000/api/users/
http://127.0.0.1:5000/api/users/1
```

Dùng PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/
Invoke-RestMethod -Uri http://127.0.0.1:5000/health
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users/
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users/1
```

Dùng curl:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/api/users/
curl http://127.0.0.1:5000/api/users/1
```

## 21. Checklist khi tạo API project mới

- clone repo
- kiểm tra Python bằng `python --version`
- tạo virtual environment nếu chưa có
- cài dependency bằng `pip install -r requirements.txt`
- cấu hình `.env`
- chạy `.\run.ps1`
- test `GET /`
- test `GET /health`
- test `GET /api/users/`
- tạo module mới trong `app/modules`
- tạo route mới
- tạo controller mới
- tạo service mới
- tạo model mới
- đăng ký blueprint trong `app/routes.py`
- giữ business logic trong service
- chỉ query database trong model hoặc repository
- thêm validation trước khi nhận POST/PUT/PATCH
- giới hạn CORS origin khi lên production
- không commit secret thật trong `.env`

## 22. Gợi ý hướng phát triển tiếp cho template này

Nếu muốn biến template này thành base mạnh hơn, có thể thêm:

- database connection layer
- SQLAlchemy hoặc repository layer
- DTO/schema layer
- validation helper
- global exception classes
- JWT auth
- pagination helper
- query filter helper
- migration tool
- SQLite mode cho dev nhanh
- Dockerfile
- logging config
- unit test bằng pytest
- API documentation bằng file `.http` hoặc OpenAPI thủ công

## 23. Tóm tắt

Nếu bạn muốn một setup backend cân bằng giữa:

- dễ bắt đầu
- dễ đọc
- ít dependency
- cấu trúc rõ
- dễ hiểu luồng backend
- dễ copy module
- có thể nâng cấp dần sang database thật, auth, validation và repository

thì `Python Flask + app factory + blueprint + controller/service/model` là lựa chọn rất thực dụng.

Template này đang đi theo hướng đó:

- entry rõ ở `main.py`
- app factory rõ ở `app/__init__.py`
- route tổng rõ ở `app/routes.py`
- module users mẫu rõ
- controller/service/model tách riêng
- CORS có sẵn
- JSON response helper có sẵn
- cấu hình qua `.env`
- folder có tài liệu song ngữ
- dễ phát triển tiếp hoặc chuyển lên framework lớn khi cần
