from fastapi import FastAPI
import uvicorn

from criptosem.api.views import router as criptosem_router


app = FastAPI()

app.include_router(criptosem_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host="0.0.0.0", port=8000)