### YoloV7_prj

## 项目需求 (详见requirements.txt)
* python == 3.13
* numpy == 1.23.4
* opencv-python == 4.5.5.62
* PyQt5 == 5.15.7
* onnxruntime == 1.13.1
## 内容
本项目使用yolov7-tiny.pt和yolov7.pt预训练权重，使其在onnx模型下进行运行，主要功能有以下几个：
* 支持视频、图片、本地摄像头、网络视频流、屏幕
* 实时帧数
* 重定向控制台输出到软件界面上
* 更改检测置信度、IOU阈值
* 显示/关闭锚框、更改锚框宽度及颜色
* 打印/隐藏检测结果
* 录制检测视频
* 保存实时截图、控制台记录
## 步骤
1. 官网下载yolov7代码和与训练权重文件yolov7.pt和yolov7-tiny.pt  https://gitcode.net/mirrors/WongKinYiu/yolov7.git 
2. 使用 YOLOv7 源码中 export.py 脚本，将 pytorch 模型转换为 onnx 模型，在cmd命令行中输入命令python export.py --weights yolov7-tiny.pt --grid --simplify，预训练权重文件转换成yolov7.onnx和 yolov7-tiny.pt.onnx。
![image](https://github.com/wangna123456/YoloV7_prj/assets/142497906/29d9110b-b183-4465-8fca-b58aec8585d5)
3. 使用yolov7.onnx和 yolov7-tiny.pt.onnx部署到onnx模型上，进行目标检测。
![image](https://github.com/wangna123456/YoloV7_prj/assets/142497906/32d9e139-04dc-48fe-a6b1-659c64b2c2b1)
4. 使用pyqt5构建GUI界面。
![image](https://github.com/wangna123456/YoloV7_prj/assets/142497906/2ed0c562-6432-4e16-841d-f246926bd430)
5. 运行Yolo2onnxDetectProjectDemo.py可以看到检测的可视化界面。
 ![image](https://github.com/wangna123456/YoloV7_prj/assets/142497906/85d111ec-de1e-4e2e-bb65-6767bfaa784f)
6. 利用pyinstaller将代码打包成.exe
![image](https://github.com/wangna123456/YoloV7_prj/assets/142497906/dc8205cf-887c-4ad4-a576-cbbf494291f3)
