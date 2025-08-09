#!/usr/bin/env python3
"""
Lesson File Renumbering Script - Enhanced Safety Version

This script automates the renumbering of lesson markdown files within a directory 
when a new lesson needs to be inserted into the sequence.

SAFETY FEATURES:
- Creates backup copies of all files before renumbering
- Dry-run mode to preview changes
- Comprehensive validation and error handling
- Rollback capability if errors occur
- Detailed logging of all operations

Usage:
    python renumber_lessons.py <insertion_point> [--dry-run] [--backup-dir=DIR]
    
Examples:
    python renumber_lessons.py 3 --dry-run          # Preview changes only
    python renumber_lessons.py 3                    # Execute with default backup
    python renumber_lessons.py 3 --backup-dir=backup_2025_01_07  # Custom backup directory
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime


class LessonRenumberingTool:
    def __init__(self, insertion_point, dry_run=False, backup_dir=None):
        self.insertion_point = insertion_point
        self.dry_run = dry_run
        self.backup_dir = backup_dir or f"backup_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
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
        self.errors.append(message)
        self.log(message, "ERROR")
        
    def get_lesson_files(self):
        """
        Get all markdown files in the current directory that match the lesson naming convention.
        Returns a list of filenames that match the pattern NN-NN-*.md where NN is a two-digit number.
        """
        lesson_pattern = re.compile(r'^\d{2}-\d{2}-.*\.md$')
        
        lesson_files = []
        for file in self.current_dir.iterdir():
            if file.is_file() and lesson_pattern.match(file.name):
                lesson_files.append(file.name)
        
        return sorted(lesson_files)  # Sort to ensure consistent order
    
    def parse_lesson_number(self, filename):
        """
        Extract the unit and lesson numbers from a filename.
        
        Args:
            filename (str): The filename to parse (e.g., '02-03-working-with-temperature.md')
        
        Returns:
            tuple: (unit_number, lesson_number) or (None, None) if parsing fails
        """
        match = re.match(r'^(\d{2})-(\d{2})', filename)
        if match:
            unit_number = int(match.group(1))
            lesson_number = int(match.group(2))
            return unit_number, lesson_number
        return None, None
    
    def determine_insertion_unit(self, all_files):
        """
        Determine which unit the insertion point refers to based on existing files.
        
        Args:
            all_files (list): List of all lesson files
            
        Returns:
            int: The unit number where the insertion should occur
        """
        # Look for files that would be affected by this insertion point
        for filename in all_files:
            unit_number, lesson_number = self.parse_lesson_number(filename)
            if unit_number is not None and lesson_number >= self.insertion_point:
                return unit_number
        
        # If no files would be affected, assume the most common unit (3 in this case)
        # This is a fallback - in practice, the insertion point should be in a context where
        # there are files to be renumbered
        return 3
    
    def provide_workflow_guidance(self, all_files):
        """Provide clear workflow guidance to prevent duplicate creation."""
        self.log("=" * 50)
        self.log("WORKFLOW GUIDANCE - PREVENT DUPLICATE LESSONS")
        self.log("=" * 50)
        
        # Check if there are files that will be renamed
        files_to_be_affected = []
        for filename in all_files:
            unit_number, lesson_number = self.parse_lesson_number(filename)
            if unit_number is not None and lesson_number >= self.insertion_point:
                files_to_be_affected.append((filename, unit_number, lesson_number))
        
        if files_to_be_affected:
            self.log(f"✓ This operation will create space for a new lesson at position {self.insertion_point:02d}")
            self.log(f"✓ {len(files_to_be_affected)} existing lessons will be renumbered")
            self.log("")
            self.log("IMPORTANT WORKFLOW REMINDER:")
            self.log("1. ✓ This script creates the empty slot (CURRENT STEP)")
            self.log("2. → Next: Manually create your new lesson file")
            self.log("3. → Finally: Run generate_course_outline.py")
            self.log("")
            self.log("⚠️  DO NOT create the lesson file before running this script!")
            self.log("⚠️  That workflow creates duplicates and requires manual cleanup.")
        else:
            self.log(f"ℹ️  No files need renumbering for insertion point {self.insertion_point:02d}")
            self.log("This suggests the slot is already available.")
        
        self.log("=" * 50)
    
    def create_new_filename(self, unit_number, new_lesson_number, old_filename):
        """
        Create a new filename with the incremented lesson number.
        
        Args:
            unit_number (int): The unit number (e.g., 2)
            new_lesson_number (int): The new lesson number (e.g., 4)
            old_filename (str): The original filename
        
        Returns:
            str: The new filename with updated lesson number
        """
        # Extract the part after the lesson number
        pattern = r'^\d{2}-\d{2}-(.*)'
        match = re.match(pattern, old_filename)
        
        if match:
            suffix = match.group(1)
            new_filename = f"{unit_number:02d}-{new_lesson_number:02d}-{suffix}"
            return new_filename
        
        # Fallback - this shouldn't happen if the file matches our pattern
        self.error(f"Could not parse filename structure: {old_filename}")
        return old_filename
    
    def create_backup(self, files_to_backup):
        """Create backup copies of all files that will be modified."""
        if self.dry_run:
            self.log(f"DRY-RUN: Would create backup directory: {self.backup_path}")
            for filename in files_to_backup:
                self.log(f"DRY-RUN: Would backup: {filename}")
            return True
            
        try:
            # Create backup directory
            self.backup_path.mkdir(exist_ok=True)
            self.log(f"Created backup directory: {self.backup_path}")
            
            # Copy all files to backup
            backup_count = 0
            for filename in files_to_backup:
                source_path = self.current_dir / filename
                backup_file_path = self.backup_path / filename
                
                shutil.copy2(source_path, backup_file_path)
                self.log(f"Backed up: {filename}")
                backup_count += 1
            
            self.log(f"Successfully backed up {backup_count} files")
            return True
            
        except Exception as e:
            self.error(f"Failed to create backup: {e}")
            return False
    
    def validate_renaming_plan(self, files_to_rename):
        """Validate the renaming plan to prevent conflicts."""
        new_filenames = set()
        existing_files = set(self.get_lesson_files())
        
        for old_filename, unit_number, current_lesson_number in files_to_rename:
            new_lesson_number = current_lesson_number + 1
            new_filename = self.create_new_filename(unit_number, new_lesson_number, old_filename)
            
            # Check for duplicate new filenames
            if new_filename in new_filenames:
                self.error(f"Conflict: Multiple files would be renamed to {new_filename}")
                return False
            
            new_filenames.add(new_filename)
            
            # Check if new filename already exists (and is not being renamed)
            if new_filename in existing_files and new_filename not in [f[0] for f in files_to_rename]:
                self.error(f"Conflict: {new_filename} already exists and would be overwritten")
                return False
        
        # NEW: Check for content similarity that indicates duplicate lessons
        if not self.check_for_duplicate_content(files_to_rename):
            return False
        
        return True
    
    def check_for_duplicate_content(self, files_to_rename):
        """Check for potential duplicate lessons based on content similarity."""
        from difflib import SequenceMatcher
        
        # Get all current lesson files for comparison
        all_current_files = self.get_lesson_files()
        
        for old_filename, unit_number, current_lesson_number in files_to_rename:
            try:
                # Read the content of the file being renamed
                old_file_path = self.current_dir / old_filename
                if not old_file_path.exists():
                    continue
                    
                with open(old_file_path, 'r', encoding='utf-8') as f:
                    old_content = f.read()
                
                # Extract the descriptive part of the filename for comparison
                old_desc = self.extract_lesson_description(old_filename)
                
                # Check against all other files for potential duplicates
                for other_filename in all_current_files:
                    if other_filename == old_filename:
                        continue
                    
                    other_desc = self.extract_lesson_description(other_filename)
                    
                    # Check filename similarity
                    similarity = SequenceMatcher(None, old_desc.lower(), other_desc.lower()).ratio()
                    
                    if similarity > 0.8:  # 80% similarity threshold
                        # Also check content similarity if filenames are very similar
                        try:
                            other_file_path = self.current_dir / other_filename
                            with open(other_file_path, 'r', encoding='utf-8') as f:
                                other_content = f.read()
                            
                            content_similarity = SequenceMatcher(None, old_content, other_content).ratio()
                            
                            if content_similarity > 0.5:  # 50% content similarity
                                self.error(f"DUPLICATE DETECTED: '{old_filename}' appears to be very similar to '{other_filename}'")
                                self.error(f"  - Filename similarity: {similarity:.1%}")
                                self.error(f"  - Content similarity: {content_similarity:.1%}")
                                self.error("  - This suggests duplicate lessons that should be consolidated")
                                return False
                                
                        except Exception as e:
                            self.log(f"Warning: Could not read {other_filename} for content comparison: {e}")
            
            except Exception as e:
                self.log(f"Warning: Could not read {old_filename} for duplicate checking: {e}")
        
        return True
    
    def extract_lesson_description(self, filename):
        """Extract the descriptive part of a lesson filename."""
        # Remove the NN-NN- prefix and .md suffix
        match = re.match(r'^\d{2}-\d{2}-(.*?)\.md$', filename)
        if match:
            return match.group(1)
        return filename
    
    def execute_renaming(self, files_to_rename):
        """Execute the file renaming operations."""
        if self.dry_run:
            self.log("DRY-RUN: File renaming operations that would be performed:")
            for old_filename, unit_number, current_lesson_number in files_to_rename:
                new_lesson_number = current_lesson_number + 1
                new_filename = self.create_new_filename(unit_number, new_lesson_number, old_filename)
                self.log(f"DRY-RUN: Would rename '{old_filename}' → '{new_filename}'")
            return True, len(files_to_rename)
        
        renamed_count = 0
        failed_renames = []
        
        for old_filename, unit_number, current_lesson_number in files_to_rename:
            new_lesson_number = current_lesson_number + 1
            new_filename = self.create_new_filename(unit_number, new_lesson_number, old_filename)
            
            try:
                old_path = self.current_dir / old_filename
                new_path = self.current_dir / new_filename
                
                old_path.rename(new_path)
                self.log(f"✓ Renamed '{old_filename}' → '{new_filename}'")
                renamed_count += 1
                
            except Exception as e:
                error_msg = f"Failed to rename '{old_filename}': {e}"
                self.error(error_msg)
                failed_renames.append((old_filename, str(e)))
        
        if failed_renames:
            self.error(f"Some renames failed. {len(failed_renames)} errors occurred.")
            return False, renamed_count
        
        return True, renamed_count
    
    def rollback_changes(self):
        """Rollback changes by restoring from backup."""
        if not self.backup_path.exists():
            self.error("No backup directory found for rollback")
            return False
        
        self.log("Attempting to rollback changes...")
        
        try:
            # Get all backup files
            backup_files = list(self.backup_path.glob("*.md"))
            
            for backup_file in backup_files:
                target_path = self.current_dir / backup_file.name
                
                # Remove current file if it exists
                if target_path.exists():
                    target_path.unlink()
                
                # Restore from backup
                shutil.copy2(backup_file, target_path)
                self.log(f"Restored: {backup_file.name}")
            
            self.log(f"Rollback completed successfully. Restored {len(backup_files)} files.")
            return True
            
        except Exception as e:
            self.error(f"Rollback failed: {e}")
            return False
    
    def run(self):
        """Main execution method."""
        self.log("=" * 60)
        self.log("LESSON RENUMBERING TOOL - ENHANCED SAFETY VERSION")
        self.log("=" * 60)
        
        if self.dry_run:
            self.log("*** DRY-RUN MODE - NO FILES WILL BE MODIFIED ***")
        
        self.log(f"Insertion point: Lesson {self.insertion_point:02d}")
        self.log(f"Working directory: {self.current_dir}")
        self.log(f"Backup directory: {self.backup_path}")
        
        # Step 1: Get all lesson files
        all_files = self.get_lesson_files()
        if not all_files:
            self.error("No lesson files found matching the pattern NN-NN-*.md")
            return False
        
        self.log(f"Found {len(all_files)} lesson files")
        
        # Step 1.5: Enhanced workflow guidance
        self.provide_workflow_guidance(all_files)
        
        # Step 2: Filter and collect files that need to be renamed
        files_to_rename = []
        files_not_affected = []
        
        for filename in all_files:
            unit_number, lesson_number = self.parse_lesson_number(filename)
            
            if unit_number is None or lesson_number is None:
                self.error(f"Could not parse lesson number from: {filename}")
                continue
            
            if lesson_number >= self.insertion_point:
                files_to_rename.append((filename, unit_number, lesson_number))
            else:
                files_not_affected.append(filename)
        
        if not files_to_rename:
            self.log(f"No files need to be renumbered (no lessons >= {self.insertion_point:02d})")
            return True
        
        # Sort in descending order by lesson number to avoid overwriting
        files_to_rename.sort(key=lambda x: x[2], reverse=True)
        
        self.log(f"Files to be renumbered: {len(files_to_rename)}")
        self.log(f"Files not affected: {len(files_not_affected)}")
        
        # Step 3: Validate renaming plan
        if not self.validate_renaming_plan(files_to_rename):
            self.error("Renaming plan validation failed. Aborting.")
            return False
        
        self.log("Renaming plan validation passed")
        
        # Step 4: Create backups
        all_affected_files = [f[0] for f in files_to_rename]
        if not self.create_backup(all_affected_files):
            self.error("Backup creation failed. Aborting for safety.")
            return False
        
        # Step 5: Execute renaming
        success, renamed_count = self.execute_renaming(files_to_rename)
        
        if success:
            if self.dry_run:
                self.log(f"DRY-RUN COMPLETE: {renamed_count} files would be processed")
            else:
                self.log(f"SUCCESS: {renamed_count} files renamed successfully")
                self.log(f"New lesson can now be created at position {self.insertion_point:02d}")
                self.log(f"Backup files are available in: {self.backup_path}")
        else:
            self.error("Renaming operation failed")
            if not self.dry_run:
                self.log("Attempting automatic rollback...")
                if self.rollback_changes():
                    self.log("Rollback completed successfully")
                else:
                    self.error("Rollback failed - manual restoration may be required")
        
        # Step 6: Summary
        self.log("=" * 60)
        self.log("OPERATION SUMMARY")
        self.log("=" * 60)
        self.log(f"Total operations logged: {len(self.operations_log)}")
        self.log(f"Errors encountered: {len(self.errors)}")
        
        if self.errors:
            self.log("ERRORS:")
            for error in self.errors:
                self.log(f"  - {error}")
        
        return success and len(self.errors) == 0


def main():
    """Main entry point with enhanced argument parsing."""
    parser = argparse.ArgumentParser(
        description="Safely renumber lesson files to make room for new lessons",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python renumber_lessons.py 3 --dry-run          # Preview changes only
  python renumber_lessons.py 3                    # Execute with default backup
  python renumber_lessons.py 3 --backup-dir=backup_2025_01_07  # Custom backup
        """
    )
    
    parser.add_argument('insertion_point', type=int, 
                        help='The lesson number where new lesson will be inserted (1-99)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without modifying files')
    parser.add_argument('--force', action='store_true',
                        help='Skip confirmation prompt and execute automatically')
    parser.add_argument('--backup-dir', type=str,
                        help='Custom backup directory name (default: backup_YYYY_MM_DD_HH_MM_SS)')
    
    args = parser.parse_args()
    
    # Validate insertion point
    if args.insertion_point < 1 or args.insertion_point > 99:
        print("Error: insertion_point must be between 1 and 99")
        sys.exit(1)
    
    # Create and run the tool
    tool = LessonRenumberingTool(
        insertion_point=args.insertion_point,
        dry_run=args.dry_run,
        backup_dir=args.backup_dir
    )
    
    # Get user confirmation unless in dry-run mode or force mode
    if not args.dry_run and not args.force:
        print(f"\nThis will renumber all lessons from {args.insertion_point:02d} onwards.")
        print("Backup copies will be created automatically.")
        print("Files will be renamed in descending order to prevent overwriting.")
        
        response = input("\nContinue? (y/N): ").lower().strip()
        
        if response not in ('y', 'yes'):
            print("Operation cancelled.")
            sys.exit(0)
    
    # Execute the renumbering
    success = tool.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
