import matplotlib.pyplot as plt

def plot_fatalities_per_region(fatalities_per_region: dict, region: str) -> object:

    colors = []
    for reg in fatalities_per_region.keys():
        if reg == region:
            colors.append('darkslategray')
        else:
            colors.append('m')


     # Plotting the data
    the_plot_bar_fpr = plt.bar(fatalities_per_region.keys(), fatalities_per_region.values(), color=colors) 
    print(type(the_plot_bar_fpr))
    
    # Adding labels and custom title
    plt.xlabel('Region')
    plt.ylabel('Fatalities')
    plt.title('Fatalities per region')  # Use the title parameter for the chart title
    
    plt.xticks(rotation=45)
    
    return the_plot_bar_fpr
