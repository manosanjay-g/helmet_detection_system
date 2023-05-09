from rest_framework.decorators import api_view
from  rest_framework.response import Response
import os
import cv2
import shutil
@api_view(['POST'])
def test(request):
   try:
      print(request.body)
      y=os.listdir("yolov5/runs/detect")
      # print("Working",request.FILES.get("image"))      
      # img = request.FILES.get("image")
      op = open('op.txt',"r")
      
      with open("file.jpeg", "wb") as f:
         f.write(request.body)
      with open("test.txt", "r") as file:
            i=file.readline()
      i=int(i)
      i+=1
      with open("test.txt", "w") as file:
         file.write(str(i))
      i-=1
      # cv2.imwrite("file.jpeg", img)
      x=os.system('python yolov5/detect.py --source file.jpeg --weights static/best.pt --conf 0.5')
      print(x)
      temp=cv2.imread(f"yolov5/runs/detect/exp{i}/file.jpeg")
      shutil.copy(f"yolov5/runs/detect/exp{i}/file.jpeg", f"static/file{i}.jpeg")
      return Response({"res":f"http://localhost:8080/static/file{i}.jpeg","conf":op.read()})
   except Exception as e:
      print(e)
      return Response()