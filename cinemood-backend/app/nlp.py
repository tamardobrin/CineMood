# from openai import OpenAI
# from app.config import OPENAI_API_KEY

# client = OpenAI(api_key=OPENAI_API_KEY)

from transformers import pipeline
import re
import ast

def _extract_list_from_output(output: str) -> list[str]:
    """Private helper function to extract a list from model output."""
    matches = re.finditer(r"\[.*?\]", output, re.DOTALL)
    matches_list = list(matches)
    if matches_list:
        try:
            tags = ast.literal_eval(matches_list[-1].group(0))
            if isinstance(tags, list) and all(isinstance(tag, str) for tag in tags):
                return tags
        except Exception as e:
            print("Error parsing list:", e)
    return ["sad", "hopeful"]

def extract_mood_tags(text: str) -> list[str]:
    """
    Extract emotional and thematic keywords from the input text using a local language model.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        list[str]: A list of 2-4 emotional or thematic keywords
    """
    # Initialize the model only when the function is called
    model_name = "Qwen/Qwen2.5-3B-Instruct"
    generator = pipeline("text-generation", model=model_name, max_new_tokens=100, truncation=True)
    
    prompt = (
        f"The user is feeling sad and wrote: \"{text}\"\n"
        "Extract 2 to 4 simple emotional or thematic keywords that describe why they're feeling this way. "
        "Return ONLY a Python list of strings containing the keywords."
    )

    response = generator(prompt, num_return_sequences=1)
    raw_output = response[0]['generated_text']

    return _extract_list_from_output(raw_output)
