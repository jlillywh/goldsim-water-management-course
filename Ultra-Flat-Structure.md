# Ultra-Flat Course Structure 🎯

## Philosophy: Maximum Simplicity

**Why make it complicated when it can be simple?**

- **Filenames contain all the organization** - no need for folders
- **One images folder** - all images in one predictable place  
- **Flat is better than nested** - easier to find, manage, and navigate

## Structure

```
goldsim-water-management-course/
├── images/                           ← ALL images here
│   ├── 01-01-01-welcome-screen.png
│   ├── 01-03-01-system-diagram.png
│   ├── 04-01-01-demand-concepts.png
│   ├── 04-01-02-sectors-chart.png
│   ├── 07-03-01-well-boundary.png
│   └── goldsim-monolake-example.png
├── 01-01-welcome-to-the-course.md
├── 01-02-course-resources-and-setup.md
├── 01-03-dynamic-simulation-primer.md
├── 04-01-introduction-to-water-demand.md
├── 04-02-municipal-water-modeling.md
├── 07-01-groundwater-concepts.md
├── 07-03-modeling-wells-and-pumping.md
└── README.md
```

## Daily Workflow

### 1. Capture Screenshots
- **SnagIt saves to**: `C:\Users\JasonLillywhite\Documents\Snagit\OnlineCourse`
- **Use UULL naming**: `04 01 Introduction to Water Demand-01-concepts.png`
- **Or simple naming**: `04 01 Introduction to Water Demand.png`

### 2. Sort Images
```batch
# Preview what will be moved
quick-sort-flat.bat --dry-run

# Actually move the files
quick-sort-flat.bat
```

### 3. Reference in Markdown
```markdown
![Water Demand Concepts](images/04-01-01-concepts.png)
![System Overview](images/goldsim-monolake-example.png)
```

## File Naming Conventions

### Lesson Files
Format: `UU-LL-lesson-name.md`

Examples:
- `01-01-welcome-to-the-course.md`
- `04-01-introduction-to-water-demand.md`
- `07-03-modeling-wells-and-pumping.md`
- `12-05-risk-assessment-methods.md`

### Image Files  
Format: `UU-LL-SS-description.png`

Examples:
- `04-01-01-demand-concepts.png`
- `04-01-02-sectors-diagram.png`
- `07-03-01-well-boundary.png`
- `07-03-12-results-analysis.png`

### Special Images
For course-wide images (not lesson-specific):
- `goldsim-monolake-example.png`
- `course-overview-diagram.png`
- `system-architecture.png`

## Benefits

✅ **Ultra-simple navigation** - All lessons visible at once  
✅ **No folder hunting** - Everything at root level  
✅ **Easy bulk operations** - Select all Unit 4 files instantly  
✅ **Predictable image paths** - Always `images/filename.png`  
✅ **Version control friendly** - Flat structure diffs better  
✅ **Easy searching** - All content searchable from root  
✅ **No duplication** - Filename IS the organization  

## Migration

If you have existing nested structure, run:

```bash
python migrate-to-flat.py
```

This will:
- ✅ Copy all `lesson.md` files to root with new names
- ✅ Move all images to global `images/` folder
- ✅ Preserve all content and metadata

## VS Code Tips

- **File Explorer**: All lessons visible at once - no drilling down
- **Quick Open** (`Ctrl+P`): Type `04-01` to find Unit 4 Lesson 1 instantly
- **Search** (`Ctrl+Shift+F`): Searches all lessons simultaneously
- **Markdown Preview**: Images always load from `images/` folder

## The Result

**Before**: 47 nested folders, complex paths, hunting for files  
**After**: 2 folders total, everything instantly visible, zero confusion

*Sometimes the best solution is the simplest one.* 🎯
