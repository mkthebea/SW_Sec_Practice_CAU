## YOLO ##
# colab에서 실습
import torch

model = torch.hub.load('ultralytics/yolov5','yolov5s')
im='https://thumb.mt.co.kr/06/2022/09/2022090513121359333_1.jpg/dims/optimize/'
results = model(im)
results.print()
results.show()

###############################

!git clone https://github.com/ultralytics/yolov5 #clone
%cd yolov5
%pip install -qr requirements.txt # install -q:quiet -r:requirements

import torch
import utils
display = utils.notebook_init() #checks

###############################
# 옵션 주기
!python detect.py --weights yolov5s.pt --img 640 --source ./data/images # for object detection 숫자는 128의 배수로(사진 크기)
display.Image(filename='runs/detect/exp/zidane.jpg', width=600)
# display.Image(filename='runs/detect/exp/bus.jpg', width=600)

###############################
# ms coco 사용하면
# 정확도 측정 가능
# ppt 7페이지의 그래프 결과가 나옴
!bash data/scripts/get_coco.sh --val
!python hon val.py --weights yolov5n6.pt yolov5m6.pt yolov5l6.pt --task study --data ./data/coco.yaml --img 640 --half --device 0 # 에러 뜸.. 뭔가 잘못됨