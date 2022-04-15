************
Projects
************

==============================
Saving and loading projects
==============================



======================
The TMAP file format
======================


The TMAP format contains a description of image layers, markers, regions, and settings. It is highly recommended to create .tmap files by saving projects from TissUUmaps, but you can also edit the files manually to add or change projects' settings, or generate them as exported data from other software for import in TissUUmaps.

The TMAP format uses JSON, with the following specifications:

.. jsonschema::
    :lift_definitions:
    :auto_reference:
    :auto_target:

    {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "TMAP project specifications",
        "description": "Description of image layers, markers, regions, and settings of a project. Required properties are shown in **bold** text",
        "type": "object",
        "properties": {
            "filename": {
                "description": "Name of the project",
                "type": "string"
            },
            "layers": {
                "type": "array",
                "items": [
                    { "$ref" : "#/definitions/Layer"}
                ],
                "default": "[]"
            },
            "layerOpacities": {
                "type": "object",
                "patternProperties": {
                    "^[0-9]+$": {
                    "type": "integer"
                    }
                },
                "required": [
                ]
            },
            "layerVisibilities": {
                "type": "object",
                "patternProperties": {
                    "^[0-9]+$": {
                    "type": "boolean"
                    }
                },
                "required": [
                ]
            },
            "layerFilters": {
                "type": "object",
                "patternProperties": {
                    "^[0-9]+$": {
                    "$ref": "#/definitions/LayerFilter"
                    }
                },
                "required": [
                    "0"
                ]
            },
            "filters": {
                "description": "List of filters shown as active filters in the GUI under the Image layers tab",
                "type": "array",
                "items": [
                    { "$ref": "#definitions/Filter" }
                ],
                "default": "[\"Saturation\", \"Brightness\", \"Contrast\"]"
            },
            "compositeMode": {
                "description": "Mode defining how image layers will be merged (composited) with each other. Valid string values are \"source-over\" and \"lighter\", which correspond to 'Channels' and 'Composite' in the GUI.",
                "type": "string",
                "default": "source-over"
            },
            "markerFiles": { 
                "type": "array",
                "items": [
                    { "$ref": "#/definitions/MarkerFile" }
                ],
                "default": "[]"
            },
            "regions": {
                "description": "GeoJSON object, see :ref:`Regions section<regions>`.",
                "type": "object",
                "default": "{}"
            },
            "regionFile": {
                "type": "string",
                "default": ""
            },
            "regionFiles": {
                "type": "array",
                "items": {},
                "default": "[]"
            },
            "plugins": {
                "description": "List of plugins to load with the project. See also the :ref:`Plugins section<plugins>`.",
                "type": "array",
                "items": [
                    { "type": "string" }
                ],
                "default": "[]"
            },
            "hideTabs": {
                "description": "Hide tabs of markers dataset. Only use when you have a unique marker tab.",
                "type": "boolean",
                "default": "false"
            },
            "settings": { 
                "type": "array",
                "items": [
                    { "$ref": "#/definitions/Setting" }
                ],
                "default": "[]"
            }
        },
        "definitions": {
            "Layer": {
                "description": "Description of an image layer. Required properties are shown in **bold** text",
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Name of the image layer",
                        "type": "string"
                    },
                    "tileSource": {
                        "description": "Relative path to an image file in a supported format. See also the :ref:`Images section<images>`.",
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "tileSource"
                ]
            },
            "LayerFilter": {
                "description": "Description of an image filter to be applied to the pixels in an image layer. Required properties are shown in **bold** text",
                "type": "array",
                "items": [
                    {
                    "type": "object",
                    "properties": {
                        "name": {
                            "description": "Filter name. See :ref:`Filter` for more details.",
                            "type": "string"
                        },
                        "value": {
                            "description": "Filter parameter. See :ref:`Filter` for more details.",
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "value"
                    ]
                    }
                ]
            },
            "Filter": {
                "description": "TissUUmaps supports most filters available in OpenSeadragon via the https://github.com/usnistgov/OpenSeadragonFiltering plugin.",
                "enum": ["Color","Brightness", "Exposure", "Hue", 
                        "Contrast", "Vibrance", "Noise", 
                        "Saturation","Gamma","Invert","Greyscale",
                        "Threshold","Erosion","Dilation"]
            },
            "ColorScale": {
                "description": "TissUUmaps supports most of the color scales available in the D3.js library. See https://github.com/d3/d3-scale-chromatic for reference. Note: the colors for 'interpolateRainbow' are currently overridden by a custom Turbo-like color scale in version 3.0.x of TissUUmaps.",
                "enum": ["interpolateCubehelixDefault", "interpolateRainbow", "interpolateWarm", "interpolateCool", "interpolateViridis", "interpolateMagma", "interpolateInferno", "interpolatePlasma", "interpolateBlues", "interpolateBrBG", "interpolateBuGn", "interpolateBuPu", "interpolateCividis", "interpolateGnBu", "interpolateGreens", "interpolateGreys", "interpolateOrRd", "interpolateOranges", "interpolatePRGn", "interpolatePiYG", "interpolatePuBu", "interpolatePuBuGn", "interpolatePuOr", "interpolatePuRd", "interpolatePurples", "interpolateRdBu", "interpolateRdGy", "interpolateRdPu", "interpolateRdYlBu", "interpolateRdYlGn", "interpolateReds", "interpolateSinebow", "interpolateSpectral", "interpolateTurbo", "interpolateYlGn", "interpolateYlGnBu", "interpolateYlOrBr", "interpolateYlOrRd"]
            },
            "Shape": {
                "description": "TissUUmaps supports most of the marker shapes that are also used by the Napari software, https://napari.org. In addition to the name strings listed below, shape can also be specified by a corresponding index in range 0-13.",
                "enum": ["cross", "diamond", "square", "triangle up", "star", "clobber", "disc", "hbar", "vbar", "tailed arrow", "triangle down", "ring", "x", "arrow"]
            },
            "MarkerFile": {
                "description": "Description of settings and GUI objects for a marker dataset loaded from CSV file. Required properties are shown in **bold** text.",
                "type": "object",
                "properties": {
                    "title": {
                        "description": "Name of marker button",
                        "type": "string"
                    },
                    "comment": {
                        "description": "Optional description text shown next to marker button",
                        "type": "string",
                        "default": ""
                    },
                    "name": {
                        "description": "Name of marker tab",
                        "type": "string"
                    },
                    "autoLoad": {
                        "description": "If the CSV file for the marker dataset should be automatically loaded when the TMAP project is opened. If this is false, the user instead has to click on the marker button in the GUI to load the dataset.",
                        "type": "boolean",
                        "default": "false"
                    },
                    "uid": {
                        "description": "A unique identifier used internally by TissUUmaps to reference the marker dataset",
                        "type": "string"
                    },
                    "expectedHeader": {
                        "$ref": "#definitions/ExpectedHeader"
                    },
                    "expectedRadios": {
                        "$ref": "#definitions/ExpectedRadios"
                    },
                    "path": {
                        "description": "Relative file path to CSV file in which marker data is stored",
                        "type": "string"
                    },
                    "settings": {
                        "type": "array",
                        "items": [
                            {
                            "$ref": "#/definitions/Setting"
                            }
                        ],
                        "default": "[]"
                    }
                },
                "required": [
                    "title",
                    "name",
                    "uid",
                    "expectedHeader",
                    "expectedRadios",
                    "path"
                ]
            },
            "ExpectedHeader": {
                "description": "Input field values for settings in a marker tab. Required properties are shown in **bold** text.",
                "type": "object",
                "properties": {
                    "X": {
                        "description": "Name of CSV column to use as X-coordinate",
                        "type": "string"
                    },
                    "Y": {
                        "description": "Name of CSV column to use as Y-coordinate",
                        "type": "string"
                    },
                    "gb_col": {
                        "description": "Name of CSV column to use as key to group markers by",
                        "type": "string",
                        "default": "null"
                    },
                    "gb_name": {
                        "description": "Name of CSV column to display for groups instead of group key value",
                        "type": "string",
                        "default": "null"
                    },
                    "cb_cmap": {
                        "description": "Name of D3 color scale to be used for color mapping. See :ref:`ColorScale` for valid string values.",
                        "type": "string",
                        "default": ""
                    },
                    "cb_col": {
                        "description": "Name of CSV column containing scalar values for color mapping or hexadecimal RGB colors in format '#ff0000'",
                        "type": "string",
                        "default": "null"
                    },
                    "cb_gr_dict": {
                        "description": "JSON string specifying a custom dictionary for mapping group keys to group colors. Example: '{\"key1\": \"#ff0000\", \"key2\": \"#00ff00\", \"key3\": \"#0000ff\"}'",
                        "type": "string",
                        "default": ""
                    },
                    "scale_col": {
                        "description": "Name of CSV column containing scalar values for changing the size of markers",
                        "type": "string",
                        "default": "null"
                    },
                    "scale_factor": {
                        "description": "Numerical value for a fixed scale factor to be applied to markers",
                        "type": "string",
                        "default": "1"
                    },
                    "pie_col": {
                        "description": "Name of CSV column containing data for pie chart sectors",
                        "type": "string",
                        "default": "null"
                    },
                    "pie_dict": {
                        "description": "JSON string specifying a custom dictionary for mapping pie chart sector indices to colors. Example: '{0: \"#ff0000\", 1: \"#00ff00\", 2: \"#0000ff\"}'. If no dictionary is specified, TissUUmaps will use a default color palette instead.",
                        "type": "string",
                        "default": ""
                    },
                    "shape_col": {
                        "description": "Name of CSV column containing a name or an index for marker shape. See also :ref:`Shape`.",
                        "type": "string",
                        "default": "null"
                    },
                    "shape_fixed": {
                        "description": "Name or index of a single fixed shape to be used for all markers. See :ref:`Shape` for valid string values.",
                        "type": "string",
                        "default": "cross"
                    },
                    "shape_gr_dict": {
                        "description": "JSON string specifying a custom dictionary for mapping group keys to group shapes. Example: '{\"key1\": \"square\", \"key2\": \"diamond\", \"key3\": \"triangle up\"}'. See also :ref:`Shape`.",
                        "type": "string",
                        "default": ""
                    },
                    "opacity_col": {
                        "description": "Name of CSV column containing scalar values for opacities",
                        "type": "string",
                        "default": "null"
                    },
                    "opacity": {
                        "description": "Numerical value for a fixed opacity factor to be applied to markers",
                        "type": "string",
                        "default": "1"
                    },
                    "tooltip_fmt": {
                        "description": "Custom formatting string used for displaying metadata about a selected marker. See https://github.com/TissUUmaps/TissUUmaps/issues/2 for an overview of the grammer and keywords. If no string is specified, TissUUmaps will show default metadata depending on the context.",
                        "type": "string",
                        "default": ""
                    }
                },
                "required": [
                    "X",
                    "Y"
                ]
            },
            "ExpectedRadios": {
                "description": "Radio button state and checkbox state for settings in a marker tab. Required properties are shown in **bold** text.",
                "type": "object",
                "properties": {
                    "cb_col": {
                        "description": "If markers should be colored by data in CSV column",
                        "type": "boolean",
                        "default": "false"
                    },
                    "cb_gr": {
                        "description": "If markers should be colored by group",
                        "type": "boolean",
                        "default": "true"
                    },
                    "cb_gr_rand": {
                        "description": "If group color should be generated randomly",
                        "type": "boolean",
                        "default": "false"
                    },
                    "cb_gr_dict": {
                        "description": "If group color should be read from custom dictionary",
                        "type": "boolean",
                        "default": "false"
                    },
                    "cb_gr_key": {
                        "description": "If group color should be generated from group key",
                        "type": "boolean",
                        "default": "true"
                    },
                    "pie_check": {
                        "description": "If markers should be rendered as pie charts",
                        "type": "boolean",
                        "default": "false"
                    },
                    "scale_check": {
                        "description": "If markers should be scaled by data in CSV column",
                        "type": "boolean",
                        "default": "false"
                    },
                    "shape_col": {
                        "description": "If markers should get their shape from data in CSV column",
                        "type": "boolean",
                        "default": "false"
                    },
                    "shape_gr": {
                        "description": "If markers should get their shape from group",
                        "type": "boolean",
                        "default": "true"
                    },
                    "shape_gr_rand": {
                        "description": "If group shape should be generated randomly",
                        "type": "boolean",
                        "default": "true"
                    },
                    "shape_gr_dict": {
                        "description": "If group shape should be read from custom dictionary",
                        "type": "boolean",
                        "default": "false"
                    },
                    "shape_fixed": {
                        "description": "If a single fixed shape should be used for all markers",
                        "type": "boolean",
                        "default": "false"
                    },
                    "opacity_check": {
                        "description": "If markers should get their opacities from data in CSV column",
                        "type": "boolean",
                        "default": "false"
                    },
                    "_no_outline": {
                        "description": "If marker shapes should be rendered without outline",
                        "type": "boolean",
                        "default": "false"
                    }
                },
                "required": []
            },
            "Setting": {
                "description": "[Add description]. Required properties are shown in **bold** text.",
                "type": "object",
                "properties": {
                    "function": {
                    "type": "string"
                    },
                    "module": {
                    "type": "string"
                    },
                    "value": {
                    "type": "number"
                    }
                },
                "required": [
                    "function",
                    "module",
                    "value"
                ]
            }
        },
        "required": [
            "filename"
        ]
    }

~~~~~~~~~~~~~~~~~~~~~~~~
Example of a .tmap file
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "filename": "TissUUmaps_Example.tmap",
        "layers": [
            {
                "name": "Round1_A.tif",
                "tileSource": "images/Round1_A.tif.dzi"
            },
            {
                "name": "Round1_C.tif",
                "tileSource": "images/Round1_C.tif.dzi"
            }
        ],
        "layerOpacities": {
            "0": "1",
            "1": "1"
        },
        "layerVisibilities": {
            "0": true,
            "1": false,
        },
        "layerFilters": {
            "0": [
                {
                    "name": "Color",
                    "value": "0,100,0"
                }
            ],
            "1": [
                {
                    "name": "Color",
                    "value": "0,100,0"
                }
            ]
        },
        "filters": [
            "Color"
        ],
        "compositeMode": "lighter",
        "markerFiles": [
            {
                "autoLoad": false,
                "comment": "",
                "expectedHeader": {
                    "X": "global_x",
                    "Y": "global_y",
                    "cb_cmap": "",
                    "cb_col": "null",
                    "cb_gr_dict": "",
                    "gb_col": "Gene",
                    "gb_name": "",
                    "opacity": "1",
                    "opacity_col": "null",
                    "pie_col": "null",
                    "pie_dict": "",
                    "scale_col": "null",
                    "scale_factor": "0.5",
                    "shape_col": "null",
                    "shape_fixed": "cross",
                    "shape_gr_dict": "",
                    "tooltip_fmt": ""
                },
                "expectedRadios": {
                    "cb_col": false,
                    "cb_gr": true,
                    "cb_gr_dict": false,
                    "cb_gr_key": true,
                    "cb_gr_rand": false,
                    "pie_check": false,
                    "scale_check": false,
                    "shape_col": false,
                    "shape_fixed": false,
                    "shape_gr": true,
                    "shape_gr_dict": false,
                    "shape_gr_rand": true,
                    "opacity_check": false
                },
                "name": " markers",
                "path": "./istdeco_codes_n.csv",
                "title": "Download markers",
                "uid": "uniquetab"
            }
        ],
        "regions": {},
        "plugins": [
            "Spot_Inspector"
        ],
        "hideTabs": true,
        "settings": []
    }
