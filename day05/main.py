import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

contents1="Explain dependency injection."

contents2="Explain dependency injection to a Java developer."
contents3="""
Explain dependency injection to a Java developer.

The developer already understands interfaces
and Spring Boot.

Use one simple example.
Keep the explanation concise.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=contents1
)

print(response.text)