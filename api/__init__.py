from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.authentication.routes import router as AuthRouter
from api.upload.routes import router as UploadRouter
from .settings import TESTING
import sys


app = FastAPI(
    title="MSPR2"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(AuthRouter)
app.include_router(UploadRouter)

if TESTING:
    sys.exit(0)
