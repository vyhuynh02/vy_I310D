<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
"""volume_of_sphere

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EhMOFR9DwJXyfCCfinnorTQP2m0cy9fI
"""

>>>>>>> 83b1c3dec310f6c9c5985c87d6ab1a6befda3b3b
def calculate_volume_of_sphere(radius):
  pi = 3.14
  volume = (4/3) * pi * radius**3
  return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")