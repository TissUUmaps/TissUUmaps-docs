************************
The TMAP file format
************************

The TMAP format contains a description of image layers, markers, regions, and settings. It is highly recommended to create .tmap files by saving projects from TissUUmaps, but you can also edit the files manually to add or change projects' settings, or generate them as exported data from other software for import in TissUUmaps.

For more information on the TMAPS format, see the `TissUUmaps-schema github page <https://github.com/TissUUmaps/TissUUmaps-schema>`_.

The TMAP format uses JSON, with the following specifications:

.. jsonschema:: https://tissuumaps.github.io/TissUUmaps-schema/1/project.json
    :lift_definitions:
    :auto_reference:
    :auto_target:
    
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
