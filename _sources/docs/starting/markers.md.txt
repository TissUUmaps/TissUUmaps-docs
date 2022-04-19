# Markers

## Supported marker format

TissUUmaps can read CSV (Comma Separated Values) files with a header row, and at least spatial coordinate columns (X and Y). CSV files are not limited in the number of columns or number of rows. Other columns can contain information for displaying markers (key to group markers, color, size, shape, piecharts, etc.)

CSV files can be exported from any spreadsheet program, or any programming language (Python, R, etc.)

## Load markers
You can load the markers when you select the Markers tab and click the button + as you can see in the figure below. You can click the plus several times to load various marker files.
![markers](images/markers.png)

## Markers settings
Before the markers are displayed you have to set up the markers settings.

### File and coordinates
The first step is to select the desired file from your computer under the tab File and coordinates - Choose file.

![load markers](images/load_markers.png)

You can change the Tab name to the desired name, so it is easier to navigate between them when there are more tabs.

![Tab name](images/Tab_name.png)

The next step is to select the column names from the .csv file corresponding to the X and Y coordinates.

![XY coordinates](images/XY_coordinates.png)

### Render options
Here, you can define a key to group by, what is a column from the .csv file which will be used to display the dataset grouped by different colors and shapes of the markers. In this example, we use the column genes, where different colors and shapes of markers represent different genes.

![group by](images/group_by.png)

There is an option to display an extra column, for example when the data are clustered but you want to see the original genes and also the cluster names.

![group by2](images/group_by2.png)

In Color options, you can select to color by groups where each group has a different color. Then on the right side, you can select the color palette:
* Key value - Colors are generated from the name of the group (first 4 letters). Groups starting with the same letter have similar colors.
* Randomly - Colors are generated randomly.
* Dictionary - you can insert a specific dictionary in the text area which will be used for generating the colors.

![Color options](images/Color_options.png)

If you want to color by markers, you have to select the column from the .csv file which will be used to create the colors, and the colormap, but only if the color column is numeral.

![Color options2](images/Color_options2.png)


### Advanced options

### Table of markers

