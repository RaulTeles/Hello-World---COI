from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def update_admin():
    return "Acesso concedido para o admin"