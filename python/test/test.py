import os
import send2trash

fileDir = r'D:\Home\edison\ee_std\fw\project\func\Project\Obj'

files = ["api_lib.d"]

os.chdir(fileDir)
print(os.getcwd())

for i in range(len(files)):
    filePath = fileDir+"\\"+files[i]
    print(filePath)
    send2trash.send2trash(filePath)
