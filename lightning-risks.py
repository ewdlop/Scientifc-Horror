import math

# Key statistics
us_population = 332_000_000
annual_lightning_deaths = 27  # Average annual deaths in the US
annual_lightning_injuries = 243  # Average annual injuries
annual_lightning_strikes = 25_000_000  # Average cloud-to-ground strikes in US

# Risk calculations
def calculate_lightning_risks():
    # Annual probabilities
    annual_death_risk = annual_lightning_deaths / us_population
    annual_injury_risk = annual_lightning_injuries / us_population
    
    # Lifetime risk (average lifespan of 78.79 years)
    lifetime = 78.79
    lifetime_death_risk = 1 - (1 - annual_death_risk) ** lifetime
    lifetime_injury_risk = 1 - (1 - annual_injury_risk) ** lifetime
    
    return {
        "Annual death risk": f"1 in {int(1/annual_death_risk):,}",
        "Annual injury risk": f"1 in {int(1/annual_injury_risk):,}",
        "Lifetime death risk": f"1 in {int(1/lifetime_death_risk):,}",
        "Lifetime injury risk": f"1 in {int(1/lifetime_injury_risk):,}",
        "Lightning strikes per year": f"{annual_lightning_strikes:,}"
    }

# Location risk factors (relative to average)
location_risks = {
    "Florida": 3.5,  # 3.5x average risk
    "Oklahoma": 2.8,
    "Mississippi": 2.5,
    "Louisiana": 2.3,
    "Alabama": 2.2,
    "Kansas": 2.0,
    "Colorado": 1.8,
    "North Carolina": 1.7,
    "Texas": 1.6,
    "Arizona": 1.5
}

# Activity risk factors (relative to average)
activity_risks = {
    "Golfing": 5.0,
    "Fishing": 4.5,
    "Camping": 3.8,
    "Swimming": 3.5,
    "Beach activities": 3.2,
    "Soccer/sports": 2.8,
    "Farm work": 2.5,
    "Construction": 2.3,
    "Walking/hiking": 2.0,
    "Indoor activities": 0.1
}

# Calculate and print risks
risks = calculate_lightning_risks()
print("\nLightning Strike Statistics:")
for key, value in risks.items():
    print(f"{key}: {value}")

print("\nRelative Risk by Location (compared to US average):")
for location, risk in location_risks.items():
    print(f"{location}: {risk}x average risk")

print("\nRelative Risk by Activity (compared to average):")
for activity, risk in activity_risks.items():
    print(f"{activity}: {risk}x average risk")

# Monthly distribution of lightning strikes
monthly_distribution = {
    "June": 0.20,
    "July": 0.25,
    "August": 0.20,
    "September": 0.15,
    "May": 0.10,
    "Rest of year": 0.10
}

print("\nMonthly Distribution of Lightning Strikes:")
for month, probability in monthly_distribution.items():
    print(f"{month}: {probability*100}% of annual strikes")

# Safety tips effectiveness (risk reduction factor)
safety_measures = {
    "Stay indoors": 0.99,  # 99% risk reduction
    "Avoid tall objects": 0.85,
    "Stay away from water": 0.80,
    "Avoid metal objects": 0.75,
    "Use surge protectors": 0.70,
    "30/30 rule (sound/sight)": 0.65
}

print("\nEffectiveness of Safety Measures (Risk Reduction):")
for measure, reduction in safety_measures.items():
    print(f"{measure}: {reduction*100}% risk reduction")
