import math

# California population (2023 estimate)
ca_population = 39_240_000

# Average annual statistics (based on recent years)
annual_wildfires = 7500  # Average number of wildfires in CA per year
average_acres_burned = 2_000_000  # Average acres burned per year
total_ca_acres = 101_000_000  # Total acres in California
ca_residential_acres = 30_000_000  # Approximate developed/residential areas

# Risk calculations
def calculate_fire_risks():
    # Probability of any given acre burning in a year
    acre_burn_probability = average_acres_burned / total_ca_acres
    
    # Probability of a fire affecting residential areas (weighted higher due to WUI)
    residential_risk_factor = 1.5  # Wildland-Urban Interface risk multiplier
    residential_burn_prob = (average_acres_burned / total_ca_acres) * residential_risk_factor
    
    # Annual risk of being evacuated due to wildfire (based on recent evacuation data)
    annual_evacuation_risk = 500_000 / ca_population  # Approximate number of people evacuated annually
    
    # Calculate lifetime risks (assuming 50-year residence in California)
    lifetime_years = 50
    lifetime_evac_risk = 1 - (1 - annual_evacuation_risk) ** lifetime_years
    lifetime_property_risk = 1 - (1 - residential_burn_prob) ** lifetime_years
    
    return {
        "Annual acre burn probability": f"1 in {int(1/acre_burn_probability):,}",
        "Annual residential area risk": f"1 in {int(1/residential_burn_prob):,}",
        "Annual evacuation risk": f"1 in {int(1/annual_evacuation_risk):,}",
        "Lifetime evacuation risk (50 years)": f"1 in {int(1/lifetime_evac_risk):,}",
        "Lifetime property risk (50 years)": f"1 in {int(1/lifetime_property_risk):,}",
        "Average fires per year": f"{annual_wildfires:,}",
        "Average acres burned per year": f"{average_acres_burned:,}"
    }

# Compare with other natural disasters in California
annual_disaster_risks = {
    "Wildfire evacuation": 500_000 / ca_population,
    "Earthquake damage (magnitude 5+)": 0.02,  # 2% annual chance of significant earthquake damage
    "Flood (100-year floodplain)": 0.01,  # 1% annual chance in flood zones
    "Landslide (in susceptible areas)": 0.005  # 0.5% annual chance in high-risk areas
}

# Calculate and print all risks
risks = calculate_fire_risks()
print("\nCalifornia Wildfire Statistics:")
for key, value in risks.items():
    print(f"{key}: {value}")

print("\nAnnual Natural Disaster Risks in California (1 in X):")
for disaster, risk in annual_disaster_risks.items():
    print(f"{disaster}: 1 in {int(1/risk):,}")

# Calculate fire season risk distribution (monthly probabilities)
fire_season_distribution = {
    "June": 0.05,
    "July": 0.15,
    "August": 0.25,
    "September": 0.30,
    "October": 0.15,
    "November": 0.05,
    "Rest of year": 0.05
}

print("\nFire Risk Distribution Throughout the Year:")
for month, probability in fire_season_distribution.items():
    print(f"{month}: {probability*100}% of annual fire activity")
