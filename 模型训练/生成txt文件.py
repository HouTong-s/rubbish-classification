import os
import random
# -*- coding: utf-8 -*-
def traintxt1():
    file1 = os.listdir('./DATASET/TRAIN/R/')
    file2 = os.listdir('./DATASET/TRAIN/O/')
    files = file1+file2
    random.shuffle(files)
    train = open('./DATASET/train.txt','a')
    for file in files:
        if file[0] == 'R' :
            name =  './DATASET/TRAIN/R/' +  file + ' ' + str(0) +'\n' 
            train.write(name)
        elif file[0] == 'O' :
            name =  './DATASET/TRAIN/O/' +  file + ' ' + str(2) +'\n'
            train.write(name)
        else:
            pass
    train.close()

def testtxt1():
    file1 = os.listdir('./DATASET/TEST/R/')
    file2 = os.listdir('./DATASET/TEST/O/')
    files = file1+file2
    random.shuffle(files)
    test = open('./DATASET/test.txt','a')
    for file in files:
        if file[0] == 'R' :
            name =  './DATASET/TEST/R/' +  file + ' ' + str(0) +'\n' 
            test.write(name)
        elif file[0] == 'O' :
            name =  './DATASET/TEST/O/' +  file + ' ' + str(2) +'\n'
            test.write(name)
        else:
            pass
    test.close()

def testtxt2():
    folders = os.listdir('./DATASET/TEST/厨余垃圾/')
    test = open('./DATASET/test.txt','a',encoding='utf-8')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/厨余垃圾/'+folder)
        for file in files:
            test.write('./DATASET/TEST/厨余垃圾/'+folder+'/' + file+ ' ' + str(2) +'\n' )

    folders = os.listdir('./DATASET/TEST/可回收垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/可回收垃圾/'+folder)
        for file in files:
            test.write('./DATASET/TEST/可回收垃圾/'+folder+'/' + file+ ' ' + str(0) +'\n' )
    
    folders = os.listdir('./DATASET/TEST/其他垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/其他垃圾/'+folder)
        for file in files:
            test.write('./DATASET/TEST/其他垃圾/'+folder+'/' + file+ ' ' + str(1) +'\n' )
    
    folders = os.listdir('./DATASET/TEST/有害垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/有害垃圾/'+folder)
        for file in files:
            test.write('./DATASET/TEST/有害垃圾/'+folder+'/' + file+ ' ' + str(3) +'\n' )
    test.close()

def traintxt2():
    folders = os.listdir('./DATASET/TRAIN/厨余垃圾/')
    train = open('./DATASET/train.txt','a',encoding='utf-8')
    for folder in folders:
        files = os.listdir('./DATASET/TRAIN/厨余垃圾/'+folder)
        for file in files:
            train.write('./DATASET/TRAIN/厨余垃圾/'+folder+'/' + file+ ' ' + str(2) +'\n' )

    folders = os.listdir('./DATASET/TRAIN/可回收垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TRAIN/可回收垃圾/'+folder)
        for file in files:
            train.write('./DATASET/TRAIN/可回收垃圾/'+folder+'/' + file+ ' ' + str(0) +'\n' )
    
    folders = os.listdir('./DATASET/TRAIN/其他垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TRAIN/其他垃圾/'+folder)
        for file in files:
            train.write('./DATASET/TRAIN/其他垃圾/'+folder+'/' + file+ ' ' + str(1) +'\n' )

    folders = os.listdir('./DATASET/TRAIN/有害垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TRAIN/有害垃圾/'+folder)
        for file in files:
            train.write('./DATASET/TRAIN/有害垃圾/'+folder+'/' + file+ ' ' + str(3) +'\n' )
    train.close()

def deletefiles1():
    folders = os.listdir('./DATASET/TEST/厨余垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/厨余垃圾/'+folder)
        random.shuffle(files)
        length =len(files) * 0.85
        for i in range(0,int(length)):
            os.remove('./DATASET/TEST/厨余垃圾/'+folder+'/' + files[i])

def deletefiles2():
    folders = os.listdir('./DATASET/TEST/可回收垃圾/')
    for folder in folders:
        files = os.listdir('./DATASET/TEST/可回收垃圾/'+folder)
        random.shuffle(files)
        length =len(files) * 0.85
        for i in range(0,int(length)):
            os.remove('./DATASET/TEST/可回收垃圾/'+folder+'/' + files[i])

def traintxt3():
    folders = os.listdir('./DATASET/TRAIN/厨余垃圾/')
    train = open('./DATASET/train.txt','a',encoding='utf-8')
    for folder in folders:
        files = os.listdir('./DATASET/TRAIN/厨余垃圾/'+folder)
        for file in files:
                name =  './DATASET/TRAIN/厨余垃圾/'+folder+'/' +  file + ' ' + str(2) +'\n'
                train.write(name)
    train.close()

def renamefiles():
    folders = os.listdir('./DATASET/TRAIN/')
    for folder in folders:
        if folder!= 'O' and folder!='R':
            folders1 = os.listdir('./DATASET/TRAIN/'+folder+"/")
            for folder1 in folders1:
                files = os.listdir('./DATASET/TRAIN/'+folder+"/"+folder1+"/")
                for file in files:
                    if ' ' in file:
                        file1 = file.replace(' ','_')
                        os.rename('./DATASET/TRAIN/'+folder+"/"+folder1+"/"+file,'./DATASET/TRAIN/'+folder+"/"+folder1+"/"+file1)
    
    folders = os.listdir('./DATASET/TEST/')
    for folder in folders:
        if folder!= 'O' and folder!='R':
            folders1 = os.listdir('./DATASET/TEST/'+folder+"/")
            for folder1 in folders1:
                files = os.listdir('./DATASET/TEST/'+folder+"/"+folder1+"/")
                for file in files:
                    if ' ' in file:
                        file1 = file.replace(' ','_')
                        os.rename('./DATASET/TEST/'+folder+"/"+folder1+"/"+file,'./DATASET/TEST/'+folder+"/"+folder1+"/"+file1)
    
    folders = os.listdir('./DATASET/TEST/')
    for folder in folders:
        if folder!= 'O' and folder!='R':
            folders1 = os.listdir('./DATASET/TEST/'+folder+"/")
            for folder1 in folders1:
                files = os.listdir('./DATASET/TEST/'+folder+"/"+folder1+"/")
                for file in files:
                    if ' ' in file:
                        file1 = file.replace(' ','_')
                        os.rename('./DATASET/TEST/'+folder+"/"+folder1+"/"+file,'./DATASET/TRAIN/'+folder+"/"+folder1+"/"+file1)

def createtrain():
    traintxt1()
    traintxt2()

def createtest():
    testtxt1()
    testtxt2()

renamefiles()
createtest()

