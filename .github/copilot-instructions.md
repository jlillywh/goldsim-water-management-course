# GoldSim Water Management Course - AI Agent Instructions

## Project Overview
This is an educational course repository focused on water management modeling using GoldSim software. The project uses a **flat directory structure** with sophisticated automation for lesson management, documentation generation, and asset deployment.

## Critical File Structure & Naming Conventions

### Lesson Files (MANDATORY FORMAT)
- **Pattern**: `UU-LL-lesson-title.md` (e.g., `03-05-case-study-the-australian-water-balance-model.md`)
- **UU**: Unit number (01, 02, 03...)
- **LL**: Lesson number within unit (01, 02, 03...)
- **Location**: All lesson files live in root directory (flat structure, not nested folders)

### Images
- **Naming**: `UU_LL_DescriptionInCamelCase.png` (e.g., `01_01_MonoLakeModel.png`)
- **Location**: Single `images/` directory at root level
- **Organization**: UULL naming convention for lesson-image association

## Essential Workflows (NEVER SKIP THESE)

### 1. After ANY Lesson File Changes
```batch
run_update.bat
```
**This MUST be run after creating, editing, or modifying lesson files.** It:
- Updates README.md course outline (auto-generated between `<!-- COURSE_OUTLINE_START -->` and `<!-- COURSE_OUTLINE_END -->`)
- Updates ASSETS_NEEDED.md with lesson counts
- Synchronizes all documentation

### 2. Inserting New Lessons (Requires Renumbering)
```batch
# Step 1: Create space by renumbering existing lessons
python renumber_lessons.py [insertion_point] --dry-run  # Preview changes
python renumber_lessons.py [insertion_point]            # Execute renumbering

# Step 2: Create new lesson file in the empty slot
# (Manual file creation with proper UU-LL naming)

# Step 3: MANDATORY - Update all documentation
run_update.bat
```

### 3. Safety Features
- **Automatic backups**: Created before any renumbering operations (`backup_YYYY_MM_DD_HH_MM_SS/` folders)
- **Dry-run validation**: Use `--dry-run` flag to preview all operations
- **Rollback capability**: `rollback_lessons.py` can restore from backups

## Key Architecture Components

### Core Automation Scripts
- **`generate_course_outline.py`**: Scans lesson files, generates structured course outline for README.md
- **`renumber_lessons.py`**: Safely renumbers lesson files when inserting new content
- **`run_update.bat`**: Master automation script - combines renumbering + documentation updates

### Asset Management Pipeline
- **`Deploy-Lesson-Images.ps1`**: Stages images for web deployment with unit-based organization
- **`Optimize-Images-For-Web.ps1`**: Processes images for web delivery
- **Image workflow**: Central capture → automated sorting → lesson-specific directories

### Documentation Auto-Generation
- **README.md**: Course structure auto-updated between comment markers
- **ASSETS_NEEDED.md**: Lesson counts and unit summaries auto-maintained
- **Pattern**: Look for `<!-- SECTION_START -->` / `<!-- SECTION_END -->` markers for auto-generated content

## Development Patterns

### Content Structure
- **Units**: Thematic groupings (Climate Data, Hydrology, Reservoir Modeling, etc.)
- **Lessons**: Individual markdown files with practical GoldSim modeling instruction
- **Progressive complexity**: Units build from foundational concepts to advanced applications

### Windows-Centric Environment
- **Batch scripts**: Primary automation interface (`.bat` files)
- **PowerShell**: Advanced image processing and deployment workflows
- **Python**: Core logic for file operations and course structure management

### Error Handling Philosophy
- **Safety-first**: All destructive operations have dry-run modes
- **Comprehensive backups**: Automatic backup creation before any file moves/renames
- **Validation chains**: Multiple validation steps before executing operations

## Common Anti-Patterns to Avoid

1. **Never edit lesson files without running `run_update.bat` afterward**
2. **Never create lesson files with incorrect UU-LL naming format**
3. **Never manually edit auto-generated sections in README.md or ASSETS_NEEDED.md**
4. **Never renumber lessons without first running dry-run preview**
5. **Never assume lesson numbering gaps are errors** - they may be intentional placeholders

## Integration Points

### External Dependencies
- **GoldSim software**: The modeling tool being taught
- **SnagIt**: Screenshot capture tool for lesson images
- **Web deployment**: Staging system for course delivery

### Cross-References
- Lessons reference specific GoldSim model files and techniques
- Image references use relative paths to `images/` directory
- Course structure reflected in both README.md and ASSETS_NEEDED.md simultaneously
