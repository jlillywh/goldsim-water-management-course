# Lesson 2: Simulating Operational Rules

## Learning Objectives

By the end of this lesson, you will be able to:
- Implement seasonal rule curves using lookup tables and temporal logic
- Model on/off control systems using GoldSim's `Status` element with hysteresis
- Apply rate-based constraints including drawdown limits for safety and environmental protection
- Combine multiple operational rules into comprehensive reservoir management strategies
- Understand how operational rules transform simple storage models into realistic management simulations

## Context: From Storage to Management

In Lesson 1, we learned to model reservoirs as dynamic storage systems that integrate inflows and outflows over time. However, our releases were either constant demands or simple withdrawal requests. Real reservoir operations are far more sophisticated—they respond to changing conditions, follow seasonal patterns, respect safety constraints, and implement complex management policies.

**Operational rules** are the decision-making logic that determines how much water to release, when to release it, and under what conditions. These rules encode:
- **Legal requirements** (minimum environmental flows, downstream water rights)
- **Safety constraints** (maximum drawdown rates, flood control protocols)
- **Economic optimization** (seasonal pricing, hydropower generation schedules)
- **Environmental protection** (fish habitat requirements, water quality standards)

This lesson transforms your reservoir models from simple accounting tools into sophisticated representations of real-world water management systems. Mastering these techniques is essential for modeling everything from small municipal systems to complex multi-reservoir networks.

## Technical Content

### Seasonal Rule Curves: Time-Based Operations

Most reservoir operations follow predictable seasonal patterns that reflect the annual cycle of water supply and demand. **Rule curves** define target water levels, release rates, or operational modes that vary throughout the year.

#### Common Seasonal Patterns

**Flood Control Operations**: Many reservoirs maintain lower water levels during potential flood seasons (typically spring) to provide flood storage capacity. This "flood pool" is gradually released as flood risk decreases.

**Water Supply Operations**: Storage is maximized during high-demand periods (often summer) and gradually drawn down during periods when inflows typically exceed demands.

**Environmental Operations**: Releases may be timed to support fish spawning, maintain downstream ecosystems, or provide recreational flows during peak seasons.

**Hydropower Operations**: Releases may be scheduled to maximize electricity generation during peak demand periods or to take advantage of favorable energy prices.

#### Implementation in GoldSim

The most straightforward approach uses GoldSim's built-in temporal functions:

```
Seasonal_Release = Lookup_Table(Month, Monthly_Release_Schedule)
```

This approach allows you to define different target releases for each month of the year. More sophisticated implementations might use:
- **Day of year** for fine-grained seasonal control
- **Multi-year cycles** for longer-term operational patterns
- **Conditional logic** that combines seasonal patterns with current system conditions

#### Adaptive Rule Curves

Advanced rule curves adapt to current system conditions. For example:
- **Drought adjustments**: Reduce target releases when storage falls below normal levels
- **Flood adjustments**: Increase releases when inflows exceed seasonal expectations
- **Multi-year planning**: Adjust seasonal targets based on long-term forecasts or carryover storage

### Status-Based Control: Discrete Operational Logic

Many reservoir operations involve discrete on/off decisions rather than continuous adjustments. GoldSim's `Status` element provides powerful tools for modeling these discrete control systems.

#### The Status Element Framework

A `Status` element represents a system that can exist in one of several defined states (e.g., "Normal", "Drought", "Flood"). Transitions between states are triggered by user-defined conditions based on system variables.

**Key Features:**
- **Multiple states**: Define as many operational modes as needed
- **Conditional triggers**: Transitions based on any model variable or combination
- **Hysteresis**: Different trigger values for entering vs. exiting states
- **State-dependent outputs**: Different behaviors in each operational mode

#### Hysteresis: Preventing Operational Instability

**Hysteresis** is the use of different trigger thresholds for state changes in different directions. This prevents rapid cycling between operational modes when system conditions fluctuate around a single threshold.

**Example**: A pump control system might:
- Turn ON when water level rises to 5.0 meters
- Turn OFF when water level falls to 2.0 meters

Without hysteresis, the pump would rapidly cycle on/off if the water level fluctuated around a single trigger point, potentially damaging equipment and creating unrealistic operations.

#### Common Status-Based Applications

**Emergency Spillway Control**: Automatically open flood gates when reservoir levels exceed safe thresholds, close when levels return to normal ranges.

**Pump Station Operations**: Activate pumps when downstream demands exceed gravity flow capacity, deactivate when storage or demand conditions change.

**Drought Response**: Implement escalating restrictions (Normal → Watch → Warning → Emergency) based on storage levels or system performance indicators.

**Multi-Purpose Operations**: Switch between operational objectives (flood control vs. water supply) based on seasonal conditions or system status.

### Rate-Based Constraints: Dynamic Operational Limits

Many reservoir operations are constrained by **maximum allowable rates of change** rather than absolute limits. These constraints protect infrastructure, maintain environmental conditions, or ensure system stability.

#### Drawdown Rate Limits

**Drawdown rate limits** restrict how quickly reservoir water levels can be lowered. These limits serve multiple purposes:
- **Dam safety**: Prevent rapid pressure changes that could destabilize structures
- **Environmental protection**: Avoid sudden exposure of shoreline areas or stranding of aquatic life
- **Downstream impacts**: Prevent sudden flow changes that could affect downstream users or ecosystems
- **Water quality**: Avoid rapid mixing of water layers with different temperatures or chemical properties

#### Mathematical Implementation

The maximum allowable outflow must satisfy the drawdown constraint:

```
Max_Drawdown_Release = Current_Inflows + (Current_Volume - Min_Allowed_Volume) / Timestep
```

Where `Min_Allowed_Volume` is determined by the current volume minus the maximum allowable volume change for the current timestep.

The actual release is then constrained by:

```
Actual_Release = min(Requested_Release, Physical_Capacity, Max_Drawdown_Release)
```

#### Dynamic Rate Calculations

Rate constraints become more complex when multiple factors interact:
- **Variable surface area**: Drawdown rates may be specified in terms of water level change, requiring conversion to volume changes
- **Multiple outlets**: Different outlet structures may have different rate limitations
- **Environmental windows**: Rate limits may vary seasonally based on ecological sensitivity
- **Emergency overrides**: Safety conditions may temporarily suspend normal rate limits

### Combining Multiple Operational Rules

Real reservoir operations typically involve multiple, sometimes competing, operational rules that must be integrated into a coherent management strategy.

#### Rule Priority Hierarchies

When multiple rules conflict, clear priority hierarchies must be established:
1. **Safety rules** (dam safety, emergency procedures) typically have highest priority
2. **Legal requirements** (environmental flows, water rights) have intermediate priority  
3. **Economic optimization** (hydropower, water supply efficiency) have lowest priority

#### Rule Integration Strategies

**Minimum Flow Approach**: Take the minimum of all applicable constraints to ensure all limits are respected.

**Priority Switching**: Use `Status` elements to switch between different operational modes, each with its own rule set.

**Weighted Objectives**: Use optimization techniques to balance competing objectives when strict hierarchies are insufficient.

## Exercise: Implementing Comprehensive Operational Rules

This multi-part exercise demonstrates how to implement and integrate different types of operational rules in a realistic reservoir management scenario.

### Exercise Setup

We'll enhance the municipal reservoir from Lesson 1 with sophisticated operational rules that address seasonal water management, emergency protocols, and environmental constraints.

### Part 1: Seasonal Rule Curve Implementation

**Objective**: Implement a seasonal release strategy that balances summer water supply with winter flood control.

1. **Open Base Model**
   - Start with `Municipal_Reservoir.gsm` from Lesson 1
   - Save as `Operational_Rules_Reservoir.gsm`

2. **Create Seasonal Release Schedule**
   - Add a `Lookup Table` element named `Seasonal_Release_Targets`
   - Define monthly release targets:
     - **Winter (Dec-Feb)**: 0.4 m³/s (flood control mode)
     - **Spring (Mar-May)**: 0.6 m³/s (transition period)
     - **Summer (Jun-Aug)**: 1.0 m³/s (peak demand period)
     - **Fall (Sep-Nov)**: 0.7 m³/s (storage recovery)

3. **Implement Temporal Logic**
   - Create an `Expression` named `Seasonal_Release_Request`
   - Formula: `Lookup(Month, Seasonal_Release_Targets)`
   - Connect to the `Withdrawal Requests` input of `Supply_Reservoir`

4. **Initial Analysis**
   - Run simulation and compare results to constant demand case
   - Analyze seasonal storage patterns and spill behavior

### Part 2: Emergency Drought Response System

**Objective**: Add a status-based drought response system with multiple restriction levels.

5. **Create Drought Status Element**
   - Add a `Status` element named `Drought_Status`
   - Define four states: "Normal", "Watch", "Warning", "Emergency"

6. **Define State Triggers** (based on reservoir volume as percentage of capacity)
   - **Normal to Watch**: Volume < 60% of capacity
   - **Watch to Normal**: Volume > 70% of capacity
   - **Watch to Warning**: Volume < 40% of capacity  
   - **Warning to Watch**: Volume > 50% of capacity
   - **Warning to Emergency**: Volume < 20% of capacity
   - **Emergency to Warning**: Volume > 30% of capacity

7. **Implement Demand Restrictions**
   - Create `Expression` named `Drought_Multiplier`
   - Logic:
     - Normal: 1.0 (no restrictions)
     - Watch: 0.9 (10% reduction)
     - Warning: 0.7 (30% reduction)
     - Emergency: 0.5 (50% reduction)

8. **Update Release Calculation**
   - Modify `Seasonal_Release_Request` to:
   - `Lookup(Month, Seasonal_Release_Targets) * Drought_Multiplier`

### Part 3: Drawdown Rate Constraints

**Objective**: Implement safety constraints that limit how quickly the reservoir can be drawn down.

9. **Define Drawdown Parameters**
   - Create `Data` element `Max_Drawdown_Rate`: 2.0 m³/s per day
   - Create `Data` element `Reservoir_Surface_Area`: 8,000 m² (from Lesson 1)

10. **Calculate Drawdown Constraint**
    - Create `Expression` named `Max_Drawdown_Release`
    - Formula: `Supply_Reservoir.Inflows + (Supply_Reservoir.Volume - (Supply_Reservoir.Volume - Max_Drawdown_Rate * dt)) / dt`
    - Simplifies to: `Supply_Reservoir.Inflows + Max_Drawdown_Rate`

11. **Apply Final Release Logic**
    - Create `Expression` named `Final_Release_Request`
    - Formula: `min(Seasonal_Release_Request, Max_Drawdown_Release)`
    - Connect to `Supply_Reservoir.Withdrawal_Requests`

### Part 4: Advanced Exercise - Pump Control System

**Objective**: Model an auxiliary pumping system that activates during low storage conditions.

12. **Create Pumping Infrastructure**
    - Add new `Status` element named `Pump_Status` (states: "Off", "On")
    - Add `Data` element `Pump_Capacity`: 0.3 m³/s

13. **Define Pump Control Logic**
    - **Pump On**: When `Supply_Reservoir.Volume < 30,000 m³` AND `Drought_Status != "Normal"`
    - **Pump Off**: When `Supply_Reservoir.Volume > 50,000 m³` OR `Drought_Status == "Normal"`

14. **Implement Auxiliary Inflow**
    - Create `Expression` named `Pump_Inflow`
    - Logic: `If(Pump_Status == "On", Pump_Capacity, 0)`
    - Add to `Supply_Reservoir.Inflows` (requires summing with existing inflows)

### Analysis and Interpretation

After completing all exercise parts, analyze the integrated system:

**Operational Performance**: Compare storage patterns, release reliability, and system response under different scenarios.

**Rule Interactions**: Identify how different rules interact and whether conflicts arise between objectives.

**Emergency Response**: Test system behavior during extreme drought by reducing inflows or increasing demands.

**Optimization Opportunities**: Consider how rule parameters might be adjusted to improve overall system performance.

## Professional Application

Operational rules are essential for multiple aspects of professional water management:

**Regulatory Compliance**: Many reservoir operations are governed by permits, licenses, or legal agreements that specify operational requirements. Accurate modeling ensures compliance and supports permit renewal processes.

**Risk Management**: Operational rules help quantify risks associated with different management strategies, supporting decision-making under uncertainty.

**System Optimization**: Understanding how different rules affect system performance enables optimization of operational parameters to balance competing objectives.

**Emergency Planning**: Modeling emergency operational procedures helps prepare for extreme events and ensures coordinated response capabilities.

**Stakeholder Communication**: Reservoir models with realistic operational rules help explain management decisions to diverse stakeholder groups and build support for operational policies.

**Infrastructure Planning**: Understanding operational constraints helps identify infrastructure improvements that could enhance system flexibility and performance.

## Key Takeaways

- **Operational rules transform storage models into management tools** by encoding real-world decision-making processes
- **Seasonal rule curves** provide time-based operational guidance that reflects annual patterns in water supply and demand
- **Status elements enable discrete control logic** with hysteresis to prevent operational instability around trigger thresholds
- **Rate constraints protect infrastructure and environment** by limiting the speed of operational changes
- **Multiple rules must be integrated hierarchically** with clear priorities when conflicts arise
- **Realistic operational modeling** requires understanding both technical constraints and management objectives
- **Rule validation through scenario analysis** helps ensure robust performance under varying conditions

## Quiz

Test your understanding of reservoir operational rules:

1. **Seasonal Operations**: Why do many reservoirs maintain lower water levels during spring months?
   - A) To reduce evaporation losses
   - B) To provide flood storage capacity during high-inflow periods
   - C) To improve water quality through mixing
   - D) To reduce maintenance costs

2. **Hysteresis in Control Systems**: A pump control system turns ON when water level reaches 5m and turns OFF when level drops to 2m. What is the purpose of this 3m difference?
   - A) To ensure the pump has adequate suction
   - B) To prevent rapid cycling on/off around a single trigger point
   - C) To allow time for manual intervention
   - D) To reduce electrical power consumption

3. **Drawdown Rate Limits**: If a reservoir has a maximum allowable drawdown rate of 1.5 m³/s and current inflows of 2.0 m³/s, what is the maximum total outflow that respects the drawdown constraint?
   - A) 1.5 m³/s
   - B) 2.0 m³/s
   - C) 3.5 m³/s
   - D) Cannot be determined without knowing the current volume

4. **Rule Integration**: When multiple operational rules conflict, which type typically has the highest priority?
   - A) Economic optimization rules
   - B) Environmental flow requirements
   - C) Safety and emergency procedures
   - D) Hydropower generation schedules

**Answers**: 1-B, 2-B, 3-C, 4-C

## Assets Needed

### GoldSim Model Files
- `Operational_Rules_Reservoir.gsm`: Complete exercise model demonstrating seasonal rules, drought response, and rate constraints
- `Pump_Control_Demo.gsm`: Simplified model focusing specifically on status-based pump control with hysteresis

### Data Files Required
- `Seasonal_Release_Schedule.xlsx`: Monthly target release rates for different operational scenarios
- `Extended_Inflow_Data.xlsx`: Multi-year inflow dataset for testing operational rules under various hydrologic conditions

### Images Required
- `seasonal-rule-curve-example.png`: Graph showing typical seasonal variation in target releases with annotations explaining operational logic
- `status-element-configuration.png`: Screenshot of Status element setup showing state definitions and trigger conditions
- `hysteresis-behavior-diagram.png`: Illustration of on/off control behavior with and without hysteresis
- `drawdown-constraint-calculation.png`: Diagram showing how rate constraints are calculated and applied
- `integrated-operations-flowchart.png`: Flowchart showing how multiple operational rules are combined and prioritized

### Supporting Documents
- `Operational_Rules_Reference.pdf`: Quick reference guide for common operational rule types and implementation strategies
- `Troubleshooting_Control_Logic.pdf`: Guide for debugging common issues in operational rule implementation

*Note: This lesson bridges fundamental reservoir modeling with advanced operational strategies. The concepts learned here form the foundation for multi-reservoir systems, shared storage allocation, and specialized applications covered in subsequent lessons.*
