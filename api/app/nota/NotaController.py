from fastapi import APIRouter, Depends
from pydantic import BaseModel
from nota.NotaService import NotaService

router = APIRouter(
    prefix = "/notas_casa",
    tags = ["notas_casa"]
)

# Pega o serviço
def get_nota_service() -> NotaService:
    return NotaService()

class Payload(BaseModel):
    url_notinha: str

@router.get('')
def pegar_nota_online(
    payload: Payload,
    notaService: NotaService = Depends(get_nota_service)
):
    url = payload.url_notinha
    html = notaService.buscar(url)
    dados = notaService.scrape(html)

    return dados 