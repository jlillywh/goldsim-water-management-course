# Python Image Sorting Automation

## Overview
The Python-based image sorting system provides a robust, reliable way to automatically organize captured screenshots into the correct lesson folders based on the UULL naming convention.

## Key Advantages over PowerShell
✅ **Cross-platform compatibility** - Works on Windows, Mac, Linux  
✅ **Better error handling** - Clear error messages and recovery  
✅ **More reliable parsing** - Robust regex pattern matching  
✅ **Easier debugging** - Cleaner code structure  
✅ **Better logging** - Detailed progress reporting  

## UULL Naming Convention (Updated)

### Full Format
`UU LL LessonName-sequence-description.png`
- **Example**: `04 01 Introduction to Water Demand-01-concepts-diagram.png`

### Simple Format  
`UU LL LessonName.png`
- **Example**: `01 03 System Model.png`

## Quick Usage

### Method 1: Batch File (Easiest)
```batch
# For dry run (preview what will happen)
quick-sort-images.bat --dry-run

# To actually move files
quick-sort-images.bat
```

### Method 2: Direct Python Command
```bash
# Dry run
python sort_images.py --dry-run

# Actual execution
python sort_images.py

# Custom source directory
python sort_images.py --source "C:\Custom\Path\To\Images"
```

## Workflow Integration

### Daily Course Development Workflow

1. **Capture Screenshots**
   - Configure SnagIt to save to: `C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse`
   - Name files using UULL convention as you capture
   - Work on multiple lessons without worrying about organization

2. **Sort Images (End of Session)**
   ```batch
   # Preview what will be sorted
   quick-sort-images.bat --dry-run
   
   # Actually move the files
   quick-sort-images.bat
   ```

3. **Continue with Existing Workflow**
   - Images are now organized in lesson folders: `raw/` and `processed/`
   - Use existing optimization and staging scripts as needed

## Directory Structure After Sorting

```
Lesson_XX-Lesson-Name/
├── lesson.md
└── images/
    ├── raw/          # Original captures (moved here automatically)
    │   └── 01-03-01-image.png
    ├── processed/    # Ready for editing (copied here automatically)  
    │   └── 01-03-01-image.png
    └── web/          # Web-optimized versions (create manually or with scripts)
```

## Advanced Features

### Flexible Naming Support
- **Full UULL**: `04 01 Introduction to Water Demand-01-concepts-diagram.png`
- **Simple UULL**: `01 03 System Model.png` (auto-assigns sequence "01" and description "image")

### Smart Directory Detection
- Automatically finds unit directories by pattern matching (`04-*`)
- Locates lesson directories within units (`Lesson_01-*`)
- Handles various naming conventions and structures

### Error Handling
- Clear error messages for unrecognized file names
- Shows available lessons if target not found
- Provides helpful naming examples
- Continues processing even if some files fail

### Safety Features
- Dry run mode to preview operations
- Moves originals to `raw/` and copies to `processed/`
- Creates missing directory structures automatically
- Preserves original timestamps and metadata

## Command Line Options

```bash
python sort_images.py --help

Options:
  --source, -s      Source directory (default: SnagIt OnlineCourse folder)
  --course-root, -c Course root directory (default: course workspace)
  --dry-run, -d     Preview mode - no files moved
  --help, -h        Show help message
```

## Troubleshooting

### Common Issues

**"No images found"**
- Check that SnagIt is saving to the correct directory
- Verify PNG files exist in source directory

**"Unrecognized naming pattern"**
- Ensure files follow UULL convention with spaces
- Examples: `04 01 Introduction to Water Demand-01-diagram.png`

**"Could not find unit/lesson directory"**
- Verify the course structure exists
- Check unit and lesson numbers match directory names

### Testing New File Names
```bash
# Test a specific file pattern
python sort_images.py --dry-run
```

## Benefits for Course Development

1. **Efficiency**: Capture multiple lessons worth of images, then sort in batch
2. **Consistency**: Standardized file naming and organization
3. **Safety**: Dry run mode prevents accidental moves
4. **Flexibility**: Works with partial or full UULL naming
5. **Scalability**: Handles hundreds of images across dozens of lessons
6. **Integration**: Works with existing optimization and deployment scripts

## Migration from PowerShell

The Python script is a drop-in replacement for the PowerShell version with these improvements:
- ✅ More reliable parsing and error handling
- ✅ Better progress reporting and debugging
- ✅ Cross-platform compatibility
- ✅ Simpler command-line interface
- ✅ More robust directory detection

All existing image workflow scripts (optimization, staging) continue to work unchanged.
