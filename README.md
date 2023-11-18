# CIS 422 Cold Call System Project
January 30, 2022

# Introduction
The Cold-Call system provides the instructor functionality to view four random student names “on-deck”. Students that are “on-deck” can then formulate a response ahead of time, thus increasing student enthusiasm and participation. 

# Authors
Ginni Gallagher
Rebecca Hu
Xiang Hao
Riana Valenzuela

# Running the Cold Call System
The Cold-Call System is intended to run on Mac with version 10.13 or above. Additionally, Python v. 3.10 should be installed in order to run the system. 

Start by navigating to the directory where source code is located. To start the system, run the command:

```
python3 main.py
```

# First Time Usage
Before using the “on-deck” functionality, student data must be imported. Begin by pressing the “Import Data” button. A window will appear allowing you to choose a text file with student data. Note that only tab-delimited .txt files can be input in order to be parsed correctly. Text files should be formatted similarly to sample_data_40.txt with the same headers.

After selecting a file, a warning will appear stating that current data will be overridden. Select “yes”, or press “return”.  

The system is now ready for usage! 

Navigate to the "on-deck" window by pressing "Student View". To navigate through student names, start by pressing the right arrow key. You can now drop and flag students from the deck.

# Repository Overview
project_root/<br>
|- io_interface.py<br>
|- main.py<br>
|- queue_manager.py<br>
|- student_data.py<br>
|- student_view.py<br>
|- test_randomness.py<br>
|- sample_data_40.txt<br>
|- README.md<br>
|- .gitignore<br>
