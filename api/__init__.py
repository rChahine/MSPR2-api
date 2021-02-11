from fastapi import FastAPI
from api.authentication.routes import router as AuthRouter
from api.upload.routes import router as UploadRouter

app = FastAPI(
    title="MSPR2"
)

app.include_router(AuthRouter)
app.include_router(UploadRouter)
