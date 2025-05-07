from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_mood_tags(text: str) -> list[str]:
    prompt = (
        f"The user is feeling sad and wrote: \"{text}\"\n"
        "Extract 2 to 4 simple emotional or thematic keywords that describe why they're feeling this way. "
        "Return the keywords as a Python list of strings. For example: ['heartbreak', 'loneliness', 'healing']"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    raw_output = response.choices[0].message.content

    try:
        tags = eval(raw_output)
        if isinstance(tags, list) and all(isinstance(tag, str) for tag in tags):
            return tags
    except Exception as e:
        print("Error parsing response from OpenAI:", e)
        print("Raw output was:", raw_output)

    return ["sad", "hopeful"]
