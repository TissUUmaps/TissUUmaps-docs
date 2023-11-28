# Regions

## Supported region formats

TissUUmaps can read and write region files in the <a href="https://geojson.org/" target="_blank">GeoJSON</a> format.

Only a subset of the GeoJSON format is supported, as TissUUmaps uses only polygonal regions:

__Main types__:
 * Feature
 * FeatureCollection
 * GeometryCollection

__Geometries__:
 * Polygon
 * Multipolygon

The coordinate system must be the same as the image and marker coordinate systems.

TissUUmaps is a powerful annotation tool designed to facilitate the annotation process for biological tissues.

## Toolbar Features

When entering the Regions tab, the user will see the following toolbar:
![Region toolbar](images/Regions_toolbar.png)

### Drawing Tools

When the user clicks on the drawing tool, a dropdown menu will appear with five different drawing tools:
![Drawing tools](images/Regions_drawing_tools.png)

#### 1. Free Hand Drawing

The free hand drawing tool allows users to annotate regions with free-form shapes.

#### 2. Point-Based Drawing

Use the point-based drawing tool to create annotations by placing individual points.

#### 3. Brush-Based Drawing

The brush-based drawing tool enables users to draw annotations using a brush-like tool. Press `Shift` to erase and `Ctrl` to add to selected region. 

#### 4. Rectangle Drawing

Create rectangular annotations by selecting the rectangle drawing tool. Pressing Shift while dragging makes it a square, and Ctrl centers it around the cursor.

#### 5. Ellipse Drawing

Similar to the rectangle tool, the ellipse drawing tool allows users to create ellipses. Press Shift for a circle and Ctrl for centering.

### Other Tools

- **Selection Tool**: Click on regions to select them. Press Shift to select multiple regions.
- **Show Instance**: Color each region randomly to distinguish between polygons.
- **Fill Opacity**: Control if regions are filled, and the opacity of the filling.
- **Line Width**: Adjust line width and determine if it adapts when zooming.

### Selected Region Tools

When a region is selected, additional tools become available:

- **Zoom to Selected Regions**
- **Unselect All Regions (Shortcut: Escape)**
- **Delete Selected Region**
- **Duplicate Region**
- **Scale Region**
- **Erode/Dilate Regions**
- **Split Multipolygons into Multiple Regions**
- **Fill Holes in Regions**

### Multiple Selected Regions

When multiple regions are selected, access the "Boolean Operation" dropdown with options like:

- **Merge Selected Regions**
- **XOR Selected Regions**
- **Intersect Selected Regions**

## List of regions in the right menu

![List of regions](images/Regions_List_menu.png)

On the right side, there is a menu listing all regions ordered by class. For each region:

- **Select**: Click to select the region in the viewer.
- **Change Class**: Modify the class of the region.
- **Change Name**: Edit the name of the region.
- **Statistics**: View region statistics.
- **Hide**: Toggle the visibility of the region.
- **Delete**: Remove the region.

For groups of regions of one class:

- **Rename Class**
- **Change Class Color**
- **Hide All Regions**
- **Delete All Regions**

For all regions:

- **Hide All**
- **Delete All**

## Region Statistics

Clicking on the statistics button for a specific region reveals:

- **Area**
- **Perimeter**
- **Number of Sub-regions**
- **Bounds (left, top, right, bottom in pixel coordinates)**
- **Number of Each Type of Markers**

![Statistics Example](images/Regions_statistics.png)

## Import Regions

Regions can be imported from .json file, which could be achieved from an external software or also from TissUUmaps' plugin *Points2Regions*. The user just click on the tab *Import* -> *Choose File* and press the button *Import*.

![Regions_Import](images/Regions_Import.png)

After that, the displayed regions appear in the left panel and the list of regions in the right panel as you can see in the example below. In this case, there are 10 different regions, called clusters. The user can change the color, the name, and the class of the regions if necessary. The user can as well draw some extra regions. These regions can be analyzed to observe the marker expression.

![Regions_Import_ex](images/Regions_Import_ex.png)

## Export Regions

The regions can be exported by clicking the tab *Export*, there the user can export two types of files. The first one is the .json file and the name can be selected. The second file is the marker expression in the regions which can be exported as .csv file (this is exported only if the regions were analyzed).

![Regions_Export](images/Regions_Export.png)

In the figure below can be seen an example of the exported .cvs file.

![Regions_Export_ex](images/Regions_Export_ex.png)