from typing import Optional, Dict, Any
from pydantic import BaseModel
import fireworks.client
import base64

"""
JUSTIFICATIONS
1. This is a MVP that demonstrates the ability to extract information from an image
2. Used LLAMA 90B as it has the highest ranking on MMMU leaderboard and accuracy should be important
  for this task, hence higher cost per million token is justified. Further more, information extraction
  is not done frequently, likely once per potential customer, so cost is not a major concern.
3. Output is in JSON format, which is easy to parse and use in other applications.
4. Essential information such as name and DOB are extracted, and additional information can be added.
5. Misidentification is an issue, did not fine-tune the model as there is not enough data to do so.
6. Played around with some of the parameters (temperature, n), but did not find any significant improvements.
"""

# Helper function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Schema for the result
class Result(BaseModel):
    full_name: str
    first_name: str
    last_name: str
    date_of_birth: str
    date_of_issue: str
    date_of_expiry: str
    address: str
    id_number: str
    additional_info: Optional[Dict[str, Any]] = None  # New optional generic dictionary

# The path to your image
image_path = "Identity_Documents/License 1.png"

# The base64 string of the image
image_base64 = encode_image(image_path)

fireworks.client.api_key = "fw_3Zgituv8HotQiPTbjeeQW7nV"

response = fireworks.client.ChatCompletion.create(
  model = "accounts/fireworks/models/llama-v3p2-90b-vision-instruct",
  messages = [{
    "role": "user",
    "content": [{
      "type": "text",
      "text": "Extract information from this image. Output in JSON format.",
    }, {
      "type": "image_url",
      "image_url": {
        "url": f"data:image/png;base64,{image_base64}"
      },
    }, ],
  }],
  response_format={"type": "json_object", "schema": Result.model_json_schema()},
  temperature=1,
  n=1,
)
print(response)
