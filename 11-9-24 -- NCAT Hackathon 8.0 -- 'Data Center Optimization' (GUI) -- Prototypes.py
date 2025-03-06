#imports useful modules for the entirety of the code
import PIL
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
from tkinter import PhotoImage

#sets apperance theme and color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Makes a window object, sets size, and makes a title
mainwindow = ctk.CTk()
mainwindow.geometry('600x700')
mainwindow.title("Data Center Optimization")

#class for optimization pie chart
class OptimizationPieChart:
    def __init__(self, cooling=0.0, lighting=0.0, pc=0.0, nh=0.0, ss=0.0):
        self.cooling = cooling
        self.lighting = lighting
        self.pc = pc
        self.nh = nh
        self.ss = ss

#adds all user input percentages and prints a message telling current optimization power
    def assign_percentage(self):
        total_percentages = self.cooling + self.lighting + self.pc + self.nh + self.ss
        if total_percentages > 100:
            messagebox.showwarning('Over-optimized',f'Total percentage exceeds 100%. Current total: {total_percentages}%. Please adjust the values.')
        else:
            messagebox.showwarning('Under-optimized',f'Total optimization percentage assigned: {total_percentages}%')

#sets logo image
image_path = 'C:/Users/jadin/OneDrive/Documents/CS/Hackathon 8.0 - 11-9-24/np_logo.png'
logo_image = Image.open(image_path)
logo_image = logo_image.resize((150, 150))
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(mainwindow, image=logo_image, text='')
logo_label.pack(pady=10)

#makes title label
title_label = ctk.CTkLabel(mainwindow, text='Data Center Optimization', text_color='#0078c1', font=('8514oem', 50, 'bold', 'underline'))
title_label.pack(pady=10)

#sets the background image to black
canvas = ctk.CTkCanvas(mainwindow, bg='#1e1f22')
canvas.pack(side="left", fill="both", expand=True)

#makes and configures a scroll bar
scrollbar = ctk.CTkScrollbar(mainwindow, command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

#sets canvas size
entry_frame = ctk.CTkFrame(canvas, width=1000, height=600)
canvas.create_window((0, 0), window=entry_frame, anchor="c")
#entry_frame = ctk.CTkFrame(mainwindow, width=600, height=600)
#entry_frame.pack(pady=10)

entries = {}

#creates labels and placeholder text
def create_factor_input(frame, text_factor, entry_placeholder, y_position, min_value, max_value):
    label = ctk.CTkLabel(frame, text=text_factor)
    label.place(x=100, y=y_position)

    entry = ctk.CTkEntry(frame, placeholder_text=entry_placeholder, width=175)
    entry.place(x=100, y=y_position + 30)

#outputs a message if the input is too high or too low
    def on_button_click():
        try:
            entry_value = float(entry.get())
            if entry_value < min_value or entry_value > max_value:
                messagebox.showerror("Input Error", f"{text_factor} must be between {min_value}% and {max_value}%")
            else:
                print(f'{text_factor} Value: {entry_value}')
        except ValueError:
            messagebox.showerror("Input Error", f"Please enter a valid number for {text_factor}")

#creates button for entering values
    button = ctk.CTkButton(master=frame, text='Enter', command=on_button_click)
    button.place(x=300, y=y_position + 30)

    entries[text_factor] = entry

#text for placeholder values
create_factor_input(entry_frame, "Cooling:", "Enter between 40% and 60%", 50, 40, 60)
create_factor_input(entry_frame, "Lighting:", "Enter between 1% and 5%", 150, 1, 5)
create_factor_input(entry_frame, "Power Conversion:", "Enter between 6% and 16%", 250, 6, 16)
create_factor_input(entry_frame, "Hardware:", "Enter between 5% and 15%", 350, 5, 15)
create_factor_input(entry_frame, "Storage:", "Enter between 16% and 36%", 450, 16, 36)

#creates a scroll region
entry_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

#validates the input values from the user
def validate_inputs_and_create_chart():
    try:
        cooling = float(entries["Cooling:"].get())
        lighting = float(entries["Lighting:"].get())
        pc = float(entries["Power Conversion:"].get())
        nh = float(entries["Hardware:"].get())
        ss = float(entries["Storage:"].get())

        if not (40 <= cooling <= 60):
            messagebox.showerror("Input Error", "Cooling must be between 40% and 60%")
            return
        if not (1 <= lighting <= 5):
            messagebox.showerror("Input Error", "Lighting must be between 1% and 5%")
            return
        if not (6 <= pc <= 16):
            messagebox.showerror("Input Error", "Power Conversion must be between 6% and 16%")
            return
        if not (5 <= nh <= 15):
            messagebox.showerror("Input Error", "Hardware must be between 5% and 15%")
            return
        if not (16 <= ss <= 36):
            messagebox.showerror("Input Error", "Storage must be between 16% and 36%")
            return

#creates an instance for pie chart class
        pie_chart_instance = OptimizationPieChart(cooling, lighting, pc, nh, ss)
        pie_chart_instance.assign_percentage()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

#creates final check button
check_button = ctk.CTkButton(mainwindow, text="Check Total Optimization", command=validate_inputs_and_create_chart)
check_button.pack(pady=20, side='bottom', anchor='nw')

entry_frame.place(relx=0.5, rely=0.5, anchor='c')
mainwindow.mainloop()














#===================================================================

'''
# this is where all the libraries and modules are imported that
# are used throughout the entire code
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

# this sets the appearance mode and color theme
ctk.set_appearance_mode("dark")  # options to either change the theme to "dark" or "light"
ctk.set_default_color_theme("dark-blue")

# this function creates the main window
mainwindow = ctk.CTk()
mainwindow.geometry('600x700')  # this is the size of the window to fit elements
mainwindow.title("Data Center Optimization")


# lines 18-23 is responsible for finding the path of the logo image in the computer files
# and opening it in the window
image_path = 'C:/Users/bastr/Downloads/np_logo.png' # this is the path where the image is taken
logo_image = Image.open(image_path)
logo_image = logo_image.resize((150, 150))  # this is how the image can be sized/resized
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(mainwindow, image=logo_image, text='') # this creates the image and allows it to appear using the ctk.CTkLabel
logo_label.pack(pady=10) # 'pady' is used to add padding around the image vertically


# this creates a bold, underlined label for the title
title_label = ctk.CTkLabel(mainwindow, text='Data Center Optimization',text_color='black', font=('Agency FB', 50, 'bold', 'underline'))
title_label.pack(pady=10)


# this adds a frame to hold the inputs
entry_frame = ctk.CTkFrame(mainwindow, width=600, height=600)
entry_frame.pack(pady=10)

entries = {}

# this function is responsible for creating a label, text box
# and a button for each factor
def create_factor_input(frame, text_factor, entry_placeholder, y_position):
    # this controls where the factors are placed
    label = ctk.CTkLabel(frame, text=text_factor)
    label.place(x=100, y=y_position)

    # this is the space between the factors and the text boxes/enter buttons
    entry = ctk.CTkEntry(frame, placeholder_text=entry_placeholder, width=175)
    entry.place(x=100, y=y_position + 30)

    # this function is responsible for printing the value that is typed in from
    # the user in the text boxes
    def on_button_click():
        entry_value = entry.get()
        print(f'{text_factor} Value: {entry_value}')

    # this is responsible for positioning "Enter" buttons
    button = ctk.CTkButton(master=frame, text='Enter', command=on_button_click)
    button.place(x=300, y=y_position + 30)


# this function is responsible for checking if the values fall
# either below or above the asked thresholds for the inputs
def validate_inputs_and_create_chart():
    try:
        # Collect values and validate them
        cooling = float(entries["Cooling:"].get())
        lighting = float(entries["Lighting:"].get())
        pc = float(entries["Power Conversion:"].get())
        nh = float(entries["Hardware:"].get())
        ss = float(entries["Storage:"].get())

        # Define the valid ranges for each input
        if not (40 <= cooling <= 60):
            messagebox.showerror("Input Error", "Cooling must be between 40% and 60%")
            return
        if not (1 <= lighting <= 5):
            messagebox.showerror("Input Error", "Lighting must be between 1% and 5%")
            return
        if not (6 <= pc <= 16):
            messagebox.showerror("Input Error", "Power Conversion must be between 6% and 16%")
            return
        if not (5 <= nh <= 15):
            messagebox.showerror("Input Error", "Hardware must be between 5% and 15%")
            return
        if not (16 <= ss <= 36):
            messagebox.showerror("Input Error", "Storage must be between 16% and 36%")
            return

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")


# these lines call the 'create_factor_input' with the parameters for each factor
create_factor_input(entry_frame, "Cooling:", "Enter between 40% and 60%", 50)
create_factor_input(entry_frame, "Lighting:", "Enter between 1% and 5%", 150)
create_factor_input(entry_frame, "Power Conversion:", "Enter between 6% and 16%", 250)
create_factor_input(entry_frame, "Hardware:", "Enter between 5% and 15%", 350)
create_factor_input(entry_frame, "Storage:", "Enter between 16% and 36%", 450)

# this runs the entire mainwindow function as a loop
mainwindow.mainloop()
'''

#===================================================================
'''
class OptimizationPieChart:
    def __init__(self, cooling = 0.0, lighting = 0.0, pc = 0.0, nh = 0.0, ss = 0.0):
        self.cooling = cooling
        self.lighting = lighting
        self.pc = pc
        self.nh = nh
        self.ss = ss

    def assign_percentage(self):
        while True:
            total_percentages = 0.0

            while True:
                self.cooling = float(input('Assign cooling a percentage of optimization power: '))
                if self.cooling > 60:
                    print('Optimization percentage is too high for this category. Enter a lower value')
                elif self.cooling < 40:
                    print('Optimization percentage is too low for this category. Enter a higher value')
                else:
                    print('Good')
                    break
            total_percentages += self.cooling

            while True:
                self.lighting = float(input('Assign lighting percentage of optimization power: '))
                if self.lighting > 5:
                    print('Optimization percentage is too high for this category. Enter a lower value')
                elif self.lighting < 1:
                    print('Optimization percentage is too low for this category. Enter a higher value')
                else:
                    print('Good')
                    break
            total_percentages += self.lighting

            while True:
                self.pc = float(input('Assign percent of optimization power: '))
                if self.pc > 16:
                    print('Optimization percentage is too high for this category. Enter a lower value')
                elif self.pc < 6:
                    print('Optimization percentage is too low for this category. Enter a higher value')
                else:
                    print('Good')
                    break
            total_percentages += self.pc

            while True:
                self.nh = float(input('Assign percent of optimization network hardware: '))
                if self.nh > 15:
                    print('Optimization percentage is too high for this category. Enter a lower value')
                elif self.nh < 5:
                    print('Optimization percentage is too low for this category. Enter a higher value')
                else:
                    print('Good')
                    break
            total_percentages += self.nh

            while True:
                self.ss = float(input('Assign percent of optimization server & storage: '))
                if self.ss > 36:
                    print('Optimization percentage is too high for this category. Enter a lower value')
                elif self.ss < 16:
                    print('Optimization percentage is too low for this category. Enter a higher value')
                else:
                    print('Good')
                    break
            total_percentages += self.ss

            if total_percentages > 100:
                print(f'Total percentage exceeds 100%. Current total: {total_percentages}%. Please adjust the values.')
                continue
            else:
                print(f'Total optimization percentage assigned: {total_percentages}%')
                break


    def delete_percentage(self):
        pass

pie_chart1= OptimizationPieChart()
pie_chart1.assign_percentage()
'''