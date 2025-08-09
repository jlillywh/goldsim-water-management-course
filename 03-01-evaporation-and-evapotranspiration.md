# Lesson 1: Evaporation and Evapotranspiration

**Objective:** Learn to differentiate between evaporation and evapotranspiration and implement both simple and standard methods for calculating these critical water losses in a GoldSim model.

## Why This Matters

In many water systems, especially in arid or semi-arid regions, more water can be lost to the atmosphere through evaporation and plant uptake than is used for direct human consumption. Failing to account for these losses can lead to a significant overestimation of available water supply, impacting decisions on everything from reservoir management to agricultural planning.

Evaporation and evapotranspiration are key processes that remove water from a system. Modeling them accurately is essential for any realistic water balance, and understanding these processes will form the foundation for all subsequent surface water modeling in this course.

## Understanding the Fundamentals

### Evaporation vs. Evapotranspiration

While often used interchangeably in casual conversation, evaporation and evapotranspiration represent distinct but related processes:

**Evaporation** applies specifically to direct water loss from open water surfaces such as lakes, reservoirs, ponds, or wet soil surfaces. It's driven by atmospheric demand and the energy available to convert liquid water to vapor.

**Evapotranspiration (ET)** describes water loss from land surfaces and combines two distinct processes:
- **Evaporation:** Water evaporating directly from the soil surface
- **Transpiration:** Water taken up by plant roots and released as vapor through leaf stomata

Understanding this distinction is crucial because each process responds differently to environmental conditions and requires different modeling approaches.

## Part 1: Understanding Evapotranspiration (ET)

Evapotranspiration modeling requires understanding two critical concepts that determine water loss from vegetated surfaces.

### Potential vs. Actual Evapotranspiration

**Potential ET (PET):** The amount of evapotranspiration that would occur if water were never a limiting factor—essentially, the atmospheric demand for water. PET represents the maximum possible ET under given climatic conditions.

**Actual ET (AET):** The amount of evapotranspiration that actually occurs, which can be limited by:
- Soil moisture availability
- Plant stress conditions
- Root zone characteristics
- Irrigation practices

The relationship between PET and AET is fundamental to water balance modeling:
- When soil moisture is abundant: AET ≈ PET
- When soil moisture is limited: AET < PET
- The ratio AET/PET indicates water stress levels

### Factors Controlling ET

ET rates are influenced by:

**Climatic Factors:**
- Solar radiation (primary energy source)
- Air temperature
- Humidity (vapor pressure deficit)
- Wind speed

**Surface Factors:**
- Vegetation type and density
- Leaf area index
- Root zone depth
- Soil moisture content

**Management Factors:**
- Irrigation scheduling
- Crop rotation
- Mulching practices

## Part 2: The Standard Method - FAO Penman-Monteith

The **FAO Penman-Monteith equation** represents the global standard for calculating potential evapotranspiration. Developed by the Food and Agriculture Organization (FAO), this physically-based equation provides the most accurate method for estimating atmospheric water demand.

### Why Penman-Monteith is the Standard

The Penman-Monteith equation:
- **Physically based:** Incorporates energy balance and aerodynamic principles
- **Internationally standardized:** Consistent methodology worldwide
- **Comprehensive:** Accounts for all major climatic factors
- **Validated:** Extensively tested across climates and crops

### Required Inputs

The equation requires four primary meteorological variables:
- **Air temperature** (daily maximum and minimum)
- **Relative humidity** (or vapor pressure)
- **Wind speed** (measured at 2m height)
- **Solar radiation** (or sunshine hours)

### **Use the Pre-Built Model from the Help Center**

**IMPORTANT:** For this method, you should **use the pre-built model** available in the GoldSim Help Center rather than attempting to implement the complex equations yourself. The Penman-Monteith equation involves intricate calculations including:
- Saturation vapor pressure curves
- Psychrometric constants
- Net radiation calculations
- Aerodynamic and surface resistance parameters

The Help Center provides a thoroughly tested, professional implementation that:
- Handles all mathematical complexity
- Includes proper error checking
- Uses standardized FAO-56 methodology
- Can be easily integrated into your project

**Help Center Resource:** [Reference Evapotranspiration (ETo) from Meteorological Data](https://help.goldsim.com)

### Reference Evapotranspiration (ETo)

The output of the Penman-Monteith equation is **Reference Evapotranspiration (ETo)**, which represents the PET for a standardized reference surface:
- Well-watered grass
- 0.12 m height
- Fixed surface resistance (70 s/m)
- Albedo of 0.23

This standardization allows consistent comparison across locations and applications.

![Penman-Monteith Components](images/PenmanMonteithDiagram.png)

## Part 3: From Reference ET to Crop-Specific ET

Reference ET provides the baseline atmospheric demand, but actual crop water requirements vary significantly based on crop type, growth stage, and management practices.

### Crop Coefficients (Kc)

To estimate crop-specific potential ET, we use **crop coefficients (Kc)**:

```
PET_crop = ETo × Kc
```

Where:
- `ETo` is reference evapotranspiration
- `Kc` is the crop coefficient (dimensionless)
- `PET_crop` is crop-specific potential ET

### Crop Coefficient Characteristics

Crop coefficients vary by:

**Crop Type:**
- Corn: 0.3 - 1.2
- Wheat: 0.3 - 1.15
- Alfalfa: 0.4 - 1.2
- Potatoes: 0.5 - 1.15

**Growth Stage:**
- **Initial:** Low Kc (limited leaf area)
- **Development:** Increasing Kc
- **Mid-season:** Peak Kc (full canopy)
- **Late season:** Declining Kc (senescence)

**Management:**
- Irrigation frequency
- Fertilization practices
- Variety selection

### Temporal Variation

Crop coefficients change throughout the growing season, typically following a characteristic curve:
1. **Initial stage:** Plants establish, minimal water use
2. **Crop development:** Rapid growth, increasing water demand
3. **Mid-season:** Full canopy, maximum water use
4. **Late season:** Maturity and harvest, declining demand

![Crop Coefficient Curve](images/CropCoefficientSeasonal.png)

---

## Exercise: Applying a Crop Coefficient (Kc)

**Objective:** Calculate crop-specific ET (`PET_crop`) using a given Reference ET (`ETo`) timeseries and a seasonal crop coefficient.

**Task:** Use a GoldSim Lookup Table to define seasonal crop coefficients and calculate crop-specific evapotranspiration.

**Steps:**
1. Create a new GoldSim model and save as `Crop_Coefficient_Exercise.gsm`
2. Import the provided Reference ET time series data (`ETo_Daily_Data.xlsx`)
3. Create a Lookup Table element `Seasonal_Kc` with the following values:
   - Day 1-90 (Spring): Kc = 0.4
   - Day 91-180 (Early Summer): Kc = 0.8
   - Day 181-270 (Late Summer): Kc = 1.2
   - Day 271-365 (Fall): Kc = 0.6
4. Create an Expression element `PET_crop` with the formula: `ETo × Seasonal_Kc`
5. Run the simulation for one year
6. Plot both Reference ET and Crop-specific ET on the same chart
7. Calculate the total annual crop water requirement

**Deliverables:**
- Working GoldSim model with seasonal crop coefficient implementation
- Time series plot comparing Reference ET vs. Crop-specific ET
- Analysis of seasonal patterns and total annual water requirement
- Discussion of how crop coefficients modify the base atmospheric demand

---

## Key Takeaways

1. **ET vs. Evaporation distinction:** Evapotranspiration combines soil evaporation and plant transpiration, while evaporation refers only to direct water loss from open surfaces

2. **Potential vs. Actual ET:** PET represents atmospheric demand under unlimited water conditions; AET is what actually occurs when limited by soil moisture, plant stress, or other factors

3. **Penman-Monteith is the global standard:** FAO Penman-Monteith provides the most accurate, physically-based method for calculating reference evapotranspiration when full meteorological data is available

4. **Crop coefficients enable application:** Reference ET (ETo) from Penman-Monteith is adapted to specific crops using crop coefficients (Kc) that vary by crop type and growth stage

5. **Seasonal variation is critical:** Crop coefficients change dramatically throughout the growing season, making time-varying Kc essential for accurate water requirement calculations

6. **Focus on concepts, not equations:** Understanding the relationship between PET, AET, reference ET, and crop coefficients is more important than memorizing complex mathematical formulations

---

## Required Assets

### Supporting Data Files
- **ETo_Daily_Data.xlsx** - Reference evapotranspiration time series for crop coefficient exercise
- **Seasonal_Kc_lookup_template.xlsx** - Template for creating crop coefficient lookup tables
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
