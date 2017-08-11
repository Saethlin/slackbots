from __future__ import division,print_function
import math

import ephem
from astroquery.simbad import Simbad
from astropy.coordinates.name_resolve import NameResolveError
from astroquery.exceptions import TableParseError

from wikipedia_scraper import find_other_names
from iss_nasa_scraper import iss_nasa_ephem

gainesville = ephem.Observer()
gainesville.lat = '29.6652'
gainesville.lon = '-82.325'
gainesville.elevation = 37

planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus',
           'neptune', 'pluto', 'moon']
sun_names = ['sun', 'the sun', 'sol']
moon_names = ['moon', 'the moon', 'lune', 'luna']\


def simbad_resolve(name):
    table = Simbad.query_object(name)
    if table is not None:
        return ephem.readdb(name+',f|S,'+table[0]['RA']+','+table[0]['DEC']+',0')


def check_is_up(user_input, location=None):
    if location is None:
        location = gainesville

    # Clean user input
    target_name = user_input.strip().lower()
    
    # Clean 'the' prefix and strange capitalization
    if target_name.startswith('the'):
        target_name = target_name.split('the',1)[-1].strip()

    # Resolve target name
    if target_name in moon_names:
        target = ephem.Moon()

    elif target_name == 'zenith' or target_name == 'nadir' or target_name in sun_names:
        return '```Really?```'
    
    elif target_name == 'milky way':
        return ('```The Milky Way is a highly extended object. \n' +
                'Are you looking for the galactic center?```')

    # Handle planets directly
    elif target_name in planets:
        target = eval('ephem.'+target_name.capitalize()+'(location)')

    # The ISS is a special case, want to return additional information if not up
    elif target_name == 'iss':
        iss = ephem.readtle(*iss_nasa_ephem())
        iss.compute(location)
        
        iss_alt = math.degrees(float(iss.alt))
        
        if iss_alt < 1:
            next_visible = location.next_pass(iss)
            rise_time, rise_az, _, max_alt, set_time, set_az = next_visible

            rise_time = ephem.localtime(rise_time)
            set_time = ephem.localtime(set_time)

            rise_az = math.degrees(float(rise_az)) % 360
            set_az = math.degrees(float(rise_az)) % 360
            max_alt = math.degrees(float(max_alt)) % 360
            
            output = '```The ISS is not up.\n'
            output += 'It will be visible between\n'
            output += str(rise_time).split('.')[0]+' and\n'
            output += str(set_time).split('.')[0]+',\n'
            output += 'rising at azimuth {:.0f} and\n'.format(rise_az)
            output += 'setting at azimuth {:.0f}\n'.format(set_az)
            output += 'with a max altitude of {:.0f}```'.format(max_alt)
            return output
    
    # Everything else
    else:
        # Try to resolve with simbad
        try:
            target = simbad_resolve(target_name)
        except (NameResolveError, TableParseError):
            # Use wikipedia to look for other names and try those
            other_names = find_other_names(target)
            if other_names is None:
                return ('```Could not resolve target name: "' +
                        user_input+'"```')
            
            ind = -1
            while True:
                try:
                    ind += 1
                    if ind == len(other_names):
                        return ('```Could not resolve target name: "' +
                                user_input+'"```')
                    
                    target_location = simbad_resolve(other_names[ind])

                except NameResolveError:
                    continue
                else:
                    break

        if any(c.isalpha() for c in target_name) and any(c.isdigit() for c in target_name):
            target_name = target_name.upper()
        else:
            target_name = target_name.capitalize()

    target.compute(location)

    # Special cases of re-formatting for ouput's sake
    if target_name == 'moon':
        target_name = 'The moon'
    elif target_name == 'sun':
        target_name = 'The sun'
    elif target_name == 'iss':
        target_name = 'The ISS'

    # Format target RA and DEC for output
    target_ra = str(target.ra)
    if len(target_ra) == 10:
        target_ra = '0'+target_ra
    target_dec = str(target.dec)
    deg, min, sec = target_dec.split(':')
    deg = '{0:+03d}'.format(int(deg))
    if deg.startswith('+'):
        deg = ' '+deg[1:]
    target_dec = ':'.join((deg, min, sec))

    # Format target altitude and azimuth for output
    target_alt = math.degrees(target.alt)
    target_az = math.degrees(target.az)
        
    if target_alt < 1:
        return '```' + target_name + ' is not visible.```'

    airmass = 1/math.cos(90-target_alt)

    # Format output string
    output = ('```' + user_input + " is visible\n" +
             'alt, az: {:.2f}, {:.2f}'.format(target_alt, target_az) + "\n" +
             'airmass: {:.2f}'.format(airmass) + "\n" +
             'RA:  ' + target_ra + "\n" +
             'DEC: ' + target_dec)
    
    # Check if sun is up
    sun = ephem.Sun()
    sun.compute(location)
    
    if math.degrees(sun.alt) > 0:
        output += '\nSUN WARNING'
    
    # Check if moon is close to target
    moon = ephem.Moon()
    moon.compute(location)

    if math.degrees(ephem.separation(target, moon)) < 15:
        output += '\nMOON WARNING, phase: {:.2f}'.format(moon.moon_phase)
    
    output += '```'
    return output


if __name__ == '__main__':
    print(check_is_up('the iss'))
