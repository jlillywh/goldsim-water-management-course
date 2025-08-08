# Standard Operating Procedure (SOP): Safe Lesson Addition
## Version 2.0 - Enhanced Safety Protocol

**Status**: MANDATORY - This SOP must be followed for all lesson additions to prevent duplicate files and maintain course integrity.

---

## **Overview**

This SOP establishes the definitive workflow for adding new lessons to the GoldSim Water Management Course. The previous workflow created critical bugs including duplicate files and manual cleanup requirements. This enhanced procedure eliminates those risks.

---

## **The Problem (Why This SOP Exists)**

The old workflow of "create file first, then make space" caused:
- ✗ Duplicate lesson files (e.g., both `03-04-topic.md` and `03-05-topic.md`)  
- ✗ Manual file juggling and cleanup requirements
- ✗ Risk of losing content during manual operations
- ✗ Inconsistent course structure

---

## **The Solution: Renumber-First Workflow**

### **STEP 1: Create Space (RENUMBER FIRST)**
```cmd
python renumber_lessons.py [SLOT_NUMBER] --dry-run
```
- **Purpose**: Preview the renumbering operation
- **Validation**: Confirm the correct files will be moved
- **Safety**: No files are modified in dry-run mode

```cmd
python renumber_lessons.py [SLOT_NUMBER]
```
- **Purpose**: Execute the renumbering to create empty slot
- **Automatic**: Backup files are created automatically
- **Result**: Empty slot ready for new lesson

### **STEP 2: Create Lesson File**
```cmd
# Manual file creation in the empty slot
notepad 03-05-new-lesson-topic.md
```
- **Purpose**: Create the new lesson file in the prepared slot
- **Safety**: No conflicts possible - slot is guaranteed empty
- **Content**: Add lesson content using standard template

### **STEP 3: Update Documentation**  
```cmd
python generate_course_outline.py
```
- **Purpose**: Update course outline and navigation
- **Result**: Course documentation reflects new structure

---

## **Enhanced Safety Features (Script Improvements)**

The `renumber_lessons.py` script now includes:

### **Pre-Flight Workflow Guidance**
- Clear step-by-step reminders displayed during execution
- Warnings about duplicate creation risks
- Confirmation of correct workflow sequence

### **Comprehensive Backup System**
- Automatic backup of all affected files
- Timestamped backup directories  
- Rollback capability if issues occur

### **Duplicate Detection** *(Added in v2.0)*
- Content similarity analysis between lessons
- Filename pattern matching
- Early warning for potential duplicates

### **Detailed Operation Logging**
- Complete audit trail of all operations
- Error tracking and reporting
- Success confirmation with file counts

---

## **Example: Adding Lesson 03-05**

```cmd
# Step 1: Create space (renumber first)
python renumber_lessons.py 5 --dry-run
# Review the planned changes, then:
python renumber_lessons.py 5

# Step 2: Create lesson file  
notepad 03-05-integrated-watershed-modeling.md
# Add lesson content

# Step 3: Update documentation
python generate_course_outline.py
```

**Result**: Clean insertion with no duplicates or manual cleanup required.

---

## **Rollback Procedure**

If issues occur during renumbering:

```cmd
# Automatic rollback (built into script)
# Manual rollback if needed:
python rollback_lessons.py backup_2025_08_07_16_54_23
```

---

## **Verification Checklist**

After lesson addition, verify:
- [ ] No duplicate lesson files exist
- [ ] All lesson numbers are sequential
- [ ] Course outline is updated
- [ ] Backup directory contains original files
- [ ] New lesson integrates properly with navigation

---

## **Non-Compliance Consequences**

**Using the old workflow (create-first) will result in:**
- Duplicate files requiring manual cleanup
- Risk of content loss
- Course structure inconsistencies
- Development team investigation time

**All team members must follow this SOP without exception.**

---

## **Script Locations**

- **Renumbering**: `renumber_lessons.py` (Enhanced v2.0)
- **Rollback**: `rollback_lessons.py`  
- **Outline Generation**: `generate_course_outline.py`

---

## **Contact**

For questions about this SOP or issues with the scripts, contact the development team immediately. Do not attempt workarounds that bypass this workflow.

---

**Document Version**: 2.0  
**Last Updated**: August 7, 2025  
**Next Review**: September 7, 2025
