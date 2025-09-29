# Real-Time Face Recognition Attendance System

This project is a Python application that leverages computer vision to build an automated attendance system. It uses a live webcam feed to detect and recognize faces, matching them against a database of known individuals. Once a person is identified, their attendance is recorded in a CSV file with their name and a timestamp.



## 🚀 Features

-   **Real-Time Detection:** Identifies faces in a live video stream from a webcam.
-   **Accurate Recognition:** Uses the `face_recognition` library to compare detected faces with known faces.
-   **Automated Attendance:** Automatically records the name, date, and time of the first sighting of a person each day.
-   **CSV Logging:** Saves attendance records in a simple and clean `Attendance.csv` file.
-   **Dynamic Database:** Easily add new individuals by simply placing their image in the `ImagesAttendance` folder.

---

## 🛠️ Technologies Used

-   **Python 3**
-   **OpenCV:** For capturing video from the webcam and drawing on the frames.
-   **face_recognition:** A powerful library for face detection and recognition (built on dlib).
-   **NumPy:** For handling image arrays and numerical operations.

---

## ⚙️ Setup and Usage

Follow these steps to set up and run the project on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shash-135/Face-Recognition-Python-Project.git](https://github.com/shash-135/Face-Recognition-Python-Project.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Face-Recognition-Python-Project
    ```
3.  **Create your image database:**
    -   Create a folder named `ImagesAttendance` in the project directory.
    -   Add images of the people you want to recognize into this folder. Name the image files after the person (e.g., `Shashank Kumar.jpg`, `Elon Musk.png`).

4.  **Install the required libraries:**
    *(It is highly recommended to use a Python virtual environment)*
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    ```bash
    python main.py
    ```

A window will open showing your webcam feed. When a known face is detected, a green rectangle and the person's name will appear. The `Attendance.csv` file will be created or updated automatically.
