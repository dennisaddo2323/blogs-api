from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from database import engine
import models 

models.Base.metadata.create_all(bind=engine)

origins=['http://localhost:5173']

app=FastAPI()
app.include_router(router=router)
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])



