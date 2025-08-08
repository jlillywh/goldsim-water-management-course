#!/usr/bin/env python3
"""
Migrate from nested lesson folders to ultra-flat structure

Converts:
  01-Getting-Started/Lesson_01-Welcome/lesson.md
  04-Water-Demand/Lesson_01-Introduction/lesson.md
  
To:
  01-01-welcome-to-the-course.md
  04-01-introduction-to-water-demand.md
  images/ (all images moved here)
"""

import os
import shutil
from pathlib import Path
import re


def main():
    course_root = Path(".")
    print("=" * 60)
    print("MIGRATING TO ULTRA-FLAT STRUCTURE")
    print("=" * 60)
    
    # Create global images directory
    global_images = course_root / "images"
    global_images.mkdir(exist_ok=True)
    print(f"✅ Created: {global_images}")
    
    # Find all current lesson.md files
    lesson_files = list(course_root.rglob("lesson.md"))
    print(f"\nFound {len(lesson_files)} lesson files to migrate")
    
    for lesson_file in lesson_files:
        print(f"\nProcessing: {lesson_file}")
        
        # Parse the path to get unit and lesson info
        # Example: 01-Getting-Started/Lesson_01-Welcome-to-the-Course/lesson.md
        parts = lesson_file.parts
        
        if len(parts) >= 3:
            unit_dir = parts[-3]  # "01-Getting-Started"
            lesson_dir = parts[-2]  # "Lesson_01-Welcome-to-the-Course"
            
            # Extract unit number
            unit_match = re.match(r'^(\d{2})', unit_dir)
            if not unit_match:
                print(f"  ⚠️  Could not parse unit number from: {unit_dir}")
                continue
            unit_num = unit_match.group(1)
            
            # Extract lesson number and name
            lesson_match = re.match(r'^Lesson_(\d+)-(.+)$', lesson_dir)
            if not lesson_match:
                print(f"  ⚠️  Could not parse lesson from: {lesson_dir}")
                continue
            
            lesson_num = lesson_match.group(1).zfill(2)  # Ensure 2 digits
            lesson_name = lesson_match.group(2)
            
            # Create new filename
            safe_name = lesson_name.lower().replace(' ', '-').replace('_', '-')
            new_filename = f"{unit_num}-{lesson_num}-{safe_name}.md"
            new_path = course_root / new_filename
            
            print(f"  📝 New name: {new_filename}")
            
            # Copy lesson.md to new location
            try:
                shutil.copy2(lesson_file, new_path)
                print(f"  ✅ Copied lesson content")
            except Exception as e:
                print(f"  ❌ Failed to copy lesson: {e}")
                continue
            
            # Move images from lesson folder to global folder
            lesson_images_dir = lesson_file.parent / "images"
            if lesson_images_dir.exists():
                moved_count = 0
                for img_file in lesson_images_dir.rglob("*.png"):
                    try:
                        # Move to global images folder
                        target_path = global_images / img_file.name
                        if not target_path.exists():
                            shutil.move(str(img_file), str(target_path))
                            moved_count += 1
                    except Exception as e:
                        print(f"    ⚠️  Could not move {img_file.name}: {e}")
                
                if moved_count > 0:
                    print(f"  📁 Moved {moved_count} images to global folder")
        
        else:
            print(f"  ⚠️  Unexpected path structure: {lesson_file}")
    
    print(f"\n✅ Migration complete!")
    print(f"\nNew structure:")
    print(f"  images/           ← All images here") 
    print(f"  01-01-*.md        ← All lessons here")
    print(f"  04-01-*.md")
    print(f"  07-03-*.md")
    print(f"\nYou can now delete the old unit directories if everything looks good!")


if __name__ == "__main__":
    main()
