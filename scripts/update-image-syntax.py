#!/usr/bin/env python3
"""
Update image references in lesson files to use UU_LL_Name.png syntax
"""

import os
import re
import glob
from pathlib import Path

def convert_filename_to_underscore(filename):
    """Convert various filename formats to UU_LL_Name.png format"""
    # Remove .png extension for processing
    name = filename.replace('.png', '')
    
    # If it already follows UU_LL_Name format, return as-is
    if re.match(r'^\d{2}_\d{2}_', name):
        return filename
    
    # Handle UULL format like "01_01_MonoLakeModel"
    if re.match(r'^\d{2}_\d{2}_\w+', name):
        return filename
    
    # Convert dash-based names to underscores: "01-01-01-concepts" -> "01_01_Concepts"
    if re.match(r'^\d{2}-\d{2}', name):
        parts = name.split('-')
        if len(parts) >= 3:
            unit = parts[0]
            lesson = parts[1] 
            # Capitalize and join the remaining parts
            description = ''.join(word.capitalize() for word in parts[2:])
            return f"{unit}_{lesson}_{description}.png"
    
    # Handle underscore-based technical names
    # Convert snake_case to PascalCase for the description part
    words = name.split('_')
    if len(words) >= 2:
        # Check if first two words are numbers (UU LL format)
        try:
            unit = f"{int(words[0]):02d}"
            lesson = f"{int(words[1]):02d}" 
            # Convert remaining words to PascalCase
            description = ''.join(word.capitalize() for word in words[2:])
            return f"{unit}_{lesson}_{description}.png"
        except:
            pass
    
    # For generic technical names without UU_LL prefix, keep as descriptive name
    # Convert to PascalCase: "system_model_overview_diagram" -> "SystemModelOverviewDiagram"
    if words:
        description = ''.join(word.capitalize() for word in words)
        return f"{description}.png"
    
    # If no words found, return original filename
    return filename

def update_lesson_file(filepath):
    """Update all image references in a lesson file"""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find all image references: ![alt text](images/filename.png)
    image_pattern = r'!\[([^\]]*)\]\(images/([^)]+)\)'
    
    def replace_image_ref(match):
        alt_text = match.group(1)
        old_filename = match.group(2)
        
        # Convert filename to new format
        new_filename = convert_filename_to_underscore(old_filename)
        
        if old_filename != new_filename:
            print(f"  📝 {old_filename} -> {new_filename}")
        
        return f"![{alt_text}](images/{new_filename})"
    
    # Replace all image references
    content = re.sub(image_pattern, replace_image_ref, content)
    
    # Write back if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated image references")
    else:
        print(f"  📌 No changes needed")
    
    return content != original_content

def main():
    """Update all lesson files"""
    print("=" * 60)
    print("UPDATING IMAGE SYNTAX TO UU_LL_Name.png FORMAT")
    print("=" * 60)
    
    # Find all migrated lesson files (UU-LL-*.md format at root level)
    lesson_pattern = "[0-9][0-9]-[0-9][0-9]-*.md"
    lesson_files = glob.glob(lesson_pattern)
    
    if not lesson_files:
        print("❌ No lesson files found matching UU-LL-*.md pattern")
        return
    
    print(f"Found {len(lesson_files)} lesson files to update\n")
    
    updated_count = 0
    for filepath in sorted(lesson_files):
        if update_lesson_file(filepath):
            updated_count += 1
    
    print(f"\n✅ Processing complete!")
    print(f"📊 Updated {updated_count} of {len(lesson_files)} files")
    print("\nNew image naming convention:")
    print("  - UU_LL_DescriptiveName.png")
    print("  - Example: 04_01_WaterDemandConcepts.png")
    print("  - Reference: ![Title](images/04_01_WaterDemandConcepts.png)")

if __name__ == "__main__":
    main()
