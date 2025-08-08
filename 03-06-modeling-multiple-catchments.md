# Lesson 5: Modeling Multiple Catchments

**Objective:** Learn to construct semi-distributed watershed models in GoldSim by creating modular, reusable sub-catchment components and linking them to form complex river networks that capture spatial variability and flow routing.

## Why This Matters

Very few real-world water problems involve just a single, isolated catchment. To model how an upstream reservoir release affects a downstream water user, how land use changes in different tributaries impact a river's main stem, or how climate variability affects different parts of a watershed, you need a multi-catchment modeling approach.

This lesson teaches the fundamental GoldSim skill for scaling your models from single locations to spatially-aware systems, dramatically increasing the scope and realism of the problems you can solve:

- **Water allocation** between upstream and downstream users
- **Flood management** across interconnected river systems
- **Land use impact assessment** on watershed-scale hydrology
- **Climate change analysis** with spatial variability
- **Environmental flow management** throughout river networks
- **Infrastructure planning** considering cumulative watershed effects

Understanding multi-catchment modeling is essential for addressing the spatial complexity inherent in most water resource management challenges.

## Understanding Model Complexity Levels

### Lumped vs. Semi-Distributed vs. Fully Distributed Models

**Lumped Models:**
- Treat entire watershed as single, homogeneous unit
- Calculate one runoff value for entire area
- Simple but lose all spatial detail
- Appropriate for initial assessments and small, uniform watersheds

**Semi-Distributed Models:**
- Divide watershed into sub-catchments with similar characteristics
- Model each sub-catchment separately
- Route flows between sub-catchments
- Balance complexity with computational efficiency

**Fully Distributed Models:**
- Represent watershed as grid of cells (pixels)
- Maximum spatial detail but computationally intensive
- Often require extensive data and specialized software
- Used for detailed research and high-resolution applications

### Semi-Distributed Approach Advantages

**Spatial Representation:** Captures important spatial variability in precipitation, land use, soil types, and topography without excessive complexity.

**Modular Design:** Allows systematic organization of complex watersheds into manageable components.

**Scalability:** Easy to add or modify sub-catchments as understanding improves or conditions change.

**Physical Realism:** Represents actual flow paths and tributary structure of river networks.

**Computational Efficiency:** Maintains reasonable run times while preserving spatial detail.

![Model Complexity Comparison](images/ModelComplexitySpectrum.png)

## Part 1: GoldSim's Hierarchical Container Strategy

### Containers as Organizational Tools

GoldSim's **Container** elements provide the perfect framework for building modular, multi-catchment models. Containers offer several key advantages:

**Encapsulation:** Group related elements together in logical units
**Reusability:** Create standardized components that can be copied and modified
**Organization:** Manage complexity through hierarchical structure
**Interfaces:** Define clear inputs and outputs for each component
**Modularity:** Build and test components independently

### Localized Containers for Sub-Catchments

**Localized Containers** act as self-contained "black boxes" with defined interfaces, making them ideal for sub-catchment modeling:

```
Inputs → [Sub-Catchment Container] → Outputs
```

**Input Interface:**
- Precipitation time series
- Potential evapotranspiration  
- Upstream inflow from other sub-catchments
- Catchment parameters (area, characteristics)

**Internal Processing:**
- Rainfall-runoff calculations
- Evapotranspiration losses
- Flow routing and timing
- Storage accounting

**Output Interface:**
- Local runoff generation
- Total outflow to downstream areas
- Water balance components
- State variables for analysis

![Container Architecture](images/LocalizedContainerStructure.png)

## Part 2: Designing the Sub-Catchment Component

### Component Architecture

The core of any multi-catchment model is a robust, reusable sub-catchment component. This component must be flexible enough to handle different catchment characteristics while maintaining consistency across the watershed.

#### Essential Input Parameters

**Meteorological Inputs:**
```
Precipitation (mm/day) - Local precipitation time series
Potential_ET (mm/day) - Potential evapotranspiration demand
Temperature (°C) - For snow modeling if applicable
```

**Physical Characteristics:**
```
Catchment_Area (km²) - Sub-catchment drainage area
Land_Use_Type - Classification affecting runoff coefficients
Soil_Group - Hydrologic soil group for SCS or other methods
Elevation (m) - For temperature and precipitation adjustments
```

**Network Connectivity:**
```
Upstream_Inflow (m³/s) - Flow from upstream sub-catchments
Routing_Parameters - Lag time, attenuation factors
```

#### Internal Model Structure

The sub-catchment component typically includes:

**1. Climate Processing:**
- Local climate adjustments (elevation effects)
- Snow accumulation and melt (if applicable)
- Potential ET calculations

**2. Runoff Generation:**
- Choice of runoff method (SCS, AWBM, simple coefficient)
- Local calibration parameters
- Soil moisture accounting

**3. Flow Routing:**
- Unit hydrograph or lag routing
- Channel transmission losses
- Timing adjustments

**4. Water Balance:**
- Mass balance verification
- Storage accounting
- Loss calculations

### Modular Design Principles

**Standardization:** Use consistent naming conventions and units across all sub-catchment instances.

**Parameterization:** Make key characteristics easily adjustable through Data elements.

**Documentation:** Include clear descriptions of parameters and assumptions.

**Validation:** Build in checks for mass balance and reasonable outputs.

**Flexibility:** Allow easy swapping of internal methods (e.g., different runoff approaches).

![Sub-Catchment Component Design](images/SubcatchmentComponentArchitecture.png)

## Part 3: Building the River Network

### Network Topology

Real river networks follow dendritic (tree-like) patterns where smaller tributaries join to form larger streams. Representing this topology in GoldSim requires careful attention to:

**Flow Direction:** Ensure flows move from upstream to downstream
**Confluence Points:** Properly combine flows from multiple tributaries  
**Timing:** Account for travel time between sub-catchments
**Flow Accumulation:** Track cumulative watershed area and flow

### Connection Strategy

#### Simple Linear Network:
```
[Sub-A] → [Sub-B] → [Sub-C] → Outlet
```

#### Tributary Network:
```
[Sub-A] → [Sub-C] → Outlet
[Sub-B] → [Sub-C] → Outlet
```

#### Complex Network:
```
[Sub-A] → [Sub-C] → [Sub-E] → Outlet
[Sub-B] → [Sub-C] → [Sub-E] → Outlet
[Sub-D] → [Sub-E] → Outlet
```

### Implementation in GoldSim

**Step 1: Create Template**
- Build and test single sub-catchment container
- Verify all inputs, outputs, and internal logic
- Document parameter meanings and typical ranges

**Step 2: Replicate Components**
- Copy container for each sub-catchment in watershed
- Rename containers to reflect geographic locations
- Adjust parameters for local conditions

**Step 3: Establish Connections**
- Link upstream outputs to downstream inputs
- Use Selector elements for complex routing if needed
- Implement flow accumulation at confluence points

**Step 4: Network Validation**
- Check mass balance across entire network
- Verify timing and flow propagation
- Compare total outlet flow with observations

![Network Implementation Strategy](images/NetworkImplementationSteps.png)

## Part 4: Advanced Multi-Catchment Concepts

### Spatial Variability Representation

**Climate Gradients:**
- Elevation-based temperature and precipitation adjustments
- Rain shadow effects and orographic precipitation
- Seasonal and storm-specific spatial patterns

**Land Use Heterogeneity:**
- Different runoff coefficients by sub-catchment
- Urban vs. rural vs. forest characteristics
- Land use change scenarios over time

**Soil and Geology:**
- Varying infiltration capacities
- Different baseflow characteristics
- Groundwater interaction variations

### Flow Routing Between Sub-Catchments

**Simple Lag Routing:**
```
Outflow(t) = Inflow(t - lag_time)
```

**Linear Reservoir Routing:**
```
Outflow(t) = K × Storage(t)
Storage(t+1) = Storage(t) + Inflow(t) - Outflow(t)
```

**Unit Hydrograph Routing:**
- Distribute upstream flow over time using characteristic response
- Account for channel storage and travel time
- Represent peak attenuation and timing delays

### Model Calibration Strategies

**Hierarchical Calibration:**
1. Calibrate individual sub-catchments using local data
2. Adjust routing parameters for timing at downstream points
3. Fine-tune network-wide parameters for total volume

**Nested Approach:**
- Calibrate at multiple scales (sub-catchment and watershed)
- Use different objective functions for different locations
- Balance local accuracy with watershed-scale performance

**Multi-Objective Optimization:**
- Simultaneously optimize multiple performance metrics
- Balance competing objectives (peaks vs. volumes vs. timing)
- Consider uncertainty in parameters and observations

![Calibration Strategy Flowchart](images/MultiCatchmentCalibration.png)

## Part 5: Practical Implementation Guidelines

### Model Setup Workflow

**1. Watershed Delineation:**
- Define sub-catchment boundaries based on drainage patterns
- Consider available data and computational constraints
- Balance detail with model complexity

**2. Data Preparation:**
- Organize climate data by sub-catchment
- Develop parameter databases for each sub-catchment
- Prepare network connectivity information

**3. Template Development:**
- Build robust, well-tested sub-catchment component
- Include comprehensive error checking
- Document all parameters and assumptions

**4. Network Assembly:**
- Systematically connect components following watershed topology
- Implement flow routing and timing
- Validate network connectivity

**5. Testing and Calibration:**
- Test individual components before network assembly
- Calibrate systematically from upstream to downstream
- Validate using independent data periods

### Common Implementation Challenges

**Computational Complexity:**
- Balance detail with run time requirements
- Use efficient algorithms for flow routing
- Consider parallel processing for large networks

**Data Requirements:**
- Handle missing data in some sub-catchments
- Interpolate or estimate parameters where data is limited
- Validate parameter transfers from similar areas

**Calibration Complexity:**
- Avoid over-parameterization
- Use physical constraints to guide parameter selection
- Implement systematic sensitivity analysis

**Model Management:**
- Maintain organized file structure
- Version control for model development
- Clear documentation for future users

---

## Exercises

### Exercise 1: Basic Network Construction

**Objective:** Build a three-catchment river network using modular sub-catchment components.

**Steps:**
1. Open the provided model `Multi_Catchment_Exercise.gsm`
2. Examine the `Sub-Catchment_Template` container:
   - Identify input interfaces (precipitation, potential ET, upstream inflow)
   - Understand internal logic (AWBM implementation)
   - Review output variables (local outflow, water balance components)
3. Create watershed network:
   - Copy template three times: `Upper_Catchment`, `Middle_Catchment`, `Lower_Catchment`
   - Set catchment areas: 50 km², 75 km², 40 km² respectively
   - Connect flow network: Upper → Middle → Lower → Outlet
4. Configure spatial variability:
   - Apply elevation adjustments to temperature (Upper: +200m, Middle: +100m, Lower: 0m)
   - Use different land use parameters for each catchment
5. Run simulation and analyze results:
   - Plot outflow from each sub-catchment
   - Observe flow accumulation and timing effects
   - Calculate flow contributions by sub-catchment

**Deliverables:**
- Working three-catchment network model
- Time series plots showing flow accumulation
- Analysis of spatial patterns and timing effects
- Water balance verification for entire network

### Exercise 2: Tributary Network Implementation

**Objective:** Construct a more complex network with tributary confluence and flow routing.

**Steps:**
1. Expand to five-catchment system with tributary structure:
   ```
   [Tributary_A] → [Main_Stem_1] → [Main_Stem_2] → Outlet
   [Tributary_B] → [Main_Stem_1] → [Main_Stem_2] → Outlet
   [Side_Channel] → [Main_Stem_2] → Outlet
   ```
2. Implement confluence logic:
   - Sum flows from multiple tributaries
   - Account for timing differences between tributaries
   - Verify mass balance at confluence points
3. Add flow routing between sub-catchments:
   - Implement simple lag routing (1-day travel time)
   - Compare routed vs. unrouted flow patterns
   - Analyze impact on peak flows and timing
4. Conduct scenario analysis:
   - Simulate land use change in one tributary
   - Assess downstream impact of upstream modifications
   - Quantify contribution of each tributary to total flow

**Deliverables:**
- Five-catchment tributary network model
- Confluence flow calculations and validation
- Flow routing implementation and analysis
- Scenario analysis results and interpretation

### Exercise 3: Spatial Variability Analysis

**Objective:** Investigate the impact of spatial variability on watershed response.

**Steps:**
1. Create scenarios with different spatial precipitation patterns:
   - Uniform precipitation across all sub-catchments
   - Gradient from wet (upstream) to dry (downstream)
   - Random spatial pattern with high variability
2. Implement elevation-based climate adjustments:
   - Temperature lapse rate corrections
   - Precipitation-elevation relationships
   - Snow accumulation and melt variations
3. Compare lumped vs. semi-distributed results:
   - Run equivalent lumped model using area-weighted averages
   - Compare total flow volumes and timing
   - Analyze differences in peak flows and low flows
4. Sensitivity analysis:
   - Test impact of sub-catchment delineation choices
   - Evaluate effect of parameter uncertainties
   - Assess model performance at different scales

**Deliverables:**
- Multiple spatial scenario implementations
- Lumped vs. semi-distributed comparison analysis
- Sensitivity analysis results and documentation
- Recommendations for spatial modeling approach

### Exercise 4: Model Calibration and Validation

**Objective:** Implement systematic calibration approach for multi-catchment model.

**Steps:**
1. Prepare calibration data:
   - Organize observed flow data for multiple stations
   - Quality control and gap-fill missing observations
   - Separate data into calibration and validation periods
2. Implement hierarchical calibration:
   - Start with upstream sub-catchments using local data
   - Progressively calibrate downstream areas
   - Adjust routing parameters for timing at downstream stations
3. Apply multiple performance metrics:
   - Nash-Sutcliffe efficiency for overall fit
   - Percent bias for volume accuracy
   - Peak flow timing accuracy
   - Low flow performance assessment
4. Validation testing:
   - Test calibrated model against independent data
   - Assess performance across different flow conditions
   - Evaluate seasonal and annual performance
5. Uncertainty analysis:
   - Document parameter uncertainty ranges
   - Assess model prediction uncertainty
   - Identify key sources of model uncertainty

**Deliverables:**
- Systematic calibration methodology and implementation
- Multi-station performance assessment
- Validation results with uncertainty bounds
- Calibrated model ready for operational use
- Documentation of calibration process and results

---

## Key Takeaways

1. **Semi-distributed modeling captures spatial variability** while maintaining computational efficiency and manageable complexity
2. **Localized containers provide the ideal framework** for building modular, reusable sub-catchment components
3. **Network topology must accurately represent** real watershed drainage patterns and flow connectivity
4. **Spatial variability in climate, land use, and soils** significantly affects watershed response and must be represented
5. **Flow routing between sub-catchments** affects timing and peak flows throughout the network
6. **Hierarchical calibration approaches** work systematically from upstream to downstream areas
7. **Model complexity should match** available data quality and project objectives

## Professional Applications

### Water Resource Management
- Multi-purpose reservoir operations considering tributary inflows
- Water allocation between upstream and downstream users
- Drought management across interconnected systems

### Flood Risk Assessment
- Basin-wide flood forecasting and warning systems
- Infrastructure impact assessment on downstream areas
- Land use change effects on flood risk

### Environmental Management
- Environmental flow requirements throughout river networks
- Habitat connectivity and flow regime assessment
- Pollution source tracking and impact analysis

### Climate Change Studies
- Spatially-distributed climate change impact assessment
- Adaptation strategy evaluation across watersheds
- Uncertainty quantification in climate projections

### Urban Development Planning
- Cumulative urbanization impacts on downstream flows
- Green infrastructure effectiveness at watershed scale
- Stormwater management system optimization

---

## Required Assets

- **Multi_Catchment_Exercise.gsm** - Base model with sub-catchment template and example network setup
- **Watershed_Network_Data.xlsx** - Sub-catchment characteristics, connectivity, and parameter data
- **Multi_Station_Flow_Data.xlsx** - Observed streamflow data for multiple gauging stations
- **Spatial_Climate_Data.xlsx** - Precipitation and temperature data with spatial variability
- **Network_Calibration_Tools.gsm** - Advanced model with calibration utilities and performance metrics
