import os
import shutil

path = 'C:/Users/xcy/Desktop/'

list1 = os.listdir(path)

for dir1 in list1:
    try:
        if not os.path.exists(path+dir1):
            os.makedirs(path+dir1.split('.')[-1])
            shutil.move(path+dir1, path+dir1.split('.')[-1])
        else:
            shutil.move(path+dir1, path+dir1.split('.')[-1])
    except:
        pass
    
            
