```python
import numpy as np
from scipy.constants import G  # Gravitational constant
from scipy.integrate import solve_ivp

class GravityStorage:
    def __init__(self, height, mass, efficiency=0.85):
        self.height = height  # meters
        self.mass = mass      # kg
        self.efficiency = efficiency
        self.g = 9.81        # m/s^2

    def potential_energy(self):
        """Calculate stored energy in joules"""
        return self.mass * self.g * self.height * self.efficiency
    
    def power_output(self, time_period):
        """Calculate power output in watts"""
        return self.potential_energy() / time_period

class TidalPower:
    def __init__(self, basin_area, tidal_range):
        self.basin_area = basin_area    # m^2
        self.tidal_range = tidal_range  # m
        self.water_density = 1025       # kg/m^3
        self.efficiency = 0.8

    def available_energy_per_tide(self):
        """Calculate available energy per tidal cycle"""
        volume = self.basin_area * self.tidal_range
        return 0.5 * self.water_density * self.g * volume * self.tidal_range * self.efficiency

class GravityAssist:
    def __init__(self, planet_mass, planet_radius):
        self.planet_mass = planet_mass      # kg
        self.planet_radius = planet_radius  # m
        
    def escape_velocity(self):
        """Calculate escape velocity at surface"""
        return np.sqrt(2 * G * self.planet_mass / self.planet_radius)
    
    def orbital_velocity(self, radius):
        """Calculate orbital velocity at given radius"""
        return np.sqrt(G * self.planet_mass / radius)
    
    def gravity_assist_delta_v(self, v_approach, planet_velocity):
        """Calculate velocity change from gravity assist"""
        # Simplified model for hyperbolic trajectory
        v_inf = np.linalg.norm(v_approach - planet_velocity)
        return 2 * v_inf

class GravityFoundation:
    def __init__(self, soil_density, depth):
        self.soil_density = soil_density  # kg/m^3
        self.depth = depth                # m
        self.g = 9.81                     # m/s^2
        
    def bearing_capacity(self, foundation_width, cohesion, friction_angle):
        """Calculate ultimate bearing capacity using Terzaghi's equation"""
        Nc = (1/np.tan(friction_angle)) * (np.exp(2 * friction_angle * np.pi/180) - 1)
        Nq = np.exp(2 * friction_angle * np.pi/180) * np.tan(45 + friction_angle/2)**2
        Ny = 2 * (Nq + 1) * np.tan(friction_angle)
        
        qu = (cohesion * Nc + self.soil_density * self.depth * Nq + 
              0.5 * self.soil_density * foundation_width * Ny)
        return qu

# Example calculations

# 1. Pumped Hydro Storage
def pumped_hydro_example():
    storage = GravityStorage(height=500, mass=1e6)  # 500m height, 1000 tons
    print(f"Stored energy: {storage.potential_energy()/3.6e6:.2f} MWh")
    print(f"Power output (6h discharge): {storage.power_output(6*3600)/1e6:.2f} MW")

# 2. Tidal Power Plant
def tidal_power_example():
    tidal = TidalPower(basin_area=1e6, tidal_range=10)  # 1km^2 basin, 10m range
    energy_per_tide = tidal.available_energy_per_tide()
    print(f"Energy per tide: {energy_per_tide/3.6e9:.2f} GWh")

# 3. Gravity Assist Calculations
def gravity_assist_example():
    earth = GravityAssist(5.97e24, 6.37e6)
    jupiter = GravityAssist(1.9e27, 6.99e7)
    
    print(f"Earth escape velocity: {earth.escape_velocity()/1000:.2f} km/s")
    print(f"Jupiter gravity assist ΔV: {jupiter.gravity_assist_delta_v(
        np.array([0, 10000, 0]), np.array([13000, 0, 0]))/1000:.2f} km/s")

# 4. Foundation Engineering
def foundation_example():
    foundation = GravityFoundation(soil_density=1800, depth=3)
    bearing_capacity = foundation.bearing_capacity(
        foundation_width=2, cohesion=25000, friction_angle=30)
    print(f"Ultimate bearing capacity: {bearing_capacity/1000:.2f} kPa")

# Advanced Applications

class GravityTrain:
    """Gravity train through Earth (theoretical)"""
    def __init__(self):
        self.earth_radius = 6.37e6  # m
        self.earth_mass = 5.97e24   # kg
        
    def tunnel_acceleration(self, depth):
        """Calculate acceleration at given depth"""
        if depth > self.earth_radius:
            return 0
        return G * self.earth_mass * depth / (self.earth_radius**3)
    
    def travel_time(self, tunnel_length):
        """Calculate travel time through gravity tunnel"""
        return 2 * np.pi * np.sqrt(self.earth_radius / (3 * G * self.earth_mass))

class SpaceElevator:
    """Space elevator analysis"""
    def __init__(self):
        self.earth_radius = 6.37e6
        self.geo_radius = 4.2164e7
        self.earth_mass = 5.97e24
        
    def tension_at_height(self, height, cable_density, cable_area):
        """Calculate cable tension at given height"""
        r = self.earth_radius + height
        Omega = 7.292e-5  # Earth's angular velocity
        
        def tension_derivative(r, T):
            return (cable_density * cable_area * 
                   (G * self.earth_mass/(r**2) - Omega**2 * r))
        
        # Solve differential equation for tension
        r_span = np.linspace(self.earth_radius, r, 1000)
        solution = solve_ivp(tension_derivative, 
                           [self.earth_radius, r], 
                           [0], t_eval=r_span)
        return solution.y[0][-1]

# Run examples
if __name__ == "__main__":
    print("=== Pumped Hydro Storage ===")
    pumped_hydro_example()
    
    print("\n=== Tidal Power Plant ===")
    tidal_power_example()
    
    print("\n=== Gravity Assist Maneuvers ===")
    gravity_assist_example()
    
    print("\n=== Foundation Engineering ===")
    foundation_example()
    
    # Advanced examples
    gravity_train = GravityTrain()
    print(f"\nGravity train travel time (diameter): {gravity_train.travel_time(2*6.37e6)/60:.0f} minutes")
    
    elevator = SpaceElevator()
```
    tension = elevator.tension_at_height(1e7, 1500, 0.1)
    print(f"\nSpace elevator tension at 10,000 km: {tension/1e9:.2f} GN")
