#imports useful modules for the entirety of the code
# import PIL
# from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

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
        elif total_percentages == 100:
            messagebox.showwarning('Perfectly-optimized',f'Total percentage is 100%. Current total: {total_percentages}%t Perfectly Optimized.')

        else:
            messagebox.showwarning('Under-optimized',f'Total optimization percentage assigned: {total_percentages}%')

#sets logo image
image_path = '(path to the "np_logo.png" image on your own computer)'
logo_image = Image.open(image_path)
logo_image = logo_image.resize((150, 150))
logo_image = ctk.CTkImage(logo_image)
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
entry_frame = ctk.CTkFrame(canvas, width=1500, height=600)
canvas.create_window((0, 0), window=entry_frame, anchor="c")
#entry_frame = ctk.CTkFrame(mainwindow, width=600, height=600)
#entry_frame.pack(pady=10)

entries = {}

#creates labels and placeholder text
def create_factor_input(frame, text_factor, entry_placeholder, y_position, min_value, max_value):
    label = ctk.CTkLabel(frame, text=text_factor)
    label.place(x=600, y=y_position)

    entry = ctk.CTkEntry(frame, placeholder_text=entry_placeholder, width=175)
    entry.place(x=600, y=y_position + 30)

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
    button.place(x=900, y=y_position + 30)

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
