# :)
from data_processor import get_file_dimensions
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_fname = 'iris.data'
len_unit = 'cm'
fname1 = 'iris_boxplot.png'
fname2 = 'petal_length_v_width_scatter.png'
fname3 = 'multi_panel_figure.png'
column_labels = ['sepal_width', 'sepal_length',
                 'petal_width', 'petal_length', 'species']


def gen_boxplot(pd_data, plt_cols, ylabel=len_unit, fname=fname1,
                root=plt, save=True, sub=False):

    """ Generates a boxplot figure with given arguments
    Perameters:
    ----------
    REQUIRED
             pd_data: Data to plot
                      ASSUMPTIONS: Must be a pandas.DataFrame object
                                   Must be given column names
            plt_cols: Labels of columns to plot
                      ASSUMPTIONS: Must be a list of strings
                                   Each string must appear in the
                                     pd_data column names
    OPTIONAL
              ylabel: String to use for y axis label
                      DEFAULT: length unit type defined in len_unit above
               fname: String to use to save image to
                      ASSUMPTIONS: Must have ".png" suffix
                      DEFAULT: fname1 as defined above
                root: Matplotlib object where plot will be generated
                      ASSUMPTIONS: Must be capable of holding a boxplot
                      DEFAULT: matplotlib.pyplot
                save: Boolean whether to save the boxplot figure to fname
                 sub: Boolean whether the root passed is a part of a subplot
    Returns:
    --------
    None
    """

    root.boxplot(pd_data[plt_cols],
                 labels=plt_cols)
    if sub:
        root.set_ylabel(ylabel)
    else:
        root.ylabel(ylabel)
    if save:
        root.savefig(fname)


def gen_scatterplot(pd_data, cattype, valtype1, valtype2,
                    len_unit=len_unit, fname=fname2, root=plt,
                    sub=False, save=True):

    """ Generates a scatterplot figure with given arguments
    Perameters:
    ----------
    REQUIRED
             pd_data: Data to plot
                      ASSUMPTIONS: Must be a pandas.DataFrame object
                                   Must be given column names
             cattype: Label for column header for how to divvy the data
                      ASSUMPTIONS: Must be a string
                                   String must appear in the
                                     pd_data column names
            valtype1: Label for column header of x values to plot
                      ASSUMPTIONS: Must be a string
                                   String must appear in the
                                     pd_data column names
            valtype2: Label for column header of y values to plot
                      ASSUMPTIONS: Must be a string
                                   String must appear in the
                                     pd_data column names
    OPTIONAL
               fname: String to use to save image to
                      ASSUMPTIONS: Must have ".png" suffix
                      DEFAULT: fname1 as defined above
                root: Matplotlib object where plot will be generated
                      ASSUMPTIONS: Must be capable of holding a boxplot
                      DEFAULT: matplotlib.pyplot
                save: Boolean whether to save the boxplot figure to fname
                 sub: Boolean whether the root passed is a part of a subplot
    Returns:
    --------
    None
    """

    for s in set(pd_data[cattype]):
        subset = pd_data[pd_data[cattype] == s]
        root.scatter(subset[valtype1], subset[valtype2], label=s)
    root.legend()
    xlabel_str = valtype1 + ' (' + len_unit + ')'
    ylabel_str = valtype2 + ' (' + len_unit + ')'
    if sub:
        root.set_xlabel(xlabel_str)
        root.set_ylabel(ylabel_str)
    else:
        root.xlabel(xlabel_str)
        root.ylabel(ylabel_str)
    if save:
        root.savefig(fname)


def gen_multiplot(pd_data, box_plt_cols, scat_cattype,
                  scat_valtype1, scat_valtype2,
                  fname=fname3, box_ylabel='cm'):

    """ Generates a scatterplot figure with given arguments
    Perameters:
    ----------
    REQUIRED
             pd_data: Data to plot
                      ASSUMPTIONS: Must be a pandas.DataFrame object
                                   Must be given column names
        box_plt_cols: Passed as plt_cols in gen_boxplot function
        scat_cattype: Passed as cattype in gen_scatterplot function
       scat_valtype1: Passed as valtype1 in gen_scatterplot function
       scat_valtype2: Passed as valtype2 in gen_scatterplot function
    OPTIONAL
               fname: String to use to save image to
                      ASSUMPTIONS: Must have ".png" suffix
                      DEFAULT: fname1 as defined above
          box_ylabel: Passed as ylabel in gen_boxplot function
    Returns:
    --------
    None
    """

    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)
    gen_boxplot(pd_data, box_plt_cols, ylabel=box_ylabel,
                root=axes[0], save=False, sub=True)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    gen_scatterplot(pd_data, scat_cattype, scat_valtype1,
                    scat_valtype2, root=axes[1], sub=True, save=False)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    fig.savefig(fname)


def main():
    data = pd.read_csv(data_fname, header=None)
    data.columns = column_labels
    box_plt_cols = data.columns[0:4]
    scat_cattype = data.columns[-1]
    scat_valtype1 = data.columns[2]
    scat_valtype2 = data.columns[3]
    plt.figure(1)
    gen_boxplot(data, box_plt_cols)
    plt.figure(2)
    gen_scatterplot(data, scat_cattype, scat_valtype1, scat_valtype2)
    plt.figure(3)
    gen_multiplot(data, box_plt_cols, scat_cattype,
                  scat_valtype1, scat_valtype2)


if __name__ == '__main__':
    main()
