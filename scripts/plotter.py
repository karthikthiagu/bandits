import numpy as np

from matplotlib import pyplot as plt

def configure():

    # Set the plot
    paperwidth = 11.7
    paperheight = 8.3
    
    margin = 1.0
    plt.figure(1, figsize = (paperwidth - 2 * margin, paperheight - 2*margin))
    plt.margins(0.1, 0.0)
    plt.xticks([1] + list(np.arange(0, 1001, 250))[1:])
    plt.yticks(np.arange(0, 2, 0.5))
    plt.ylim((0, 1.6))
    
    margin = 0.8
    plt.figure(2, figsize = (paperwidth - 2 * margin, paperheight - 2*margin))
    plt.margins(0.1, 0.0)
    y = np.arange(0, 101, 20)
    y_labels = ['%d%%' % d for d in y]
    plt.xticks([1] + list(np.arange(0, 1001, 250))[1:])
    plt.yticks(y, y_labels)
    plt.ylim((0, 101))

def plot(x, y, simulation):
    plt.figure(simulation['figure'])
    # Plotting
    plt.plot(x, y, color = simulation['color'])
    # Labeling
    plt.xlabel(simulation['xlabel'])
    plt.ylabel(simulation['ylabel'], rotation = 'horizontal', labelpad = 30)
    plt.text(simulation['x_text'], simulation['y_text'], simulation['text'])
    
    if 'filename' in simulation:
        plt.savefig(simulation['filename'])
        print 'saving plots'

