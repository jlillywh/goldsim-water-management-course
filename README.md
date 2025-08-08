# GoldSim Water Management Course

This repository contains the complete curriculum for the GoldSim Water Management course, organized into 12 comprehensive units covering all aspects of water system modeling.

## Course Structure

The course is organized into three main parts, building from foundational concepts to advanced applications:

<!-- COURSE_OUTLINE_START -->
### Unit 1: Foundations and Data Preparation
- Lesson 01: [Welcome To The Course](01-01-welcome-to-the-course.md)
- Lesson 03: [Course Resources And Setup](01-03-course-resources-and-setup.md)
- Lesson 05: [What Makes Water Management Modeling Unique](01-05-what-makes-water-management-modeling-unique.md)
- Lesson 06: [Overview Of A Water Management System Model](01-06-overview-of-a-water-management-system-model.md)
- Lesson 07: [Thinking In Goldsim Dynamic Simulation Primer](01-07-thinking-in-goldsim-dynamic-simulation-primer.md)
- Lesson 08: [Understanding Temporal And Spatial Scales](01-08-understanding-temporal-and-spatial-scales.md)
- Lesson 09: [Representing Data In Goldsim](01-09-representing-data-in-goldsim.md)
- Lesson 10: [Modeling Workflow And Best Practices](01-10-modeling-workflow-and-best-practices.md)

### Unit 2: Climate Data and Weather Modeling
- Lesson 01: [Working With Precipitation Data](02-01-working-with-precipitation-data.md)
- Lesson 03: [Stochastic Weather Generation](02-03-stochastic-weather-generation.md)
- Lesson 05: [Practical Implementation The Precipgen Simulator](02-05-practical-implementation-the-precipgen-simulator.md)
- Lesson 06: [Design Storms](02-06-design-storms.md)
- Lesson 07: [Working With Temperature Data](02-07-working-with-temperature-data.md)
- Lesson 08: [Handling Climate Data Gaps And Spatial Variability](02-08-handling-climate-data-gaps-and-spatial-variability.md)
- Lesson 09: [Advanced Climate Analysis Drought Indices](02-09-advanced-climate-analysis-drought-indices.md)
- Lesson 10: [Using Historical Records For Probabilistic Simulation](02-10-using-historical-records-for-probabilistic-simulation.md)
- Lesson 11: [Incorporating Climate Model Projections](02-11-incorporating-climate-model-projections.md)

### Unit 3: Hydrology and Water Balance
- Lesson 01: [Evaporation And Evapotranspiration](03-01-evaporation-and-evapotranspiration.md)
- Lesson 02: [Temperature Based Et Methods](03-02-temperature-based-et-methods.md)
- Lesson 03: [Snow Accumulation And Melt](03-03-snow-accumulation-and-melt.md)
- Lesson 04: [Runoff Estimation Methods](03-04-runoff-estimation-methods.md)
- Lesson 05: [Case Study The Australian Water Balance Model](03-05-case-study-the-australian-water-balance-model.md)
- Lesson 06: [Modeling Multiple Catchments](03-06-modeling-multiple-catchments.md)

### Unit 4: Water Demand and Consumption
- Lesson 01: [Introduction To Water Demand](04-01-introduction-to-water-demand.md)

### Unit 5: Reservoir Modeling and Operations
- Lesson 01: [Introduction To Reservoir Modeling](05-01-introduction-to-reservoir-modeling.md)
- Lesson 03: [Simulating Operational Rules](05-03-simulating-operational-rules.md)
- Lesson 09: [Advanced Shared Storage Allocation](05-09-advanced-shared-storage-allocation.md)
- Lesson 10: [Physical Processes In Reservoirs](05-10-physical-processes-in-reservoirs.md)

### Unit 7: Groundwater Systems
- Lesson 01: [Introduction To Groundwater Concepts](07-01-introduction-to-groundwater-concepts.md)
- Lesson 03: [Simulating Flow With The Aquifer Element](07-03-simulating-flow-with-the-aquifer-element.md)
- Lesson 09: [Modeling Wells And Pumping](07-09-modeling-wells-and-pumping.md)
- Lesson 10: [Surface Water Groundwater Interaction](07-10-surface-water-groundwater-interaction.md)
- Lesson 11: [Managed Aquifer Recharge Case Study](07-11-managed-aquifer-recharge-case-study.md)
<!-- COURSE_OUTLINE_END -->

## Prerequisites

- Basic GoldSim experience
- Understanding of water systems and hydrology
- Engineering background
- GoldSim Pro or higher license

## Course Objectives

By completion, students will be able to model integrated water systems, handle complex flow networks, incorporate uncertainty, perform risk analysis, and apply real-world solutions to water management challenges.

---

## 🚨 CRITICAL: Development Workflows for Lesson Management

### **⚠️ MANDATORY WORKFLOW: Always Update Documentation After Lesson Changes**

**EVERY TIME** you create, edit, or modify any lesson file, you **MUST** run the documentation update:

```batch
run_update.bat
```

This single command will:
- ✅ Update README.md with current course structure
- ✅ Update ASSETS_NEEDED.md with current lesson counts
- ✅ Synchronize lesson counts and links
- ✅ Maintain accurate course documentation

### **Essential Lesson Management Commands**

#### 1. **Documentation Update Only** (Most Common)
Use when you've manually created/edited lesson files and need to sync documentation:
```batch
run_update.bat
```

#### 2. **Insert Lesson + Auto-Renumber** (Advanced)
Use when inserting a lesson between existing lessons:
```batch
run_update.bat [lesson_number]
# Example: run_update.bat 3  (inserts after lesson 3, renumbers rest)
```

#### 3. **Manual Course Outline Generation**
Direct access to outline generator:
```batch
python generate_course_outline.py --update-readme
```

#### 4. **Safe Lesson Renumbering** (Use with Caution)
For complex renumbering operations:
```batch
python renumber_lessons.py [insertion_point] --force
```

### **Lesson File Naming Convention**

**CRITICAL:** All lesson files MUST follow the UU-LL-lesson-title.md format:
- UU = Unit number (01, 02, 03...)
- LL = Lesson number within unit (01, 02, 03...)
- Example: `02-09-incorporating-climate-model-projections.md`

### **Required Workflow for New Conversations**

🔥 **FOR ALL FUTURE CONVERSATIONS INVOLVING LESSON MANAGEMENT:**

1. **After creating any new lesson file**: Run `run_update.bat`
2. **After editing existing lessons**: Run `run_update.bat` 
3. **After renumbering lessons**: Run `run_update.bat`
4. **Before completing any lesson-related task**: Verify README.md is updated

### **Quality Assurance Checklist**

Before considering any lesson work complete:
- [ ] New/modified lesson files follow naming convention
- [ ] `run_update.bat` has been executed successfully
- [ ] README.md reflects all changes
- [ ] Course outline shows correct lesson count
- [ ] All lesson links are functional

### **Backup and Safety**

The automation system includes:
- **Automatic backups** before any renumbering operations
- **Dry-run validation** for all file operations
- **Rollback capability** if operations fail
- **Error handling** with clear failure messages

### **File Structure Management**

```
goldsim-water-management-course/
├── run_update.bat              # Main automation script
├── generate_course_outline.py  # Documentation generator  
├── renumber_lessons.py         # Lesson renumbering tool
├── README.md                   # Course documentation (auto-updated)
├── UU-LL-lesson-title.md      # Lesson files (flat structure)
└── images/                     # Course images and assets
```

---
