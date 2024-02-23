import os
from openai import OpenAI
import base64
import requests
from openai import OpenAI

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()

def save_text_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)


def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
    
image_path = "screenshot.png"

base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describe the image by extracting the SAP form elements, their roles, type of data inside and any additional information. If form contains any data inside inputs, treat it as confidential and do not include it in the description. Guess types of input and expected data inside."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 600
}

vision_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

vision_description = vision_response.json()['choices'][0]['message']['content']

save_text_to_file(vision_description, "vision_description.txt")

print('vision data has been extracted')

functional_specs_response = client.chat.completions.create(
      model="gpt-4-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "You're business analyst and you're working on a project to create a functional specification document for a new SAP form. Based on given output, write a functional specification document for the SAP form."
        },
        {
            "role": "user",
            "content": vision_description
        }
    ],
)

functional_specs_description = functional_specs_response.choices[0].message.content

save_text_to_file(functional_specs_description, "functional_specs_description.txt")

print ('functional specs has been created')

testcases_response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "You're a QA engineer and you're working on a project to create test cases for the SAP form. Based on given input, write test cases for the SAP form. Each test case should include test case ID, test case description, steps, expected result"
            },
            {
                "role": "user",
                "content": functional_specs_description
            }
        ],
    )

testcases_description = testcases_response.choices[0].message.content

save_text_to_file(testcases_description, "testcases_description.txt")


print(testcases_description)