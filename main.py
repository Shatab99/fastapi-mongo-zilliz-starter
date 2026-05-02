from fastapi import Depends, FastAPI, Query
import uvicorn
from contextlib import asynccontextmanager
from databases.db import connect_to_mongo, close_mongo_connection
from contexts.middleware import ContextMiddleware
from databases.zilliz_db import close_zilliz_connection, connect_to_zilliz
from contexts.api_gateway_v1 import api_v1
from contexts.error_handlers import setup_global_error_handlers
from contexts.check_client import check_client
from contexts.api_gateway_v2 import security_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize Ollama client or any other resources if needed
    print("Starting up...")
    await connect_to_mongo()
    
    # Uncommentwhen we have zilliz cloud account then we can connect to zilliz cloud and create collection
    # await connect_to_zilliz()
    yield
    await close_mongo_connection()

    # Uncommentwhen we have zilliz cloud account then we can connect to zilliz cloud and create collection
    # await close_zilliz_connection()
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.add_middleware(ContextMiddleware)
setup_global_error_handlers(app)


@app.get("/")
def read_root():
    return {"Server": "fastapi-bp-mongo-zilliz-ollama" , "message": "Welcome to the FastAPI boilerplate with MongoDB, Zilliz, and Ollama!" , "status": "running"}

# import all routers from v1
app.include_router(api_v1, prefix="/api/v1", tags=["API"], dependencies=[Depends(check_client)])
app.include_router(security_router, prefix="/api/v2", tags=["Handshake_me_please"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7008, reload=True)
