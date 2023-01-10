import matplotlib.pyplot as plt
print(plt.style.available)

'''Types of MatPlotLib Style :['Solarize_Light2',
'_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid',
'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright',
'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid',
 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook',
 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster',
 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white',
 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
'''


'''The "plt.style.use()" function in matplotlib is used to set 
the style of the plots that are created using the library. 
The './deeplearning.mplstyle' parameter specifies the name 
of the style file to use.The "mplstyle" file is a plain text 
file that contains a list of style elements and their values.

When you call plt.style.use(), matplotlib will read the style
file and apply the specified style elements to all the plots 
you create. For example, the deeplearning.mplstyle file might
specify the colors, fonts, and line widths to use in the plots, 
as well as other graphical elements such as the grid lines and tick marks.

This allows you to easily customize the appearance of your plots
without having to specify all the style elements manually each time
you create a plot. 
You can find more information about matplotlib styles in the documentation: 
https://matplotlib.org/stable/tutorials/introductory/customizing.html#style-sheets'''