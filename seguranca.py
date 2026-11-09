from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
import jwt  
from passlib.context import CryptContext  

app = FastAPI(title="Clubinho Secreto API")

# ---------------------------------------------------------
#  FERRAMENTAS DE SEGURANÇA
# ---------------------------------------------------------

SECRET_KEY = "super_segredo_do_criador"
ALGORITHM = "HS256"

# Configurando o (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


banco_de_dados_usuarios = {}


# ---------------------------------------------------------
# (Pydantic)
# ---------------------------------------------------------
class CadastroSchema(BaseModel):
  username: str = Field(..., min_length=3)
  senha: str = Field(..., min_length=6)
  cargo: str = Field(
      "usuario", description="Pode ser 'usuario' ou 'admin'"
  )  # RBAC!


class LoginSchema(BaseModel):
  username: str
  senha: str


# Funções auxiliares de segurança
def criar_hash_senha(senha_normal: str):
  return pwd_context.hash(senha_normal)


def verificar_senha(senha_digitada: str, senha_hash: str):
  return pwd_context.verify(senha_digitada, senha_hash)


def criar_token_jwt(dados: dict):
  return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)


# ---------------------------------------------------------
#  AS ROTAS DA API
# ---------------------------------------------------------


#  Cadastrar novo membro 
@app.post("/cadastro")
async def cadastrar(dados: CadastroSchema):
  try:
    if dados.username in banco_de_dados_usuarios:
      raise ValueError("Esse nome de usuário já existe!")

    # Protegendo a senha 
    senha_segura = criar_hash_senha(dados.senha)

    # Salvando no "banco"
    banco_de_dados_usuarios[dados.username] = {
        "username": dados.username,
        "senha_hash": senha_segura,
        "cargo": dados.cargo,
    }

    return {
        "mensagem": f"Membro {dados.username} cadastrado com sucesso como"
        f" {dados.cargo}!"
    }

  except ValueError as erro:
    raise HTTPException(status_code=400, detail=str(erro))


#  (JWT)
@app.post("/login")
async def login(dados: LoginSchema):
  try:
    usuario = banco_de_dados_usuarios.get(dados.username)

    
    if not usuario or not verificar_senha(dados.senha, usuario["senha_hash"]):
      raise HTTPException(
          status_code=401, detail="Usuário ou senha incorretos!"
      )

   
    payload = {"sub": usuario["username"], "cargo": usuario["cargo"]}
    token_vip = criar_token_jwt(payload)

    return {
        "access_token": token_vip,
        "token_type": "bearer",
        "mensagem": "Parabéns, aqui está seu crachá VIP!",
    }

  except HTTPException as erro:
    raise erro
  except Exception:
    raise HTTPException(status_code=500, detail="Erro interno no servidor.")



@app.get("/sala-comum")
async def sala_comum(token: str):
  try:
    
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return {
        "mensagem": f"Bem-vindo à sala comum, {payload['sub']}! Divirta-se."
    }
  except jwt.PyJWTError:
    raise HTTPException(
        status_code=401, detail="Crachá inválido ou falsificado!"
    )


#  (Controle de Acesso RBAC )
@app.get("/sala-do-chefe")
async def sala_do_chefe(token: str):
  try:
   
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    
    if payload.get("cargo") != "admin":
      raise HTTPException(
          status_code=403,
          detail="Acesso negado! Esta sala é só para Administradores.",
      )

    return {
        "mensagem": (
            "Parabéns Chefe! Você entrou na sala secreta de administração."
        )
    }

  except jwt.PyJWTError:
    raise HTTPException(status_code=401, detail="Crachá inválido!")
  except HTTPException as erro:
    raise erro