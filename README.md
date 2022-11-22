# Algeo02-21099
<h2 align="center">
  🤖 Simple Face Recognition 🤖<br/>
</h2>
<hr>

> Live demo [_here_](https://www.youtube.com/watch?v=xm5gqvvVv0k&ab_channel=MohammadRifqiFarhansyah). 

<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Line-00C300?style=for-the-badge&logo=line&logoColor=white">
</p>

## Table of Contents
1. [General Info](#general-information)
2. [Member List](#member-list)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
7. [Structure](#structure)
8. [Project Status](#project-status)
9. [Room for Improvement](#room-for-improvement)
10. [Acknowledgements](#acknowledgements)
11. [Contact](#contact)

<a name="general-information"></a>

## General Information
A simple face recognition GUI that utilizing the Eigen Concepts of matrices using Tkinter, OpenCV, PIL, numpy, etc.

<a name="member-list"></a>

## Member List

| Nama                  | NIM      |
| --------------------- | -------- |
| Vieri Fajar Firdaus   | 13521099 |
| M. Rizky Sya'ban      | 13521119 |
| M. Rifqi Farhansyah   | 13521166 |

<a name="features"></a>

## Features
- Upload your photo or use the webcam of your device to take a realtime photos
- The result of comparison between the uploaded photo with the eigen face database
- Download the result (input image and closest image) as a PDF file

<a name="technologies-used"></a>

## Technologies Used
- CustomTkinter - version 4.6.3
- OpenCV2 - version 4.5.4
- PIL - version 8.4.0
- fpdf - version 1.7.2
- numpy - version 1.21.3
- sys - version 3.9.4
- tkinter - version 8.6

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
You can setup your project by cloning this repository and install the libraries above.

For specific version of the libraries, please check the `requirements.txt` file. You can install the libraries by using the command below.

```bash
pip install -r requirements.txt
```

<a name="usage"></a>

## Usage
You can run the program by using the command below.

```bash
python main.py
```

<a name="screenshots"></a>

## Screenshots
<p align=center>
  <img src="//image//ss//ss_1.png">
  <img src="//image//ss//ss_2.png">
  <img src="//image//ss//ss_3.png">
</p>

<a name="structure"></a>

## Structure
```bash
│   data3.csv
│   detcted.jpg
│   face.jpg
│   README.md
│   requirement.txt
│
├───.vscode
│       settings.json
│
├───doc
│       Tubes2-Algeo-2022.pdf
│
├───image
│   │   folder.jpg
│   │   icon.png
│   │   nf.jpg
│   │   nim.png
│   │   no_imagejpg.jpg
│   │   rifki.jpg
│   │   Success.ico
│   │
│   └───ss
│           ss_1.png
│           ss_2.png
│           ss_3.png
│
├───result
│       1.png
│       10.png
│       2.png
│       3.png
│       4.png
│       5.png
│       6.png
│       7.png
│       8.png
│       9.png
│
├───src
│   │   main.py
│   │
│   ├───eigenface
│   │   │   driver.py
│   │   │   dummyeigen.py
│   │   │   dummyfile.py
│   │   │   eigen.py
│   │   │   eigenfaces.py
│   │   │   QRDecomposition.py
│   │   │   SVD.py
│   │   │   tes.py
│   │   │
│   │   └───__pycache__
│   │           driver.cpython-37.pyc
│   │           driver.cpython-39.pyc
│   │           dummyeigen.cpython-39.pyc
│   │           eigen.cpython-37.pyc
│   │           eigen.cpython-39.pyc
│   │           eigenfaces.cpython-37.pyc
│   │           eigenfaces.cpython-39.pyc
│   │           QRDecomposition.cpython-37.pyc
│   │           QRDecomposition.cpython-39.pyc
│   │
│   ├───etc
│   │       haarcascade_frontalface_alt2.xml
│   │
│   ├───GUI
│   │   │   coba.py
│   │   │
│   │   └───__pycache__
│   │           main.cpython-39.pyc
│   │
│   └───imageprocess
│       │   dl2.py
│       │   driver.py
│       │   face.py
│       │   imageprocessing.py
│       │   inputpicture.py
│       │   resizing.py
│       │
│       └───__pycache__
│               imageprocessing.cpython-37.pyc
│               imageprocessing.cpython-39.pyc
│
├───test
│   ├───Coba_coba
│   │   ├───DataCoba
│   │   │   ├───Adriana
│   │   │   │
│   │   │   ├───Alex
│   │   │   │
│   │   │   ├───Alexandra
│   │   │   │
│   │   │   ├───Alvaro
│   │   │   │
│   │   │   └───Alycia
│   │   │
│   │   ├───data_100
│   │   │
│   │   ├───Data_Set
│   │   │   ├───pins_Adriana Lima
│   │   │   │
│   │   │   ├───pins_Alex Lawther
│   │   │   │
│   │   │   ├───pins_Alexandra Daddario
│   │   │   │
│   │   │   ├───pins_Alvaro Morte
│   │   │   │
│   │   │   ├───pins_alycia dabnem carey
│   │   │   │
│   │   │   ├───pins_Amanda Crew
│   │   │   │
│   │   │   ├───pins_amber heard
│   │   │   │
│   │   │   ├───pins_Andy Samberg
│   │   │   │
│   │   │   ├───pins_Anne Hathaway
│   │   │   │
│   │   │   └───pins_Anthony Mackie
│   │   │
│   │   ├───gray
│   │   │
│   │   ├───Input_DataSet
│   │   │   ├───Adriana_Lima
│   │   │   │
│   │   │   ├───Alexandra_Daddario
│   │   │   │
│   │   │   ├───Alex_Lawther
│   │   │   │
│   │   │   ├───Alvaro_Morte
│   │   │   │
│   │   │   └───Alycia_Dabnem_Carey
│   │   │
│   │   ├───kita
│   │   │
│   │   ├───resvieri
│   │   │
│   │   └───vieri
│   │
│   ├───Input
│   │   │
│   │   ├───live
│   │   │   ├───csv_file
│   │   │   │
│   │   │   ├───input
│   │   │   │
│   │   │   └───result
│   │   │
│   │   └───User_DataSet
│   │
│   └───Output
│           output.pdf
│
└───__pycache__
        imageprocessing.cpython-37.pyc
```

<a name="project-status">

## Project Status
Project is: _complete_

<a name="room-for-improvement">

## Room for Improvement
Room for Improvement:
- Optimalization of the code
- Adding more features

<a name="acknowledgements">

## Acknowledgements
- Thanks To Allah SWT
- This project was inspired by [Eigenface](https://en.wikipedia.org/wiki/Eigenface)
- Many thanks to [Dr. Ir. Rinaldi Munir, M.T.](https://informatika.stei.itb.ac.id/~rinaldi.munir/) for his guidance and support

<a name="contact"></a>

## Contact
<h4 align="center">
  Created by @Penggendong_Handal<br/>
  2022
</h4>
<hr>
