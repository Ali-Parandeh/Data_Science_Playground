# refactor a function into smaller units

def polygon_area(n_sides, side_len):
    """Find the area of a regular polygon

    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: area of polygon

    >>> round(polygon_area(4, 5))
    25
    """
    perimeter = n_sides * side_len

    apothem_denominator = 2 * math.tan(math.pi / n_sides)
    apothem = side_len / apothem_denominator

    return perimeter * apothem / 2

# Refactored Version

def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len


def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator


def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2


# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))
