from ballet import Feature


def _education_bucket(highest_attained):
    # unknown or no lower education attained
    if not highest_attained or highest_attained <= 15:
        return 0
    # high school or high school equivalency
    if highest_attained <= 19:
        return 1
    # associates degree
    if highest_attained <= 20:
        return 2
    # bachelors degree
    if highest_attained <= 21:
        return 3
    # advanced degree
    if highest_attained <= 23:
        return 4
    # doctorate degree
    if highest_attained <= 24:
        return 5
    # unknown
    return 0


input = "SCHL"  # TODO - str or list of str
transformer = lambda ser: ser.apply(_education_bucket)
name = "Condensed Educational Attainment"  # TODO - str
description = "Degree of education"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
