from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - paytmdev-coll-b595d18362e04e16a8e3b1dc85f80c0d',debug=False,docs_url='/nervous-clarke-fc7f17f6c8de11efb4b20242ac12000517/docs',openapi_url='/nervous-clarke-fc7f17f6c8de11efb4b20242ac12000517/openapi.json')

app.include_router(router, prefix='/nervous-clarke-fc7f17f6c8de11efb4b20242ac12000517/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()