# Lesson 2: Snow Accumulation and Melt

**Objective:** Learn to model snowpack dynamics using both a simple temperature-index method and industry-standard pre-built components in GoldSim, understanding how snow acts as a natural water storage system.

## Why This Matters

In mountainous and cold regions, the majority of the annual water supply comes from snowmelt, not direct rainfall. The timing and volume of this melt are critical for water supply planning, flood risk management, and hydropower generation. An inaccurate snow model can lead to major errors in predicting streamflow for the most important time of the year.

Snowpack represents one of nature's largest water storage systems, often holding more water than all constructed reservoirs in a region combined. Understanding snowpack dynamics is essential for:

- **Water supply forecasting:** Predicting spring and summer water availability
- **Flood management:** Anticipating rapid snowmelt events
- **Hydropower operations:** Optimizing generation during peak melt periods
- **Agricultural planning:** Timing irrigation and crop selection
- **Recreation and tourism:** Managing ski areas and mountain recreation

## Understanding Snowpack as a Natural Reservoir

Snowpack acts as a natural reservoir, storing solid precipitation during cold periods and releasing it as liquid water (melt) during warm periods. This creates a fundamental shift in the timing of water availability compared to rainfall-dominated systems.

### Key Characteristics of Snow Systems

**Temporal Storage:** Snow can accumulate for months, creating a delayed response between precipitation and runoff. This seasonal storage effect is crucial for water management in snow-dominated watersheds.

**Temperature Sensitivity:** Unlike rainfall systems where precipitation immediately becomes runoff, snow systems are highly sensitive to temperature variations. Small temperature changes can dramatically affect the timing and magnitude of water release.

**Elevation Dependence:** Snowpack behavior varies significantly with elevation, creating complex spatial patterns of accumulation and melt across watersheds.

**Energy Balance:** Snow accumulation and melt are fundamentally energy-driven processes, making them more complex than simple rainfall-runoff relationships.

## Part 1: The Temperature-Index Method

The temperature-index method represents the most straightforward approach to snow modeling, requiring only precipitation and temperature data. Despite its simplicity, this method forms the foundation for many operational snow models.

### Fundamental Principles

The temperature-index approach operates on two basic rules:

**Accumulation Rule:** When air temperature falls below a threshold temperature (typically 0°C), precipitation falls as snow and accumulates in the snowpack.

**Melt Rule:** When air temperature rises above the threshold, accumulated snow melts at a rate proportional to the temperature difference above the base temperature.

### Mathematical Framework

#### Snow Accumulation
```
If T_avg < T_threshold:
    Snowfall = Precipitation
    SWE = SWE + Snowfall
Else:
    Snowfall = 0
```

#### Snow Melt
```
If T_avg > T_base AND SWE > 0:
    Melt_Rate = Melt_Factor × (T_avg - T_base)
    SWE = SWE - min(Melt_Rate, SWE)
Else:
    Melt_Rate = 0
```

Where:
- `SWE` = Snow Water Equivalent (mm)
- `T_threshold` = Temperature threshold for snow/rain (typically 0°C)
- `T_base` = Base temperature for melt calculations (typically 0°C)
- `Melt_Factor` = Empirical melt coefficient (mm/day/°C)

### Snow Water Equivalent (SWE)

SWE represents the depth of water that would result from instantly melting the entire snowpack. This standardized measure allows:
- Comparison across different snow densities
- Direct integration with water balance calculations
- Simplified tracking of water storage

Typical SWE values:
- **Early season:** 50-200 mm
- **Peak accumulation:** 200-1000+ mm (depending on climate)
- **Late season:** Gradually declining to zero

### Melt Factor Considerations

The melt factor represents the efficiency of temperature in producing snowmelt and varies based on:

**Physical Factors:**
- Solar radiation exposure
- Wind conditions
- Humidity levels
- Snow surface characteristics

**Typical Values:**
- **Forest areas:** 2-4 mm/day/°C
- **Open areas:** 4-8 mm/day/°C
- **Alpine regions:** 6-10 mm/day/°C

**Seasonal Variation:** Melt factors often increase through the season as snow ages and becomes more efficient at absorbing energy.

![Temperature-Index Snow Model](images/TemperatureIndexSnowDiagram.png)

## Part 2: Advanced Snow Modeling - Snow-17

The **Snow-17 (SNOW-17)** model represents a more sophisticated, physically-based approach developed by the U.S. National Weather Service. It is widely used for operational river forecasting throughout North America and forms the foundation for many water supply forecasts.

### Evolution Beyond Temperature-Index

Snow-17 addresses several limitations of simple temperature-index methods:

**Energy Balance Considerations:** Incorporates multiple energy sources including solar radiation, longwave radiation, and wind effects.

**Dynamic Melt Factors:** Adjusts melt efficiency based on snow age, density, and seasonal conditions.

**Rain-on-Snow Events:** Explicitly handles the complex dynamics when warm rain falls on existing snowpack.

**Cold Content:** Tracks the energy required to bring snowpack to melting temperature before melt can begin.

**Heat Deficit:** Accounts for energy losses during cold periods that must be overcome before melting resumes.

### Key Snow-17 Components

#### Heat Balance
Snow-17 maintains a continuous energy balance for the snowpack:
```
Heat_Balance = Solar_Radiation + Longwave_Radiation + 
               Sensible_Heat + Latent_Heat + Ground_Heat
```

#### Variable Melt Factor
Unlike simple models with constant melt factors, Snow-17 adjusts the melt coefficient based on:
- Antecedent temperature conditions
- Snow age and metamorphism
- Seasonal radiation patterns

#### Liquid Water Storage
The model tracks liquid water within the snowpack, accounting for:
- Retention capacity based on snow density
- Drainage when retention is exceeded
- Refreezing during cold periods

### Other Widely-Used Snow Models

While Snow-17 is an industry standard, it's important to know that other excellent, pre-built conceptual models exist. One notable example available in the GoldSim Model Library is **CemaNeige**. This model, developed in France, is also widely used internationally and provides another robust option for simulating snowpack dynamics.

The key takeaway is that modelers have a choice of sophisticated, pre-validated tools. The principles of using pre-built components—understanding inputs, parameterizing, and validating—apply equally to Snow-17, CemaNeige, and other similar models.

### Snow-17 Advantages

**Physical Basis:** Grounded in energy balance principles rather than purely empirical relationships.

**Operational Validation:** Extensively tested and calibrated across diverse climates and watersheds.

**Industry Standard:** Widely accepted for water supply forecasting and flood prediction.

**Continuous Improvement:** Regularly updated based on research and operational experience.

![Snow-17 Model Components](images/Snow17EnergyBalance.png)

## Part 3: Practical Implementation with Pre-Built Components

Building complex snow models like Snow-17 from scratch requires extensive expertise in snow physics and significant development time. The most efficient approach leverages pre-built, tested components.

### GoldSim Model Library Approach

The GoldSim Model Library contains professionally developed components including:
- **Snow-17 Implementation:** Complete model with standard parameterization
- **Documentation:** Detailed input requirements and output descriptions
- **Validation Examples:** Test cases demonstrating proper usage
- **Parameter Guidance:** Recommended values for different regions

### Benefits of Pre-Built Components

**Quality Assurance:** Components undergo extensive testing and validation.

**Time Efficiency:** Eliminates need to develop complex algorithms from scratch.

**Standardization:** Ensures consistent implementation across projects.

**Focus Shift:** Allows concentration on application rather than algorithm development.

**Maintenance:** Components are updated as improvements become available.

### Implementation Strategy

#### Step 1: Component Selection
Choose appropriate complexity level based on:
- Available input data
- Required accuracy
- Project timeline
- User expertise

#### Step 2: Data Preparation
Ensure input data meets component requirements:
- Temporal resolution (daily, hourly)
- Units and formats
- Quality control and gap filling

#### Step 3: Parameterization
Apply appropriate parameter values for:
- Geographic region
- Elevation zone
- Vegetation type
- Local climate

#### Step 4: Validation
Compare model outputs with:
- Observed snow measurements
- Historical melt patterns
- Regional flow records

![GoldSim Snow Component Integration](images/GoldsimSnowComponents.png)

## GoldSim Implementation Strategies

### Method 1: Simple Temperature-Index
```
Snowfall = if(Temperature < 0°C, Precipitation, 0)
Melt = if(Temperature > 0°C AND SWE > 0, 
          Melt_Factor × Temperature, 0)
```

### Method 2: Enhanced Temperature-Index
```
Variable_Melt_Factor = Base_Factor × Seasonal_Adjustment × Elevation_Factor
Melt = Variable_Melt_Factor × max(Temperature - Base_Temp, 0)
```

### Method 3: Pre-Built Snow-17 Component
```
Snow17_Output = Snow17_Container(
    Precipitation, Temperature, Radiation,
    Humidity, Wind_Speed, Parameters
)
```

## Comparison of Approaches

| Aspect | Temperature-Index | Snow-17 |
|--------|------------------|---------|
| **Data Requirements** | Temperature, Precipitation | Temperature, Precipitation, Radiation, Humidity, Wind |
| **Complexity** | Low | High |
| **Accuracy** | Moderate | High |
| **Development Time** | Short | Long (if built from scratch) |
| **Calibration Effort** | Minimal | Extensive |
| **Physical Basis** | Empirical | Energy Balance |
| **Seasonal Adaptation** | Limited | Dynamic |

---

## Exercises

### Exercise 1: Simple Temperature-Index Snow Model

**Objective:** Build a functional temperature-index snow model to understand fundamental snowpack dynamics.

**Steps:**
1. Create new GoldSim model: `Simple_Snow_Model.gsm`
2. Import climate data from `Snow_Climate_Data.xlsx`:
   - Create Time Series `Precip_TS` (mm/day)
   - Create Time Series `T_avg_TS` (°C)
3. Set up snowpack tracking:
   - Create Reservoir `Snowpack` with units in mm (SWE)
   - Set initial SWE value (e.g., 0 mm for bare ground start)
4. Implement snow accumulation:
   - Create Expression `Snowfall`:
     ```
     if(T_avg_TS < 0°C, Precip_TS, 0 mm/day)
     ```
   - Connect to Snowpack inflow
5. Implement snowmelt:
   - Create Expression `Melt_Rate`:
     ```
     if(T_avg_TS > 0°C AND Snowpack > 0 mm,
        2.5 mm/day/°C × (T_avg_TS - 0°C),
        0 mm/day)
     ```
   - Connect to Snowpack withdrawal
6. Run simulation for full year
7. Create plots showing:
   - Daily temperature and precipitation
   - SWE accumulation and depletion
   - Melt rate timing and magnitude

**Deliverables:**
- Working GoldSim snow model
- Time series plots of key variables
- Analysis of seasonal snow patterns
- Calculation of peak SWE and total melt volume

### Exercise 2: Snow-17 Component Implementation

**Objective:** Apply an industry-standard snow model using pre-built components.

**Steps:**
1. Create new model: `Snow17_Exercise.gsm`
2. Access GoldSim Model Library Snow-17 component
3. Copy Snow-17 container into your model
4. Examine required inputs:
   - Precipitation (mm/day)
   - Temperature (°C)
   - Additional meteorological variables
5. Connect climate data to Snow-17 inputs
6. Configure parameters:
   - Latitude for your study region
   - Elevation adjustment factors
   - Melt factor parameters
7. Run simulation with same climate data as Exercise 1
8. Compare Snow-17 outputs with simple model results

**Deliverables:**
- Functional Snow-17 implementation
- Comparative analysis with temperature-index model
- Documentation of parameter selections
- Evaluation of differences in timing and magnitude of melt

### Exercise 3: Elevation Zone Snow Modeling

**Objective:** Implement multiple snow zones to represent elevation effects.

**Steps:**
1. Create model with three elevation zones:
   - Low elevation (1000m): Temperature-index model
   - Mid elevation (1500m): Modified temperature with elevation adjustment
   - High elevation (2000m): Snow-17 component
2. Apply elevation-based temperature adjustments:
   - Use standard lapse rate (-6.5°C/1000m)
   - Adjust base temperature data for each zone
3. Implement different melt factors by elevation:
   - Low: 4 mm/day/°C
   - Mid: 3 mm/day/°C  
   - High: 2 mm/day/°C
4. Track total water contribution from each zone
5. Analyze seasonal timing differences

**Deliverables:**
- Multi-zone snow model
- Elevation-adjusted climate inputs
- Analysis of elevation effects on snow timing
- Watershed-total melt timing and volume
- Comparison of zone contributions throughout season

---

## Key Takeaways

1. **Snow acts as a natural reservoir** storing water for months and creating delayed runoff responses
2. **Temperature-index methods** provide simple, effective tools for basic snow modeling
3. **Snow-17 represents the industry standard** for operational snow forecasting
4. **Pre-built components** allow access to sophisticated models without extensive development
5. **Elevation significantly affects** snow accumulation and melt patterns
6. **Model selection depends on** data availability, accuracy requirements, and project scope
7. **Validation against observations** is essential for reliable snow modeling

## Regional Considerations

### Alpine Regions
- High elevation gradients require multi-zone approaches
- Solar radiation becomes increasingly important
- Wind redistribution affects accumulation patterns

### Arctic/Subarctic
- Extended accumulation periods (6+ months)
- Low melt factors due to limited radiation
- Permafrost interactions affect drainage

### Maritime Mountains
- Rain-on-snow events common
- High melt factors due to maritime influence
- Frequent freeze-thaw cycles

---

## Required Assets

- **Simple_Snow_Model.gsm** - Basic temperature-index snow model template
- **Snow17_Exercise.gsm** - Model with integrated Snow-17 component
- **Snow_Climate_Data.xlsx** - Daily precipitation and temperature data for snow modeling
- **Snow_Parameters_Regional.xlsx** - Melt factors and parameters for different regions
- **Elevation_Snow_Zones.gsm** - Multi-zone snow model for mountainous watersheds
