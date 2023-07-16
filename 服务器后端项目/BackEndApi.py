# -*- coding: utf-8 -*-
from fastapi import FastAPI, File, UploadFile
import os
import uvicorn
from fastapi.middleware.cors import  CORSMiddleware
from Predictor import predictor
mypredictor = predictor()
app = FastAPI()
origins = [
     "*",
  ]
  
app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}



@app.post("/uploadfile/") #接口名称

async def create_upload_file(file: UploadFile = File(...)):
    
    contents = await file.read()#接受的文件内容
    
    with open('./img/'+file.filename,'wb') as f:
        f.write(contents)
    
    PClass = mypredictor.predict('./img/'+file.filename)
    #os.remove('./img/'+file.filename)
    return {"filename": file.filename,"file_type": file.content_type,"class":PClass}#向前端返回文件名称和类型

if __name__ == "__main__":
    uvicorn.run("BackEndApi:app", host="0.0.0.0", port=80, log_level="info")

