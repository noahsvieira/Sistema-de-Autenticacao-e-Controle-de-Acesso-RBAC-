<div align="center">

# 🛡️ FastAPI RBAC & JWT Authentication Service

**Secure RESTful API architecture engineered for Stateless Authentication and Granular Role-Based Access Control.**

![Python](https://img.shields.io/badge/Python-3.10+-000000?style=for-the-badge&logo=python&logoColor=00FF41)
![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=00FF41)
![JWT](https://img.shields.io/badge/JWT-Stateless-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=00FF41)
![OWASP](https://img.shields.io/badge/OWASP-Top_10_Security-000000?style=for-the-badge&logo=owasp&logoColor=00FF41)

</div>

---

## 🏗️ Architecture & Security Decisions (`Security by Design`)

This service implements robust backend security patterns to mitigate common web vulnerabilities and enforce strict access boundaries:

| Security Pillar | Technical Implementation |
| :--- | :--- |
| **🔐 Cryptographic Hashing** | Passwords are never stored in plaintext. Uses **Bcrypt** (`Passlib`) with automated salt generation to protect against brute-force and rainbow table attacks. |
| **🎟️ Stateless Authentication** | Issues and validates digitally signed tokens via **PyJWT** carrying configured expiration claims (`exp`), removing server-side session overhead. |
| **🛂 Granular Authorization (RBAC)** | Leverages FastAPI's Dependency Injection (`Depends`) to evaluate permissions and roles (`user` vs `admin`) before routing requests. |
| **🛡️ Payload Sanitization** | Strict input/output schema validation via **Pydantic** to block malformed data and prevent sensitive attribute leakage. |
| **🚦 Standardized Exception Handling** | Explicit HTTP status code mapping (`400`, `401`, `403`) preventing internal stack trace exposure. |

---

## 🔌 API Endpoints Specification

| Method | Endpoint | Description | Access Scope / Auth |
| :--- | :--- | :--- | :--- |
| `POST` | `/cadastro` | Registers a new identity with assigned role (`usuario` or `admin`). | 🔓 Public |
| `POST` | `/login` | Authenticates credentials and returns a signed `access_token` (Bearer JWT). | 🔓 Public |
| `GET` | `/sala-comum` | Protected resource accessible by any authenticated identity. | 🔑 `Bearer Token` (Any role) |
| `GET` | `/sala-do-chefe` | Administrative resource restricted by privilege validation. | 👑 `Bearer Token` (`role == admin`) |

---

## 🚀 Quick Start / Local Deployment

Follow these commands to clone and run the service locally:

```bash
# 1. Clone the repository and navigate to the directory
git clone [https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git](https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git)
cd Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-

# 2. Install dependencies
pip install fastapi uvicorn pydantic "passlib[bcrypt]" pyjwt

# 3. Launch the ASGI server
uvicorn seguranca:app --reload
