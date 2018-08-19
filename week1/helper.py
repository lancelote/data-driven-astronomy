import numpy as np
from astropy.io import fits


def running_stats(file_names):
    """Calculates the running mean and stdev for a list of FITS files using
    Welford's method."""
    n, s, mean = 0, 0, 0
    for filename in file_names:
        hdu_list = fits.open(filename)
        data = hdu_list[0].data
        if n == 0:
            mean = np.zeros_like(data)
            s = np.zeros_like(data)

        n += 1
        delta = data - mean
        mean += delta / n
        s += delta * (data - mean)
        hdu_list.close()

    s /= n - 1
    np.sqrt(s, s)

    if n < 2:
        return mean, None
    else:
        return mean, s
