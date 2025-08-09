#!/usr/bin/env python3
r"""
Image Sorting Automation for GoldSim Water Management Course

This script automatically sorts captured images from SnagIt or other capture tools
into the appropriate lesson folders based on the UULL naming convention.

UULL Naming Convention:
- Full format: "UU LL LessonName-sequence-description.png"
- Simple format: "UU LL LessonName.png"

Examples:
- "04 01 Introduction to Water Demand-01-concepts-diagram.png"
- "01 03 System Model.png"
- "07 02 Aquifer Element Practice-05-flow-results.png"

Usage:
    python sort_images.py
    python sort_images.py --source "C:\\custom\\path" --dry-run
    python sort_images.py --help
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class ImageSorter:
    def __init__(self, course_root: str, source_dir: str, dry_run: bool = False):
        self.course_root = Path(course_root)
        self.source_dir = Path(source_dir)
        self.dry_run = dry_run
        
        # UULL pattern regex
        self.full_pattern = re.compile(r'^(\d{2})\s+(\d{2})\s+([^-]+)-(\d+)-(.+)$')
        self.simple_pattern = re.compile(r'^(\d{2})\s+(\d{2})\s+(.+)$')
        
    def find_images(self) -> List[Path]:
        """Find all PNG images in the source directory."""
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {self.source_dir}")
        
        images = list(self.source_dir.glob("*.png"))
        print(f"Found {len(images)} PNG images in {self.source_dir}")
        return images
    
    def parse_filename(self, image_path: Path) -> Optional[Dict[str, str]]:
        """Parse image filename using UULL convention."""
        filename = image_path.stem  # filename without extension
        
        # Try full pattern first: UU LL Name-sequence-description
        match = self.full_pattern.match(filename)
        if match:
            return {
                'unit': match.group(1),
                'lesson': match.group(2),
                'name': match.group(3).strip(),
                'sequence': match.group(4),
                'description': match.group(5),
                'original_name': image_path.name,
                'pattern_type': 'full'
            }
        
        # Try simple pattern: UU LL Name
        match = self.simple_pattern.match(filename)
        if match:
            return {
                'unit': match.group(1),
                'lesson': match.group(2),
                'name': match.group(3).strip(),
                'sequence': '01',
                'description': 'image',
                'original_name': image_path.name,
                'pattern_type': 'simple'
            }
        
        return None
    
    def find_lesson_directory(self, unit: str, lesson: str) -> Optional[Path]:
        """Find the target lesson directory based on unit and lesson numbers."""
        # Find unit directory
        unit_pattern = f"{unit}-*"
        unit_dirs = list(self.course_root.glob(unit_pattern))
        
        if not unit_dirs:
            print(f"  ⚠️  Could not find unit directory for pattern: {unit_pattern}")
            return None
        
        unit_dir = unit_dirs[0]
        
        # Find lesson directory
        lesson_pattern = f"Lesson_{lesson}-*"
        lesson_dirs = list(unit_dir.glob(lesson_pattern))
        
        if not lesson_dirs:
            print(f"  ⚠️  Could not find lesson directory for pattern: {lesson_pattern}")
            print(f"     Available lessons in {unit_dir.name}:")
            for lesson_dir in unit_dir.iterdir():
                if lesson_dir.is_dir():
                    print(f"       - {lesson_dir.name}")
            return None
        
        return lesson_dirs[0]
    
    def create_image_directories(self, lesson_dir: Path) -> Dict[str, Path]:
        """Create the standard image directory structure."""
        images_dir = lesson_dir / "images"
        raw_dir = images_dir / "raw"
        processed_dir = images_dir / "processed"
        web_dir = images_dir / "web"
        
        dirs = {
            'images': images_dir,
            'raw': raw_dir,
            'processed': processed_dir,
            'web': web_dir
        }
        
        if not self.dry_run:
            for dir_path in dirs.values():
                dir_path.mkdir(parents=True, exist_ok=True)
                if not dir_path.exists():
                    print(f"    📁 Created: {dir_path}")
        
        return dirs
    
    def generate_new_filename(self, image_info: Dict[str, str]) -> str:
        """Generate standardized filename."""
        unit = image_info['unit']
        lesson = image_info['lesson']
        sequence = image_info['sequence'].zfill(2)  # Ensure 2 digits
        description = image_info['description']
        
        return f"{unit}-{lesson}-{sequence}-{description}.png"
    
    def move_image(self, source_path: Path, image_info: Dict[str, str], lesson_dir: Path) -> bool:
        """Move and organize a single image."""
        try:
            # Create directory structure
            dirs = self.create_image_directories(lesson_dir)
            
            # Generate new filename
            new_filename = self.generate_new_filename(image_info)
            
            raw_dest = dirs['raw'] / new_filename
            processed_dest = dirs['processed'] / new_filename
            
            if self.dry_run:
                print(f"    [DRY RUN] Would move: {image_info['original_name']}")
                print(f"              to: raw/{new_filename}")
                return True
            else:
                # Move to raw directory
                shutil.move(str(source_path), str(raw_dest))
                print(f"    ✅ Moved to raw: {new_filename}")
                
                # Copy to processed directory for editing
                shutil.copy2(str(raw_dest), str(processed_dest))
                print(f"    ✅ Copied to processed: {new_filename}")
                
                return True
                
        except Exception as e:
            print(f"    ❌ Failed to move {image_info['original_name']}: {e}")
            return False
    
    def sort_images(self) -> Tuple[int, int]:
        """Main sorting function. Returns (successful, failed) counts."""
        print("=" * 60)
        print("SORTING CAPTURED IMAGES INTO LESSON FOLDERS")
        print("=" * 60)
        
        if self.dry_run:
            print("\n*** DRY RUN MODE - No files will be moved ***\n")
        
        # Find all images
        images = self.find_images()
        if not images:
            print("No images found to process.")
            return 0, 0
        
        # Parse and group images
        parsed_images = []
        unrecognized = []
        
        for image_path in images:
            print(f"Checking: {image_path.name}")
            image_info = self.parse_filename(image_path)
            
            if image_info:
                image_info['path'] = image_path
                parsed_images.append(image_info)
                
                pattern_type = "full" if image_info['pattern_type'] == 'full' else "simple"
                print(f"  ✅ Parsed ({pattern_type}): Unit {image_info['unit']}, "
                      f"Lesson {image_info['lesson']}, Name: {image_info['name']}")
            else:
                unrecognized.append(image_path)
                print(f"  ⏭️  Skipping (not UULL): {image_path.name}")
        
        if not parsed_images and unrecognized:
            print("\n📋 No UULL-named images found to process")
            print(f"   Found {len(unrecognized)} non-UULL files (left in SnagIt folder)")
            print("\nTo process images, use UULL naming convention:")
            self.show_naming_examples()
            return 0, 0  # Not an error - just no UULL files to process
        
        # Group by lesson
        lesson_groups = {}
        for img in parsed_images:
            key = f"{img['unit']}-{img['lesson']}"
            if key not in lesson_groups:
                lesson_groups[key] = []
            lesson_groups[key].append(img)
        
        print(f"\nProcessing {len(lesson_groups)} lesson groups:")
        
        successful = 0
        failed = 0
        
        # Process each lesson group
        for group_key, images_in_group in lesson_groups.items():
            unit = images_in_group[0]['unit']
            lesson = images_in_group[0]['lesson']
            name = images_in_group[0]['name']
            
            print(f"\n📂 Unit {unit}, Lesson {lesson}: {name}")
            print(f"   Images: {len(images_in_group)}")
            
            # Find lesson directory
            lesson_dir = self.find_lesson_directory(unit, lesson)
            if not lesson_dir:
                print(f"   ⏭️  Skipping - lesson directory not found")
                failed += len(images_in_group)
                continue
            
            print(f"   Target: {lesson_dir.name}")
            
            # Move each image in the group
            for image_info in images_in_group:
                if self.move_image(image_info['path'], image_info, lesson_dir):
                    successful += 1
                else:
                    failed += 1
        
        # Report unrecognized images (informational only)
        if unrecognized:
            print(f"\n📋 Non-UULL files ignored: {len(unrecognized)}")
            if len(unrecognized) <= 5:  # Only show details for a few files
                for img in unrecognized:
                    print(f"   - {img.name}")
            else:
                print(f"   - {unrecognized[0].name}")
                print(f"   - {unrecognized[1].name}")
                print(f"   - ... and {len(unrecognized) - 2} more")
            print("   (These files remain in SnagIt folder for manual handling)")

        # Final summary
        if self.dry_run:
            print(f"\n📋 Dry run complete - no files were moved")
            print("Remove --dry-run to actually move the files")
        else:
            if successful > 0:
                print(f"\n✅ Image sorting complete!")
                print(f"   UULL files processed: {successful}")
                if failed > 0:
                    print(f"   Skipped (missing lessons): {failed}")
            elif failed > 0:
                print(f"\n⚠️  No files could be processed")
                print(f"   Skipped (missing lessons): {failed}")
            else:
                print(f"\n✅ All done!")
            
            if unrecognized:
                print(f"   Non-UULL files left in SnagIt: {len(unrecognized)}")
        
        return successful, failed
    
    def show_naming_examples(self):
        """Show naming convention examples."""
        print("\nExpected naming patterns:")
        print("  Full: UU LL LessonName-##-description.png")
        print("  Simple: UU LL LessonName.png")
        print("\nExamples:")
        print("  04 01 Introduction to Water Demand-01-concepts-diagram.png")
        print("  01 03 System Model.png")
        print("  07 02 Aquifer Element Practice-05-flow-results.png")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Sort captured images into lesson folders using UULL naming convention",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--source", "-s",
        default=r"C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse",
        help="Source directory containing captured images"
    )
    
    parser.add_argument(
        "--course-root", "-c",
        default=r"c:\Users\JasonLillywhite\OneDrive - GoldSim\work\GoldSimOnlineCourse\goldsim-water-management-course",
        help="Root directory of the course structure"
    )
    
    parser.add_argument(
        "--dry-run", "-d",
        action="store_true",
        help="Show what would be done without actually moving files"
    )
    
    args = parser.parse_args()
    
    try:
        sorter = ImageSorter(
            course_root=args.course_root,
            source_dir=args.source,
            dry_run=args.dry_run
        )
        
        successful, failed = sorter.sort_images()
        
        # Exit with appropriate code
        # Success if any files were processed successfully, even if some failed
        if successful > 0 or (successful == 0 and failed == 0):
            exit(0)  # Success
        else:
            exit(1)  # Only exit with error if no successes and there were failures
            
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
