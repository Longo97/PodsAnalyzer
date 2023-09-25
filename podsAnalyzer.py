import os
import subprocess
import json
import plistlib


# Get the path of the directory where the script is located
base_folder = os.path.dirname(os.path.abspath(__file__))

# A list to store information for each subfolder
info_list = []

subfolders = [f.name for f in os.scandir(base_folder + "/Pods") if f.is_dir()]

# # Iterate over each subfolder and execute the pod spec command
for subfolder in subfolders:

    command = f"pod spec cat {subfolder}"  # Sostituisci con il tuo comando
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check the result
    if result.returncode == 0:
        # The command was executed successfully, parse the JSON output
        try:
            json_output = json.loads(result.stdout)
            info = {
                "name": json_output["name"],
                "version": json_output["version"],
                "license": json_output["license"],
                "git_source": json_output["source"]["git"]
            }
            info_list.append(info)

        except json.JSONDecodeError as e:
            print("Error during JSON analysis:", str(e))
    else:
        print("Error during command execution:", str(subfolder))

# plist file creation
plist_file_path = "info.plist"
with open(plist_file_path, 'wb') as plist_file:
    plistlib.dump(info_list, plist_file)

print("plist file created successfully:", plist_file_path)
