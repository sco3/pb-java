import json

def flatten_json(json_obj, parent_key='', separator='.'):
    items = []
    
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_key = parent_key + separator + key if parent_key else key
            if isinstance(value, (dict, list)):
                items.extend(flatten_json(value, new_key, separator).items())
            else:
                items.append((new_key, value))
    elif isinstance(json_obj, list):
        # Collect sibling key-value pairs for simple types
        simple_siblings = {parent_key + separator + str(i): value for i, value in enumerate(json_obj) if not isinstance(value, (dict, list))}
        
        for i, value in enumerate(json_obj):
            new_key = parent_key + separator + str(i) if parent_key else str(i)
            if isinstance(value, (dict, list)):
                nested_items = flatten_json(value, new_key, separator).items()
                # Append simple sibling key-value pairs to each nested item
                for k, v in nested_items:
                    sibling_items = " ".join([f"{sk}={sv}" for sk, sv in simple_siblings.items()])
                    if sibling_items:
                        items.append((k + " " + sibling_items, v))
                    else:
                        items.append((k, v))
            else:
                items.append((new_key, value))
    return dict(items)

def json_to_properties(json_data):
    flat_json = flatten_json(json_data)
    properties = []
    for key, value in flat_json.items():
        properties.append(key + "=" + str(value))
    return properties

# Example usage
json_data = """
{
  "devices": [
    {
      "id": "device001",
      "type": "sensor",
      "location": "Living Room",
      "status": "active",
      "actions": [
        {
          "action": "temperature_read",
          "timestamp": "2024-06-06T12:00:00Z",
          "value": 22.5,
          "unit": "Celsius"
        },
        {
          "action": "humidity_read",
          "timestamp": "2024-06-06T12:05:00Z",
          "value": 45,
          "unit": "%"
        },
        {
          "action": "play_music",
          "timestamp": "2024-06-06T13:00:00Z",
          "song": "Imagine",
          "artist": "John Lennon"
        }
      ]
    },
    {
      "id": "device002",
      "type": "camera",
      "location": "Front Door",
      "status": "inactive",
      "actions": [
        {
          "action": "motion_detected",
          "timestamp": "2024-06-06T08:15:00Z",
          "value": true,
          "confidence": 0.9
        },
        {
          "action": "image_capture",
          "timestamp": "2024-06-06T08:15:05Z",
          "image_url": "http://example.com/image1.jpg"
        },
        {
          "action": "measure_temperature",
          "timestamp": "2024-06-06T09:00:00Z",
          "value": 25,
          "unit": "Celsius"
        }
      ]
    },
    {
      "id": "device003",
      "type": "light",
      "location": "Kitchen",
      "status": "active",
      "actions": [
        {
          "action": "turn_on",
          "timestamp": "2024-06-06T07:00:00Z",
          "duration": 3600,
          "unit": "seconds"
        },
        {
          "action": "turn_off",
          "timestamp": "2024-06-06T08:00:00Z"
        },
        {
          "action": "capture_image",
          "timestamp": "2024-06-06T08:30:00Z",
          "image_url": "http://example.com/image2.jpg"
        }
      ]
    }
  ]
}
"""

data = json.loads(json_data)
properties = json_to_properties(data)

# Print properties to simulate writing to a .properties file
for prop in properties:
    print(prop)

# If you want to write to a file, uncomment the following lines:
# with open('output.properties', 'w') as f:
#     for prop in properties:
#         f.write(prop + "\n")
