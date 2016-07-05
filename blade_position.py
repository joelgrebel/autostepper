# This Python file uses the following encoding: utf-8

def gdsii_to_blades(left,right, top, bottom):
    """
    Return the autostepper blade position values xl, xr, yf, yr given distances of rectangular
    area from center of mask on GDSII design. Assumes GDSII is in units of
    microns.

    If area does not enclose the center of mask, use negative values
    for relevant side. For example, a square to the left of the center
    will have a negative right distance

    Parameters
    ----------
    left : float
        Distance from center of mask to left boundary
    right : float
        Distance from center of mask to right boundary
    top : float
        Distance from center of mask to top boundary
    bottom : float
        Distance from center of mask to bottom boundary
    """
    # check conditions
    if left > 10000.:
        raise ValueError('left distance must be less than 10,000 microns')
    if right > 10000.:
        raise ValueError('right distance must be less than 10,000 microns')
    if top > 10000.:
        raise ValueError('top distance must be less than 10,000 microns')
    if bottom > 10000.:
        raise ValueError('bottom distance must be less than 10,000 microns')

    if left + right < 1000.:
        raise ValueError('sum of left distance and right distance must be at least 1000 microns')
    if top + bottom < 1000.:
        raise ValueError('sum of top distance and bottom distance must be at least 1000 microns')

    # convert microns to mm
    left = left*0.001
    right = right*0.001
    top = top*0.001
    bottom = bottom*0.001

    xl = 50. - right*5.
    xr = 50. - left*5.
    yf = 50. - top*5.
    yr = 50. - bottom*5.

    return xl, xr, yf, yr



def blades_to_gdsii(xl, xr, yf, yr):
    """
    Return the distances of rectangular area from center of mask on GDSII design
    left, right, top, bottom given autostepper blade position values xl, xr, yf,
    yr. Assumes GDSII is in units of microns.

    Parameters
    ----------
    xl : float
        Distance from center of mask to xl boundary
    xr : float
        Distance from center of mask to xr boundary
    yf : float
        Distance from center of mask to yf boundary
    yr : float
        Distance from center of mask to yr boundary
    """
    # check conditions
    if xl > 95. or xl < 0.:
        raise ValueError('xl distance must be between 0 and 95')
    if xr > 95. or xr < 0.:
        raise ValueError('xr distance must be between 0 and 95')
    if yf > 95. or yf < 0.:
        raise ValueError('yf distance must be between 0 and 95')
    if yr > 95. or yr < 0.:
        raise ValueError('yr distance must be between 0 and 95')

    if xl + xr > 95.:
        raise ValueError('sum of xl distance and xr distance must be less than 95')
    if yf + yr > 95.:
        raise ValueError('sum of yf distance and yr distance must be less than 95')

    # convert mm to microns
    xl = xl*1000.
    xr = xr*1000.
    yf = yf*1000.
    yr = yr*1000.

    left = 10000. - xr/5.
    right = 10000. - xl/5.
    top = 10000. - yf/5.
    bottom = 10000. - yr/5.

    return left, right, top, bottom
