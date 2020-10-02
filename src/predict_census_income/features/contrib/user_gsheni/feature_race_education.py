from ballet import Feature
from ballet.eng import NullFiller

input = ["SCHL", "RAC1P", "FHISP"]


def education_to_bin(schl_value):
	bin_ = 0
	if schl_value <= 15:
		bin_ = 0 # high school
	elif schl_value < 19:
		bin_ = 1 # some college
	elif schl_value  == 20:
		bin_ = 2 # associate
	elif schl_value == 21:
		bin_ = 3 # bachelors
	elif schl_value == 22:
		bin_ = 4 # master
	elif schl_value == 23:
		bin_ = 5 # professional/doctorate
	return bin_


# US race population from highest percentage to lowest
# White, Hispanic, Black, Asian, Multiracial, Other

def race_to_bin(x):
	rac1p_value = x[0]
	fhisp_value = x[1]
	bin_ = 0 
	if rac1p_value in [8, 7, 5, 4, 3]:
		bin_ = 1
	elif rac1p_value == 9: 
		bin_ = 2
	elif rac1p_value == 6:
		bin_ = 3
	elif rac1p_value == 2:
		bin_ = 4
	elif fhisp_value == 1:
		bin_ = 5
	elif rac1p_value == 1:
		bin_ = 6
	return bin_


def bin_education(df):
	df["SCHL"].astype("int")
	df["EducationCategorized"] = df["SCHL"].apply(education_to_bin) 
	# df["RAC1P"].astype("string")
	df['RaceCategorized'] = df[['RAC1P','FHISP']].apply(race_to_bin, axis=1)
	df['EducationRaceBinned'] = df['RaceCategorized'] + df['EducationCategorized']
	return df

transformer = [
	NullFiller(replacement=0),
	bin_education,
    lambda df: df[["EducationRaceBinned"]],
] 

name = "Education and Race Binned"
description = "Educate was categorized with higher values corresponding to more attainment, Race was categorized by more representation having higher values. Values were then summed." 
feature = Feature(input, transformer, name)
