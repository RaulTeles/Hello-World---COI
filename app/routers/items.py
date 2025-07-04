from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header, get_query_token

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/")
async def read_items():

    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id: str):

    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str, token: str = Depends(get_query_token)):

    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="Você só pode atualizar o item: plumbus"
        )
    return {"item_id": item_id, "message": "Item atualizado com sucesso!"}