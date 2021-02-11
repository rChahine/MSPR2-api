from fastapi import FastAPI
from api.authentication.routes import router as AuthRouter

app = FastAPI(
    title="MSPR2"
)

app.include_router(AuthRouter)