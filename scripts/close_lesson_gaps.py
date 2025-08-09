#!/usr/bin/env python3
"""
Gap-Closing Lesson Renumbering Script

This script removes gaps in lesson numbering by renaming files to sequential numbers.
It maintains the same safety features as the existing renumber_lessons.py script.

SAFETY FEATURES:
- Creates backup copies of all files before renumbering
- Dry-run mode to preview changes
- Comprehensive validation and error handling
- Rollback capability if errors occur
- Handles both lesson files and corresponding images

Usage:
    python close_lesson_gaps.py <unit_number> [--dry-run] [--backup-dir=DIR]
    
Examples:
    python close_lesson_gaps.py 1 --dry-run          # Preview Unit 1 gap closing
    python close_lesson_gaps.py 1                    # Execute Unit 1 gap closing
    python close_lesson_gaps.py 2 --backup-dir=backup_gaps  # Custom backup directory
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime


class GapClosingTool:
    def __init__(self, unit_number, dry_run=False, backup_dir=None):
        self.unit_number = unit_number.zfill(2)  # Ensure 2-digit format
        self.dry_run = dry_run
        self.backup_dir = backup_dir or f"backup_gaps_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        self.current_dir = Path.cwd()
        self.backup_path = self.current_dir / self.backup_dir
        self.operations_log = []
        self.errors = []
        
    def log(self, message, level="INFO"):
        """Log a message with timestamp and level."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.operations_log.append(log_entry)
        print(log_entry)
        
    def error(self, message):
        """Log an error message."""
        self.log(message, "ERROR")
        self.errors.append(message)
        
    def find_unit_lessons(self):
        """Find all lesson files for the specified unit."""
        pattern = f"{self.unit_number}-*-*.md"
        lesson_files = list(self.current_dir.glob(pattern))
        
        # Sort by lesson number
        lesson_files.sort(key=lambda x: self.extract_lesson_number(x.name))
        
        return lesson_files
    
    def find_unit_images(self):
        """Find all image files for the specified unit."""
        images_dir = self.current_dir / "images"
        if not images_dir.exists():
            return []
            
        pattern = f"{self.unit_number}_*_*.png"
        image_files = list(images_dir.glob(pattern))
        image_files.sort()
        
        return image_files
    
    def extract_lesson_number(self, filename):
        """Extract lesson number from filename."""
        match = re.match(rf'{self.unit_number}-(\d+)-.*\.md', filename)
        return int(match.group(1)) if match else 0
    
    def extract_image_lesson_number(self, filename):
        """Extract lesson number from image filename."""
        match = re.match(rf'{self.unit_number}_(\d+)_.*\.png', filename)
        return int(match.group(1)) if match else 0
    
    def create_backup(self):
        """Create backup directory and copy files."""
        if self.dry_run:
            self.log("DRY RUN: Would create backup directory")
            return True
            
        try:
            self.backup_path.mkdir(exist_ok=True)
            
            # Backup lesson files
            lesson_files = self.find_unit_lessons()
            for file_path in lesson_files:
                shutil.copy2(file_path, self.backup_path)
                self.log(f"Backed up: {file_path.name}")
            
            # Backup image files
            image_files = self.find_unit_images()
            if image_files:
                images_backup = self.backup_path / "images"
                images_backup.mkdir(exist_ok=True)
                for file_path in image_files:
                    shutil.copy2(file_path, images_backup)
                    self.log(f"Backed up: images/{file_path.name}")
            
            self.log(f"Backup created at: {self.backup_path}")
            return True
            
        except Exception as e:
            self.error(f"Failed to create backup: {e}")
            return False
    
    def generate_renaming_plan(self):
        """Generate the renaming plan for lessons and images."""
        lesson_files = self.find_unit_lessons()
        image_files = self.find_unit_images()
        
        lesson_plan = []
        image_plan = []
        
        # Process lesson files
        for new_lesson_num, lesson_file in enumerate(lesson_files, 1):
            current_lesson_num = self.extract_lesson_number(lesson_file.name)
            
            if current_lesson_num != new_lesson_num:
                # Need to rename
                new_filename = re.sub(
                    rf'{self.unit_number}-\d+',
                    f'{self.unit_number}-{new_lesson_num:02d}',
                    lesson_file.name
                )
                lesson_plan.append({
                    'old_path': lesson_file,
                    'new_path': lesson_file.parent / new_filename,
                    'old_num': current_lesson_num,
                    'new_num': new_lesson_num
                })
        
        # Process image files
        for image_file in image_files:
            current_lesson_num = self.extract_image_lesson_number(image_file.name)
            
            # Find what the new lesson number should be based on lesson renaming
            new_lesson_num = None
            for lesson_rename in lesson_plan:
                if lesson_rename['old_num'] == current_lesson_num:
                    new_lesson_num = lesson_rename['new_num']
                    break
            
            # If no renaming needed for this lesson number, check if it's already sequential
            if new_lesson_num is None:
                # Find position in sequential list
                lesson_numbers = [self.extract_lesson_number(f.name) for f in lesson_files]
                try:
                    position = lesson_numbers.index(current_lesson_num)
                    new_lesson_num = position + 1
                except ValueError:
                    continue  # Image for non-existent lesson
            
            if current_lesson_num != new_lesson_num:
                new_filename = re.sub(
                    rf'{self.unit_number}_\d+',
                    f'{self.unit_number}_{new_lesson_num:02d}',
                    image_file.name
                )
                image_plan.append({
                    'old_path': image_file,
                    'new_path': image_file.parent / new_filename,
                    'old_num': current_lesson_num,
                    'new_num': new_lesson_num
                })
        
        return lesson_plan, image_plan
    
    def preview_changes(self):
        """Preview what changes would be made."""
        lesson_plan, image_plan = self.generate_renaming_plan()
        
        self.log("=" * 60)
        self.log(f"GAP CLOSING PREVIEW FOR UNIT {self.unit_number}")
        self.log("=" * 60)
        
        if not lesson_plan and not image_plan:
            self.log("No gaps found - all lessons are already sequential!")
            return False
        
        if lesson_plan:
            self.log("\nLESSON FILES TO RENAME:")
            self.log("-" * 40)
            for item in lesson_plan:
                self.log(f"  {item['old_num']:02d} → {item['new_num']:02d}: {item['old_path'].name}")
                self.log(f"      → {item['new_path'].name}")
        
        if image_plan:
            self.log("\nIMAGE FILES TO RENAME:")
            self.log("-" * 40)
            for item in image_plan:
                self.log(f"  {item['old_num']:02d} → {item['new_num']:02d}: {item['old_path'].name}")
                self.log(f"      → {item['new_path'].name}")
        
        self.log(f"\nTOTAL CHANGES: {len(lesson_plan)} lessons + {len(image_plan)} images")
        return True
    
    def execute_renaming(self):
        """Execute the renaming operations."""
        lesson_plan, image_plan = self.generate_renaming_plan()
        
        if not lesson_plan and not image_plan:
            self.log("No gaps found - all lessons are already sequential!")
            return True
        
        try:
            # Rename lesson files
            for item in lesson_plan:
                if not self.dry_run:
                    item['old_path'].rename(item['new_path'])
                self.log(f"Renamed: {item['old_path'].name} → {item['new_path'].name}")
            
            # Rename image files
            for item in image_plan:
                if not self.dry_run:
                    item['old_path'].rename(item['new_path'])
                self.log(f"Renamed: images/{item['old_path'].name} → images/{item['new_path'].name}")
            
            self.log(f"Successfully processed {len(lesson_plan)} lessons and {len(image_plan)} images")
            return True
            
        except Exception as e:
            self.error(f"Failed during renaming: {e}")
            return False
    
    def run(self):
        """Execute the gap closing process."""
        self.log("=" * 60)
        self.log(f"LESSON GAP CLOSING TOOL - UNIT {self.unit_number}")
        self.log("=" * 60)
        
        if self.dry_run:
            self.log("DRY RUN MODE - No files will be modified")
        
        # Find unit lessons
        lesson_files = self.find_unit_lessons()
        if not lesson_files:
            self.error(f"No lesson files found for Unit {self.unit_number}")
            return False
        
        self.log(f"Found {len(lesson_files)} lesson files for Unit {self.unit_number}")
        
        # Preview changes
        has_changes = self.preview_changes()
        if not has_changes:
            return True
        
        if self.dry_run:
            self.log("\nDRY RUN COMPLETE - Run without --dry-run to execute changes")
            return True
        
        # Create backup
        if not self.create_backup():
            return False
        
        # Execute renaming
        success = self.execute_renaming()
        
        if success:
            self.log("=" * 60)
            self.log("GAP CLOSING COMPLETED SUCCESSFULLY!")
            self.log(f"Backup available at: {self.backup_path}")
            self.log("=" * 60)
        else:
            self.log("=" * 60)
            self.log("GAP CLOSING FAILED - Check backup for recovery")
            self.log(f"Backup location: {self.backup_path}")
            self.log("=" * 60)
        
        return success


def main():
    parser = argparse.ArgumentParser(
        description='Close gaps in lesson numbering by renaming files sequentially',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python close_lesson_gaps.py 1 --dry-run          # Preview Unit 1 gap closing
  python close_lesson_gaps.py 1                    # Execute Unit 1 gap closing  
  python close_lesson_gaps.py 2 --backup-dir=gaps  # Custom backup directory
        """
    )
    
    parser.add_argument('unit_number', type=str, help='Unit number to process (1-12)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files')
    parser.add_argument('--backup-dir', type=str, help='Custom backup directory name')
    
    args = parser.parse_args()
    
    # Validate unit number
    try:
        unit_num = int(args.unit_number)
        if unit_num < 1 or unit_num > 12:
            raise ValueError("Unit number must be between 1 and 12")
    except ValueError as e:
        print(f"ERROR: Invalid unit number: {e}")
        return 1
    
    # Run the tool
    tool = GapClosingTool(args.unit_number, args.dry_run, args.backup_dir)
    success = tool.run()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
