# Temperature-Based ET Methods

**Objective:** Learn to select and apply data-limited evapotranspiration methods based on available meteorological data, with focus on comparing results from different approaches.

## Why This Matters

In many water management projects, comprehensive meteorological data is simply not available. Weather stations may only collect basic temperature measurements, or historical records might be incomplete. Yet accurate estimates of evapotranspiration and evaporation are still essential for water balance calculations.

Rather than abandoning ET modeling in data-limited situations, experienced modelers select appropriate methods based on the data they have. The key is understanding which methods work well with limited data, how to implement them efficiently, and how their results compare to more complex approaches.

This lesson teaches you to be resourceful and practical: use proven, simplified methods when data is limited, and always validate your choice through comparative analysis.

## Part 1: Data-Driven Evaporation Models

In professional water management modeling, selecting the appropriate evaporation method depends primarily on data availability. Rather than building models from scratch, experienced modelers choose from established methods based on the meteorological data they have access to. This approach leverages proven algorithms while focusing effort on project-specific application logic.

### Hamon Method for Lake Evaporation

The **Hamon method** is a widely used approach for calculating daily evaporation from lake surfaces when detailed meteorological data is limited. This method is particularly valuable because it requires only basic temperature data and location information.

**Key Characteristics:**
- Requires air temperature and maximum daylight hours
- Daylight hours calculated from latitude and Julian day
- Primary choice for data-limited scenarios
- Widely validated for lake and reservoir applications

**When to Use:**
- Limited meteorological data availability
- Initial project assessments
- Regional-scale water balance modeling
- Situations where solar radiation data is unavailable

**GoldSim Implementation:**
Rather than programming the Hamon equations manually, use the pre-built model available in the GoldSim Help Center. The **"Lake Evaporation Using the Hamon Method"** article provides a ready-to-use implementation that you can download and integrate into your project.

**Help Center Resource:** [Lake Evaporation Using the Hamon Method](https://help.goldsim.com)

### Hargreaves-Samani Method for Reference ET

The **Hargreaves-Samani equation** estimates reference evapotranspiration (ETo) using only minimum and maximum daily temperature along with latitude. This method fills the gap between simple temperature-based approaches and complex energy balance methods.

**Key Characteristics:**
- Requires only min/max daily temperature and latitude
- Good for sites lacking measured solar radiation data
- Should be calibrated locally when possible
- Widely accepted alternative to Penman-Monteith

**When to Use:**
- Solar radiation data unavailable
- Wind speed and humidity data limited
- Regional ET assessments
- Irrigation planning with limited weather stations

**GoldSim Implementation:**
Use the pre-built model from the Help Center rather than implementing the equations yourself. The **"Hargreaves-Samani Evapotranspiration"** article provides a complete implementation that handles all the mathematical complexity.

**Help Center Resource:** [Hargreaves-Samani Evapotranspiration](https://help.goldsim.com)

![Data-Driven Model Selection](images/EvaporationMethodSelection.png)

## GoldSim Implementation Strategies

The key to successful ET modeling in GoldSim is selecting the appropriate method based on data availability and leveraging pre-built Help Center resources for complex calculations.

### Method Selection Framework
**Choose your approach based on available data:**

**Hamon Method:**
- Use when: Temperature data available, minimal other meteorological data
- Download: "Lake Evaporation Using the Hamon Method" from Help Center
- Best for: Lake and reservoir evaporation modeling

**Hargreaves-Samani Method:**
- Use when: Min/max temperature available, solar radiation unavailable
- Download: "Hargreaves-Samani Evapotranspiration" from Help Center
- Best for: Reference ET in data-limited regions

**Penman-Monteith Method:**
- Use when: Full meteorological dataset available
- Download: "Reference Evapotranspiration (ETo)" from Help Center
- Best for: High-accuracy applications

### Building Application Logic Around Pre-Built Models
Focus your modeling effort on the project-specific components:
```
Reference_ET = Help_Center_Model(Weather_Data)
Crop_ET = Reference_ET × Crop_Coefficient_Logic
Actual_ET = Crop_ET × Soil_Moisture_Function
```

### Implementing Seasonal Variation
Use GoldSim's Lookup Tables for time-varying coefficients:
```
Seasonal_Kc = LookupTable(Day_of_Year, Crop_Stage_Values)
Dynamic_ET = Reference_ET × Seasonal_Kc
```

## Exercises

### Exercise 1: Applying a Data-Limited Model

**Objective:** Use a pre-built Help Center model to quickly estimate lake evaporation.

**Task:** Download and apply the "Lake Evaporation Using the Hamon Method" model to analyze the impact on a water body's balance.

**Steps:**
1. Access the GoldSim Help Center and download the "Lake Evaporation Using the Hamon Method" model
2. Create a new GoldSim project and import the Hamon evaporation model
3. Add a Reservoir element named `Pond` with:
   - Initial volume: 10,000 m³
   - Surface area: 2,000 m²
   - No inflows (to isolate evaporation effects)
4. Connect the Hamon model's evaporation output to the Pond's evaporation input
5. Provide the required inputs (temperature data, latitude)
6. Run simulation for 365 days
7. Plot pond volume and daily evaporation rate over time

**Deliverables:**
- Working GoldSim model incorporating Help Center evaporation model
- Analysis of total annual evaporation loss
- Discussion of when the Hamon method is most appropriate

### Exercise 2: Building Application Logic Around a Complex Model

**Objective:** Use the standard Penman-Monteith model and build project-specific logic around it.

**Task:** Download the "Reference Evapotranspiration (ETo)" model and add crop coefficient logic to calculate crop-specific water requirements.

**Steps:**
1. Download the "Reference Evapotranspiration (ETo) from Meteorological Data" model from the Help Center
2. Import the Penman-Monteith model into a new GoldSim project
3. Create a Lookup Table element `Crop_Coefficient_Seasonal` with seasonal Kc values:
   - Initial stage (Days 1-30): Kc = 0.3
   - Development (Days 31-80): Kc = 0.3 to 1.2 (linear increase)
   - Mid-season (Days 81-120): Kc = 1.2
   - Late season (Days 121-150): Kc = 1.2 to 0.6 (linear decrease)
4. Create Expression element `PET_crop` to calculate: `Reference_ET × Seasonal_Kc`
5. Run the simulation and compare Reference ET vs. Crop ET
6. Calculate total seasonal water requirement

**Deliverables:**
- GoldSim model combining Help Center ET calculation with custom crop logic
- Comparative plots of Reference ET and Crop-specific ET
- Analysis of total seasonal water requirements for the crop

### Exercise 3: Comparative Analysis and Model Selection

**Objective:** Understand how model selection impacts results and learn to choose appropriate methods.

**Task:** Compare all three evaporation/ET methods using the same water body and analyze the differences.

**Steps:**
1. Download all three Help Center models:
   - "Lake Evaporation Using the Hamon Method"
   - "Hargreaves-Samani Evapotranspiration"
   - "Reference Evapotranspiration (ETo) from Meteorological Data"
2. Create a single GoldSim model with one Pond reservoir (5,000 m³, 1,500 m² surface area)
3. Connect all three evaporation/ET calculations in parallel to track each method
4. Use the same meteorological inputs for all methods (where applicable)
5. For methods that calculate ET, apply a standard grass coefficient (Kc = 1.0) to make them comparable to lake evaporation
6. Run simulation for a full year
7. Create a single chart comparing all three methods
8. Calculate the percentage difference between methods

**Deliverables:**
- Integrated GoldSim model with all three calculation methods
- Comparative plot showing results from all three approaches
- Analysis of differences between methods and recommendations for when to use each
- Discussion of the trade-offs between data requirements and accuracy

## Key Takeaways

1. **Data limitations don't stop modeling:** Temperature-based methods (Hamon, Hargreaves-Samani) provide reliable alternatives when comprehensive meteorological data is unavailable

2. **Method selection is data-driven:** Choose Hamon for lake evaporation with temperature-only data, Hargreaves-Samani for reference ET with min/max temperatures, and Penman-Monteith when full weather data is available

3. **Pre-built models save time and reduce errors:** Use validated implementations from the GoldSim Help Center rather than programming complex equations yourself

4. **Comparative analysis reveals method sensitivity:** Different approaches can yield significantly different results; understanding these differences is crucial for making informed decisions

5. **Professional practice emphasizes pragmatism:** Experienced modelers balance accuracy with data availability, choosing the best method possible given project constraints

6. **Focus effort on application logic:** While the core algorithms are available as pre-built tools, your expertise lies in implementing crop coefficients, seasonal variations, and project-specific adaptations

## Required Assets

### GoldSim Help Center Models (Students will download these)
- **"Lake Evaporation Using the Hamon Method"** - Pre-built implementation for data-limited lake evaporation
- **"Hargreaves-Samani Evapotranspiration"** - Temperature-based reference ET calculation
- **"Reference Evapotranspiration (ETo) from Meteorological Data"** - Full Penman-Monteith implementation

### Supporting Data Files
- **Sample_meteorological_data.xlsx** - Multi-year weather dataset for testing all three methods
- **Crop_coefficient_seasonal_values.xlsx** - Lookup table data for seasonal Kc implementation
- **Method_comparison_template.gsm** - Template model structure for Exercise 3 comparative analysis
