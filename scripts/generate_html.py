from openai import OpenAI
import pathlib

client = OpenAI()

resume_text = pathlib.Path("resume.md").read_text()

prompt = f"""
Convert the following resume into a clean, professional,
ATS-optimized HTML resume website.
Use semantic HTML and clear section headers.

Resume:
{resume_text}
"""

response = client.responses.create(
    model="gpt-4.1",
    input=prompt
)

html = response.output_text
pathlib.Path("index.html").write_text(html)

print("HTML resume generated")
