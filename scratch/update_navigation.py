import os

def update_nav(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                # Determine depth to root
                rel_root = os.path.relpath(directory, root)
                if rel_root == ".":
                    prefix = ""
                else:
                    prefix = rel_root.replace(os.sep, "/") + "/"
                
                with open(filepath, 'r') as f:
                    content = f.read()
                
                if 'FreightDesign™' in content and 'logistics-web-design' not in content:
                    print(f"Updating {filepath}")
                    
                    # Pattern 1: Dropdown nav
                    old_nav = f'<a href="{prefix}freightdesign/index.html">FreightDesign™</a>'
                    new_nav = f'<a href="{prefix}freightdesign/index.html">FreightDesign™</a>\n                        <a href="{prefix}logistics-web-design/index.html">Logistics Web Design</a>'
                    
                    # Pattern 2: Footer nav
                    old_footer = f'<a href="{prefix}freightdesign/index.html">FreightDesign™</a>'
                    new_footer = f'<a href="{prefix}freightdesign/index.html">FreightDesign™</a>\n                <a href="{prefix}logistics-web-design/index.html">Logistics Web Design</a>'
                    
                    # Surgical replacement based on context
                    # Identifying navigation block vs footer block using indentation
                    content = content.replace(f'                        {old_nav}', f'                        {new_nav}')
                    content = content.replace(f'                {old_footer}', f'                {new_footer}')
                    
                    with open(filepath, 'w') as f:
                        f.write(content)

update_nav('/Users/alexander/Desktop/freightlabs')
