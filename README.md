# 📚 Smart Study Companion

Smart Study Companion is a Python-based Command Line Interface (CLI) application that helps students track daily study sessions, analyze subject-wise study time, and automatically identify weak subjects.

The application records study data, summarizes learning patterns, and helps improve study efficiency using simple analytics.

---

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.x

---

## Features
- Add study sessions with subject and duration
- View all recorded study sessions
- Get subject-wise study summary
- Automatically identifies the weakest subject based on total time spent
- Simple and interactive command-line interface
- Persistent data storage using file handling

---

## How It Works
The program allows users to enter study sessions with subject name and duration.
All study data is stored persistently in a text file (data.txt).
The application reads stored data and calculates total time spent per subject.
The subject with the least total study time is identified as the weakest subject.
All interactions are handled through a simple CLI menu.

---

## Technologies Used
- Python
- File Handling
- Dictionaries & Lists
- Command Line Interface (CLI)

---

## Project Structure

smart-study-companion/
│
├── study_tracker.py
├── data.txt
├── README.md
└── .gitignore  

