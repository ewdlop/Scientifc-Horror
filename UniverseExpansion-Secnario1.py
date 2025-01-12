# Constants
H0 = 70  # Hubble constant in km/s/Mpc
SPEED_OF_LIGHT = 299792  # km/s
SECONDS_PER_YEAR = 31557600

class UniverseExpansion:
    def __init__(self, hubble_constant=H0):
        self.H0 = hubble_constant
        self.hubble_time = 1 / (hubble_constant * 1.023e-10)  # Years
        
    def calculate_expansion_rate(self, distance_mpc):
        """Calculate expansion rate at given distance"""
        return self.H0 * distance_mpc  # km/s
    
    def time_dilation_factor(self, distance_mpc):
        """Calculate time dilation factor due to expansion"""
        v = self.calculate_expansion_rate(distance_mpc)
        if v >= SPEED_OF_LIGHT:
            return float('inf')
        return 1 / (1 - (v/SPEED_OF_LIGHT)**2)**0.5
    
    def age_difference(self, distance_mpc, earth_years):
        """Calculate age difference due to cosmic expansion"""
        dilation = self.time_dilation_factor(distance_mpc)
        if dilation == float('inf'):
            return float('inf')
        return earth_years * (dilation - 1)

# Create universe calculator
universe = UniverseExpansion()

# Calculate effects at different distances
distances = [1, 10, 100, 1000, 4300]  # Megaparsecs
earth_time = 100  # years

print(f"Universe Expansion Effects Over {earth_time} Earth Years")
print("\nDistance (Mpc) | Expansion Rate (km/s) | Time Dilation | Age Difference (years)")
print("-" * 75)

for dist in distances:
    rate = universe.calculate_expansion_rate(dist)
    dilation = universe.time_dilation_factor(dist)
    age_diff = universe.age_difference(dist, earth_time)
    
    if dilation == float('inf'):
        dilation_str = "Beyond horizon"
        age_diff_str = "N/A"
    else:
        dilation_str = f"{dilation:.6f}"
        age_diff_str = f"{age_diff:.2f}"
    
    print(f"{dist:13.0f} | {rate:17.2f} | {dilation_str:12} | {age_diff_str:>20}")

# Calculate current universe parameters
print(f"\nUniverse Parameters:")
print(f"Hubble Constant: {H0} km/s/Mpc")
print(f"Hubble Time: {universe.hubble_time:.2f} billion years")
print(f"Observable Universe Radius: ~4300 Mpc")

# Calculate acceleration of expansion
print("\nExpansion Acceleration Effects:")
dark_energy_fraction = 0.68  # Current estimate of dark energy contribution
print(f"Dark Energy Contribution: {dark_energy_fraction*100:.1f}%")
print("Future expansion rate will increase exponentially due to dark energy")
