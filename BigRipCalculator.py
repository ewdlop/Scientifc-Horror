import math
from datetime import datetime, timedelta

class BigRipCalculator:
    def __init__(self):
        # Fundamental forces (relative strengths)
        self.STRONG_FORCE = 1
        self.ELECTROMAGNETIC_FORCE = 1/137
        self.WEAK_FORCE = 1e-6
        self.GRAVITY = 1e-38
        
        # Current Hubble constant (km/s/Mpc)
        self.H0 = 70
        
        # Time until various structures break apart (years from now)
        self.breakdown_sequence = {
            "Superclusters": 1e9,        # Gravity binding
            "Galaxy Clusters": 1e10,      # Gravity binding
            "Galaxies": 1e11,            # Gravity binding
            "Solar Systems": 1e12,        # Gravity binding
            "Planets": 1e14,             # Electromagnetic binding
            "Molecules": 1e15,           # Electromagnetic binding
            "Atoms": 1e16,              # Electromagnetic binding
            "Atomic Nuclei": 1e17,       # Strong force binding
            "Quarks": 1e18              # Strong force binding
        }
    
    def calculate_breakdown_dates(self):
        current_year = datetime.now().year
        dates = {}
        
        for structure, years in self.breakdown_sequence.items():
            breakdown_date = current_year + years
            dates[structure] = breakdown_date
        
        return dates
    
    def calculate_binding_energy(self, structure_type):
        """Calculate approximate binding energy for different structures"""
        energies = {
            "Superclusters": 1e45,    # Joules
            "Galaxy Clusters": 1e44,
            "Galaxies": 1e43,
            "Solar Systems": 1e34,
            "Planets": 1e32,
            "Molecules": 1e-18,
            "Atoms": 1e-17,
            "Atomic Nuclei": 1e-10,
            "Quarks": 1e-9
        }
        return energies.get(structure_type, 0)
    
    def expansion_force_at_time(self, years_from_now):
        """Calculate expansion force at given time"""
        # Simplified model of accelerating expansion
        return self.H0 * math.exp(years_from_now / 1e11)

# Create calculator instance
calculator = BigRipCalculator()

# Get breakdown dates
breakdown_dates = calculator.calculate_breakdown_dates()

print("Timeline of Universal Breakdown:")
print("-" * 60)
print("Structure          | Years from Now | Force Overcoming")
print("-" * 60)

for structure, years in calculator.breakdown_sequence.items():
    force_type = "Gravity" if years <= 1e12 else \
                 "Electromagnetic" if years <= 1e16 else \
                 "Strong Nuclear"
    
    print(f"{structure:<18} | {years:13.2e} | {force_type}")

print("\nBinding Energy Requirements:")
print("-" * 60)
print("Structure          | Binding Energy (J) | Primary Force")
print("-" * 60)

for structure in calculator.breakdown_sequence.keys():
    energy = calculator.calculate_binding_energy(structure)
    force_type = "Gravity" if energy > 1e30 else \
                 "Electromagnetic" if energy > 1e-15 else \
                 "Strong Nuclear"
    
    print(f"{structure:<18} | {energy:14.2e} | {force_type}")

print("\nKey Implications:")
print("1. Local structures (atoms, molecules) are safe for trillions of years")
print("2. Larger structures break apart first due to weaker gravity")
print("3. Fundamental particles remain stable the longest")
print(f"4. Current Hubble constant: {calculator.H0} km/s/Mpc")
