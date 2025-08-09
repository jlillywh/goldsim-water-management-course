# Required Course Assets

<!-- COURSE_SUMMARY_START -->
<!-- This section is auto-updated by generate_course_outline.py -->
**Current Course Structure:** 6 units, 33 lessons

**Units Overview:**
- Unit 1: Foundations and Data Preparation (8 lessons)
- Unit 2: Climate Data and Weather Modeling (9 lessons)
- Unit 3: Hydrology and Water Balance (6 lessons)
- Unit 4: Water Demand and Consumption (1 lessons)
- Unit 5: Reservoir Modeling and Operations (4 lessons)
- Unit 7: Groundwater Systems (5 lessons)

*Last updated: Auto-generated with course outline*
<!-- COURSE_SUMMARY_END -->

























---

## TODO: Research and Development Tasks

### High Priority - Climate Data Sources Research
**Task:** Research and identify sources for pre-processed climate data for Lesson 02-09
**Due:** Before lesson implementation
**Details:**
- Find publicly available, pre-processed climate projection datasets suitable for water management applications
- Identify datasets that include both historical baselines and future scenarios (RCP4.5, RCP8.5)
- Focus on sources that provide daily time series data for precipitation and temperature
- Look for datasets that already include bias correction and statistical downscaling
- Investigate availability of pre-calculated PrecipGen parameter adjustments

**Potential Sources to Investigate:**
- **ClimateData.ca** (Canada) - Bias-corrected daily climate projections
- **NASA NEX-GDDP** - Global bias-corrected downscaled climate projections  
- **Climate Explorer (KNMI)** - European climate data service
- **USGS Water Resources Climate Change** - Hydrologic climate projections for US
- **World Bank Climate Change Portal** - Global climate data for development
- **CORDEX Regional Downscaling** - Regional climate projections worldwide
- **Australian Climate Projections** - Comprehensive climate data for Australia
- **ECAD (European Climate Assessment)** - European daily climate data

**Expected Deliverables:**
- Curated list of 3-5 reliable data sources with download procedures
- Sample datasets for a representative location (e.g., western US mining region)
- Documentation of data formats, spatial/temporal resolution, and processing methods
- Assessment of data quality and suitability for GoldSim integration

---









This document catalogs all external files (.gsm, .xlsx, etc.) required for the GoldSim Water Management course exercises.

## Unit 1: Getting Started

### Lesson 4: Thinking in GoldSim - Dynamic Simulation Primer
*No additional assets required beyond content*

### Lesson 5: GoldSim vs Spreadsheet Modeling
- **ComparingTimeVaryingResults.gsm** - GoldSim model demonstrating reservoir overflow dynamics
- **simple_timebased_input.xlsx** - Excel spreadsheet for comparison with GoldSim results

### Lesson 6: GoldSim vs Specialized Water Modeling Software
*No additional assets required beyond content*

### Lesson 7: Understanding Temporal and Spatial Scales
*No additional assets required beyond content*

### Lesson 8: Common Data Types and Sources
*No additional assets required beyond content*

### Lesson 9: Modeling Workflow and Best Practices
*No additional assets required beyond content*

---

## Unit 2: Climate Drivers

### Lesson 1: Working with Precipitation Data
- **precipitation_data_examples.xlsx** - Sample precipitation data for different time scales
- **Data_Handling_Example.gsm** - Model showing file input and interpolation
- **Time_Series_Basics.gsm** - Introduction to time series handling

### Lesson 2: Stochastic Weather Generation
- **Historical_Climate_Data.xlsx** - Long-term weather data for statistical analysis
- **Weather_Generator_Example.gsm** - Basic weather generation implementation
- **Stochastic_Weather_Model.gsm** - Complete weather generation model
- **ENSO_Data.xlsx** - El Niño Southern Oscillation index data

### Lesson 3: Working with Temperature Data
- **Monthly_Temperature_Data.xlsx** - Temperature data with monthly resolution
- **Temperature_Vector_Example.gsm** - Model showing vector-based temperature handling
- **Spline_Interpolation_Demo.gsm** - Demonstration of spline interpolation techniques

### Lesson 4: Design Storms
- **IDF_Curves_Example.xlsx** - Sample intensity-duration-frequency data
- **Design_Storm_Patterns.xlsx** - Various storm temporal distributions
- **Simple_Reservoir_System.gsm** - Base model for storm impact analysis

### Lesson 5: Drought Indices and Spatial Estimation
- **Climate_Stations_Multiple.xlsx** - Multi-station climate data with gaps
- **Elevation_Lapse_Rates.xlsx** - Temperature and precipitation correction factors
- **Historical_Drought_Records.xlsx** - Long-term precipitation data for drought analysis
- **PDSI_SPI_Examples.xlsx** - Sample drought index calculations
- **Gap_Filling_Example.gsm** - GoldSim model demonstrating gap-filling methods
- **Spatial_Interpolation.gsm** - Model showing spatial climate distribution
- **Drought_Index_Calculator.gsm** - Simplified drought index implementation

---

## Image Assets Required

### Unit 1: Getting Started
- **goldsim_monolake_example.png** - Screenshot of the GoldSim user interface showing the "MonoLake.gsm" water balance model
- **system_model_overview_diagram.png** - Block diagram showing typical components of a water management model
- **dynamic_simulation_operators.png** - Stylized graphic of people working at control panels, representing dynamic control
- **reservoir_overflow_schematic.png** - Simple schematic of a reservoir showing constant inflow and overflow path

### Unit 2: Climate Drivers
- Various precipitation data visualization examples
- Weather generation flow charts and statistical distributions
- Temperature interpolation comparison graphics
- IDF curves and storm pattern examples
- Spatial interpolation maps, drought index time series, and statistical analysis examples

---

## Unit 3: Surface Flow Modeling

### Lesson 1: Evaporation and Evapotranspiration
- **Reference_ET_Exercise.gsm** - Pre-built model with Penman-Monteith calculation and meteorological time series data
- **Evaporation_coefficient_data.xlsx** - Local evaporation coefficients for different regions
- **Crop_coefficient_database.xlsx** - Comprehensive crop coefficient values by crop type and growth stage

### Lesson 2: Snow Accumulation and Melt
- **Simple_Snow_Model.gsm** - Basic temperature-index snow model template
- **Snow17_Exercise.gsm** - Model with integrated Snow-17 component
- **Snow_Climate_Data.xlsx** - Daily precipitation and temperature data for snow modeling
- **Snow_Parameters_Regional.xlsx** - Melt factors and parameters for different regions
- **Elevation_Snow_Zones.gsm** - Multi-zone snow model for mountainous watersheds

### Lesson 3: Runoff Estimation Methods
- **Runoff_Exercise.gsm** - Base model with precipitation time series for runoff calculations
- **SCS_Parameters_Database.xlsx** - Comprehensive curve number tables by land use and soil type
- **Watershed_Characteristics.xlsx** - Sample watershed data for composite analysis
- **Daily_Precipitation_Runoff.xlsx** - Extended daily precipitation data for continuous simulation
- **Runoff_Validation_Data.xlsx** - Observed streamflow data for model validation

### Lesson 4: Case Study - The Australian Water Balance Model
- **AWBM_Case_Study.gsm** - Complete GoldSim model with AWBM component and sample data
- **AWBM_Climate_Data.xlsx** - Daily precipitation and potential ET time series for model input
- **Observed_Streamflow_Data.xlsx** - Historical streamflow records for calibration and validation
- **AWBM_Parameter_Guidelines.xlsx** - Parameter ranges and calibration guidance for different regions
- **Climate_Change_Scenarios.xlsx** - Modified climate data for impact assessment exercises

### Lesson 5: Modeling Multiple Catchments
- **Multi_Catchment_Exercise.gsm** - Base model with sub-catchment template and example network setup
- **Watershed_Network_Data.xlsx** - Sub-catchment characteristics, connectivity, and parameter data
- **Multi_Station_Flow_Data.xlsx** - Observed streamflow data for multiple gauging stations
- **Spatial_Climate_Data.xlsx** - Precipitation and temperature data with spatial variability
- **Network_Calibration_Tools.gsm** - Advanced model with calibration utilities and performance metrics

---

## Image Assets Required

### Unit 1: Getting Started
- **goldsim_monolake_example.png** - Screenshot of the GoldSim user interface showing the "MonoLake.gsm" water balance model
- **system_model_overview_diagram.png** - Block diagram showing typical components of a water management model
- **dynamic_simulation_operators.png** - Stylized graphic of people working at control panels, representing dynamic control
- **reservoir_overflow_schematic.png** - Simple schematic of a reservoir showing constant inflow and overflow path

### Unit 2: Climate Drivers
- Various precipitation data visualization examples
- Weather generation flow charts and statistical distributions
- Temperature interpolation comparison graphics
- IDF curves and storm pattern examples
- Spatial interpolation maps, drought index time series, and statistical analysis examples

### Unit 3: Surface Flow Modeling
- **simple_evaporation_model.png** - Diagram showing temperature-based evaporation model components
- **penman_monteith_diagram.png** - Schematic of Penman-Monteith equation components and energy balance
- **crop_coefficient_seasonal.png** - Graph showing typical crop coefficient variation throughout growing season
- **temperature_index_snow_diagram.png** - Flowchart showing temperature-index snow model logic
- **snow17_energy_balance.png** - Diagram of Snow-17 energy balance components
- **goldsim_snow_components.png** - Screenshot showing Snow-17 component integration in GoldSim
- **runoff_generation_diagram.png** - Conceptual diagram of runoff generation processes and loss mechanisms
- **runoff_coefficient_diagram.png** - Illustration of simple runoff coefficient method application
- **scs_curve_number_diagram.png** - Graph showing SCS method precipitation-runoff relationships for different CN values
- **scs_advanced_methods.png** - Diagram showing composite watershed analysis and time distribution methods
- **conceptual_model_framework.png** - Comparison diagram of event-based vs. continuous conceptual modeling approaches
- **awbm_structure_diagram.png** - Detailed schematic of AWBM three-store structure and water balance components
- **awbm_parameter_effects.png** - Sensitivity analysis charts showing effects of different parameters on flow outputs
- **goldsim_awbm_container.png** - Screenshot of AWBM container structure in GoldSim interface
- **calibration_workflow.png** - Flowchart showing systematic approach to model calibration process
- **model_complexity_spectrum.png** - Comparison chart of lumped vs. semi-distributed vs. fully distributed modeling approaches
- **localized_container_structure.png** - Diagram showing input/output interfaces and internal structure of localized containers
- **subcatchment_component_architecture.png** - Detailed schematic of modular sub-catchment component design
- **network_implementation_steps.png** - Step-by-step workflow for building multi-catchment river networks
- **multi_catchment_calibration.png** - Flowchart showing hierarchical calibration strategy for complex watersheds

---

*This list has been updated with all assets identified from Units 1-3.*
