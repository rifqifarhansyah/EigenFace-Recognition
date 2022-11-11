from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from PyQt5 import *
from fpdf import FPDF

import datetime
import cv2
import customtkinter
import os

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
        global image_input
        super().__init__()

        self.cap = cv2.VideoCapture(0)
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
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing

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

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Open Camera",
                                                command=self.start_cam)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Execution Time:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_3.grid(row=5, column=0, pady=5, padx=10)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="00:00",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=6, column=0, pady=5, padx=10)

        self.label_spacing = customtkinter.CTkLabel(master=self.frame_left,
                                                text="",
                                                text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_spacing.grid(row=7, column=0, pady=5, padx=10)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Result",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_5.grid(row=8, column=0, pady=5, padx=10)
        

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Download",
                                                command=self.formating_output_file)
        self.button_5.grid(row=9, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=10, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=11, column=0, pady=10, padx=20, sticky="w")

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

    def open_file_dataset(self): # open file dialog for dataset
        self.filepath = filedialog.askopenfilename(title="Open a Text File", filetypes=(("jpg files","*.jpg"), ("png files","*.png"), ("jpeg files","*.jpeg")))
        file = open(self.filepath, encoding="latin1")
        image_data = Image.open(f"{self.filepath}").resize((255, 190), Image.ANTIALIAS)
        self.photo_data = ImageTk.PhotoImage(image_data)
        file.close()

    def open_file_image(self): # open file dialog for image
        self.filepath_image = filedialog.askopenfilename(title="Open a Text File", filetypes=(("jpg files","*.jpg"), ("png files","*.png"), ("jpeg files","*.jpeg")))
        file = open(self.filepath_image, encoding="latin1")
        image_input = Image.open(f"{self.filepath_image}")
        width, height = image_input.size
        if(width == height): 
            image_input = image_input
        offset = abs(width - height) // 2
        if(width > height):
            image_input = image_input.crop([offset, 0, width - offset, height]) # crop image
        else:
            image_input = image_input.crop([0, offset, width, height - offset])
        image_input = image_input.resize((720, 720), Image.ANTIALIAS) # resize the square image
        self.photo_input = ImageTk.PhotoImage(image_input) # convert to PhotoImage
        print_image = self.image_label1.configure(image=self.photo_input)
        file.close()

    def print_image(self): # print image
        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info1.grid(row=4, column=0, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label1 = customtkinter.CTkLabel(master=self.frame_info1, image=self.photo_input)
        self.image_label1.place(relx=0.5, rely=0.5, anchor=CENTER)        

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    # Defining stop_cam() to stop WEBCAM Preview
    def stop_cam(self):
        # Stopping the camera using release() method of cv2.VideoCapture()
        image_none = Image.open(PATH + "..\\..\\image\\folder.jpg")
        self.photo_input = ImageTk.PhotoImage(image=image_none)
        self.image_label1.configure(image=self.photo_input)
        self.cap.release()
        self.button_3.configure(text="Start Camera", command=self.start_cam)

    # Defining start_cam() to start WEBCAM Preview
    def start_cam(self):
        # Starting the camera using cv2.VideoCapture()
        self.img = self.cap.read()[1]
        self.imgBGR = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.cam = Image.fromarray(self.imgBGR)
        self.photo_input = ImageTk.PhotoImage(image=self.cam)
        self.image_label1.configure(image=self.photo_input)
        self.image_label1.after(20, self.start_cam)
        self.button_3.configure(text="Stop Camera", command=self.stop_cam)

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
        file_directory = filedialog.askdirectory()
        fpdf.output(os.path.join(file_directory, "output.pdf"))



if __name__ == "__main__":
    app = App()
    app.mainloop()