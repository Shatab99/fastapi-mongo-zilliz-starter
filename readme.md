<div align="center">

# ⚡ FastAPI Starter Pack
### `MongoDB` · `Zilliz Vector DB` · `Ollama AI` · `JWT Auth` · `RBAC` · `3-Way Handshake`

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Motor_Async-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Handshake](https://img.shields.io/badge/3--Way_Handshake-Bot_Protection-FF4B4B?style=for-the-badge&logo=shieldsdotio&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> 🚀 **A production-ready, batteries-included FastAPI boilerplate** — so you can skip the boring setup and jump straight into building your next big idea.
>
> 🤖 **Now with a built-in 3-Way Client Handshake** — a custom bot-reduction mechanism that ensures only legitimate clients can talk to your API.

</div>

---

curl.exe -sL https://raw.githubusercontent.com/Shatab99/fastapi-mongo-zilliz-starter/refs/heads/main/install.sh | bash -s my-new-project

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
- ✅ **Versioned API routing** (`/api/v1/...` & `/api/v2/...`) — scale gracefully
- ✅ Fully **async lifespan** management (startup & shutdown hooks)
- ✅  🤖 **3-Way Client Handshake** — short-lived token gate that blocks bots & automated scrapers

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
│   ├── check_client.py            #   🤖 3-Way Handshake bot-guard dependency
│   ├── routers_v1.py              #   Central v1 router registry (guarded by handshake)
│   └── routers_v2.py              #   Security router — handshake token issuer
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

### 🌍 Open Routes — No Token Needed

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — server info & status |
| `POST` | `/api/v2/token` | 🤝 **Request a handshake token** (Step 1 of 3-way handshake) |

### 🔒 Handshake-Guarded Routes — `X-Client-Token` Header Required

> All `/api/v1/` routes require a valid `X-Client-Token` from the handshake step.

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/v1/auth/login` | Handshake only | Login with email & password, returns JWT |
| `POST` | `/api/v1/users/register` | Handshake only | Register a new user account |
| `GET` | `/api/v1/users/public-posts` | Handshake only | Sample public route |

### 🔐 Fully Protected Routes — Handshake + JWT Required

| Method | Endpoint | Role | Description |
|---|---|---|---|
| `GET` | `/api/v1/users/me` | `user` | Get the authenticated user's profile |

---

## 🤝 3-Way Client Handshake — Bot Protection

> **The Problem:** Bots, scrapers, and automated scripts can hammer your API endpoints — flooding your database, abusing your auth routes, and burning your server resources — all without ever being a real user.
>
> **The Solution:** Before a client can call *any* `/api/v1/` route, it must first **prove it is a live client** by completing a lightweight 3-step handshake. Bots that blindly fire requests skip this step and get blocked instantly with `403 Forbidden`.

### How It Works

```
  CLIENT                                          SERVER
    │                                               │
    │  ── STEP 1 ──────────────────────────────►  │
    │     POST /api/v2/token                        │
    │     (no headers needed)                       │  generates a JWT
    │                                               │  that expires in
    │  ◄─────────────────────────────────────────  │  exactly 5 seconds
    │     { "token": "eyJ..." }  ⏱️ 5s TTL         │
    │                                               │
    │  ── STEP 2 ──────────────────────────────►  │
    │     POST /api/v1/auth/login                   │
    │     X-Client-Token: eyJ...                    │  validates token:
    │     { email, password }                       │  ✅ exists?
    │                                               │  ✅ not expired?
    │                                               │  ✅ passed: true?
    │  ◄─────────────────────────────────────────  │
    │     { "token": "<JWT access token>" }        │
    │                                               │
    │  ── STEP 3 ──────────────────────────────►  │
    │     GET /api/v1/users/me                      │
    │     X-Client-Token: eyJ...  (new one)         │  RBAC check
    │     Authorization: Bearer <JWT>               │  role verified
    │  ◄─────────────────────────────────────────  │
    │     { "user": { ... } }                      │
```

### Why This Stops Bots

| Scenario | Result |
|---|---|
| Bot hits `/api/v1/auth/login` directly | `403` — Missing client handshake token |
| Bot replays an old handshake token | `403` — Handshake token expired (5s TTL) |
| Bot sends a forged/invalid token | `403` — Invalid client token |
| Bot is too slow (>5s between steps) | `403` — Handshake token expired |
| Legitimate client follows all 3 steps | `200` — Access granted ✅ |

### Key Files

| File | Role |
|---|---|
| `contexts/routers_v2.py` | Issues the short-lived handshake token via `POST /api/v2/token` |
| `helpers/auth_helpers.py` → `create_handshake_token()` | Mints a **strictly 5-second** JWT — expiry cannot be overridden |
| `contexts/check_client.py` | FastAPI dependency that validates `X-Client-Token` on every `/api/v1/` request |
| `main.py` | Applies `check_client` as a **global dependency** on the entire `api_v1` router |

### Implementation Peek

```python
# main.py — the entire v1 API is protected by the handshake guard
app.include_router(api_v1, prefix="/api/v1", dependencies=[Depends(check_client)])
app.include_router(security_router, prefix="/api/v2")  # token issuer — open
```

```python
# helpers/auth_helpers.py — 5-second token, no exceptions
def create_handshake_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(seconds=5)  # strictly enforced
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
```

```python
# contexts/check_client.py — the gate guard
async def check_client(request: Request):
    client_token = request.headers.get("X-Client-Token")
    if not client_token:
        raise HTTPException(403, "Missing client handshake token. Bot activity suspected.")
    payload = verify_access_token(client_token)   # raises if expired or invalid
    if not payload.get("passed"):
        raise HTTPException(403, "Invalid handshake token structure.")
    return True
```

> 💡 **Dev Tip:** During local development, you can bypass the handshake by uncommenting `return True` at the top of `check_client()` in `contexts/check_client.py`.

---

## 🔐 Authentication Flow

```
┌──────────┐   X-Client-Token: eyJ...        ┌──────────────┐
│  Client  │  ──────────────────────────►   │  FastAPI App │
│          │   POST /api/v1/auth/login        │              │
│          │   { email, password }           │  check_client│
│          │  ◄──────────────────────────   │  validates + │
│          │   { token: "eyJ..." }           │  issues JWT  │
│          │                                 │              │
│          │   X-Client-Token: eyJ... (new)  │              │
│          │   GET /api/v1/users/me           │              │
│          │   Authorization: Bearer eyJ...  │              │
│          │  ──────────────────────────►   │  RBAC check  │
│          │  ◄──────────────────────────   │              │
│          │   { user: { ... } }             │              │
└──────────┘                                 └──────────────┘
```

1. **Handshake** → `POST /api/v2/token` — get a short-lived `X-Client-Token` (5s TTL)
2. **Register** → `POST /api/v1/users/register` with `X-Client-Token` header + `name`, `email`, `password`
3. **Login** → `POST /api/v1/auth/login` with `X-Client-Token` header — receive a signed **JWT token** (30-day expiry)
4. **Access protected routes** → Pass both `X-Client-Token` (fresh) + `Authorization: Bearer <token>` headers
5. **RBAC** → Routes enforce roles (e.g., `user`, `admin`) via the `verify_token("role")` dependency

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

- [x] 🤝 3-Way Client Handshake bot protection
- [ ] 🔄 Refresh token support
- [ ] 📧 Email verification on registration
- [ ] 🧪 Pytest test suite with async support
- [ ] 🐳 Docker + Docker Compose setup
- [ ] 📊 Request logging middleware
- [ ] 🔑 API key authentication option
- [ ] 🤖 Ollama chat endpoint example
- [ ] ⏱️ Handshake rate-limiter (max N tokens per IP per minute)

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
