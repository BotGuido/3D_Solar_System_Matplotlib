from solar_system_3d import SolarSystem, Sun, Planet
solar_system = SolarSystem(500)
sun = Sun(solar_system)
planets = (
    Planet(
        # Mercury
        solar_system,
        position=(150, 50, 0),
        velocity=(0, 5, 5),
    ),
    Planet(
        # Venera
        solar_system,
        mass=10,
        position=(100, -50, 150),
        velocity=(5, 0, 0)
    ),
    Planet(
        # Earth
        solar_system,
        mass=25,
        position=(160, -100, 125),
        velocity=(5, 4, 0)
    )
    # Planet(
    #     # Mars
    #     solar_system,
    #     mass=15,
    #     position=(100, 50, 190),
    #     velocity=(0, 5, 2)
    # ),
    # Planet(
    #     # Jupiter
    #     solar_system,
    #     mass=500,
    #     position=(60, -130, 270),
    #     velocity=(4, 1, 1)
    # ),
    # Planet(
    #     # Saturn
    #     solar_system,
    #     mass=250,
    #     position=(130, 190, -240),
    #     velocity=(0, 5, 3)
    # )
)
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()