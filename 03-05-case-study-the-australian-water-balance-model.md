# Lesson 4: Case Study - The Australian Water Balance Model (AWBM)

**Objective:** Learn to implement and calibrate a complete, pre-built conceptual rainfall-runoff model (the AWBM) in GoldSim, understanding how to leverage established modeling frameworks for practical water resource applications.

## Why This Matters

In the previous lessons, we built runoff calculation methods from fundamental principles. In many real-world projects, however, it's more efficient and defensible to use established, pre-validated models that have undergone extensive testing and peer review. This lesson teaches the crucial professional skill of taking a complex, pre-built component, understanding its inputs and outputs, and applying it to solve specific problems.

This approach represents how a majority of practical modeling is accomplished in professional practice:

- **Efficiency:** Leverage decades of research and development
- **Reliability:** Use models with extensive validation and testing
- **Standardization:** Apply widely-accepted methodologies
- **Defensibility:** Use models with scientific peer review and operational history
- **Time Management:** Focus on application rather than algorithm development

Understanding how to effectively use pre-built components is as important as understanding how to build models from scratch, and often more valuable in professional practice.

## Understanding Conceptual Rainfall-Runoff Models

### Conceptual vs. Event-Based Models

**Event-Based Models** (like SCS Curve Number):
- Calculate runoff from individual storm events
- Suitable for design applications
- Require antecedent moisture assumptions
- Focus on peak flows and volumes

**Conceptual Models** (like AWBM):
- Run continuously over extended periods
- Track catchment moisture state through time
- Simulate both surface runoff and baseflow
- Capture seasonal and long-term hydrologic patterns

### Key Characteristics of Conceptual Models

**Continuous Simulation:** Models operate on continuous time series, maintaining water balance between events and tracking the evolution of catchment wetness.

**State Variables:** Internal storage components represent soil moisture, groundwater levels, and other hydrologic states that influence runoff generation.

**Physical Representation:** While simplified, conceptual models represent key physical processes including infiltration, evapotranspiration, soil moisture dynamics, and groundwater interaction.

**Parameter Calibration:** Models require calibration against observed data to optimize parameter values for specific catchments.

![Conceptual Model Principles](images/ConceptualModelFramework.png)

## Part 1: Introduction to the Australian Water Balance Model (AWBM)

The **Australian Water Balance Model (AWBM)** was developed by Walter Boughton and represents one of the most widely used conceptual rainfall-runoff models globally. Its success stems from its balance of physical realism, computational efficiency, and robust performance across diverse climates.

### Historical Development and Applications

**Origin:** Developed in the 1970s for Australian conditions but proven applicable worldwide.

**Validation:** Extensively tested across thousands of catchments with diverse climates, soils, and land uses.

**Applications:**
- Water resource assessment and planning
- Climate change impact studies
- Flood frequency analysis
- Environmental flow assessments
- Real-time streamflow forecasting

### AWBM Philosophy

The AWBM recognizes that **catchment heterogeneity** is fundamental to runoff generation. Rather than treating a watershed as a uniform surface, the model acknowledges that different areas within a catchment have varying capacities to store water before generating runoff.

### The Landscape of Conceptual Models

The AWBM is an excellent and widely-used model, but it is one of several major conceptual rainfall-runoff models used in professional practice. Other prominent models available as pre-built components in the GoldSim Help Center include:

* **Sacramento Soil Moisture Accounting Model (SAC-SMA):** Developed by the U.S. National Weather Service, this is a complex and highly respected model used for operational river forecasting in North America.
* **HSPF (Hydrological Simulation Program—Fortran):** Developed by the U.S. EPA, HSPF is a comprehensive framework for simulating not only runoff but also water quality in a wide range of watersheds.

This case study focuses on the AWBM because its structure is particularly clear for teaching the core principles of conceptual modeling. **The skills you learn here—understanding parameters, manual calibration, and model application—are directly transferable to using SAC-SMA, HSPF, or any other conceptual model.**

## Part 2: AWBM Structure and Components

### The Three-Store Concept

The AWBM's core concept is a sophisticated version of the 'soil bucket' model we introduced in the previous lesson. Instead of one bucket, the AWBM uses three to represent the different water-holding capacities across a heterogeneous catchment.

The AWBM's core innovation represents a catchment using **three partial areas**, each with different soil moisture storage characteristics:

**Store 1 (Smallest Capacity):**
- Represents areas with shallow soils, impermeable surfaces, or saturated zones
- Fills quickly and generates runoff from small precipitation events
- Typically 10-30% of total catchment area

**Store 2 (Medium Capacity):**
- Represents moderate soil depths and average infiltration characteristics
- Generates runoff from moderate precipitation events
- Typically 30-50% of total catchment area

**Store 3 (Largest Capacity):**
- Represents areas with deep soils and high infiltration capacity
- Only generates runoff during large precipitation events or when soils are saturated
- Typically 20-60% of total catchment area

### Mathematical Framework

#### Surface Runoff Generation
For each store i at time step t:
```
If Precipitation > (Capacity_i - Current_Storage_i):
    Runoff_i = Precipitation - (Capacity_i - Current_Storage_i)
    Current_Storage_i = Capacity_i
Else:
    Runoff_i = 0
    Current_Storage_i = Current_Storage_i + Precipitation
```

#### Evapotranspiration
```
Actual_ET_i = min(Potential_ET × Current_Storage_i / Capacity_i, Current_Storage_i)
Current_Storage_i = Current_Storage_i - Actual_ET_i
```

#### Baseflow Generation
```
Infiltration = Total_Precipitation - Surface_Runoff
Baseflow_Storage = Baseflow_Storage + (BFI × Infiltration)
Baseflow = K_base × Baseflow_Storage
Baseflow_Storage = Baseflow_Storage - Baseflow
```

#### Total Streamflow
```
Total_Flow = Surface_Runoff + Baseflow
```

![AWBM Structure Diagram](images/AwbmStructureDiagram.png)

## Part 3: Key AWBM Parameters

Understanding parameter meanings and typical ranges is essential for effective model application and calibration.

### Surface Store Parameters

**A1, A2, A3 (Partial Area Fractions):**
- Must sum to 1.0 (representing 100% of catchment)
- Control the distribution of runoff generation across the catchment
- Typical ranges: A1: 0.1-0.3, A2: 0.3-0.5, A3: 0.2-0.6

**C1, C2, C3 (Storage Capacities, mm):**
- Represent maximum soil moisture storage in each partial area
- C1 < C2 < C3 (smallest to largest capacity)
- Typical ranges: C1: 10-50mm, C2: 50-200mm, C3: 100-500mm

### Baseflow Parameters

**BFI (Baseflow Index, 0-1):**
- Fraction of infiltrated water that becomes baseflow
- Controls overall runoff coefficient and flow regime
- Higher BFI = more baseflow, lower surface runoff peaks
- Typical range: 0.1-0.8

**K_base (Baseflow Recession Constant, 1/day):**
- Controls rate of baseflow decline between events
- Higher K_base = faster baseflow recession
- Related to catchment geology and groundwater characteristics
- Typical range: 0.01-0.3 day⁻¹

### Parameter Sensitivity and Relationships

**Flow Volume Control:**
- BFI primarily controls total flow volume and runoff coefficient
- Surface store capacities (C1, C2, C3) affect seasonal flow patterns

**Flow Timing Control:**
- K_base controls baseflow recession rates and low-flow characteristics
- Partial area fractions (A1, A2, A3) affect peak flow timing and magnitude

**Seasonal Patterns:**
- Large stores (C3) create seasonal memory effects
- Small stores (C1) respond to individual precipitation events

![AWBM Parameter Sensitivity](images/AwbmParameterEffects.png)

## Part 4: Implementation in GoldSim

### Using Pre-Built Components

The GoldSim Model Library provides a complete AWBM implementation as a self-contained container, offering several advantages:

**Quality Assurance:** Thoroughly tested and validated implementation
**Documentation:** Complete parameter descriptions and usage guidelines  
**Efficiency:** Immediate availability without development time
**Standardization:** Consistent implementation across projects
**Support:** Professional support and updates

### Integration Strategy

#### Input Requirements
- **Precipitation:** Daily time series (mm/day)
- **Potential ET:** Daily potential evapotranspiration (mm/day)
- **Parameters:** Calibrated values for specific catchment

#### Output Variables
- **Surface Runoff:** Direct runoff from surface stores (mm/day)
- **Baseflow:** Delayed groundwater contribution (mm/day)
- **Total Flow:** Combined surface and subsurface flow (mm/day)
- **Soil Moisture:** Storage levels in each surface store

#### Unit Conversions
```
Streamflow_m3s = Total_Flow_mm × Catchment_Area_km2 × (1000/86400)
```

### Model Structure in GoldSim

The AWBM container typically includes:
- **Input interfaces** for precipitation and ET time series
- **Parameter data elements** for all calibration parameters
- **Calculation logic** implementing the water balance equations
- **Output interfaces** providing flow components and state variables
- **Documentation** explaining parameter meanings and typical ranges

![GoldSim AWBM Implementation](images/GoldsimAwbmContainer.png)

## Part 5: Model Calibration Principles

### Calibration Philosophy

Model calibration optimizes parameter values to achieve the best possible match between simulated and observed streamflow. Effective calibration requires understanding:

**Objective Functions:** Quantitative measures of model performance
**Parameter Sensitivity:** Understanding which parameters affect which aspects of model behavior
**Equifinality:** Recognition that multiple parameter sets may provide similar performance
**Validation:** Testing calibrated models against independent data

### Manual Calibration Approach

Manual calibration provides valuable insights into model behavior and parameter sensitivity:

#### Step 1: Visual Assessment
- Plot observed and simulated hydrographs
- Identify systematic biases (under/over-prediction)
- Assess timing accuracy and peak flow reproduction

#### Step 2: Volume Calibration
- Adjust BFI to match total flow volumes
- Higher BFI increases total flow volume
- Lower BFI decreases total flow volume

#### Step 3: Timing and Peak Flow Calibration
- Adjust surface store parameters to match peak flows
- Smaller C1 increases peak flow responsiveness
- Larger C3 provides seasonal storage effects

#### Step 4: Baseflow Calibration
- Adjust K_base to match recession behavior
- Higher K_base creates faster recession rates
- Lower K_base creates sustained baseflows

### Performance Metrics

**Nash-Sutcliffe Efficiency (NSE):**
```
NSE = 1 - Σ(Qobs - Qsim)² / Σ(Qobs - Qmean)²
```
Values: -∞ to 1, where 1 = perfect fit, 0 = model no better than mean

**Percent Bias (PBIAS):**
```
PBIAS = 100 × Σ(Qobs - Qsim) / Σ(Qobs)
```
Values: Optimal = 0, negative = over-prediction, positive = under-prediction

**Root Mean Square Error (RMSE):**
```
RMSE = √[Σ(Qobs - Qsim)² / n]
```
Lower values indicate better fit

![Calibration Process Flowchart](images/CalibrationWorkflow.png)

### A Note on Automated Calibration

While this lesson focuses on manual calibration to build intuition, GoldSim also includes powerful optimization tools that can automate this process. We will cover these advanced techniques in detail in Unit 11: Model Analyses.

---

## Exercises

### Exercise 1: AWBM Implementation and Exploration

**Objective:** Set up and run the AWBM model to understand its basic behavior and outputs.

**Steps:**
1. Open the provided model `AWBM_Case_Study.gsm`
2. Navigate into the AWBM container and explore its structure:
   - Identify input elements (precipitation, potential ET)
   - Locate parameter data elements
   - Examine calculation logic and water balance components
   - Find output elements (runoff, baseflow, total flow)
3. Run model with default parameters for 10-year simulation period
4. Create comprehensive plots showing:
   - Input time series (precipitation and potential ET)
   - Individual flow components (surface runoff vs. baseflow)
   - Total streamflow output
   - Soil moisture storage in each surface store
5. Analyze seasonal patterns and flow regime characteristics

**Deliverables:**
- Working AWBM implementation in GoldSim
- Comprehensive time series plots of all major variables
- Written analysis of seasonal flow patterns
- Identification of periods when each surface store contributes to runoff

### Exercise 2: Model Calibration Against Observed Data

**Objective:** Perform manual calibration to improve model performance against observed streamflow data.

**Steps:**
1. Create comparison plot showing simulated `Total_Flow` and `Observed_Flow`
2. Calculate initial performance metrics:
   - Visual assessment of hydrograph match
   - Total volume bias (sum of simulated vs. observed)
   - Peak flow accuracy
3. Systematic parameter adjustment:
   - **Volume Calibration:** Adjust BFI to match total flow volumes
   - **Peak Flow Calibration:** Modify surface store capacities (C1, C2, C3)
   - **Timing Calibration:** Adjust partial area fractions (A1, A2, A3)
   - **Baseflow Calibration:** Optimize K_base for recession behavior
4. Document parameter changes and performance improvements
5. Validate final parameter set against independent time period

**Deliverables:**
- Calibrated AWBM model with optimized parameters
- Before/after comparison plots showing calibration improvements
- Parameter sensitivity analysis documenting effects of each adjustment
- Performance metrics comparison (initial vs. final)
- Recommended parameter set with uncertainty bounds

**Advanced/Optional Exercises:** The following two exercises apply the calibrated model to more advanced analyses. They are highly recommended for those interested in seasonal performance and climate change applications.

### Exercise 3: Seasonal Performance Analysis

**Objective:** Evaluate model performance across different seasons and flow conditions.

**Steps:**
1. Separate simulation results by seasons (wet vs. dry seasons)
2. Analyze performance for different flow conditions:
   - Low flows (bottom 25% of observations)
   - Medium flows (25-75% of observations)  
   - High flows (top 25% of observations)
3. Create seasonal scatter plots (observed vs. simulated)
4. Calculate performance metrics by season and flow range
5. Identify periods of poor model performance
6. Propose parameter adjustments to improve seasonal accuracy

**Deliverables:**
- Seasonal performance analysis with statistics by season
- Flow duration curves comparing observed and simulated flows
- Scatter plots showing performance across flow ranges
- Analysis of model limitations and potential improvements
- Recommendations for seasonal parameter variations

### Exercise 4: Climate Change Impact Assessment

**Objective:** Apply the calibrated AWBM to assess potential climate change impacts on streamflow.

**Steps:**
1. Use calibrated model from Exercise 2 as baseline
2. Create climate change scenarios:
   - Temperature increase: +2°C (affects potential ET)
   - Precipitation change: ±10% annual total
   - Precipitation timing: shift seasonal distribution
3. Generate modified climate time series for each scenario
4. Run AWBM with each climate scenario
5. Compare results with baseline simulation:
   - Annual flow volumes
   - Seasonal flow patterns
   - Peak flow magnitudes
   - Low flow characteristics
6. Quantify climate sensitivity of flow regime

**Deliverables:**
- Climate scenario development methodology
- AWBM simulations for all climate scenarios
- Comparative analysis of climate change impacts
- Flow regime sensitivity assessment
- Management implications and adaptation strategies

---

## Key Takeaways

1. **Pre-built conceptual models provide sophisticated capabilities** without requiring extensive development time
2. **The AWBM's three-store concept effectively represents catchment heterogeneity** and runoff generation variability
3. **Model calibration is essential** for accurate representation of specific catchment behavior
4. **Parameter understanding enables effective calibration** and interpretation of model results
5. **Manual calibration provides insights** into model behavior and parameter sensitivity
6. **Performance evaluation requires multiple metrics** and assessment across different flow conditions
7. **Conceptual models enable long-term analysis** including climate change impact assessment

## Professional Applications

### Water Resource Assessment
- Long-term yield studies for water supply planning
- Climate change impact assessment on water availability
- Environmental flow requirement determination

### Flood Risk Analysis
- Design flood estimation using continuous simulation
- Flood frequency analysis with extended records
- Climate change effects on flood risk

### Operational Forecasting
- Real-time streamflow forecasting for water management
- Drought monitoring and early warning systems
- Reservoir inflow forecasting for operations

### Research Applications
- Hydrologic process understanding and hypothesis testing
- Climate-streamflow relationship analysis
- Model comparison and methodology development

---

## Required Assets

- **AWBM_Case_Study.gsm** - Complete GoldSim model with AWBM component and sample data
- **AWBM_Climate_Data.xlsx** - Daily precipitation and potential ET time series for model input
- **Observed_Streamflow_Data.xlsx** - Historical streamflow records for calibration and validation
- **AWBM_Parameter_Guidelines.xlsx** - Parameter ranges and calibration guidance for different regions
- **Climate_Change_Scenarios.xlsx** - Modified climate data for impact assessment exercises
