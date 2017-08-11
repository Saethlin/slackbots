import urllib2

URL = 'http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html'


def iss_nasa_ephem():
    
    opener = urllib2.build_opener()
    the_page = opener.open(URL).read()
    
    data = the_page.split('TWO LINE MEAN ELEMENT SET')[-1].strip().split('\n')
    
    return [line.strip() for line in data[:3]]
    
if __name__ == '__main__':
    print(iss_nasa_ephem())
