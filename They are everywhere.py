import numpy as np
from scipy.constants import G, c

def quadrupole_moment(mass, separation):
    """
    Calculate quadrupole moment for a rotating system
    mass: in kg
    separation: in meters
    """
    return mass * separation**2

def gw_strain_amplitude(mass, separation, frequency, distance):
    """
    Calculate gravitational wave strain amplitude h
    mass: kg
    separation: meters
    frequency: Hz
    distance: meters
    """
    # Quadrupole formula for GW strain
    h = 4 * G * quadrupole_moment(mass, separation) * (2*np.pi*frequency)**2
    h = h / (c**4 * distance)
    return h

def power_radiated(mass, separation, frequency):
    """
    Calculate power radiated in gravitational waves
    Using the quadrupole formula
    """
    omega = 2 * np.pi * frequency
    P = (32/5) * G**4 * mass**2 * separation**4 * omega**6 / c**5
    return P

# Example 1: Laboratory scale rotating masses
def lab_scale_example():
    mass = 1000  # 1 ton
    separation = 10  # 10 meters
    freq = 10  # 10 Hz
    distance = 100  # 100 meters
    
    h = gw_strain_amplitude(mass, separation, freq, distance)
    P = power_radiated(mass, separation, freq)
    
    print("\nLaboratory Scale Example:")
    print(f"Strain amplitude h: {h:.2e}")
    print(f"Power radiated: {P:.2e} watts")
    
    # Compare to LIGO sensitivity (~10^-21)
    print(f"Ratio to LIGO sensitivity: {h/1e-21:.2e}")

# Example 2: Large industrial machine
def industrial_example():
    mass = 100000  # 100 tons
    separation = 50  # 50 meters
    freq = 1  # 1 Hz
    distance = 1000  # 1 km
    
    h = gw_strain_amplitude(mass, separation, freq, distance)
    P = power_radiated(mass, separation, freq)
    
    print("\nIndustrial Scale Example:")
    print(f"Strain amplitude h: {h:.2e}")
    print(f"Power radiated: {P:.2e} watts")

# Example 3: Theoretical maximum with current materials
def theoretical_max():
    # Using strongest known materials (carbon nanotubes)
    tensile_strength = 130e9  # Pa
    density = 1750  # kg/m^3
    
    # Maximum rotating mass limited by material strength
    max_velocity = np.sqrt(tensile_strength/density)
    radius = 100  # meters
    freq = max_velocity/(2*np.pi*radius)
    mass = density * np.pi * radius**2 * 1  # 1 meter thick
    
    h = gw_strain_amplitude(mass, radius, freq, 1000)
    P = power_radiated(mass, radius, freq)
    
    print("\nTheoretical Maximum with Current Materials:")
    print(f"Maximum frequency: {freq:.2f} Hz")
    print(f"Strain amplitude h: {h:.2e}")
    print(f"Power radiated: {P:.2e} watts")

# Example 4: Comparison with natural sources
def natural_source_comparison():
    # Binary neutron star system
    mass_ns = 1.4 * 2e30  # 1.4 solar masses
    separation = 100000  # 100 km
    freq = 100  # 100 Hz
    distance = 1e20  # ~10 kpc (galactic scale)
    
    h = gw_strain_amplitude(mass_ns, separation, freq, distance)
    P = power_radiated(mass_ns, separation, freq)
    
    print("\nBinary Neutron Star System:")
    print(f"Strain amplitude h: {h:.2e}")
    print(f"Power radiated: {P:.2e} watts")

# Run all examples
if __name__ == "__main__":
    print("Gravitational Wave Generation Analysis")
    print("=====================================")
    
    lab_scale_example()
    industrial_example()
    theoretical_max()
    natural_source_comparison()
    
    print("\nKey Conclusions:")
    print("1. Human-scale devices produce extremely weak gravitational waves")
    print("2. Even with optimal materials, artificial GW are far below detection limits")
    print("3. Power radiated is negligible compared to mechanical power input")
    print("4. Natural astronomical sources are many orders of magnitude stronger")
