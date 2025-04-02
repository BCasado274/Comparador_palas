from fastapi import FastAPI
from routers.palas import router as palas_router

app = FastAPI(
    title="Comparador de Palas de Pádel",
    version="1.0"
)

# Registrar rutas
app.include_router(palas_router, prefix="/palas", tags=["Palas"])
