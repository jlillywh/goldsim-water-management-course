#!/usr/bin/env python3
"""
Lesson Rollback Script

This script helps manually rollback lesson renumbering operations
by restoring files from a backup directory.

Usage:
    python rollback_lessons.py <backup_directory>
    
Example:
    python rollback_lessons.py backup_2025_01_07_14_30_45
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


def log(message):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")


def rollback_from_backup(backup_dir_name):
    """Rollback lesson files from backup directory."""
    current_dir = Path.cwd()
    backup_path = current_dir / backup_dir_name
    
    log(f"Starting rollback operation...")
    log(f"Working directory: {current_dir}")
    log(f"Backup directory: {backup_path}")
    
    # Check if backup directory exists
    if not backup_path.exists():
        log(f"ERROR: Backup directory '{backup_path}' does not exist")
        return False
    
    if not backup_path.is_dir():
        log(f"ERROR: '{backup_path}' is not a directory")
        return False
    
    # Get all markdown files in backup
    backup_files = list(backup_path.glob("*.md"))
    
    if not backup_files:
        log("ERROR: No markdown files found in backup directory")
        return False
    
    log(f"Found {len(backup_files)} backup files")
    
    # Confirm with user
    print(f"\nThis will restore {len(backup_files)} lesson files from backup.")
    print("Any existing files with the same names will be overwritten.")
    
    response = input("Continue with rollback? (y/N): ").lower().strip()
    
    if response not in ('y', 'yes'):
        log("Rollback cancelled by user")
        return False
    
    # Perform rollback
    restored_count = 0
    errors = []
    
    for backup_file in backup_files:
        target_path = current_dir / backup_file.name
        
        try:
            # Remove current file if it exists
            if target_path.exists():
                target_path.unlink()
                log(f"Removed existing: {backup_file.name}")
            
            # Restore from backup
            shutil.copy2(backup_file, target_path)
            log(f"Restored: {backup_file.name}")
            restored_count += 1
            
        except Exception as e:
            error_msg = f"Failed to restore {backup_file.name}: {e}"
            log(f"ERROR: {error_msg}")
            errors.append(error_msg)
    
    # Summary
    log("-" * 50)
    log(f"Rollback completed: {restored_count} files restored")
    
    if errors:
        log(f"Errors encountered: {len(errors)}")
        for error in errors:
            log(f"  - {error}")
        return False
    else:
        log("All files restored successfully!")
        return True


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python rollback_lessons.py <backup_directory>")
        print("Example: python rollback_lessons.py backup_2025_01_07_14_30_45")
        print("\nAvailable backup directories:")
        
        # List available backup directories
        current_dir = Path.cwd()
        backup_dirs = [d.name for d in current_dir.iterdir() 
                      if d.is_dir() and d.name.startswith('backup_')]
        
        if backup_dirs:
            for backup_dir in sorted(backup_dirs, reverse=True):
                print(f"  - {backup_dir}")
        else:
            print("  (No backup directories found)")
        
        sys.exit(1)
    
    backup_dir = sys.argv[1]
    success = rollback_from_backup(backup_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
