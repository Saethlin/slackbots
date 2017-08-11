#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import ephem

stars = [ephem.readdb('α CMa,f|S, 06:45:08.9173, -16:42:58.0171, -1.46'),
         ephem.readdb('α Car,f|S, 06:23:57.1099, -52:41:44.381, -0.74'),
         ephem.readdb('α Cen,f|S, 14:39:36.204, -60:50:08.2298, -0.27'),
         ephem.readdb('α Boo,f|S, 14:15:39.6721, +19:10:56.673, -0.05'),
         ephem.readdb('α Lyr,f|S, 18:36:56.3363, +38:47:01.2802, 0.03'),
         ephem.readdb('α Aur,f|S, 05:16:41.3587, +45:59:52.7693, 0.08'),
         ephem.readdb('β Ori,f|S, 05:14:32.2721, -08:12:05.8981, 0.13'),
         ephem.readdb('α CMi,f|S, 07:39:18.1195, +05:13:29.9552, 0.34'),
         ephem.readdb('α Eri,f|S, 01:37:42.8455, -57:14:12.3101, 0.46'),
         ephem.readdb('α Ori,f|S, 05:55:10.3054, +07:24:25.4304, 0.42'),
         ephem.readdb('β Cen,f|S, 14:03:49.4053, -60:22:22.9266, 0.61'),
         ephem.readdb('α Aql,f|S, 19:50:46.9986, +08:52:05.9563, 0.76'),
         ephem.readdb('α Cru,f|S, 12:26:35.8952, -63:05:56.7343, 0.76'),
         ephem.readdb('α Tau,f|S, 04:35:55.2391, +16:30:33.4885, 0.86'),
         ephem.readdb('α Sco,f|S, 16:29:24.4597, -26:25:55.2094, 0.96'),
         ephem.readdb('α Vir,f|S, 13:25:11.5794, -11:09:40.7501, 0.97'),
         ephem.readdb('β Gem,f|S, 07:45:18.9499, +28:01:34.316, 1.14'),
         ephem.readdb('α PsA,f|S, 22:57:39.0463, -29:37:20.0533, 1.16'),
         ephem.readdb('α Cyg,f|S, 20:41:25.9151, +45:16:49.2197, 1.25'),
         ephem.readdb('β Cru,f|S, 12:47:43.2688, -59:41:19.5792, 1.25'),
         ephem.readdb('α Leo,f|S, 10:08:22.311, +11:58:01.9516, 1.39'),
         ephem.readdb('ε CMa,f|S, 06:58:37.5488, -28:58:19.5102, 1.50'),
         ephem.readdb('λ Sco,f|S, 17:33:36.5201, -37:06:13.7648, 1.62'),
         ephem.readdb('α Gem,f|S, 07:34:35.8732, +31:53:17.816, 1.62'),
         ephem.readdb('γ Cru,f|S, 12:31:09.9596, -57:06:47.5684, 1.64'),
         ephem.readdb('γ Ori,f|S, 05:25:07.8633, +06:20:58.9318, 1.64'),
         ephem.readdb('β Tau,f|S, 05:26:17.5131, +28:36:26.8262, 1.65'),
         ephem.readdb('β Car,f|S, 09:13:11.9775, -69:43:01.9473, 1.69'),
         ephem.readdb('ε Ori,f|S, 05:36:12.8133, -01:12:06.9089, 1.69'),
         ephem.readdb('γ Vel,f|S, 08:09:31.9501, -47:20:11.7108, 1.72'),
         ephem.readdb('α Gru,f|S, 22:08:13.9847, -46:57:39.5078, 1.74'),
         ephem.readdb('ε UMa,f|S, 12:54:01.7496, +55:57:35.3627, 1.77'),
         ephem.readdb('ζ Ori,f|S, 05:40:45.5267, -01:56:33.2649, 1.77'),
         ephem.readdb('α UMa,f|S, 11:03:43.6715, +61:45:03.7249, 1.79'),
         ephem.readdb('α Per,f|S, 03:24:19.3701, +49:51:40.2455, 1.80'),
         ephem.readdb('δ CMa,f|S, 07:08:23.4841, -26:23:35.5185, 1.82'),
         ephem.readdb('θ Sco,f|S, 17:37:19.1299, -42:59:52.1808, 1.84'),
         ephem.readdb('ε Sgr,f|S, 18:24:10.3184, -34:23:04.6193, 1.85'),
         ephem.readdb('ε Car,f|S, 08:22:30.8353, -59:30:34.1431, 1.86'),
         ephem.readdb('η UMa,f|S, 13:47:32.4378, +49:18:47.7602, 1.86'),
         ephem.readdb('β Aur,f|S, 05:59:31.7229, +44:56:50.7573, 1.90'),
         ephem.readdb('α TrA,f|S, 16:48:39.8951, -69:01:39.7626, 1.91'),
         ephem.readdb('γ Gem,f|S, 06:37:42.7105, +16:23:57.4095, 1.92'),
         ephem.readdb('α Pav,f|S, 20:25:38.857, -56:44:06.323, 1.94'),
         ephem.readdb('δ Vel,f|S, 08:44:42.2266, -54:42:31.7493, 1.96'),
         ephem.readdb('β CMa,f|S, 06:22:41.9854, -17:57:21.3073, 1.98'),
         ephem.readdb('α Hya,f|S, 09:27:35.2427, -08:39:30.9583, 2.00'),
         ephem.readdb('α UMi,f|S, 02:31:49.0946, +89:15:50.7923, 1.98'),
         ephem.readdb('α Ari,f|S, 02:07:10.4057, +23:27:44.7032, 2.00'),
         ephem.readdb('γ Leo,f|S, 10:19:58.3506, +19:50:29.3468, 2.08'),
         ephem.readdb('β Cet,f|S, 00:43:35.3709, -17:59:11.7827, 2.02'),
         ephem.readdb('σ Sgr,f|S, 18:55:15.9265, -26:17:48.2068, 2.05'),
         ephem.readdb('θ Cen,f|S, 14:06:40.9475, -36:22:11.8371, 2.06'),
         ephem.readdb('β And,f|S, 01:09:43.9239, +35:37:14.0075, 2.05'),
         ephem.readdb('α And,f|S, 00:08:23.2599, +29:05:25.552, 2.06'),
         ephem.readdb('α Oph,f|S, 17:34:56.0695, +12:33:36.1346, 2.07'),
         ephem.readdb('β UMi,f|S, 14:50:42.3258, +74:09:19.8142, 2.08'),
         ephem.readdb('κ Ori,f|S, 05:47:45.3888, -09:40:10.5777, 2.09'),
         ephem.readdb('β Leo,f|S, 11:49:03.5783, +14:34:19.409, 2.11'),
         ephem.readdb('β Per,f|S, 03:08:10.1325, +40:57:20.328, 2.12'),
         ephem.readdb('β Gru,f|S, 22:42:40.0503, -46:53:04.4752, 2.15'),
         ephem.readdb('γ Cen,f|S, 12:41:31.0401, -48:57:35.5375, 2.17'),
         ephem.readdb('ι Car,f|S, 09:17:05.4069, -59:16:30.8353, 2.21'),
         ephem.readdb('λ Vel,f|S, 09:07:59.7579, -43:25:57.3273, 2.21'),
         ephem.readdb('α CrB,f|S, 15:34:41.268, +26:42:52.894, 2.23'),
         ephem.readdb('δ Ori,f|S, 05:32:00.4001, -00:17:56.7424, 2.23'),
         ephem.readdb('γ Cyg,f|S, 20:22:13.7018, +40:15:24.045, 2.23'),
         ephem.readdb('γ Dra,f|S, 17:56:36.3699, +51:29:20.0242, 2.23'),
         ephem.readdb('α Cas,f|S, 00:40:30.4411, +56:32:14.3922, 2.24'),
         ephem.readdb('ζ Pup,f|S, 08:03:35.0475, -40:00:11.3321, 2.25'),
         ephem.readdb('γ And,f|S, 02:03:53.9523, +42:19:47.0223, 2.26'),
         ephem.readdb('ζ UMa,f|S, 13:23:55.5405, +54:55:31.2671, 2.27'),
         ephem.readdb('β Cas,f|S, 00:09:10.6852, +59:08:59.212, 2.28'),
         ephem.readdb('ε Boo,f|S, 14:44:59.2175, +27:04:27.2099, 2.29'),
         ephem.readdb('α Lup,f|S, 14:41:55.7558, -47:23:17.5155, 2.30'),
         ephem.readdb('ε Cen,f|S, 13:39:53.2577, -53:27:59.0081, 2.30'),
         ephem.readdb('δ Sco,f|S, 16:00:20.0053, -22:37:18.1431, 2.31'),
         ephem.readdb('ε Sco,f|S, 16:50:09.8108, -34:17:35.6337, 2.31'),
         ephem.readdb('η Cen,f|S, 14:35:30.4242, -42:09:28.1708, 2.35'),
         ephem.readdb('β UMa,f|S, 11:01:50.4765, +56:22:56.7339, 2.37'),
         ephem.readdb('α Phe,f|S, 00:26:17.0514, -42:18:21.5539, 2.38'),
         ephem.readdb('κ Sco,f|S, 17:42:29.2752, -39:01:47.9391, 2.39'),
         ephem.readdb('ε Peg,f|S, 21:44:11.1561, +09:52:30.0311, 2.40'),
         ephem.readdb('β Peg,f|S, 23:03:46.4575, +28:04:58.0336, 2.42'),
         ephem.readdb('η Oph,f|S, 17:10:22.6869, -15:43:29.6639, 2.43'),
         ephem.readdb('γ UMa,f|S, 11:53:49.8473, +53:41:41.135, 2.44'),
         ephem.readdb('η CMa,f|S, 07:24:05.7023, -29:18:11.1798, 2.45'),
         ephem.readdb('κ Vel,f|S, 09:22:06.8176, -55:00:38.4017, 2.46'),
         ephem.readdb('γ Cas,f|S, 00:56:42.5317, +60:43:00.265, 2.47'),
         ephem.readdb('α Peg,f|S, 23:04:45.6534, +15:12:18.9617, 2.48'),
         ephem.readdb('ε Cyg,f|S, 20:46:12.6824, +33:58:12.925, 2.48'),
         ephem.readdb('β Sco,f|S, 16:05:26.2301, -19:48:19.4004, 2.50')]


def find_bright_stars(location=None):
    if location is None:
        location = ephem.Observer()
        location.lon = 29.6520
        location.lat = -82.3250
        location.elevation = 54

    output = ''
    for star in stars:
        star.compute(location)
        if math.degrees(star.alt) > 15:
            ra = str(star.ra)
            if len(ra) == 10:
                ra = '0'+ra
            dec = str(star.dec)
            deg, min, sec = dec.split(':')
            deg = '{0:+03d}'.format(int(deg))
            if deg.startswith('+'):
                deg = ' '+deg[1:]
            dec = ':'.join((deg, min, sec))
            output += ('{:+.2f}   '+star.name+'   '+ra+'   '+dec+'\n').format(star.mag)

    return output

if __name__ == '__main__':
    import re
    import time
    js_header = r'<!DOCTYPE html>\n<html>\n<head>\n<title>Starlist</title></head><body>'
    js_header += r'<table style="width=100%">'
    while True:
        output = find_bright_stars()
        output = re.sub('  +', ',', output)
        output = re.sub(r'\A', r'<tr><td>', output)
        output = re.sub('\n', '</td></tr>\n<tr><td>', output)
        output = re.sub(',', r'</td><td>', output)
        output = re.sub(r'\Z', r'</td></tr></table>', output)
        output = js_header + output + '</body></html>'
        with open('brightstars2.html', 'w') as outfile:
            outfile.write(output)
        time.sleep(60)