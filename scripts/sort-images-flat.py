#!/usr/bin/env python3
r"""
Ultra-Simple Image Sorting for GoldSim Course

Moves UULL-named images from SnagIt to single global images folder.
No lesson folders needed - everything is flat!

Structure:
  goldsim-water-management-course/
  ├── images/                     ← ALL images here
  ├── 01-01-welcome.md           ← Lessons as individual files
  ├── 04-01-water-demand.md
  └── 07-03-wells.md

Usage:
    python sort-images-flat.py
    python sort-images-flat.py --dry-run
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from typing import List, Optional


def main():
    parser = argparse.ArgumentParser(description="Sort images to global images folder")
    parser.add_argument("--source", "-s", 
                       default=r"C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse",
                       help="SnagIt source directory")
    parser.add_argument("--course-root", "-c",
                       default=r"c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course",
                       help="Course root directory")
    parser.add_argument("--dry-run", "-d", action="store_true",
                       help="Preview without moving files")
    
    args = parser.parse_args()
    
    source_dir = Path(args.source)
    course_root = Path(args.course_root)
    global_images_dir = course_root / "images"
    
    print("=" * 60)
    print("ULTRA-SIMPLE IMAGE SORTING")
    print("=" * 60)
    print(f"Source: {source_dir}")
    print(f"Target: {global_images_dir}")
    
    if args.dry_run:
        print("\n*** DRY RUN MODE ***")
    
    # Create global images directory
    if not args.dry_run:
        global_images_dir.mkdir(exist_ok=True)
    
    # Find PNG files in SnagIt directory
    if not source_dir.exists():
        print(f"❌ SnagIt directory not found: {source_dir}")
        return 1
    
    png_files = list(source_dir.glob("*.png"))
    all_files = list(source_dir.iterdir())
    
    print(f"\nFound {len(png_files)} PNG files")
    print(f"Found {len(all_files) - len(png_files)} other files (will be ignored)")
    
    if not png_files:
        print("✅ No PNG files to process")
        return 0
    
    # Parse and process UULL files
    uull_pattern = re.compile(r'^(\d{2})\s+(\d{2})\s+([^-]+)-(\d+)-(.+)$')
    simple_pattern = re.compile(r'^(\d{2})\s+(\d{2})\s+(.+)$')
    
    processed = 0
    skipped = 0
    
    for png_file in png_files:
        filename_base = png_file.stem
        print(f"\nProcessing: {png_file.name}")
        
        # Try full UULL pattern first
        match = uull_pattern.match(filename_base)
        if match:
            unit, lesson, name, seq, desc = match.groups()
            new_name = f"{unit}-{lesson}-{seq.zfill(2)}-{desc.strip()}.png"
            print(f"  ✅ UULL: Unit {unit}, Lesson {lesson}")
        else:
            # Try simple pattern
            match = simple_pattern.match(filename_base)
            if match:
                unit, lesson, name = match.groups()
                new_name = f"{unit}-{lesson}-01-{name.strip().replace(' ', '-').lower()}.png"
                print(f"  ✅ Simple: Unit {unit}, Lesson {lesson}")
            else:
                print(f"  ⏭️  Skipping: Not UULL format")
                skipped += 1
                continue
        
        # Move to global images folder
        target_path = global_images_dir / new_name
        
        if args.dry_run:
            print(f"    [DRY RUN] Would move to: images/{new_name}")
        else:
            try:
                shutil.move(str(png_file), str(target_path))
                print(f"    ✅ Moved to: images/{new_name}")
                processed += 1
            except Exception as e:
                print(f"    ❌ Failed: {e}")
        
        if not args.dry_run:
            processed += 1
    
    # Summary
    print(f"\n📋 Summary:")
    print(f"   UULL files processed: {processed}")
    print(f"   Non-UULL files skipped: {skipped}")
    print(f"   Other files ignored: {len(all_files) - len(png_files)}")
    
    if args.dry_run:
        print(f"\n📋 Dry run complete - remove --dry-run to actually move files")
    else:
        print(f"\n✅ All images now in: {global_images_dir}")
        print(f"   Markdown images: ![Title](images/filename.png)")
    
    return 0


if __name__ == "__main__":
    exit(main())
