import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sheltertools.utils import *


shelter_data = pd.read_csv('data/Animal_Shelter_Data.csv')

# Test 1
def test_number_of_animals_by_type():
	"""
	Check whether the output type is correct
	"""
	output = number_of_animals_by_type(shelter_data)
	# Assert that the output is a pandas Series
	assert type(output) == pd.core.series.Series, "The output is not a pandas Series."

# Test 2