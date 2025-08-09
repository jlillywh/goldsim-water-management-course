import os
import re
import logging
from typing import List, Dict

SPEC_PATH = 'Lesson-Design-Specification.md'
LESSON_PATTERN = re.compile(r'\d{2}-\d{2}-.+\.md$')

# Configure logging
logging.basicConfig(filename='lesson_compliance.log',
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

REQUIRED_SECTIONS = [
    'Lesson Title',
    'Learning Objectives',
    'Context / Overview',
    'Technical Content',
    'Exercise / Activities',
    'Key Takeaways / Summary',
    # Optional: 'Quiz', 'Assets Needed', 'Next Steps'
]

SECTION_HEADER_MAP = {
    'Lesson Title': re.compile(r'^# Lesson', re.IGNORECASE),
    'Learning Objectives': re.compile(r'^## Learning Objectives', re.IGNORECASE),
    'Context / Overview': re.compile(r'^## Context / Overview', re.IGNORECASE),
    'Technical Content': re.compile(r'^## Technical Content', re.IGNORECASE),
    'Exercise / Activities': re.compile(r'^## Exercise / Activities', re.IGNORECASE),
    'Key Takeaways / Summary': re.compile(r'^## Key Takeaways / Summary', re.IGNORECASE),
    'Quiz': re.compile(r'^## Quiz', re.IGNORECASE),
    'Assets Needed': re.compile(r'^## Assets Needed', re.IGNORECASE),
    'Next Steps': re.compile(r'^## Next Steps', re.IGNORECASE),
}


def parse_spec_sections(spec_path: str) -> List[str]:
    # For now, use the REQUIRED_SECTIONS list; could be extended to parse the spec dynamically
    return REQUIRED_SECTIONS


def find_lesson_files(root: str) -> List[str]:
    lesson_files = []
    for fname in os.listdir(root):
        if LESSON_PATTERN.match(fname):
            lesson_files.append(os.path.join(root, fname))
    return lesson_files


def parse_sections(lines: List[str]) -> Dict[str, List[str]]:
    sections = {}
    current_section = None
    for line in lines:
        for section, pattern in SECTION_HEADER_MAP.items():
            if pattern.match(line.strip()):
                current_section = section
                sections[current_section] = [line]
                break
        else:
            if current_section:
                sections[current_section].append(line)
    return sections


def rewrite_lesson(sections: Dict[str, List[str]], required_sections: List[str], original_lines: List[str]) -> List[str]:
    new_lines = []
    for section in required_sections:
        if section in sections:
            new_lines.extend(sections[section])
            if not new_lines[-1].endswith('\n'):
                new_lines.append('\n')
        else:
            # Insert placeholder for missing section
            if section == 'Lesson Title':
                # Try to find the original title
                for line in original_lines:
                    if line.strip().startswith('# '):
                        new_lines.append(line)
                        break
                else:
                    new_lines.append(f'# {section}\n')
            else:
                new_lines.append(f'## {section}\n\n*This section is required by the specification but was missing. Please update.*\n')
    # Add any remaining sections (e.g., Quiz, Assets Needed) at the end
    for section in ['Quiz', 'Assets Needed', 'Next Steps']:
        if section in sections:
            new_lines.extend(sections[section])
            if not new_lines[-1].endswith('\n'):
                new_lines.append('\n')
    return new_lines


def process_lesson_file(path: str, required_sections: List[str]) -> bool:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    sections = parse_sections(lines)
    new_lines = rewrite_lesson(sections, required_sections, lines)
    if new_lines != lines:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        logging.info(f'Updated: {path}')
        return True
    else:
        logging.info(f'No changes needed: {path}')
        return False


def main():
    root = os.getcwd()
    required_sections = parse_spec_sections(SPEC_PATH)
    lesson_files = find_lesson_files(root)
    updated = []
    for lesson in lesson_files:
        changed = process_lesson_file(lesson, required_sections)
        if changed:
            updated.append(lesson)
    logging.info(f'Checked {len(lesson_files)} lesson files. Updated: {len(updated)}')
    print(f'Checked {len(lesson_files)} lesson files. Updated: {len(updated)}')

if __name__ == '__main__':
    main()
