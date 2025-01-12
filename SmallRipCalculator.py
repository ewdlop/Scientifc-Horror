class SmallRipCalculator:
    def __init__(self):
        # Fundamental forces in relative strengths
        self.forces = {
            "Gravity": 1e-38,
            "Weak Nuclear": 1e-6,
            "Electromagnetic": 1/137,
            "Strong Nuclear": 1
        }
        
        # Binding energies in joules
        self.binding_energies = {
            "Galaxy Clusters": 1e45,
            "Galaxies": 1e43,
            "Solar Systems": 1e34,
            "Planets": 1e32,
            "Molecules": 1e-18,
            "Atoms": 1e-17,
            "Nuclei": 1e-10
        }
        
        # Timeline for small rip (years from now)
        self.small_rip_timeline = {
            "Begin separation of galaxy clusters": 1e11,
            "Galaxies begin to isolate": 1e12,
            "Solar systems destabilize": 1e13,
            "Planets begin orbital decay": 1e14,
            "Molecular bonds weaken": 1e15,
            "Atomic stability affected": 1e16,
            "Nuclear forces remain stable": "Never"
        }
    
    def calculate_stability(self, time_years):
        """Calculate which structures remain stable at given time"""
        stability = {}
        for structure, breakdown_time in self.small_rip_timeline.items():
            if isinstance(breakdown_time, str):
                stability[structure] = "Always stable"
            else:
                stability[structure] = "Stable" if time_years < breakdown_time else "Unstable"
        return stability
    
    def force_ratio(self, time_years):
        """Calculate ratio of dark energy to fundamental forces"""
        # Simplified model of dark energy growth
        dark_energy = 1e-35 * (1 + time_years/1e11)
        ratios = {}
        for force_name, force_strength in self.forces.items():
            ratios[force_name] = dark_energy / force_strength
        return ratios

# Create calculator
calculator = SmallRipCalculator()

# Print timeline
print("Small Rip Timeline:")
print("-" * 60)
for event, time in calculator.small_rip_timeline.items():
    print(f"{event:<30} | {str(time):>20}")

# Check stability at different times
test_times = [1e10, 1e12, 1e14, 1e16]
print("\nStability at Different Times:")
print("-" * 60)
for time in test_times:
    print(f"\nAt {time:.1e} years from now:")
    stability = calculator.calculate_stability(time)
    for structure, status in stability.items():
        print(f"{structure:<30} | {status:>20}")

# Calculate force ratios
print("\nDark Energy to Fundamental Force Ratios:")
print("-" * 60)
for time in [1e11, 1e13, 1e15]:
    print(f"\nAt {time:.1e} years:")
    ratios = calculator.force_ratio(time)
    for force, ratio in ratios.items():
        print(f"{force:<20} | {ratio:.2e}")

print("\nKey Differences from Big Rip:")
print("1. Strong nuclear force remains unaffected")
print("2. Process is much slower")
print("3. Atomic nuclei remain stable")
print("4. Some structures survive indefinitely")
