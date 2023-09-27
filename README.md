# PodsAnalyzer
This script allows you to analyze the installed CocoaPods in the project, providing a Property List (Plist) file as output containing information for each pod.

# Prerequisites
Ensure you have CocoaPods and Python installed on your system.

# Usage
To analyze the pods inside your project:
1. Clone this repository inside your project folder or simply download the podsAnalyzer.py file
2. Run the script using the command: **python podsAnalyzer.py**
    - If not working, use **python3 podsAnalyzer.py**
3. The gathered information for each CocoaPod will be saved to a Plist file that you will find inside the project folder

# Collected Information
For each pod, inside the Plist file you will find:
* Name
* Version
* License
* Git Source

# Example of the resulting plist file
<img width="691" alt="Screenshot 2023-09-27 alle 11 18 05" src="https://github.com/Longo97/PodsAnalyzer/assets/57667688/dc6cbe70-23cf-492d-97e7-89e9029263f6">
