#!/usr/bin/env python3
"""
GoldSim Course Outline Generator

This script scans the project structure and generates a formatted course outline
showing all units and their lessons. It works with the flat directory structure
where all lesson files are at the root level using the UU-LL-lesson-title.md format.

Usage:
    python generate_course_outline.py                    # Print outline to console
    python generate_course_outline.py --update-readme    # Update README.md with outline
    python generate_course_outline.py --save-outline     # Save outline to course_outline.txt

The script will automatically scan for lesson files and generate an outline.
"""

import os
import re
import argparse
from pathlib import Path
from collections import defaultdict


class CourseOutlineGenerator:
    def __init__(self, course_path=None):
        """
        Initialize the course outline generator.
        
        Args:
            course_path (str, optional): Path to the course directory. 
                                       If None, uses current directory.
        """
        self.course_path = Path(course_path) if course_path else Path.cwd()
        self.units = defaultdict(list)
        
    def parse_lesson_filename(self, filename):
        """
        Parse a lesson filename to extract unit, lesson number, and title.
        
        Args:
            filename (str): The lesson filename (e.g., '01-02-course-resources-and-setup.md')
            
        Returns:
            tuple: (unit_number, lesson_number, lesson_title) or (None, None, None) if parsing fails
        """
        # Pattern to match UU-LL-lesson-title.md format
        pattern = r'^(\d{2})-(\d{2})-(.+)\.md$'
        match = re.match(pattern, filename)
        
        if match:
            unit_number = int(match.group(1))
            lesson_number = int(match.group(2))
            lesson_title_raw = match.group(3)
            
            # Convert hyphens to spaces and apply title case
            lesson_title = lesson_title_raw.replace('-', ' ').title()
            
            return unit_number, lesson_number, lesson_title
        
        return None, None, None
    
    def scan_flat_structure(self):
        """
        Scan for lessons in a flat directory structure.
        All lesson files are directly in the course root directory.
        """
        # Clear any existing data before scanning
        self.units.clear()
        
        lesson_files = []
        
        # Get all markdown files that match the lesson pattern
        for file_path in self.course_path.iterdir():
            if file_path.is_file() and file_path.suffix.lower() == '.md':
                unit_num, lesson_num, lesson_title = self.parse_lesson_filename(file_path.name)
                
                if unit_num is not None and lesson_num is not None:
                    lesson_files.append({
                        'unit_number': unit_num,
                        'lesson_number': lesson_num,
                        'lesson_title': lesson_title,
                        'filename': file_path.name
                    })
        
        # Group lessons by unit
        for lesson in lesson_files:
            self.units[lesson['unit_number']].append(lesson)
        
        # Sort lessons within each unit
        for unit_number in self.units:
            self.units[unit_number].sort(key=lambda x: x['lesson_number'])
        
        return len(lesson_files) > 0
    
    def get_unit_title(self, unit_number):
        """
        Get the title for a unit based on the unit number.
        
        Args:
            unit_number (int): The unit number
            
        Returns:
            str: The unit title
        """
        # Predefined unit titles based on course structure
        unit_titles = {
            1: "Foundations and Data Preparation",
            2: "Climate Data and Weather Modeling", 
            3: "Hydrology and Water Balance",
            4: "Water Demand and Consumption",
            5: "Reservoir Modeling and Operations",
            6: "Water Quality and Treatment",
            7: "Groundwater Systems",
            8: "Integrated System Analysis",
            9: "Advanced Topics",
            10: "Case Studies and Applications"
        }
        
        return unit_titles.get(unit_number, f"Unit {unit_number}")
    
    def generate_outline(self):
        """
        Generate and return the formatted course outline.
        
        Returns:
            str: The formatted course outline
        """
        # Scan the flat structure (UU-LL-lesson-title.md files at root level)
        found_lessons = self.scan_flat_structure()
        
        if not found_lessons:
            return "No lesson files found matching the expected naming convention (UU-LL-lesson-title.md)."
        
        # Generate the outline
        outline_lines = []
        outline_lines.append("*******************************************")
        outline_lines.append("* GoldSim Water Management Course Outline *")
        outline_lines.append("*******************************************")
        outline_lines.append("")
        
        # Sort units by number
        sorted_units = sorted(self.units.keys())
        
        for unit_number in sorted_units:
            unit_title = self.get_unit_title(unit_number)
            lessons = self.units[unit_number]
            
            # Unit header
            unit_header = f"Unit {unit_number}: {unit_title}"
            outline_lines.append(unit_header)
            outline_lines.append("-" * len(unit_header))
            
            # Lessons for this unit
            for lesson in lessons:
                lesson_line = f"    {unit_number:02d}-{lesson['lesson_number']:02d}: {lesson['lesson_title']}"
                outline_lines.append(lesson_line)
            
            outline_lines.append("")  # Empty line after each unit
        
        return "\n".join(outline_lines)
    
    def generate_markdown_outline(self):
        """
        Generate and return the formatted course outline in Markdown format
        suitable for embedding in README.md.
        
        Returns:
            str: The formatted course outline in Markdown
        """
        # Scan the flat structure (UU-LL-lesson-title.md files at root level)
        found_lessons = self.scan_flat_structure()
        
        if not found_lessons:
            return "No lesson files found matching the expected naming convention (UU-LL-lesson-title.md)."
        
        # Generate the Markdown outline
        outline_lines = []
        
        # Sort units by number
        sorted_units = sorted(self.units.keys())
        
        for unit_number in sorted_units:
            unit_title = self.get_unit_title(unit_number)
            lessons = self.units[unit_number]
            
            # Unit header
            outline_lines.append(f"### Unit {unit_number}: {unit_title}")
            
            # Lessons for this unit as hyperlinks
            for lesson in lessons:
                lesson_filename = lesson['filename']
                lesson_link = f"[{lesson['lesson_title']}]({lesson_filename})"
                lesson_line = f"- Lesson {lesson['lesson_number']:02d}: {lesson_link}"
                outline_lines.append(lesson_line)
            
            outline_lines.append("")  # Empty line after each unit
        
        return "\n".join(outline_lines).rstrip()  # Remove trailing newline
    
    def update_readme(self, readme_path="README.md"):
        """
        Update the README.md file with the current course outline.
        
        Args:
            readme_path (str): Path to the README.md file
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        readme_file = self.course_path / readme_path
        
        if not readme_file.exists():
            print(f"ERROR: {readme_file} not found")
            return False
        
        try:
            # Read the current README content
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for markers
            start_marker = "<!-- COURSE_OUTLINE_START -->"
            end_marker = "<!-- COURSE_OUTLINE_END -->"
            
            if start_marker not in content or end_marker not in content:
                print(f"ERROR: Could not find outline markers in {readme_file}")
                print("Please add the following markers to your README.md:")
                print(f"  {start_marker}")
                print("  ... existing content ...")
                print(f"  {end_marker}")
                return False
            
            # Generate the new outline
            new_outline = self.generate_markdown_outline()
            
            # Find the positions of the markers
            start_pos = content.find(start_marker)
            end_pos = content.find(end_marker)
            
            if start_pos == -1 or end_pos == -1 or start_pos >= end_pos:
                print("ERROR: Invalid marker positions in README.md")
                return False
            
            # Calculate positions to preserve markers
            start_replace = start_pos + len(start_marker)
            end_replace = end_pos
            
            # Build the new content
            new_content = (
                content[:start_replace] + 
                "\n" + new_outline + "\n" +
                content[end_replace:]
            )
            
            # Write the updated content back to the file
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Successfully updated {readme_file}")
            print(f"✓ Updated {len(self.units)} units with {sum(len(lessons) for lessons in self.units.values())} total lessons")
            return True
            
        except Exception as e:
            print(f"ERROR: Failed to update {readme_file}: {e}")
            return False
    
    def update_assets_needed(self, assets_path="ASSETS_NEEDED.md"):
        """
        Update the ASSETS_NEEDED.md file to ensure all lessons are represented.
        
        Args:
            assets_path (str): Path to the ASSETS_NEEDED.md file
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        assets_file = self.course_path / assets_path
        
        if not assets_file.exists():
            print(f"WARNING: {assets_file} not found - creating placeholder")
            # Could create a basic template here if needed
            return True
        
        try:
            # Read the current ASSETS_NEEDED content
            with open(assets_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # For now, we'll add a timestamp and course summary at the top
            # This ensures the file gets updated and shows it's in sync
            current_outline = self.generate_markdown_outline()
            
            # Check if there's already a course summary section
            summary_marker_start = "<!-- COURSE_SUMMARY_START -->"
            summary_marker_end = "<!-- COURSE_SUMMARY_END -->"
            
            current_lessons = sum(len(lessons) for lessons in self.units.values())
            current_units = len(self.units)
            
            summary_content = f"""<!-- COURSE_SUMMARY_START -->
<!-- This section is auto-updated by generate_course_outline.py -->
**Current Course Structure:** {current_units} units, {current_lessons} lessons

**Units Overview:**
{self._generate_units_summary()}

*Last updated: Auto-generated with course outline*
<!-- COURSE_SUMMARY_END -->"""
            
            if summary_marker_start in content and summary_marker_end in content:
                # Update existing summary
                start_pos = content.find(summary_marker_start)
                end_pos = content.find(summary_marker_end) + len(summary_marker_end)
                
                new_content = (
                    content[:start_pos] + 
                    summary_content + "\n\n" +
                    content[end_pos:]
                )
            else:
                # Add summary at the beginning after the title
                lines = content.split('\n')
                insert_pos = 1  # After the first line (title)
                
                # Find a good insertion point (after title and description)
                for i, line in enumerate(lines[:10]):  # Check first 10 lines
                    if line.strip() == "" and i > 0:  # First empty line after title
                        insert_pos = i + 1
                        break
                
                lines.insert(insert_pos, summary_content)
                lines.insert(insert_pos + 1, "")  # Add spacing
                new_content = '\n'.join(lines)
            
            # Write the updated content back to the file
            with open(assets_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Successfully updated {assets_file}")
            return True
            
        except Exception as e:
            print(f"ERROR: Failed to update {assets_file}: {e}")
            return False
    
    def _generate_units_summary(self):
        """Generate a summary of units for the assets file."""
        summary_lines = []
        sorted_units = sorted(self.units.keys())
        
        for unit_number in sorted_units:
            unit_title = self.get_unit_title(unit_number)
            lesson_count = len(self.units[unit_number])
            summary_lines.append(f"- Unit {unit_number}: {unit_title} ({lesson_count} lessons)")
        
        return '\n'.join(summary_lines)
    
    def print_outline(self):
        """Generate and print the course outline to console."""
        outline = self.generate_outline()
        print(outline)
    
    def save_outline(self, output_file="course_outline.txt"):
        """
        Generate and save the course outline to a file.
        
        Args:
            output_file (str): The filename to save the outline to
        """
        outline = self.generate_outline()
        output_path = self.course_path / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(outline)
        
        print(f"Course outline saved to: {output_path}")


def main():
    """Main entry point with command-line argument support."""
    parser = argparse.ArgumentParser(
        description="Generate course outline and optionally update documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_course_outline.py                    # Print outline to console
  python generate_course_outline.py --update-readme    # Update README.md and ASSETS_NEEDED.md
  python generate_course_outline.py --save-outline     # Save outline to course_outline.txt
  python generate_course_outline.py --update-readme --save-outline  # Do both
        """
    )
    
    parser.add_argument('--update-readme', action='store_true',
                        help='Update README.md and ASSETS_NEEDED.md with the current course outline')
    parser.add_argument('--save-outline', action='store_true',
                        help='Save the course outline to course_outline.txt')
    parser.add_argument('--readme-path', type=str, default='README.md',
                        help='Path to README file (default: README.md)')
    parser.add_argument('--assets-path', type=str, default='ASSETS_NEEDED.md',
                        help='Path to ASSETS_NEEDED file (default: ASSETS_NEEDED.md)')
    parser.add_argument('--output-file', type=str, default='course_outline.txt',
                        help='Output file for saved outline (default: course_outline.txt)')
    
    args = parser.parse_args()
    
    # Create the generator
    generator = CourseOutlineGenerator()
    
    # If no arguments provided, just print to console (default behavior)
    if not args.update_readme and not args.save_outline:
        generator.print_outline()
        return
    
    # Handle README and ASSETS_NEEDED update
    if args.update_readme:
        readme_success = generator.update_readme(args.readme_path)
        assets_success = generator.update_assets_needed(args.assets_path)
        
        if not readme_success or not assets_success:
            exit(1)
    
    # Handle saving outline to file
    if args.save_outline:
        generator.save_outline(args.output_file)
    
    # If we only updated README, also show a summary
    if args.update_readme and not args.save_outline:
        print("\nCurrent Course Summary:")
        print("-" * 50)
        generator.print_outline()


if __name__ == "__main__":
    main()
