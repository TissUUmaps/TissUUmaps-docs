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
            "MarkerFile": {
                "description": "A button linked to a marker dataset",
                "type": "object",
                "properties": {
                    "title": {
                    "type": "string"
                    },
                    "comment": {
                    "type": "string"
                    },
                    "name": {
                    "type": "string"
                    },
                    "autoLoad": {
                    "type": "boolean"
                    },
                    "uid": {
                    "type": "string"
                    },
                    "expectedHeader": {
                        "description": "List of input text options",
                        "type": "object"
                    },
                    "expectedRadios": {
                        "description": "List of radio options",
                        "type": "object"
                    },
                    "path": {
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
            "Setting": {
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
                    "shape_gr_rand": true
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
