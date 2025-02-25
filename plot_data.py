Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\user> py
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import csv
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def plot_data(csv_file_path: str):
...     results=[]
...     with open(csv_file_path, newline='') as csv_file:
...             csv_reader = csv.reader(csv_file, delimiter=',')
...             next(csv_reader)
...             for row in csv_reader:
...                     row = [cell.strip() for cell in row]
...                     if len(row) < 2:
...                             continue
...                     try:
...                             results.append((float(row[0]), float(row[1])))
...                     except ValueError:
...                             print(f"Incorrect data row: {row}")
...     if not results:
...             raise ValueError("No valid data found in CSV file")
...     results = np.array(results)
...     plt.plot(results[:, 0], results[:, 1])
...     plt.xlim([-0.05, 1.05])
...     plt.ylim([-0.05, 1.05])
...     plt.xlabel("Precision")
...     plt.ylabel("Recall")
...     plt.show()
...
>>> f = open("data_file.csv", "w")
>>> w = csv.writer(f)
>>> _ = w.writerow(["precision", "recall"])
>>> w.writerows([[0.013,0.951],[0.376,0.851],[0.441,0.839],[0.570,0.758],[0.635,0.674],[0.721,0.604],[0.837,0.531],[0.860,0.453],[0.962,0.348],[0.982,0.273],[1.0,0.0]])
>>> f.close()
>>> plot_data('data_file.csv')
>>>
