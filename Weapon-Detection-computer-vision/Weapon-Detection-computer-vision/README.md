Weapon Detection using Computer Vision (YOLOv8)
=>Project Overview

This project demonstrates a Computer Vision–based weapon detection prototype using YOLOv8 and OpenCV.
The system processes images and highlights potential weapon-related regions while suppressing non-relevant background information.

This project is designed as a proof-of-concept for intelligent surveillance systems.

=>Problem Statement

Manual monitoring of surveillance footage is inefficient and prone to human error.
This project aims to assist security systems by automatically detecting weapons in images, enabling faster response and improved public safety.

=>Technologies Used

Python 3.10

YOLOv8 (Ultralytics)

OpenCV

NumPy

=>How the System Works

1.An input image is provided to the system.

2.YOLOv8 performs object detection.

3.The system filters detections related to weapons.

4.Non-weapon regions are masked (blacked out).

5.The final output highlights detected weapon areas.

6.The processed output is displayed and saved automatically.

=> How to Run the Project

1.Install required dependency:

pip install ultralytics


2.Place the test image in the project folder and rename it as:

test.jpg


3.Run the program:

python detect_weapon.py


4.Output will be:

Displayed in a window

5.Saved as output.jpg in the same folder

=> Sample Output

Only weapon-related regions are highlighted.

All non-relevant objects are hidden.

Output image is saved for review and submission.

=> Limitations

The default YOLOv8 model is trained on the COCO dataset, which does not include firearm classes.As a result, firearm detection accuracy is limited.
For real-world deployment, a custom-trained weapon dataset would be required.

=>Future Enhancements

>Train YOLO on a custom weapon dataset

>Extend detection to real-time CCTV video streams

>Integrate alert and notification system

>Improve low-light detection performance


## Model Information
This project uses the YOLOv8 pre-trained model provided by Ultralytics.
The model file (yolov8n.pt) is automatically downloaded at runtime and is
not included in this repository to keep it lightweight.


=> Academic Note

This project was developed as part of a PEPC Computer Vision requirement and demonstrates practical application of object detection techniques.

## Team Members
1. AC.Oliviya 
2. S.Mohammed Afzal
3. R.Mary Mofisha

