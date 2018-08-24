<p align="center">
  <img width="450" src="assets/logo-color.png" />
</p>

## Introduction

FEEDIE (pronounced `/ˈfi:di/`, combination of **feed** and **foodie**) is a feeding robot specially designed for people who couldn't eat or drink independently. According to our [survey](https://github.com/goolhanrry/Feeding-Robot-Demo/blob/master/assets/DataAnalysis.pptx?raw=true), over 15% of the families have at least one person who couldn't take care of himself while over 20% of them have a great demand for a robot to help them. One can interact and control the robot by natural language instructions. After receiving message from a user, FEEDIE can extract keywords from the instructions, find what they want on the table, and feed it into the user's mouth.

Our core techniques consist of **Speech Recognition**, **Image Recognition**, **Grabbing Algorithm** and **Human Computer Interaction**.

You can download and have a look at our warm up video by [clicking here](https://github.com/goolhanrry/Feeding-Robot-Demo/blob/master/assets/WarmUp.mp4?raw=true).

<p align="center">
  <img width="300px" src="assets/preview.gif" hspace="50px" />
  <img width="247px" src="assets/UI.gif" hspace="50px" />
</p>

## Hardware Configuration

* SainSmart DIY 6-Axis Servos Control Palletizing Robot Arm
* Arduino/Genuino 101 Board
* Logitech c270 web camera
* AC adapter

## Code Catalog

* Arduino code - Serial communication logic & food grabbing algorithm
* Classifier - [OpenCV](https://opencv.org/) cascade classifiers
* Flask - User Interaction module
* Modules *(abandoned)* - Speech & object recognition models
* Training - Cascade classifier training tool

## Author

Liu Ye, School of Resource and Environmental Science, Wuhan University

## License

[MIT License](LICENSE)

Copyright (c) 2018 goolhanrry
