# UULL Naming Convention Reference

## Updated Format: UU LL Name-sequence-description

### Pattern
`[UU] [LL] [LessonName]-[sequence]-[description].png`

### Components
- **UU**: Unit Number (2 digits, zero-padded)
- **LL**: Lesson Number (2 digits, zero-padded)
- **LessonName**: Natural lesson name with spaces
- **sequence**: Sequential number for ordering (2+ digits)
- **description**: Brief description in kebab-case

### Examples

#### Unit 4 (Water Demand and Use)
```
04 01 Introduction to Water Demand-01-concepts-diagram.png
04 01 Introduction to Water Demand-02-goldsim-setup.png
04 01 Introduction to Water Demand-03-demand-sectors.png
04 02 Municipal Water Modeling-01-population-input.png
04 02 Municipal Water Modeling-02-per-capita-rates.png
```

#### Unit 7 (Groundwater)
```
07 01 Groundwater Concepts-01-aquifer-types.png
07 02 Aquifer Element Practice-01-element-properties.png
07 03 Modeling Wells and Pumping-01-well-boundary.png
07 04 Surface Water Groundwater Interaction-01-stream-aquifer.png
07 05 Managed Aquifer Recharge-01-recharge-systems.png
```

### Regex Pattern
```regex
^(\d{2})\s+(\d{2})\s+([^-]+)-(\d+)-(.+)$
```

### Benefits
1. **Human Readable**: Natural spacing in lesson names
2. **Easy Parsing**: Clear delimiters between components
3. **Sortable**: Numeric prefixes ensure proper ordering
4. **Flexible**: Works with any lesson name length
5. **Descriptive**: Sequence and description provide context

### PowerShell Parsing Example
```powershell
$filename = "04 01 Introduction to Water Demand-01-concepts-diagram"
if ($filename -match '^(\d{2})\s+(\d{2})\s+([^-]+)-(\d+)-(.+)$') {
    $unitNumber = $matches[1]      # "04"
    $lessonNumber = $matches[2]    # "01" 
    $lessonName = $matches[3].Trim() # "Introduction to Water Demand"
    $sequence = $matches[4]        # "01"
    $description = $matches[5]     # "concepts-diagram"
}
```

This naming convention enables automatic sorting of captured images into the correct lesson folders while maintaining readability and organization.
