# OpenCV_PongGame

<p align="center">
  <img width="460" height="300" src=https://github.com/AdityaNikhil/OpenCV_PongGame/blob/master/pong.gif>
</p>

This game is fully controlled with a pen in hand which is recognised by your PC's camera.<br>
For this project, I have particularly selected an **orange pen**, adjusted it's colour recognition in opencv.<br>
The explanation to this mini project will be explained in a blog post soon.

## Technologies used
1) Python == 3.6.4 <br>
2) CV2 == 4.2.0 <br> 
3) PyAutoGUI == 0.9.50

## How to run?
1) First off, make sure you have all the above softwares donwloaded correctly.<br>
2) Now run the **Stage.py** file. <br>
3) Take any colourful object and adjust the Trackbars, so that only your object is visible in result window.<br>
4) Now copy the HSV values(All trackbar values) and substitute those values in the lower_orange, upper_orange variables in **Main.py** file.
5) Now open Pong_Game folder and run **Pong.exe** and also run **Main.py** file.

<br> *In general this project is a mouse controlled with OpenCV by extracting contours off the object and substituting the positions of contours to pointer position.*