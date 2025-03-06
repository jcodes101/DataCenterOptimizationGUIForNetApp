# Data Center Optimization GUI Application

## Project Overview

This project is a graphical user interface (GUI) application built using Python, `customtkinter`, and `Pillow` libraries. The purpose of the application is to simulate and optimize the distribution of power and resources in a data center. It allows users to input specific optimization values for categories such as cooling, lighting, power conversion, hardware, and storage. The application then calculates the total percentage and provides feedback on whether the data center is under-optimized, perfectly optimized, or over-optimized.

## Key Features
- **Interactive GUI:** The application uses a clean and intuitive user interface powered by `customtkinter`.
- **Real-Time Input Validation:** Users input percentages for different data center optimization factors, and the application checks whether these values fall within valid ranges.
- **Optimization Feedback:** Based on user input, the application provides warnings and feedback on whether the total optimization percentage is over, under, or perfectly optimized.
- **Pie Chart Class Structure:** The project introduces an object-oriented class `OptimizationPieChart` that models the percentages for different factors of the data center and computes their total optimization.
- **Scrolling Interface:** The application allows the user to input and scroll through the data on the main window.

## Technologies Used
- **Python:** The core programming language used in the development of the application.
- **CustomTkinter:** A modern and highly customizable version of `tkinter` to enhance the aesthetics of the GUI.
- **PIL (Python Imaging Library):** Utilized to handle image manipulation and display a company logo on the interface.
- **Tkinter Messagebox:** Displays feedback messages based on the user's input.

## Project Structure
- **Main Application (`main.py`):** Contains the core functionality of the project, including GUI setup, data validation, and optimization feedback.
- **Image Handling:** A company logo is loaded and displayed within the main window using the `Pillow` library.
- **Class Definition (`OptimizationPieChart`):** Manages the percentages of optimization factors and provides logic to sum them up and display the results.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/data-center-optimization.git
   cd data-center-optimization
   ```

2. **Install the required Python dependencies**:
   ```bash
   pip install customtkinter pillow
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage Instructions

1. Open the application using the `python main.py` command.
2. Input percentages for the following data center factors:
   - **Cooling** (Enter between 40% and 60%)
   - **Lighting** (Enter between 1% and 5%)
   - **Power Conversion** (Enter between 6% and 16%)
   - **Hardware** (Enter between 5% and 15%)
   - **Storage** (Enter between 16% and 36%)
3. Click "Enter" for each factor to validate your input.
4. After entering all the values, click the **Check Total Optimization** button.
5. The application will display a message indicating whether the total optimization is perfect, under, or over-optimized.

## Optimization Logic

- The application checks that the sum of all input percentages does not exceed 100%.
- If the total optimization is 100%, a message indicating **"Perfectly Optimized"** is displayed.
- If the total is under 100%, the application informs the user how much optimization is still needed.
- If the total exceeds 100%, an **"Over-Optimized"** warning is shown, and the user is prompted to adjust the values.

## Future Improvements
- **Pie Chart Visualization:** Add a pie chart to visually represent the distribution of optimization percentages.
- **Enhanced Styling:** Further customize the `customtkinter` appearance and theme for better aesthetics.
- **Persistence:** Store input values and results in a file or database for future analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to use this application to simulate and optimize your data center's power distribution efficiently!
