from openai import OpenAI
import json, pathlib

client = OpenAI()
resume_text = pathlib.Path("resume.md").read_text()

prompt = f"""
Analyze this resume for ATS readiness.
Return ONLY valid JSON with:
- word_count
- ats_score (0-100)
- keywords
- missing_sections
- readability_level
"""

response = client.responses.create(
    model="gpt-4.1",
    input=prompt
)

analysis = json.loads(response.output_text)
pathlib.Path("analysis.json").write_text(json.dumps(analysis, indent=2))

print("Resume analysis completed")
