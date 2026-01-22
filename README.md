# 📘 Smart Study Companion (SSC)

Smart Study Companion is a lightweight, Python-based **Command Line Interface (CLI)** application designed to help students track study sessions, analyze subject-wise effort, and identify weak areas using simple data-driven insights.

---

## Features

- **Study Session Tracking**  
  Log study sessions with subject names and durations.

- **Automatic Analytics**  
  Identifies the weakest subject based on total time spent.

- **Persistent Storage**  
  All data is stored locally in a flat file (`data.txt`) for easy access and portability.

- **Subject-wise Summary**  
  View total study time broken down by subject.

- **Interactive CLI**  
  Simple, menu-driven interface for fast input and retrieval.

---

## Requirements

- Python 3.x

---

## Installation

Clone the repository and navigate into the project directory:


git clone https://github.com/IshitaSajeev/smart-study-companion.git
cd smart-study-companion

---

##Quick Start

Run the application:
python study_tracker.py

Available Options:

- Add a Session – Enter subject name and study duration
- View Summary – Display total hours spent per subject
- Weak Subject Analysis – Identify the subject with least total study time

---

## How It Works

1. Users enter study sessions with subject names and durations.
2. Data is stored persistently in data.txt.
3. The application reads stored data and calculates:
- Total study time per subject
- The weakest subject based on minimum time spent
4. All interactions are handled through a simple CLI menu.

---

## Project Structure

smart-study-companion/
│
├── study_tracker.py
├── data.txt
├── README.md
└── .gitignore 

---

## Technologies Used
- Python
- File Handling
- Dictionaries & Lists
- Command Line Interface (CLI)

---

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.
 

