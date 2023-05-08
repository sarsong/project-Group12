import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def number_of_animals_by_type(shelter_data):
    """
    Show the number of animals in the Shelter by Intake type
    """
    return shelter_data.groupby('Intake Type')['Type'].value_counts()


def plot_top_breeds(animal_type, shelter_data):
    """
    plot the top breeds for a given type of animal: DOG, CAT, or OTHER
    """
    animal_data = shelter_data[shelter_data['Type'] == animal_type]
    animal_breed_counts = animal_data['Breed'].value_counts(ascending=True).tail(5)
    plt.figure(figsize=(10,6))
    plt.barh(animal_breed_counts.index, animal_breed_counts)
    plt.title('Top ' + animal_type +  ' Breeds in the Shelter', size=15)
    plt.xlabel('Count', size=15)
    plt.ylabel('Breed', size=15)
    plt.tight_layout()
    plt.savefig('figures/'+animal_type+'_in_the_Shelter')
    plt.show()
	
def plot_trend_line(shelter_data):
    """
    which year has the most number of animal intakes?
    """
    shelter_data['Intake Year'] = shelter_data['Intake Date'].apply(lambda x: x[-4:])
    # Filter the data to only include records from the year 2014 and later.
    shelter_data = shelter_data[shelter_data['Intake Year'] != '2013']
    intake_counts = shelter_data.groupby('Intake Year').size()
    plt.figure(figsize=(10,6))
    plt.scatter(x=intake_counts.index, y=intake_counts)
    plt.plot(intake_counts.index, intake_counts)
    plt.xticks(np.arange(len(intake_counts)), intake_counts.index)
    plt.xlabel('Intake Year', size=15)
    plt.ylabel('Count', size=15)
    plt.title('Trend Line of Animal Intakes by Year', size=15)
    plt.tight_layout()
    plt.savefig('figures/'+'Trend_Line_of_Animal_Intakes_by_Year')
    plt.show()
	
def trend_proportion(Outcome, yearly_rate):
    """
    Function to plot trend line for rates given Outcome Type
    """
    outcome_type = yearly_rate[yearly_rate["Outcome Type"]==Outcome]
    ax = outcome_type.plot(x="year",y="percent")
    ax.set_xlabel("Year", size=15)
    ax.set_ylabel("% out of total intakes", size=15)
    ax.set_title("Proportion of "+Outcome+" by year", size=15)
    fig = ax.get_figure()
    fig.set_size_inches(8, 6) 
    fig.savefig('figures/' + 'Proportion_of_'+ Outcome + '_by_Year', bbox_inches='tight')