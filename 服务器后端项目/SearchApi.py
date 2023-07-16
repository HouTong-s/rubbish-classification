from typing import Optional
from fastapi import FastAPI, File, UploadFile,Form
import json
import random
import os
import uvicorn
from fastapi.param_functions import Body, Query
from keywordsearch import Ksearch
from getPictures import getpictures
app = FastAPI()
arrs = ['可回收垃圾','干垃圾','湿垃圾','有害垃圾']
brrs = ['可回收垃圾','其他垃圾','厨余垃圾','有害垃圾']
MyKeywordSearch = Ksearch()
MyGetPictures = getpictures()


@app.post("/getPictures/") #接口名称

async def getPictures(class1: str = Body(...),class2:Optional[str] = Body(None)):
    return MyGetPictures.get(class1,class2)
    
@app.get("/searchByKeyword/") #接口名称
async def searchByKeyword(keyword: str = Query(...)):
    return MyKeywordSearch.search(keyword)
if __name__ == "__main__":
    uvicorn.run("SearchApi:app", host="0.0.0.0", port=81, log_level="info")