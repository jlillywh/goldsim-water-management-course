# GoldSim Water Management Course: Lesson Design Specification

**Version:** 1.0  
**Date:** 2025-08-08  
**Purpose:** This document provides the official template and style guide for all lessons created for the GoldSim Water Management Course. Its purpose is to ensure that all course content is consistent, high-quality, and pedagogically effective. All lessons must adhere to this specification.

## 1.0 Audience and Prerequisites

### 1.1 Target Audience Profile
This course targets experienced engineering professionals and advanced students in water resources with the following characteristics:

- **Primary Audience:** Water resource engineers, environmental consultants, and mining engineers with 2+ years of professional experience
- **Secondary Audience:** Graduate students in hydrology, environmental engineering, or related fields
- **Tertiary Audience:** Regulatory professionals and water management planners requiring technical modeling skills

### 1.2 Prerequisites Assessment
Each lesson assumes students possess:

#### Technical Prerequisites
- **GoldSim Proficiency:** Minimum 40 hours of GoldSim modeling experience or completion of Basic GoldSim Course
- **Engineering Mathematics:** Comfortable with differential equations, statistics, and numerical methods
- **Hydrology Foundation:** Understanding of water cycle, mass balance principles, and basic hydraulics
- **Data Analysis Skills:** Experience with Excel, CSV files, and time series data manipulation

#### Professional Context Prerequisites
- **Project Experience:** Exposure to water resource planning, environmental impact assessment, or mining water management
- **Regulatory Awareness:** Familiarity with water rights, environmental regulations, and permitting processes
- **Systems Thinking:** Ability to conceptualize interconnected physical and human systems

### 1.3 Prerequisite Validation
Lessons should include brief prerequisite checks where appropriate:
- Reference to specific GoldSim elements students should recognize
- Quick review of essential concepts before building upon them
- Clear statements when advanced mathematical or domain knowledge is required

## 2.0 Instructional Strategy

### 2.1 Pedagogical Approach
The course employs a **Progressive Complexity** instructional model based on established engineering education principles:

#### Bloom's Taxonomy Integration
Each lesson systematically progresses through cognitive levels:
1. **Knowledge:** Introduce key concepts and terminology
2. **Comprehension:** Explain underlying principles and relationships
3. **Application:** Demonstrate implementation in GoldSim
4. **Analysis:** Examine model behavior and sensitivity
5. **Synthesis:** Integrate concepts into complex systems
6. **Evaluation:** Assess model validity and limitations

#### Adult Learning Principles (Andragogy)
- **Problem-Centered:** All content connects to real-world water management challenges
- **Experience Integration:** Build upon students' professional backgrounds
- **Self-Directed Learning:** Provide resources for independent exploration
- **Immediate Application:** Enable direct application to students' work contexts

### 2.2 Instructional Design Framework

#### Constructivist Learning Model
- **Scaffold Complexity:** Begin with simplified models, progressively add realistic complications
- **Active Construction:** Students build models rather than passively consuming information
- **Authentic Tasks:** Use real project data and industry-standard methodologies
- **Collaborative Elements:** Encourage peer discussion through analysis questions

#### Cognitive Load Management
- **Intrinsic Load:** Focus on essential complexity inherent to water systems modeling
- **Extraneous Load:** Minimize irrelevant GoldSim interface details and software promotion
- **Germane Load:** Optimize mental effort toward building transferable problem-solving schemas

### 2.3 Engagement Strategies

#### Motivation Through Relevance
- **Industry Context:** Begin each lesson with real-world applications and case studies
- **Professional Development:** Align content with career advancement and certification requirements
- **Problem Solving:** Frame technical content as solutions to common professional challenges

#### Active Learning Techniques
- **Guided Discovery:** Lead students through logical problem-solving sequences
- **Immediate Feedback:** Provide expected results and troubleshooting guidance
- **Reflection Prompts:** Include analysis questions that promote deeper understanding
- **Hands-On Application:** Balance conceptual explanation with practical implementation

## 3.0 Assessment and Evaluation Strategy

### 3.1 Formative Assessment Design
Continuous assessment throughout each lesson to monitor learning progress:

#### Real-Time Feedback Mechanisms
- **Step Verification:** Provide expected intermediate results during exercises
- **Common Error Prevention:** Anticipate typical mistakes and provide preemptive guidance
- **Self-Check Opportunities:** Include validation steps students can perform independently
- **Progress Indicators:** Clear milestones showing successful completion of learning segments

#### Diagnostic Assessment
- **Prerequisite Validation:** Quick checks to identify knowledge gaps early
- **Conceptual Understanding:** Questions that reveal misconceptions before they compound
- **Skill Application:** Simple exercises that demonstrate procedural competency

### 3.2 Summative Assessment Framework

#### Competency-Based Evaluation
Each lesson assessment measures specific, observable competencies:

##### Knowledge Assessment (20% weight)
- **Conceptual Understanding:** Multiple-choice questions testing principles and relationships
- **Terminology Mastery:** Proper use of technical vocabulary in context
- **Factual Recall:** Key parameters, typical values, and standard procedures

##### Skill Assessment (60% weight)
- **Technical Implementation:** Ability to build functioning GoldSim models following specifications
- **Problem Diagnosis:** Troubleshooting common modeling issues and errors
- **Parameter Selection:** Choosing appropriate values and methods for given scenarios

##### Critical Thinking Assessment (20% weight)
- **Model Evaluation:** Assessing model validity, limitations, and appropriate applications
- **Systems Analysis:** Understanding interconnections and feedback loops
- **Professional Judgment:** Making defensible engineering decisions under uncertainty

### 3.3 Assessment Validity and Reliability

#### Content Validity
- **Professional Relevance:** All assessments reflect actual workplace tasks and decisions
- **Industry Standards:** Align with recognized professional practice and regulatory requirements
- **Expert Review:** Subject matter experts validate technical accuracy and practical applicability

#### Construct Validity
- **Learning Objective Alignment:** Each assessment item directly measures stated objectives
- **Cognitive Level Matching:** Assessment difficulty appropriate for target cognitive processes
- **Skill Transfer:** Evaluate ability to apply learning to novel situations

#### Reliability Measures
- **Clear Rubrics:** Objective scoring criteria for subjective assessment elements
- **Consistent Standards:** Uniform expectations across all lessons and units
- **Multiple Measures:** Combine different assessment types to improve measurement reliability

### 3.4 Feedback and Improvement Cycle

#### Student Feedback Integration
- **Immediate Correction:** Provide correct answers with explanations for all quiz items
- **Remediation Guidance:** Direct students to additional resources when assessments indicate gaps
- **Progress Tracking:** Enable students to monitor their competency development across the course

#### Continuous Improvement
- **Performance Analytics:** Track common errors and misconceptions for content refinement
- **Engagement Metrics:** Monitor completion rates and time-on-task to optimize difficulty
- **Professional Relevance Updates:** Regular review to maintain alignment with industry evolution

## 4.0 Lesson Content Structure

## 4.0 Lesson Content Structure

Each lesson `.md` file must contain the following sections in this specific order. Sections marked with an asterisk (*) are optional if not applicable to a particular lesson.

### 4.1 Required Sections

1. **Lesson Title:** `# Lesson X: [Full Lesson Title]`
2. **Learning Objectives:** A bulleted list of specific, measurable skills the student will acquire
3. **Context / Overview:** Answers the question, "Why does this lesson matter?"
4. **Technical Content:** The core instructional material, using `###` for sub-topics
5. **Exercise / Activities:** Step-by-step instructions for hands-on application, including "Analysis Questions"
6. **Key Takeaways / Summary:** A bulleted or numbered list of the most critical points

### 4.2 Optional Sections*

7. **Quiz:** A short, multiple-choice self-assessment with answers provided
8. **Assets Needed:** A categorized list of all required files (`.gsm`, `.xlsx`, images, etc.)
9. **Next Steps:** Brief transition to the following lesson when appropriate

## 5.0 Content & Style Guidelines

## 5.0 Content & Style Guidelines

### 5.1 Writing Style
- **Tone:** Professional, direct, and instructional. The voice is that of an expert consultant focused on delivering a quality product
- **Conciseness:** Use clear, direct language. Avoid conversational filler and emojis
- **Accuracy:** Prioritize technical accuracy over software promotion
- **Clarity:** Write for engineers and water resource professionals with basic GoldSim knowledge

### 5.2 Technical Standards
- **Mathematical Notation:** Use LaTeX for all mathematical and scientific notations, delimited by `$` for inline and `$$` for block equations
- **Units:** Always specify units for numerical values (e.g., 150 mm/year, 5.2 m³/s)
- **Terminology:** Use consistent technical terminology throughout the course
- **Precision:** Provide specific values and parameters rather than vague descriptions

### 5.3 Formatting Standards
- **Headers:** Use standard markdown hierarchy (`#`, `##`, `###`)
- **Lists:** Use bullet points for unordered lists, numbers for sequential steps
- **Code/File References:** Use backticks for file names, element names, and parameters
- **Emphasis:** Use **bold** for key concepts, *italics* for emphasis

## 6.0 Learning Objectives Standards

## 6.0 Learning Objectives Standards

### 6.1 Format Requirements
- Begin each objective with an action verb (analyze, build, calculate, evaluate, implement)
- Be specific and measurable
- Focus on skills students will actually demonstrate
- Limit to 3-5 objectives per lesson

### 6.2 Example Format
```markdown
## Learning Objectives

By the end of this lesson, students will be able to:

- **Calculate** evapotranspiration rates using the Penman-Monteith equation in GoldSim
- **Build** a temperature-driven ET model with seasonal adjustment factors
- **Evaluate** model sensitivity to key meteorological parameters
- **Apply** ET calculations to water balance modeling scenarios
```

## 7.0 Technical Content Guidelines

## 7.0 Technical Content Guidelines

### 7.1 Structure Requirements
- Use `###` headers for major sub-topics
- Include conceptual explanation before GoldSim implementation
- Provide real-world context and applications
- Balance theory with practical application

### 7.2 Content Flow
1. **Conceptual Foundation:** Establish the underlying principles
2. **Mathematical Framework:** Present equations and relationships
3. **GoldSim Implementation:** Show how to build the concept in the software
4. **Practical Considerations:** Discuss limitations, assumptions, and best practices

### 7.3 Example Structure
```markdown
### Evapotranspiration Fundamentals

Evapotranspiration represents the combined water loss from...

The Penman-Monteith equation provides the most physically-based approach:

$$ET_0 = \frac{0.408\Delta(R_n - G) + \gamma\frac{900}{T+273}u_2(e_s - e_a)}{\Delta + \gamma(1 + 0.34u_2)}$$

### Implementation in GoldSim

The ET calculation requires the following elements:
- **Data Source:** Meteorological time series
- **Expression Element:** Penman-Monteith calculation
- **Lookup Table:** Crop coefficients by month
```

## 8.0 Exercise and Activities Standards

## 8.0 Exercise and Activities Standards

### 8.1 Structure Requirements
- Provide clear, numbered steps
- Include specific file names and element names
- Specify expected results or outcomes
- End with analysis questions

### 8.2 Step Format
```markdown
## Exercise: Building an ET Model

### Part 1: Model Setup
1. **Open** the file `03_02_ET_Base_Model.gsm`
2. **Navigate** to the "Meteorological Data" container
3. **Create** a new Expression element named `ET_Penman_Monteith`
4. **Enter** the following equation: [specific equation]
5. **Run** the model and verify the output matches expected values

### Analysis Questions
1. How does ET vary seasonally in your model output?
2. Which meteorological parameter has the greatest influence on ET rates?
3. What happens to ET calculations when wind speed data is missing?
```

## 9.0 Image and Asset Standards

## 9.0 Image and Asset Standards

### 9.1 Image Requirements
- **File Location:** All images must be referenced from the root `/images/` directory
- **Naming Convention:** `UU_LL_DescriptionInCamelCase.png` (e.g., `03_02_PenmanMonteithEquation.png`)
- **Size Guidelines:** Optimize for readability while maintaining reasonable file sizes
- **Alt Text:** Always provide meaningful alt text for accessibility

### 9.2 Image Referencing Format
```markdown
![Penman-Monteith ET Calculation](images/03_02_PenmanMonteithEquation.png)

<!-- For size control, use HTML: -->
<img src="images/03_02_ETModelStructure.png" alt="ET Model Structure" width="75%">
```

### 9.3 Asset Documentation
When lessons require external files, document them clearly:

```markdown
## Assets Needed

### GoldSim Models
- `03_02_ET_Base_Model.gsm` - Base model with meteorological data
- `03_02_ET_Complete_Model.gsm` - Completed exercise model

### Data Files
- `Meteorological_Data_2020.xlsx` - Daily weather data for exercises
- `Crop_Coefficients.csv` - Monthly crop coefficient lookup table

### Reference Images
- `03_02_PenmanMonteithEquation.png` - Equation visualization
- `03_02_ETModelStructure.png` - GoldSim model structure diagram
```

## 10.0 Quiz Standards

## 10.0 Quiz Standards

### 10.1 Format Requirements
- 3-5 multiple choice questions maximum
- Focus on key concepts and practical application
- Provide correct answer with brief explanation
- Test understanding, not memorization

### 10.2 Example Quiz Format
```markdown
---

## Quiz

**1.** Which meteorological parameter typically has the greatest influence on ET rates?

**A)** Wind speed  
**B)** Solar radiation  
**C)** Relative humidity  
**D)** Air pressure  

**2.** In the Penman-Monteith equation, what does the term $\Delta$ represent?

**A)** Change in temperature  
**B)** Slope of saturation vapor pressure curve  
**C)** Wind speed adjustment factor  
**D)** Crop coefficient  

---

### Quiz Answers

**1. B)** Solar radiation provides the primary energy source for evapotranspiration, making it typically the most influential parameter.

**2. B)** Delta (Δ) represents the slope of the saturation vapor pressure curve with respect to temperature.
```

## 11.0 Quality Assurance Checklist

## 11.0 Quality Assurance Checklist

Before finalizing any lesson, verify:

### 11.1 Content Quality
- [ ] All learning objectives are specific and measurable
- [ ] Technical content flows logically from concepts to implementation
- [ ] Mathematical notation uses proper LaTeX formatting
- [ ] All units are specified for numerical values
- [ ] Examples use realistic, relevant data

### 11.2 Format Compliance
- [ ] Lesson follows required section structure
- [ ] Headers use proper markdown hierarchy
- [ ] Images reference correct file paths
- [ ] File names and GoldSim elements use backticks
- [ ] Lists are properly formatted

### 11.3 Exercise Validation
- [ ] All steps are clearly numbered and specific
- [ ] Required files are listed and accessible
- [ ] Expected results are specified
- [ ] Analysis questions test understanding

### 11.4 Technical Accuracy
- [ ] All equations are mathematically correct
- [ ] GoldSim implementation steps are verified
- [ ] Parameter values are realistic and appropriate
- [ ] Assumptions and limitations are clearly stated

### 11.5 Instructional Design Compliance
- [ ] Content addresses target audience prerequisites
- [ ] Instructional strategy aligns with learning objectives
- [ ] Assessment methods match cognitive complexity
- [ ] Feedback mechanisms support continuous learning

## 12.0 Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-08-08 | Initial specification document |

**Note:** This specification document focuses exclusively on lesson content standards and style guidelines. For project-level architecture, file management workflows, and automation procedures, refer to `.github/copilot-instructions.md`.
