# Lesson 9: Incorporating Climate Model Projections

**Objective:** Learn how to integrate pre-processed climate projection data into GoldSim water management models, focusing on practical implementation rather than climate data processing.

## Introduction: From Climate Science to Water Management

Climate scientists provide water managers with processed climate projections, but incorporating these projections into practical models requires understanding how to translate climate data into GoldSim elements. This lesson focuses on the **practical implementation** of climate projections in GoldSim, using pre-calculated datasets that represent realistic climate change scenarios.

**What This Lesson Covers:**
- Importing and using pre-processed climate projection files
- Implementing climate change factors in GoldSim models
- Building scenario comparison capabilities
- Connecting climate projections to water system models

**What This Lesson Does NOT Cover:**
- Downloading raw climate model data from scientific portals
- Performing bias correction or statistical downscaling
- Complex climate data processing (see Appendix A for methodology)

## Understanding Climate Projection Datasets

For this lesson, we'll work with **pre-processed climate datasets** that represent typical outputs from climate impact studies. These datasets have already undergone the complex processing needed to make them applicable to local water management.

### Provided Dataset Structure

Our example datasets represent climate projections for a southwestern U.S. mine site:

#### **Historical Baseline (1990-2020)**
- `Historical_Daily_Precip.txt` - 30 years of daily precipitation data
- `Historical_PrecipGen_Parameters.xlsx` - Calculated PWW, PWD, Alpha, Beta parameters

#### **Future Scenarios (2021-2050)**
- `RCP45_Daily_Precip.txt` - Climate projection under moderate emissions
- `RCP85_Daily_Precip.txt` - Climate projection under high emissions  
- `RCP45_PrecipGen_Parameters.xlsx` - Adjusted parameters for RCP4.5
- `RCP85_PrecipGen_Parameters.xlsx` - Adjusted parameters for RCP8.5

### Key Climate Changes Represented

The datasets incorporate realistic climate changes for the region:
- **Precipitation:** 8-15% decrease in annual totals
- **Seasonality:** Stronger winter precipitation, drier summers
- **Storm patterns:** More variable precipitation (reflected in parameter changes)
- **Temperature:** 2-4°C increase (affects evaporation)

## Practical Implementation in GoldSim

This section demonstrates how to use pre-processed climate projection data in your GoldSim water management models.

### Method 1: Direct Time Series Replacement

The simplest approach uses climate projection time series directly in place of historical data.

#### Setting Up Climate Scenarios

**Step 1: Create Time Series Elements**
```
1. Create Time Series element: "Historical_Precip"
   - Import: Historical_Daily_Precip.txt
   - Units: mm/day (or your preferred units)
   - Interpolation: Linear

2. Create Time Series element: "RCP45_Precip" 
   - Import: RCP45_Daily_Precip.txt
   - Same units and interpolation settings

3. Create Time Series element: "RCP85_Precip"
   - Import: RCP85_Daily_Precip.txt
   - Same units and interpolation settings
```

**Step 2: Add Scenario Selector**
```
Create Selector element: "Climate_Scenario"
- Choices: ["Historical", "RCP4.5", "RCP8.5"]
- Type: Specified Value (for interactive testing)
```

**Step 3: Implement Scenario Logic**
```
Create Expression element: "Active_Precipitation"
Active_Precipitation = if(Climate_Scenario == "Historical", 
                         Historical_Precip,
                         if(Climate_Scenario == "RCP4.5",
                            RCP45_Precip,
                            RCP85_Precip))
```

### Method 2: Parameter-Based Climate Adjustment (Advanced)

This method adjusts PrecipGen parameters based on climate projections, maintaining stochastic generation capabilities while incorporating climate change effects.

#### Understanding Parameter Changes

Climate change affects not just precipitation totals, but also storm patterns. Our pre-calculated parameter sets show how climate change modifies:

- **PWW (Wet-to-Wet)**: Persistence of wet weather
- **PWD (Dry-to-Wet)**: Frequency of storm initiation  
- **Alpha/Beta**: Storm intensity distributions

#### Implementation Steps

**Step 1: Load Parameter Sets**
```
Create Data elements for each scenario:

1. "Historical_PWW" - Vector with Months label set
   - Import from Historical_PrecipGen_Parameters.xlsx
   - PWW column data

2. "RCP45_PWW" - Vector with Months label set  
   - Import from RCP45_PrecipGen_Parameters.xlsx
   - PWW column data

3. Repeat for PWD, Alpha, Beta parameters
```

**Step 2: Create Parameter Selector**
```
Create Expression element: "Active_PWW"
Active_PWW = if(Climate_Scenario == "Historical",
               Historical_PWW,
               if(Climate_Scenario == "RCP4.5",
                  RCP45_PWW,
                  RCP85_PWW))

Repeat similar expressions for PWD, Alpha, Beta
```

**Step 3: Connect to PrecipGen**
```
In your PrecipGen model:
- Link Params_Mean_T to your parameter selector expressions
- This provides climate-adjusted stochastic generation
- Maintains daily weather variability while incorporating climate trends
```

### Method 3: Hybrid Approach with Time-Varying Climate

For long-term simulations, you may want gradual climate change rather than step changes.

#### Creating Climate Transition

**Step 1: Define Transition Timeline**
```
Create Expression element: "Climate_Transition_Factor"
Climate_Transition_Factor = min(1.0, max(0.0, (ElapsedTime/year - 30) / 20))

This creates:
- Factor = 0.0 for years 0-30 (historical climate)
- Factor = 0.0 to 1.0 for years 30-50 (gradual transition)  
- Factor = 1.0 for years 50+ (full future climate)
```

**Step 2: Blend Climate Scenarios**
```
Create Expression element: "Blended_Precipitation"
Blended_Precipitation = Historical_Precip * (1 - Climate_Transition_Factor) + 
                       RCP45_Precip * Climate_Transition_Factor
```

This approach provides smooth climate transitions suitable for long-term infrastructure planning.

### Connecting Climate Data to Water Systems

#### Reservoir Inflow Calculations
```
Monthly_Inflow = Catchment_Area * Active_Precipitation * Runoff_Coefficient
```

#### Evaporation Adjustments
```
# Adjust evaporation for temperature changes
Temperature_Factor = 1.0 + 0.05 * (Future_Temp_Increase)  # 5% per degree C
Adjusted_Evaporation = Base_Evaporation * Temperature_Factor
```

#### Demand Modifications  
```
# Adjust irrigation demands for temperature
Irrigation_Demand = Base_Irrigation * (1 + 0.03 * Future_Temp_Increase)
```

### Model Organization Best Practices

#### Container Structure
```
Climate_Projections (Container)
├── Scenario_Selection (Selector)
├── Time_Series_Data (Container)
│   ├── Historical_Precip (Time Series)
│   ├── RCP45_Precip (Time Series)
│   └── RCP85_Precip (Time Series)
├── Parameter_Data (Container)
│   ├── [Parameter Data elements]
│   └── [Parameter selector expressions]
└── Active_Climate (Container)
    ├── Active_Precipitation (Expression)
    └── Active_Temperature (Expression)
```

#### Results Organization
```
Climate_Comparison (Container)
├── Annual_Precipitation_Stats (Result)
├── System_Performance_by_Scenario (Result)
└── Climate_Impact_Summary (Result)
```

## Case Study: Mine Site Water Balance

Let's apply these concepts to a realistic mine site water management problem.

### Problem Setup

**Site Characteristics:**
- Copper mine in Arizona
- Open pit with ongoing dewatering needs
- Tailings storage facility requiring water balance management
- Current operations based on historical climate patterns

**Climate Projections:**
- Historical (1990-2020): 280 mm/year average precipitation
- RCP4.5 (2021-2050): 260 mm/year average precipitation (-7%)
- RCP8.5 (2021-2050): 245 mm/year average precipitation (-12%)

### GoldSim Implementation

**Step 1: Set up the basic water balance model**
```
Water_Balance = Pit_Inflow + Precipitation_Input - Evaporation_Loss - Pumping_Rate
```

**Step 2: Import climate scenarios as described in Method 1**

**Step 3: Connect climate data to water balance**
```
Precipitation_Input = Mine_Surface_Area * Active_Precipitation / 1000  # Convert to m³/day
```

**Step 4: Add climate-sensitive evaporation**
```
Climate_Evap_Factor = if(Climate_Scenario == "Historical", 1.0,
                        if(Climate_Scenario == "RCP4.5", 1.15,
                           1.25))  # 15-25% increase in evaporation

Evaporation_Loss = Base_Evaporation * Climate_Evap_Factor
```

**Step 5: Analyze results**
```
Create Result elements to track:
- Annual water surplus/deficit by scenario
- Required pumping capacity by scenario  
- Tailings facility water levels by scenario
```

### Expected Results

This case study demonstrates how climate change affects mine water management:
- **Reduced precipitation** decreases natural water inputs
- **Increased evaporation** increases water losses
- **Combined effect** requires increased water recycling or external supply
- **Planning insight** helps optimize infrastructure investments

## Validation and Quality Control

### Checking Climate Data Implementation

**Step 1: Verify Data Import**
```
Create Result elements to plot:
- Annual precipitation totals for each scenario
- Monthly precipitation patterns  
- Comparison with expected climate changes
```

**Step 2: Validate Water Balance Response**
```
Check that:
- System responds logically to precipitation changes
- Evaporation adjustments are reasonable
- Results pass basic physical consistency checks
```

**Step 3: Scenario Comparison**
```
Create comparative plots showing:
- System performance under each climate scenario
- Sensitivity to climate uncertainty
- Economic impacts of climate change
```

## Uncertainty Quantification

### Sources of Uncertainty

#### Model Structure Uncertainty
- Different GCMs produce different projections
- Various downscaling methods yield different results
- Multiple bias correction approaches available

#### Scenario Uncertainty
- Different emission pathways (RCPs)
- Socioeconomic development patterns
- Policy intervention effects

#### Natural Variability
- Internal climate variability
- Decadal oscillations (PDO, AMO)
- Random weather variations

### Uncertainty Analysis in GoldSim

#### Monte Carlo with Climate Scenarios
```
Scenario_Selector = Discrete_Distribution([RCP26, RCP45, RCP85])
Model_Selector = Discrete_Distribution([Model1, Model2, ..., ModelN])
Selected_Climate = Climate_Data[Scenario_Selector][Model_Selector]
```

#### Probabilistic Climate Projections
```
Temperature_Change ~ Normal(Mean_Change, Uncertainty_StdDev)
Precipitation_Change ~ LogNormal(Mean_Change, Uncertainty_CV)
```

## Practical Implementation Workflows

### Workflow 1: Simple Delta Method
1. **Obtain climate data:** Download GCM/RCM projections
2. **Calculate change factors:** Compare future to historical periods
3. **Apply to observations:** Modify historical data with change factors
4. **Implement in GoldSim:** Use modified time series for future scenarios

### Workflow 2: Multi-Model Ensemble
1. **Collect multiple models:** Assemble ensemble of climate projections
2. **Harmonize data:** Ensure consistent spatial/temporal resolution
3. **Calculate statistics:** Ensemble mean, range, percentiles
4. **Create scenarios:** Low/medium/high based on ensemble statistics
5. **Probabilistic analysis:** Use range to define uncertainty bounds

### Workflow 3: Integrated Assessment
1. **Historical calibration:** Validate model with observed data
2. **Bias correction:** Correct systematic model biases
3. **Scenario development:** Create multiple climate futures
4. **Impact simulation:** Run water system model with climate scenarios
5. **Risk assessment:** Evaluate system performance under uncertainty

## Quality Control and Validation

### Data Quality Checks
- **Temporal continuity:** Check for missing data periods
- **Physical realism:** Verify reasonable value ranges
- **Seasonal patterns:** Confirm expected seasonal cycles
- **Trend consistency:** Check for unrealistic discontinuities

### Model Validation
- **Historical period:** Compare GCM historical runs to observations
- **Spatial patterns:** Verify reasonable geographic variations
- **Extreme events:** Check representation of droughts, floods
- **Long-term trends:** Validate against observed climate trends

## Case Study Examples

### Example 1: Western U.S. Snowpack Projections
- **Data Source:** Downscaled CMIP5 projections
- **Variables:** Temperature, precipitation, snow water equivalent
- **Method:** Bias-corrected spatial disaggregation (BCSD)
- **Application:** Reservoir inflow projections under warming

### Example 2: Great Lakes Water Levels
- **Data Source:** Regional climate models (CORDEX)
- **Variables:** Precipitation, evaporation, temperature
- **Method:** Multi-model ensemble with uncertainty quantification
- **Application:** Adaptive management of water level regulation

### Example 3: Australian Water Resources
- **Data Source:** CSIRO climate projections
- **Variables:** Rainfall, potential evapotranspiration
- **Method:** Scaling factors applied to stochastic weather generators
- **Application:** Urban water supply risk assessment

## Integration with Existing Methods

### Combining with Stochastic Generation
```
Base_Parameters = Historical_Weather_Statistics
Climate_Adjusted_Parameters = Apply_Climate_Change(Base_Parameters)
Future_Weather = PrecipGen(Climate_Adjusted_Parameters)
```

### Linking with Drought Analysis
```
Historical_Drought_Index = Calculate_SPI(Historical_Data)
Future_Drought_Index = Calculate_SPI(Climate_Projection_Data)
Drought_Change = Compare_Statistics(Future_Index, Historical_Index)
```

---

## Exercises

### Exercise 1: Basic Climate Scenario Implementation
**Objective:** Learn to import and switch between pre-processed climate scenarios in GoldSim.

**Provided Assets:**
- `Historical_Daily_Precip.txt` - 30 years of daily precipitation data  
- `RCP45_Daily_Precip.txt` - Future climate scenario (moderate emissions)
- `RCP85_Daily_Precip.txt` - Future climate scenario (high emissions)

**Tasks:**
1. **Create a new GoldSim model** named `Climate_Scenarios_Exercise.gsm`
2. **Import the three climate datasets** using Time Series elements
3. **Add a Selector element** with choices: ["Historical", "RCP4.5", "RCP8.5"]
4. **Create an Expression element** that switches between scenarios based on selector
5. **Add a Result element** to plot the active precipitation time series
6. **Test each scenario** and document the visual differences you observe

**Expected Learning:**
- Time Series element configuration for climate data
- Selector element usage for scenario switching  
- Expression element logic for conditional data selection

### Exercise 2: Parameter-Based Climate Integration with PrecipGen  
**Objective:** Use climate-adjusted PrecipGen parameters to generate synthetic weather.

**Provided Assets:**
- `Historical_PrecipGen_Parameters.xlsx` - PWW, PWD, Alpha, Beta for historical period
- `RCP45_PrecipGen_Parameters.xlsx` - Climate-adjusted parameters for RCP4.5
- `PrecipGen_Climate_Template.gsm` - Pre-configured PrecipGen model

**Tasks:**
1. **Open the template model** and examine the structure
2. **Load parameter datasets** into Data elements using the Months label set
3. **Create parameter selector expressions** that choose parameters based on scenario
4. **Link the parameter selectors** to PrecipGen's Params_Mean_T input
5. **Run 10-year simulations** for each climate scenario
6. **Compare synthetic weather statistics** between scenarios:
   - Annual precipitation totals
   - Number of wet days per month
   - Maximum daily precipitation values

**Expected Learning:**
- Working with PrecipGen parameter tables
- Understanding how climate change affects storm patterns
- Connecting climate science results to stochastic weather generation

### Exercise 3: Mine Site Water Balance with Climate Projections
**Objective:** Apply climate scenarios to a realistic water management problem.

**Scenario Setup:**
- Open pit mine with 2.5 km² surface area
- Current dewatering rate: 500 m³/day average
- Tailings facility requiring water balance management
- Historical evaporation: 1,800 mm/year

**Tasks:**
1. **Build basic water balance model:**
   ```
   Net_Water_Input = Mine_Precip_Input - Mine_Evaporation_Loss
   ```
2. **Connect climate scenarios** to precipitation input:
   ```
   Mine_Precip_Input = Mine_Surface_Area * Active_Precipitation / 1000
   ```
3. **Add temperature-adjusted evaporation:**
   ```
   Climate_Evap_Factor = if(scenario historical: 1.0, RCP45: 1.15, RCP85: 1.25)
   Mine_Evaporation_Loss = Base_Evaporation * Climate_Evap_Factor
   ```
4. **Run annual simulations** for each climate scenario
5. **Create comparison results** showing:
   - Annual water surplus/deficit by scenario
   - Required pumping capacity changes
   - Seasonal water management challenges

**Expected Learning:**
- Practical application of climate projections
- Understanding climate change impacts on industrial operations
- Economic implications of climate change for infrastructure planning

### Exercise 4: Time-Varying Climate Change Implementation
**Objective:** Model gradual climate change over a 50-year period.

**Tasks:**
1. **Create a climate transition factor** that changes from 0 to 1 over years 20-40:
   ```
   Transition = min(1, max(0, (ElapsedTime/year - 20) / 20))
   ```
2. **Blend historical and future climate:**
   ```
   Blended_Precip = Historical * (1 - Transition) + RCP45 * Transition
   ```
3. **Apply to mine site model** from Exercise 3
4. **Run 50-year simulation** and analyze:
   - When do climate impacts become significant?
   - How does gradual change affect planning decisions?
   - What infrastructure adaptations are needed and when?

**Expected Learning:**
- Modeling gradual climate transitions
- Understanding timing of climate change impacts
- Long-term infrastructure planning under climate change

---

## Required Assets

### Pre-Processed Climate Datasets
- **Historical_Daily_Precip.txt** - 30-year daily precipitation baseline (1990-2020)
- **RCP45_Daily_Precip.txt** - Moderate climate change scenario (2021-2050)
- **RCP85_Daily_Precip.txt** - High climate change scenario (2021-2050)
- **Historical_PrecipGen_Parameters.xlsx** - Baseline stochastic weather parameters
- **RCP45_PrecipGen_Parameters.xlsx** - Climate-adjusted parameters for moderate scenario  
- **RCP85_PrecipGen_Parameters.xlsx** - Climate-adjusted parameters for high scenario

### GoldSim Model Templates
- **Climate_Scenarios_Template.gsm** - Basic climate scenario switching model
- **PrecipGen_Climate_Template.gsm** - PrecipGen model with climate parameter switching
- **Mine_Water_Balance_Template.gsm** - Complete mine site water balance with climate integration

### Documentation
- **Dataset_Documentation.pdf** - Description of climate processing methodology and data sources
- **Parameter_Calculation_Guide.pdf** - Explanation of how climate-adjusted parameters were derived

---

## Appendix A: Climate Data Processing Methodology

*This appendix provides technical details for advanced users interested in understanding how the provided datasets were created. This information is not required for completing the lesson exercises.*

### Data Sources and Processing Chain

The provided climate datasets were created using the following workflow:

#### **Source Data**
- **Historical observations:** NOAA weather station data (1990-2020)
- **Climate projections:** CMIP6 ensemble, bias-corrected and downscaled
- **Scenarios:** RCP4.5 (moderate) and RCP8.5 (high emissions)

#### **Processing Steps**
1. **Bias correction:** Quantile mapping to remove systematic GCM biases
2. **Downscaling:** Statistical downscaling to 4-km resolution  
3. **Parameter derivation:** Correlation analysis between precipitation totals and PrecipGen parameters
4. **Quality control:** Validation against independent climate data

#### **Parameter-Precipitation Relationships**
The climate-adjusted PrecipGen parameters were derived using empirical relationships:

**PWW Adjustment:**
```
PWW_future = PWW_historical × (1 + α₁ × ΔP + α₂ × ΔP²)
```
Where ΔP is the fractional change in annual precipitation, and α₁, α₂ are empirically derived coefficients.

**Alpha/Beta Adjustments:**
Similar relationships were established for gamma distribution parameters based on observed correlations between precipitation totals and storm intensity characteristics.

#### **Validation Results**
- Cross-validation R² > 0.75 for all parameter relationships
- Synthetic weather statistics within 5% of target values
- Extreme event frequencies preserved within uncertainty bounds

### Research Background

This methodology represents ongoing research in climate downscaling for water management applications. The approach addresses the limitation that traditional downscaling methods focus only on precipitation totals while ignoring changes in storm patterns and persistence characteristics.

**Key Innovation:** Using observed correlations between precipitation totals and stochastic weather generation parameters enables direct downscaling to the parameters needed for Monte Carlo simulation.

**Applications:** This method is particularly valuable for:
- Mine site water management planning
- Agricultural water allocation under climate change  
- Urban stormwater infrastructure design
- Long-term reservoir operation planning

**Future Development:** Research continues on incorporating temperature effects, spatial correlation preservation, and uncertainty quantification in parameter relationships.

---

## Summary

This lesson demonstrated how to integrate climate model projections into GoldSim water management models using three practical approaches:

1. **Direct Time Series Replacement:** Using pre-processed climate datasets as direct inputs
2. **Parameter-Based Integration:** Modifying stochastic weather generator parameters based on climate projections  
3. **Hybrid Approach:** Combining gradual climate transitions with existing models

### Key Learning Outcomes
- **Practical Implementation:** Focus on using climate science results rather than producing them
- **GoldSim Integration:** Effective use of Time Series, Data, Selector, and Expression elements for climate data
- **Real-World Applications:** Mine site water balance demonstrates economic implications of climate change
- **Parameter Relationships:** Understanding how climate changes affect stochastic weather generation

### Best Practices for Climate Integration
- **Use reliable, pre-processed datasets** from established climate data centers
- **Document all data sources and processing steps** for reproducibility
- **Test multiple climate scenarios** to understand uncertainty ranges
- **Focus on practical implementation** rather than climate data processing
- **Validate results** against historical data and physical understanding

The exercises provided hands-on experience with each method using realistic datasets and scenarios. This practical approach ensures students can immediately apply these techniques to their own water management projects while understanding the underlying climate science principles.

Future lessons will build on these techniques to explore optimization under climate uncertainty and adaptive management strategies.

---

## Required Assets

- **Sample_CMIP6_Data.nc** - Example NetCDF file with climate model projections
- **Climate_Data_Extraction_Tools.xlsx** - Spreadsheet tools for processing climate data
- **Delta_Method_Calculator.gsm** - GoldSim model implementing simple delta method
- **Bias_Correction_Example.gsm** - Model demonstrating bias correction techniques
- **Multi_Model_Ensemble.gsm** - Example of multi-model ensemble implementation
- **Climate_Scenarios_Template.gsm** - Template for scenario-based climate analysis
- **Validation_Metrics.xlsx** - Tools for validating climate projections against observations
- Various images showing climate projection maps, uncertainty ranges, and integration workflows

---

## Additional Resources

### Climate Data Portals
- **ESGF Data Portal:** https://esgf.llnl.gov/
- **Climate Explorer:** https://climexp.knmi.nl/
- **USGS GeoData Portal:** https://cida.usgs.gov/gdp/
- **NASA Giovanni:** https://giovanni.gsfc.nasa.gov/giovanni/

### Processing Tools
- **Climate Data Operators (CDO):** Command-line tools for NetCDF processing
- **GDAL/OGR:** Geospatial data processing libraries
- **R Climate Packages:** Tools for statistical downscaling and bias correction
- **Python Climate Libraries:** xarray, climpy, bias-correction toolkits

### Further Reading
- IPCC Working Group I Reports on Physical Science Basis
- Regional climate downscaling methodologies and applications
- Climate change impact assessment guidelines for water resources
- Uncertainty quantification in climate projections and impacts
## Learning Objectives

*This section is required by the specification but was missing. Please update.*
## Context / Overview

*This section is required by the specification but was missing. Please update.*
## Technical Content

*This section is required by the specification but was missing. Please update.*
## Exercise / Activities

*This section is required by the specification but was missing. Please update.*
## Key Takeaways / Summary

*This section is required by the specification but was missing. Please update.*
