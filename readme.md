<div align="center">

# ⚡ FastAPI Starter Pack
### `MongoDB` · `Zilliz Vector DB` · `Ollama AI` · `JWT Auth` · `RBAC`

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Motor_Async-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> 🚀 **A production-ready, batteries-included FastAPI boilerplate** — so you can skip the boring setup and jump straight into building your next big idea.

</div>

---

## 🌟 Why This Starter Pack?

Every great API starts with a solid foundation. This boilerplate is hand-crafted with **real-world architecture** in mind — not just a "hello world" with a database. It gives you:

- ✅ Clean, **layered architecture** (Controllers → Services → Helpers)
- ✅ **Async MongoDB** with Motor — fast, non-blocking database I/O
- ✅ **JWT Authentication** with Role-Based Access Control (RBAC)
- ✅ **Vector Database** integration (Zilliz / Milvus) ready to plug in
- ✅ **Ollama AI** integration support out of the box
- ✅ **Global error handling** — clean, consistent JSON error responses
- ✅ **Pydantic v2** request validation with human-readable error messages
- ✅ **Bcrypt + SHA-256** double-layer password hashing
- ✅ **Versioned API routing** (`/api/v1/...`) — scale gracefully
- ✅ Fully **async lifespan** management (startup & shutdown hooks)

---

## 🗂️ Project Structure

```
fastapi-starter-pack/
│
├── 📄 main.py                     # App entry point, lifespan, middleware registration
│
├── 📁 controllers/                # Route definitions — thin layer, just wires URLs to services
│   ├── auth_controllers.py        #   POST /auth/login
│   └── user_controllers.py        #   POST /users/register · GET /users/me · GET /users/public-posts
│
├── 📁 services/                   # Business logic — the brain of your app
│   ├── auth_services.py           #   Login flow, token generation
│   └── user_services.py           #   Registration, profile fetching
│
├── 📁 models/                     # Pydantic schemas — request bodies & DB models
│   └── user_schemas.py            #   UserModel, userRegistrationRequest, userLoginRequest
│
├── 📁 databases/                  # Database connection managers
│   ├── db.py                      #   Async MongoDB (Motor) setup
│   └── zilliz_db.py               #   Zilliz Cloud / Milvus vector DB setup
│
├── 📁 helpers/                    # Pure utility functions
│   ├── auth_helpers.py            #   JWT create & verify
│   ├── mongo_utils.py             #   MongoDB document formatters
│   └── security_utils.py          #   Password hashing & verification
│
├── 📁 contexts/                   # App-wide shared context
│   ├── collections.py             #   MongoDB collection references
│   ├── error_handlers.py          #   Global HTTP & validation error handlers
│   ├── middleware.py              #   ASGI context middleware + RBAC token verifier
│   └── routers_v1.py              #   Central v1 router registry
│
└── 📄 requirements.txt            # All dependencies
```

---

## 🔌 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance async web framework |
| **Server** | [Uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server |
| **Database** | [MongoDB](https://www.mongodb.com/) + [Motor](https://motor.readthedocs.io/) | Async NoSQL database |
| **Vector DB** | [Zilliz Cloud](https://zilliz.com/) / [Milvus](https://milvus.io/) | AI-powered vector similarity search |
| **AI / LLM** | [Ollama](https://ollama.ai/) | Local LLM inference integration |
| **Embeddings** | [Sentence Transformers](https://www.sbert.net/) | `all-MiniLM-L6-v2` text embeddings (dim: 384) |
| **Auth** | [PyJWT](https://pyjwt.readthedocs.io/) | JSON Web Token generation & verification |
| **Validation** | [Pydantic v2](https://docs.pydantic.dev/) | Request/response schema validation |
| **Security** | [Bcrypt](https://pypi.org/project/bcrypt/) + SHA-256 | Double-layer password hashing |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-starter-pack.git
cd fastapi-starter-pack
```

### 2. Create & Activate a Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# MongoDB
MONGO_URI=mongodb://localhost:27017

# Zilliz Cloud (Vector DB) — uncomment in main.py when ready
ZILLIZ_URI=https://your-cluster.zillizcloud.com
ZILLIZ_TOKEN=your_zilliz_api_token
```

### 5. Run the Server

```bash
python main.py
```

Or with Uvicorn directly:

```bash
uvicorn main:app --host 127.0.0.1 --port 7008 --reload
```

> 🟢 Server starts at: **`http://127.0.0.1:7008`**  
> 📖 Interactive API Docs: **`http://127.0.0.1:7008/docs`**  
> 📘 ReDoc Docs: **`http://127.0.0.1:7008/redoc`**

---

## 📡 API Endpoints

### 🔓 Public Routes

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — server info & status |
| `POST` | `/api/v1/auth/login` | Login with email & password, returns JWT |
| `POST` | `/api/v1/users/register` | Register a new user account |
| `GET` | `/api/v1/users/public-posts` | Sample public route (no auth needed) |

### 🔐 Protected Routes (JWT Required)

| Method | Endpoint | Role | Description |
|---|---|---|---|
| `GET` | `/api/v1/users/me` | `user` | Get the authenticated user's profile |

---

## 🔐 Authentication Flow

```
┌──────────┐        POST /auth/login         ┌──────────────┐
│  Client  │  ──────────────────────────►   │  FastAPI App │
│          │   { email, password }           │              │
│          │  ◄──────────────────────────   │  validates   │
│          │   { token: "eyJ..." }           │  + issues    │
│          │                                 │    JWT       │
│          │   GET /users/me                 │              │
│          │   Authorization: Bearer eyJ...  │              │
│          │  ──────────────────────────►   │  verifies    │
│          │  ◄──────────────────────────   │  RBAC check  │
│          │   { user: { ... } }             │              │
└──────────┘                                 └──────────────┘
```

1. **Register** → `POST /api/v1/users/register` with `name`, `email`, `password`
2. **Login** → `POST /api/v1/auth/login` — receive a signed **JWT token** (30-day expiry)
3. **Access protected routes** → Pass `Authorization: Bearer <token>` in headers
4. **RBAC** → Routes enforce roles (e.g., `user`, `admin`) via the `verify_token("role")` dependency

---

## 🛡️ Security Architecture

```
Raw Password  ──►  SHA-256 Hash  ──►  bcrypt Hash  ──►  Stored in DB
```

Passwords are **double-hashed**: first with SHA-256 (to normalize length), then with bcrypt (adaptive cost factor). This protects against both brute-force and length-extension attacks.

JWT tokens are signed with **HS256** and carry:
```json
{
  "_id": "user_mongo_id",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "exp": 1234567890
}
```

> ⚠️ **Before going to production:** Move `SECRET_KEY` in `auth_helpers.py` to your `.env` file!

---

## 🧠 Vector DB (Zilliz / Milvus) — AI Ready

The `databases/zilliz_db.py` module is fully wired up and ready for AI-powered features:

- 🔌 **Auto-connects** and creates the collection schema on first run
- 📐 Uses `all-MiniLM-L6-v2` (384-dim) sentence embeddings
- 🔍 **Semantic similarity search** with L2 distance metric
- ➕ Insert, 🔎 Search, and 🗑️ Delete embedding operations included
- 📦 Collection: `customer_embeddings` with `AUTOINDEX` for fast vector search

To enable, simply **uncomment** the Zilliz lines in `main.py`:

```python
# In main.py lifespan:
await connect_to_zilliz()    # ← uncomment
await close_zilliz_connection()  # ← uncomment
```

---

## 🌐 Global Error Handling

No more ugly, inconsistent error responses. Every error — from validation to server crashes — returns a clean, predictable JSON shape:

```json
// HTTP Errors (4xx)
{ "success": false, "error": "User not found" }

// Validation Errors (422)
{ "success": false, "error": "Validation Failed", "details": [{"field": "email", "message": "..."}] }

// Server Errors (500)
{ "success": false, "error": "Internal Server Error", "message": "..." }
```

---

## ➕ Adding a New Feature

Following the layered architecture is simple. Here's the pattern:

**Step 1** — Add your Pydantic schema in `models/`
```python
# models/post_schemas.py
class CreatePostRequest(BaseModel):
    title: str
    content: str
```

**Step 2** — Write your business logic in `services/`
```python
# services/post_services.py
async def create_post_service(request: CreatePostRequest):
    # ... your logic here
```

**Step 3** — Wire the route in `controllers/`
```python
# controllers/post_controllers.py
router.post("/create")(create_post_service)
```

**Step 4** — Register in `contexts/routers_v1.py`
```python
{"controllers": post_router, "prefix": "/posts", "tags": ["posts"], "dependencies": []}
```

Done! ✅ Your new endpoint is live at `/api/v1/posts/create`.

---

## 📦 Dependencies

```txt
fastapi              # Web framework
uvicorn              # ASGI server
pydantic             # Data validation
motor                # Async MongoDB driver
pymilvus             # Milvus/Zilliz vector DB client
ollama               # Local LLM integration
sentence-transformers # Text embedding models
pyjwt                # JWT token handling
bcrypt<4.0.0         # Password hashing
python-dotenv        # .env file support
```

---

## 🛣️ Roadmap

- [ ] 🔄 Refresh token support
- [ ] 📧 Email verification on registration
- [ ] 🧪 Pytest test suite with async support
- [ ] 🐳 Docker + Docker Compose setup
- [ ] 📊 Request logging middleware
- [ ] 🔑 API key authentication option
- [ ] 🤖 Ollama chat endpoint example

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** — use it freely for personal or commercial projects.

---

<div align="center">

**Built with ❤️ using FastAPI**

⭐ *If this starter pack saved you time, consider giving it a star!* ⭐

</div>
