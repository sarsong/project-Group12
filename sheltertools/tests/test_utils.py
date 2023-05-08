import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sheltertools.utils import *
import pytest
import os




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
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_plot_title():
	"""
	Check whether the plot has the correct title
	"""
	expected_title = 'Top DOG Breeds in the Shelter'
	plot_top_breeds('DOG', shelter_data)
	actual_title = plt.gca().get_title()
	assert actual_title == expected_title, f"Unexpected title. Expected: {expected_title}, Actual: {actual_title}"
	
# Test 3
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_save_figures():
	"""
	Check whether a plot is saved successfully to `figures`:
	If the file size is greater than 0, the plot png is saved successfully.
	"""
	plot_trend_line(shelter_data)
	file_path = 'figures/'+'Trend_Line_of_Animal_Intakes_by_Year.png'
	file_size = os.path.getsize(file_path)
	assert file_size > 0