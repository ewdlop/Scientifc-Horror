import math

class CosmicAgingCalculator:
    def __init__(self):
        # Constants
        self.HUBBLE_CONSTANT = 70  # km/s/Mpc
        self.SPEED_OF_LIGHT = 299792.458  # km/s
        self.DARK_ENERGY_DENSITY = 0.68  # Current proportion of dark energy
        
    def expansion_velocity(self, distance_mpc):
        """Calculate recession velocity at given distance"""
        return self.HUBBLE_CONSTANT * distance_mpc
    
    def time_dilation_factor(self, distance_mpc):
        """Calculate time dilation due to cosmic expansion"""
        v = self.expansion_velocity(distance_mpc)
        if v >= self.SPEED_OF_LIGHT:
            return float('inf')
        return 1 / math.sqrt(1 - (v/self.SPEED_OF_LIGHT)**2)
    
    def calculate_cosmic_aging(self, distance_mpc, local_time_years):
        """Calculate time differences due to expansion"""
        # Get time dilation factor
        dilation = self.time_dilation_factor(distance_mpc)
        if dilation == float('inf'):
            return {
                'local_time': local_time_years,
                'distant_time': float('inf'),
                'age_difference': float('inf'),
                'beyond_horizon': True
            }
            
        # Calculate time experienced at different distances
        distant_time = local_time_years * dilation
        age_difference = distant_time - local_time_years
        
        return {
            'local_time': local_time_years,
            'distant_time': distant_time,
            'age_difference': age_difference,
            'beyond_horizon': False
        }

# Create calculator instance
calculator = CosmicAgingCalculator()

# Test different cosmic distances
distances = [
    100,        # Local supercluster
    1000,       # Distant galaxies
    4300,       # Edge of observable universe
    10000       # Beyond observable universe
]

reference_time = 100  # years

print("Cosmic Aging Effects Over 100 Years")
print("-" * 70)
print("Distance (Mpc) | Recession Speed (c) | Time Dilation | Age Difference")
print("-" * 70)

for dist in distances:
    v = calculator.expansion_velocity(dist)
    v_c = v / calculator.SPEED_OF_LIGHT  # Speed in terms of c
    
    result = calculator.calculate_cosmic_aging(dist, reference_time)
    
    if result['beyond_horizon']:
        print(f"{dist:13.0f} | {v_c:16.2f}c | Beyond horizon | Beyond horizon")
    else:
        print(f"{dist:13.0f} | {v_c:16.2f}c | {result['distant_time']:11.2f}y | {result['age_difference']:13.2f}y")

# Calculate some interesting points
print("\nInteresting Cosmic Distances:")
print("-" * 50)

# Find distance where time dilation becomes significant (10% difference)
for dist in range(100, 5000, 100):
    result = calculator.calculate_cosmic_aging(dist, 100)
    if not result['beyond_horizon'] and result['age_difference'] > 10:
        print(f"10% time dilation at: {dist} Mpc")
        break

# Calculate cosmic horizon (where v = c)
horizon_dist = calculator.SPEED_OF_LIGHT / calculator.HUBBLE_CONSTANT
print(f"Cosmic horizon distance: {horizon_dist:.0f} Mpc")

print("\nEffects of Dark Energy:")
print(f"Current dark energy density: {calculator.DARK_ENERGY_DENSITY * 100}%")
print("Expansion is accelerating - these differences will increase over time")
