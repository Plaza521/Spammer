ui_schema = {
    "type": "object",
    "properties":
    {
        "MainSettings":
        {
            "type": "object",
            "properties":
            {
                "title": {"type": "string"},
                "width": {"type": "number"},
                "height": {"type": "number"},
            },
            "required": ["title", "width", "height"]
        },
        "Elements":
        {
            "type": "object",
            "patternProperties":
            {
                "(.*)":
                {
                    "type": "object",
                    "properties":
                    {
                        "type": {"type": "string"},
                        "param": {"type": "object"},
                        "place": {"type": "object"}
                    },
                    "required": ["type", "param", "place"]
                }
            }
        }
    },
    "required": ["MainSettings", "Elements"]
}
