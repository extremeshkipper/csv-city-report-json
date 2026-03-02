# CSV City Report

A small Python project that processes CSV data and generates a city analytics report.

## 📌 Features

- Reads data from CSV file
- Converts age values to integers
- Calculates city statistics:
  - total count
  - total age
  - average age
- Finds top N cities by:
  - highest average age
  - highest count (if equal avg)
  - alphabetical order (if equal count)
- Saves final report to JSON

## 🛠 Technologies

- Python 3
- csv module
- json module

## ▶ How to run

```bash
python main.py

generate_full_report("people.csv", "report.json", 3)

Project structure

main.py — core logic

people.csv — input data

report.json — generated output
