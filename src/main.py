from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from PyQt5 import *
from fpdf import FPDF
from eigenface import driver
from imageprocess import imageprocessing

import numpy as np
import cv2
import customtkinter
import os
import time

start = time.time()
ss=time.time()
PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue") # you chan change the theme by "blue", "dark-blue", and "green"

BACKGROUND_COLOR_OFF = "#7e69a7"
TOGGLE_COLOR_OFF = "#aaaaff"
COLOR1_OFF = "#655596"
COLOR2_OFF = "#57409f"
BLACK_OFF = "#333333"
BACKGROUND_COLOR_ON = "#f8f8fa"
TOGGLE_COLOR_ON = "#d2d4dc"
COLOR1_ON = "#e5e6eb"
COLOR2_ON = "#c0c2ce"
BLACK_ON = "#afafaf"
BLACK = "black"

PATH = os.path.dirname(os.path.realpath(__file__))

# Defining ShowFeed() function to display webcam feed in the cameraLabel;

class App(customtkinter.CTk):

    WIDTH = 1600
    HEIGHT = 1200

    def __init__(self):
        super().__init__()

        self.cap = cv2.VideoCapture(2)
        self.status_cam = True
        self.title("Face Recognition GUI")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.iconphoto(False, PhotoImage(file=f"{PATH}..\\..\\image\\icon.png"))
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============
        self.image_input = Image.open(PATH + "..\\..\\image\\folder.jpg") # image in right columns(0)
        self.image_closest = Image.open(PATH + "..\\..\\image\\folder.jpg") # image in right columns(1)
        self.photo_input = ImageTk.PhotoImage(self.image_input)
        self.photo_closest = ImageTk.PhotoImage(self.image_closest)

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(9, weight=1)  # empty row as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Your DataSet",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=5, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Upload DataSet",
                                                command=self.open_file_dataset)
        self.button_1.grid(row=1, column=0, pady=10, padx=20)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Your Image",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=2, column=0, pady=5, padx=10)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Upload Image",
                                                command=self.open_file_image)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Camera",
                                                command=self.openCam)
        self.switch_1.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_left, text="Choose Camera :")
        self.label_mode1.grid(row=4, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=['0', '1', '2', '3'],
                                                        command=self.change_camera)
        self.optionmenu_2.grid(row=5, column=0, pady=10, padx=20)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Execution Time:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_3.grid(row=7, column=0, pady=5, padx=10)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="00:00:00",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=8, column=0, pady=5, padx=10)

        self.label_spacing = customtkinter.CTkLabel(master=self.frame_left,
                                                text="",
                                                text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_spacing.grid(row=9, column=0, pady=5, padx=10)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="",
                                                width=0,
                                                height=0)
        self.button_3.grid(row=10, column=0, pady=10, padx=20)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Result",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_5.grid(row=11, column=0, pady=5, padx=10)
        

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Download",
                                                command=self.formating_output_file)
        self.button_5.grid(row=12, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=13, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=14, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0,1), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.label_title = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Test Image",
                                              text_font=("Roboto Medium", -30))  # font name and size in px
        self.label_title.grid(row=1, column=0, pady=5, padx=10)
        self.label_title = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Closest Result",
                                              text_font=("Roboto Medium", -30))  # font name and size in px
        self.label_title.grid(row=1, column=1, pady=5, padx=10)
        
        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info1.grid(row=4, column=0, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label1 = customtkinter.CTkLabel(master=self.frame_info1, image=self.photo_input)
        self.image_label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_right)

        self.frame_info2.grid(row=4, column=1, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label2 = customtkinter.CTkLabel(master=self.frame_info2, image=self.photo_closest)
        self.image_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # set default values
        self.optionmenu_1.set("Light")
        self.optionmenu_2.set("0")

    def change_camera(self, value):
        self.camera = int(value)

    def open_file_dataset(self): # open file dialog for dataset
        imageprocessing.deleteFileinFolder("test\\Input\\User_DataSet")
        # imageprocessing.deleteFileinFolder("test\\Input\\live\\csv_file")
        self.dataset_file = filedialog.askdirectory()
        imageprocessing.InputFolderWithoutCrop(self.dataset_file)
        self.average, self.bestEigen, self.allImageCoordinate = driver.getTraining()
        messagebox.showinfo("Success", "Dataset Uploaded Successfully !")

    def open_file_image(self): # open file dialog for image
        if len(os.listdir(r"test\\Input\\User_DataSet")) == 0 :
            messagebox.showerror("Error", "Please Upload Dataset First")
        else :
            self.filepath_image = filedialog.askopenfilename(title="Open a Text File", filetypes=(("png files","*.png"), ("jpg files","*.jpg"), ("jpeg files","*.jpeg")))
            print("self filpath",self.filepath_image)
            start = time.time()
            file = open(self.filepath_image, encoding="latin1")
            self.image_input = Image.open(f"{self.filepath_image}")
            self.image1 = np.asarray(self.image_input)
            print("\n\n")
            print(self.image1.shape)
            print("\n\n")
            width, height = self.image_input.size
            if(width == height): 
                self.image_input = self.image_input
            offset = abs(width - height) // 2
            if(width > height):
                self.image_input = self.image_input.crop([offset, 0, width - offset, height]) # crop image
            else: 
                self.image_input = self.image_input.crop([0, offset, width, height - offset])
            self.image_input = self.image_input.resize((500, 500), Image.ANTIALIAS) # resize the square image
            self.photo_input = ImageTk.PhotoImage(self.image_input) # convert to PhotoImage
            self.image_label1.configure(image=self.photo_input)
            self.image_adjusted = imageprocessing.adjustOneImage(self.image1)
            self.path = driver.generateClosestImage(self.image_adjusted, self.dataset_file, self.average, self.bestEigen, self.allImageCoordinate)
            self.image2 = Image.open(f"{self.path}")
            self.image2 = self.image2.resize((500, 500), Image.ANTIALIAS) # resize the square image
            self.photo_closest = ImageTk.PhotoImage(self.image2)
            self.image_label2.configure(image=self.photo_closest)
            end = time.time()
            self.execution_time_print = (end - start)
            executionTime = round((end - start)*100)
            print(executionTime)
            ms = executionTime % 100
            executionTime = executionTime // 100
            if(executionTime<600):
                if(executionTime%60<10):
                    self.label_4.configure(text=f"0{(executionTime//60):.0f}:0{(executionTime%60):.0f}:{ms}")
                else:
                    self.label_4.configure(text=f"0{(executionTime//60):.0f}:{(executionTime%60):.0f}:{ms}")
            elif(executionTime>=600):
                if(executionTime%60<10):
                    self.label_4.configure(text=f"{(executionTime//60):.0f}:0{(executionTime%60):.0f}:{ms}")
                else:
                    self.label_4.configure(text=f"{(executionTime//60):.0f}:{(executionTime%60):.0f}:{ms}")
            file.close()

    def print_image(self): # print image
        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info1.grid(row=4, column=0, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label1 = customtkinter.CTkLabel(master=self.frame_info1, image=self.photo_input)
        self.image_label1.place(relx=0.5, rely=0.5, anchor=CENTER)        

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def openCam(self):
        if not self.status_cam:
<<<<<<< HEAD
            self.cap = cv2.VideoCapture(2)
=======
            self.cap = cv2.VideoCapture(self.camera)
>>>>>>> 631b3784d710d4e3a7a0cf2fef3f2e1167697ef3
            self.camera_status = "ON"
            self.status_cam = True
        if self.switch_1.get() == 1:
            self.img = self.cap.read()[1]
            self.imgBGR = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.cam = Image.fromarray(self.imgBGR)
            self.photo_input = ImageTk.PhotoImage(image=self.cam)
            self.image_label1.configure(image=self.photo_input)
            self.image_label1.after(20, self.openCam)
            if(time.localtime().tm_sec%20==0):
                dir_path = r'test\\Input\\live\\result'
                if("result.png" in os.listdir(dir_path)):
                    os.remove("test\\Input\\live\\result\\result.png")
                cv2.imwrite("test\Input\live\input\input.png", self.img)
                self.filepath_image = ("test/Input/live/input/input.png")
                imageprocessing.croppicture("test\Input\live\input\input.png", "test\Input\\live\\result\\result.png")
                if('result.png' in os.listdir(dir_path)):
                    start_time_cam = time.time()
                    self.image_cropped = Image.open("test//Input//live//result//result.png")
                    self.image_cropped2 = np.asarray(self.image_cropped)
                    self.path = driver.generateClosestImage(self.image_cropped2, self.dataset_file, self.average, self.bestEigen, self.allImageCoordinate)
                    self.image_matched = Image.open(self.path)
                    self.image_matched = self.image_matched.resize((500, 500), Image.ANTIALIAS) # resize the square image
                    self.photo_closest = ImageTk.PhotoImage(self.image_matched)
                    end_time_cam = time.time()
                    self.execution_time_print = (end_time_cam - start_time_cam)
                    executionTime = round((end_time_cam - start_time_cam)*100)
                    print(executionTime)
                    ms = executionTime % 100
                    executionTime = executionTime // 100
                    if(executionTime<600):
                        if(executionTime%60<10):
                            self.label_4.configure(text=f"0{(executionTime//60):.0f}:0{(executionTime%60):.0f}:{ms}")
                        else:
                            self.label_4.configure(text=f"0{(executionTime//60):.0f}:{(executionTime%60):.0f}:{ms}")
                    elif(executionTime>=600):
                        if(executionTime%60<10):
                            self.label_4.configure(text=f"{(executionTime//60):.0f}:0{(executionTime%60):.0f}:{ms}")
                        else:
                            self.label_4.configure(text=f"{(executionTime//60):.0f}:{(executionTime%60):.0f}:{ms}")
                    self.image_label2.configure(image=self.photo_closest)
                else :
                      # gambar tidak tersedia
                    # print("wajah ga terdeteksi")
                    self.image_none = Image.open(PATH + "..\\..\\image\\nf.jpg")
                    self.path = PATH + "..\\..\\image\\nf.jpg"
                    self.photo_closest = ImageTk.PhotoImage(self.image_none)
                    self.image_label2.configure(image=self.photo_closest)

        else:
            self.button_3.configure(text="", width=0, height=0)
            self.image_none = Image.open(PATH + "..\\..\\image\\folder.jpg")
            self.photo_input = ImageTk.PhotoImage(self.image_none)
            self.photo_closest = ImageTk.PhotoImage(self.image_none)
            self.image_label1.configure(image=self.photo_input)
            self.image_label2.configure(image=self.photo_closest)
            self.status_cam = False
            self.camera_status = "OFF"
            self.label_4.configure(text="00:00:00")
            self.cap.release()
            return

    def saveFile(self):
        # Save file as
        file = filedialog.asksaveasfile(mode='w', defaultextension=".pdf")
        if file is None:
            return
        self.pdf_file = self.formating_output_file 
        self.pdf_file.save(file)
    
    def formating_output_file(self):
        fpdf = FPDF()
        fpdf.add_page()
        fpdf.set_font("Arial", size=40)
        fpdf.text(20,20,txt="INPUT IMAGE:")
        fpdf.image(self.filepath_image, x=20, y=30, w=150)
        fpdf.add_page()
        fpdf.text(20,20,txt="CLOSEST IMAGE:")
        fpdf.image(self.path, x=20, y=30, w=150)
        fpdf.set_font("Arial", size=20)
        fpdf.text(20,270,txt=f"Execution Time: {self.execution_time_print:.2f} seconds")
        file_directory = filedialog.askdirectory()
        fpdf.output(os.path.join(file_directory, "output.pdf"))

if __name__ == "__main__":
    app = App()
    app.mainloop()