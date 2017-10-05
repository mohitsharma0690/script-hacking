import numpy as np
import pandas as pd
import cPickle as pickle
import json
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pdb
import h5py
import importlib

sns.reset_orig()

plt.rcParams['figure.figsize'] = (6.0, 5.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'Blues'

# sns.set_style("ticks")
# for auto-reloading external modules
# see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython
# %load_ext autoreload
# %autoreload 2

def plot_multiple_likelhood_values(likelihood_arr, time_axis=0, 
                                   x=None, save_path='',
                                   title='', xlabel='', ylabel='',
                                   colors=['red', 'green', 'blue'],
                                   labels=['red', 'green', 'blue'],
                                   linestyle=['-', '-', '-', '-'],
                                   marker=['.', '.', '.', '.'],
                                   legend_fontsize=18, xlabel_fontsize=20,
                                   ylabel_fontsize=20,
                                   figsize=(6,5),
                                   legend_loc='upper right'):
    """Plot multiple results.
    
    NOTE: The time for each result should be along the time axis.
    """
    
    assert len(likelihood_arr) <= len(colors), "Missing colors for plot."
    mean_likelihood, std_likelihood = [], []

    if time_axis >= 0:
        for l in likelihood_arr:
            mean_likelihood.append(np.mean(l, axis=time_axis))
            std_likelihood.append(np.std(l, axis=time_axis))
    else:
        assert len(likelihood_arr[0].shape) == 1, \
            "Can only plot vector with -ve time axis"
        mean_likelihood = likelihood_arr
        std_likelihood = [np.zeros(likelihood_arr[0].shape)] * len(likelihood_arr)
        
    if x is None:
        x = range(len(mean_likelihood[0]))
    
    plots = []
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    
    for i in xrange(len(mean_likelihood)):
        m, s = mean_likelihood[i], std_likelihood[i]
        c = colors[i]
        p, = ax.plot(x, m, 'k', color=c, label=labels[i], 
                      linestyle=linestyle[i], 
                      # marker=marker[i],
                     )

        
        ax.fill_between(x, m - s, m + s,
                         alpha=0.2, edgecolor=c, facecolor=c,                         
                         linewidth=4, linestyle='dashdot', antialiased=True)
        

        plots.append(p)
        
    plt.legend(handles=plots, fontsize=legend_fontsize, loc=legend_loc)
    ax.set_title(title)
    ax.set_xlabel(xlabel, fontsize=xlabel_fontsize)
    ax.set_ylabel(ylabel, fontsize=ylabel_fontsize)

    if len(save_path) > 0:
        plt.savefig(save_path, bbox_inches="tight")
    plt.show()
