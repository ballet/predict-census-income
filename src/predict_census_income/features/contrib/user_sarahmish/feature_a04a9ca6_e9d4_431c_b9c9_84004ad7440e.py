from ballet import Feature

input = ["NWLK", "NWLA", "NWAV", "MIG", "MIL"]
transformer = lambda df: df.sum(axis=1)
name = "Employability Status"
description = "A collection of flags to indicate the employability status of the household. Such as mobility status, military service. Combined with the active status of work."
feature = Feature(input, transformer, name=name, description=description)
