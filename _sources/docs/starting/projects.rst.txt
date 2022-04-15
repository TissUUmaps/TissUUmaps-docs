************
Projects
************

==============================
Saving and loading projects
==============================



======================
The tmap file format
======================


The tmap format contains image layers, saved markers, regions, and settings. It is highly recommended to create tmap files by saving projects from TissUUmaps applications, but you can also edit the files manually to add or change project's settings.

The tmap format uses json, with the following specifications:

.. jsonschema::
    :lift_definitions:
    :auto_reference:
    :auto_target:

    {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Tmap specifications",
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
                ]
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
                "type": "array",
                "items": [
                    { "$ref": "#definitions/Filter" }
                ]
            },
            "compositeMode": {
                "type": "string"
            },
            "markerFiles": { 
                "type": "array",
                "items": [
                    {
                    "$ref": "#/definitions/MarkerFile"
                    }
                ]
            },
            "regions": {
                "type": "object",
                "description": "GeoJSON object, see :ref:`Regions section<regions>`."
            },
            "regionFile": {
                "type": "string"
            },
            "regionFiles": {
                "type": "array",
                "items": {}
            },
            "plugins": {
                "type": "array",
                "items": [
                    {
                    "type": "string"
                    }
                ]
            },
            "hideTabs": {
                "description": "Hide tabs of markers dataset. Only use when you have a unique marker tab.",
                "type": "boolean"
            },
            "settings": { 
                "type": "array",
                "items": [
                    {
                    "$ref": "#/definitions/Setting"
                    }
                ]
            }
        },
        "definitions": {
            "Layer": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "tileSource": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "tileSource"
                ]
            },
            "LayerFilter": {
                "type": "array",
                "items": [
                    {
                    "type": "object",
                    "properties": {
                        "name": { "$ref": "#definitions/Filter" },
                        "value": {
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
                "enum": ["Color","Brightness", "Exposure", "Hue", 
                        "Contrast", "Vibrance", "Noise", 
                        "Saturation","Gamma","Invert","Greyscale",
                        "Threshold","Erosion","Dilation"]
            },
            "ColorScale": {
                "description": "TissUUmaps supports most of the color scales available in the D3.js library. See https://github.com/d3/d3-scale-chromatic for reference. Note: the colors for 'interpolatRainbow' is currently overridden by a custom Turbo-like color scale in version 3.0.x of TissUUmaps.",
                "enum": ["interpolateCubehelixDefault", "interpolateRainbow", "interpolateWarm", "interpolateCool", "interpolateViridis", "interpolateMagma", "interpolateInferno", "interpolatePlasma", "interpolateBlues", "interpolateBrBG", "interpolateBuGn", "interpolateBuPu", "interpolateCividis", "interpolateGnBu", "interpolateGreens", "interpolateGreys", "interpolateOrRd", "interpolateOranges", "interpolatePRGn", "interpolatePiYG", "interpolatePuBu", "interpolatePuBuGn", "interpolatePuOr", "interpolatePuRd", "interpolatePurples", "interpolateRdBu", "interpolateRdGy", "interpolateRdPu", "interpolateRdYlBu", "interpolateRdYlGn", "interpolateReds", "interpolateSinebow", "interpolateSpectral", "interpolateTurbo", "interpolateYlGn", "interpolateYlGnBu", "interpolateYlOrBr", "interpolateYlOrRd"]
            },
            "MarkerFile": {
                "description": "Description of settings and GUI objects for a marker dataset loaded from CSV file",
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
                        "description": "If the CSV file for the marker dataset should be automatically loaded when the TMAP project is opened. If this is false, the user has to instead click on the marker button to load the dataset.",
                        "type": "boolean",
                        "default": "false"
                    },
                    "uid": {
                        "description": "A unique identifier used internally for the marker dataset",
                        "type": "string"
                    },
                    "expectedHeader": {
                        "$ref": "#definitions/ExpectedHeader"
                    },
                    "expectedRadios": {
                        "$ref": "#definitions/ExpectedRadios"
                    },
                    "path": {
                        "description": "Relative file path to CSV file for marker dataset",
                        "type": "string"
                    },
                    "settings": {
                        "type": "array",
                        "items": [
                            {
                            "$ref": "#/definitions/Setting"
                            }
                        ]
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
                "description": "Input field values for settings in a marker tab",
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
                        "description": "JSON string specifying a custom dictionary for group colors",
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
                        "description": "TODO",
                        "type": "string",
                        "default": ""
                    },
                    "shape_col": {
                        "description": "Name of CSV column containing a name or an index for marker shape",
                        "type": "string",
                        "default": "null"
                    },
                    "shape_fixed": {
                        "description": "Name of a single fixed shape to be used for all markers",
                        "type": "string",
                        "default": "cross"
                    },
                    "shape_gr_dict": {
                        "description": "JSON string specifying a custom dictionary for group shapes",
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
                        "description": "Custom formatting string used for overlay displayed over selected markers; see (TODO).",
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
                "description": "Radio button state and checkbox state for settings in a marker tab",
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
                "description": "TODO",
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
        ]
    }

~~~~~~~~~~~~~~~~~~~~~~~~
Example of tmap file
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
