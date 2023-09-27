import re
import subprocess
import plistlib
import json

# Extract the pod name and version from the line
def extract_pod_info(line):
    match = re.match(r'^\s*-\s+([^\s]+)\s+\(([^)]+)\)', line)
    if match:
        return match.group(1), match.group(2)
    return None, None

# Get license and git source information for the pod
def get_pod_info(pod_name):
    try:
        print("Analyzing...", str(pod_name))
        # Run the 'pod spec cat' command to get pod information
        result = subprocess.run(['pod', 'spec', 'cat', pod_name], capture_output=True, text=True)
        if result.returncode == 0:
            # Parse the result as JSON
            pod_info = json.loads(result.stdout)
            license = pod_info.get('license', 'Not specified')
            git_source = pod_info.get('source', {}).get('git', 'Not specified')
            return license, git_source
        else:
            return 'Error retrieving information', ''
    except Exception as e:
        return 'Error retrieving information', str(e)

# Path to the Podfile.lock file
file_path = 'Podfile.lock'

# Dictionary to store pod names and information
pod_info_dict = {}

# Read the file and extract information
with open(file_path, 'r') as file:
    lines = file.readlines()
    current_pod = None

    for line in lines:
        if line.startswith('    - '):
            pod_name, pod_version = extract_pod_info(line)
            if pod_name and pod_version:
                license, git_source = get_pod_info(pod_name)
                pod_info_dict[pod_name] = {
                    'version': pod_version,
                    'license': license,
                    'git_source': git_source
                }

# Write the information to a plist file
output_plist_path = 'pod_info.plist'
with open(output_plist_path, 'wb') as output_file:
    plistlib.dump(pod_info_dict, output_file)

print(f'Pod information written to: {output_plist_path}')
