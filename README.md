# V1.0
### Usage
Version 1.0 is restricted to analyzing the attached 'iris.data' csv file. Running the main script 'plotter.py' has no arguments and will generate three plots - a box plot, a scatter plot, and a multipanel box/scatter plot. The file names for these images can be specified within plotter.py.
### Functionality
#### Functions defined in data_processor.py are not used for main functionality
#### Functions in plotter.py;
##### main() calls and uses all functions in plotter.py
##### gen_multiplot() calls gen_scatterplot() and gen_boxplot() and has them act on a multiplot
##### gen_scatterplot() creates a scatterplot
##### gen_boxplot() creates a boxplot
### Testing
#### All functions defined in data_processor.py are give unit tests
#### plotter.py is given functional testing


