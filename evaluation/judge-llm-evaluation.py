
openai_api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key


from openai import OpenAI
import base64
from PIL import Image
import io
import os
from pathlib import Path
import json
import pandas as pd
import ast

from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm



from PIL import Image
import io

def bytes_to_pil(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image

def pil_to_png(image_pil) :
    image_format = image_pil.format
    if image_format is None:
        image_format = 'PNG'  

    format_mime_types = {
        'JPEG': 'image/jpeg',
        'PNG': 'image/png',
        'GIF': 'image/gif',
        'BMP': 'image/bmp',
        'TIFF': 'image/tiff',
        'WEBP': 'image/webp',
    }
    mime_type = format_mime_types.get(image_format.upper(), 'application/octet-stream')

    buffer = io.BytesIO()
    image_pil.save(buffer, format=image_format)
    img_bytes = buffer.getvalue()

    img_b64 = base64.b64encode(img_bytes).decode('utf-8')

    img_data_url = f"data:{mime_type};base64,{img_b64}"
    return img_data_url



system_prompt = """
                You are a helpful Assistant. Provide helpful response to the user's question.
                """


client = OpenAI(
    api_key=openai_api_key  
)

def compare_results(question,ground_truth,llm_response,choices=None):
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"""




                                    Evaluate the following answer based on Accuracy:
                                    Question: {question}
                                    Ground Truth: {ground_truth}
                                    Model Prediction: {llm_response}
                                    Match the meaning of the ground truth with the model prediction and if it matches give a 1. Otherwise 0.
                                    Strictly return only the numeric score, without any additional commentary

                                         """},
            ],
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o",  
        messages=messages,
        max_tokens=10,
    )

    return response.choices[0].message.content



df = pd.read_csv(".../Evaluation/gpt-4.1-final-responses.csv")

print(df.head())



import pandas as pd
import ast
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def safe_str(x):
    return "" if pd.isna(x) else str(x)

def process_row(row):
    question = safe_str(row["question"])
    gt = safe_str(row["Ground Truth steps"])
    llm_response = safe_str(row["Response Answer"])

    # Call evaluate_steps WITHOUT choices
    res = (compare_results(question, gt, llm_response))

    row["Final Answer Score"] = res

    return row

# Run with thread-based concurrency
rows = [row for _, row in df.iterrows()]
with ThreadPoolExecutor() as executor:
    results = list(tqdm(executor.map(process_row, rows), total=len(rows)))


df = pd.DataFrame(results)
df.to_csv("gpt-4o-mini-final-answer-evaluation-results.csv")


df.tail()


df['Final Answer Score'] = df['Final Answer Score'].astype(float)


print(df['Final Answer Score'].mean())

