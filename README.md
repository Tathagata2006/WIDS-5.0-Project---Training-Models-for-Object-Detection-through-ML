# WIDS-5.0-Project---Training-Models-for-Object-Detection-through-ML
This includes the coding files created during learning, self-check assignments and the project submission files and updates regarding the WIDS project program conducted by the Finance Club of IIT Bombay.<br>

### Mentee and Project Details :
**Name :** Tathagata Roy <br>
**Roll No. :** 25B3954 <br>
**Project UID :** 11 <br>
**Project-Owner ID :** 14 <br> <br>
### Mentor Details :
**Name :** Mahaswi Ganipisetty <br>
**Roll No. :** 24B1101 <br><br>

## Steps done so far & procedure followed (Midterm Submission) :-
### 1. Basic Learning :
Gone through ‘opencv’ library modules from geeksforgeeks, etc. sites and learnt the basic functions used to detect corners, face, etc. from a YouTube playlist, provided by the mentor. Learning code files included in this repository.
### 2. Self Check Assignment :
Tried to solve the 'Self Check Assignment', as provided by the mentor, as much as possible. Code included in this repository.
### 3. CNN learning :
Gone through a youtube playlist on CNN and Image classification, as provided by the mentor which includes detailed analysis of image analysis and object detetion
modules.
### 4. Choosing topic (final) :
For training models (For the final project) the chosen object type to be detected is “Chocolates” (including wrappers). 
### 5. Data Collection :
Images (data set) of chocolates were collected from ‘Roboflow’ website and folders were created to train the model. <br><br>
**Screenshot for reference :**<br><br>
![report1](https://github.com/user-attachments/assets/5d7506a9-ddf3-42f3-b01f-7d557a33ea61) <br>
<br>
### 6. Labelling Images :
The images are labelled and modified accoring to Robosflow workflow, making them suitable and ready for model training.

### 7. Model Training :
The model training is executed through online Robosflow Workflow method. It's in progress, as of now. <br>
Few details :<br>
**checkpoint:** COCOs<br>
**Model type:** YOLOv11 Object Detection (Accurate)<br><br>
**Screenshot for reference :**<br><br>
![report2](https://github.com/user-attachments/assets/7194d9d9-37f7-4d73-9fdd-6762f0db9f2f) <br> <br>

## Further Steps and Workflow (Endterm Submission) :-

### 8. Modification of Dataset :
From across 25 websites, 100+ images were collected and made blurred and lowlight using openCV functions (as suggested by mentor) for better performance in training. The code file is saved as 'blurred_dataset.py'.

### 9. Annotation and Labeling  of New Dataset :
The new dataset was labeled and annotated using robosflow workspace to make it compatible with YOLO training procedure. The final dataset used for YOLO training is included in the repo.

### 9. Model Training through own YOLO Code :
A Yolo code 'train.py' was created to train the model for detecting chocolates, within proper confidence threshold limits. The code was run through 80 epochs with 146 images per epoch for a good training.

### 10. Testing and Validation :
The 'test.py' file created was used to test the performance after the model was trained.  It predicted the chocolates in an image with proper bounding boxes and confidence scored were also mentioned alongside, depicting a specific and better result.
