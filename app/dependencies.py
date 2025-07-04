from fastapi import Header, HTTPException
from typing import Annotated

async def get_token_header(x_token: Annotated[str, Header()]):

    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header inválido")

async def get_query_token(token: str):

    if token != "jessica":
        raise HTTPException(status_code=400, detail="Token Jessica não fornecido")