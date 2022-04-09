************
Projects
************

==============================
Saving and loading projects
==============================



======================
The tmap file format
======================

..
   One idea is to use https://sphinx-jsonschema.readthedocs.io/en/latest/directive.html
   to document the tmap format 

    .. jsonschema::
        :lift_definitions:
        :auto_reference:
        :auto_target:

        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title":  "Example of Target & Reference",
            "type": "object",
            "properties": {
                "person": { "$ref": "#/definitions/person" }
            },
            "definitions": {
                "person": {
                    "type": "object",
                    "properties": {
                        "name": { "type": "string" },
                        "children": {
                            "type": "array",
                            "items": { "$ref": "#/definitions/person" },
                            "default": []
                        }
                    }
                }
            }
        }
