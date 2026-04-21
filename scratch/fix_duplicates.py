import os
import re

def fix_duplicates(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                
                new_lines = []
                last_line = None
                for line in lines:
                    # If line is target link and last line was also target link (maybe different indentation)
                    current_stripped = line.strip()
                    if 'logistics-web-design/index.html' in line:
                        if last_line and 'logistics-web-design/index.html' in last_line:
                            print(f"Skipping duplicate in {filepath}")
                            continue
                    
                    new_lines.append(line)
                    last_line = line
                
                if len(new_lines) != len(lines):
                    with open(filepath, 'w') as f:
                        f.writelines(new_lines)

fix_duplicates('/Users/alexander/Desktop/freightlabs')
