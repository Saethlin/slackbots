#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import ephem

objects = [ephem.Moon(), ephem.Mercury(), ephem.Venus(), ephem.Mars(), ephem.Jupiter(), ephem.Saturn(),
           ephem.Uranus(),
           ephem.readdb('Albireo,f|S, 19:30:43.286, 27:57:34.84, 5.09'),
           ephem.readdb('M2,f|C, 21:33:27.02, -00:49:23.7, 6.3'),
           ephem.readdb('M15,f|C, 21:29:58.33, 12:10:01.2, 6.2'),
           ephem.readdb('M31|Andromeda,f|G, 00:42:44.3, 41:16:09, 3.44'),
           ephem.readdb('M42|Orion Nebula,f|F, 05:35:17.3, -05:23:28, 4.0'),
           ephem.readdb('M45|Pleiades,f|O, 03:47:24, 24:07:00, 1.6'),
           ephem.readdb('M57|Ring Nebula,f|P, 18:53:35.079, 33:01:45.03, 8.8')
           ]

def whatsup(location=None):
    # If no observer is given, use gainesville
    if location is None:
        location = ephem.Observer()
        location.lon = 29.6520
        location.lat = -82.3250
        location.elevation = 54

    names = []
    altitude = []
    azimuth = []
    for object in objects:
        object.compute(location)
        if math.degrees(object.alt) > 5:
            names.append(object.name)
            altitude.append(math.degrees(object.alt))
            azimuth.append(math.degrees(object.az))

    for name, alt, az in zip(names, altitude, azimuth):
        print(name + ' {:.2f} {:.2f}'.format(alt,az))


if __name__ == '__main__':
    whatsup()