import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification

current_dir = Path(__file__).resolve().parent
model_dir = current_dir / "readabert-en"

print("Loading Readabert model...")

tokenizer = AutoTokenizer.from_pretrained(
    str(model_dir),
    local_files_only=True
)

model = AutoModelForSequenceClassification.from_pretrained(
    str(model_dir),
    local_files_only=True
)

print("Model loaded successfully!")

# Convert model labels to CEFR levels
cefr_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]

sentences = [
    # A1
    "I have a small dog.",

    # A2
    "Last weekend, I visited my friend and we watched a movie.",

    # B1
    "Although I was tired, I decided to finish my homework before going to bed.",

    # B2
    "Many people believe that technology has improved communication, but it has also reduced face-to-face interaction.",

    # C1
    "Despite the significant benefits of globalization, its economic consequences remain unevenly distributed across different societies.",

    # C2
    "The pervasive influence of technological innovation necessitates a nuanced examination of its implications for individual autonomy, institutional accountability, and societal cohesion."
]

results = []

for sentence in sentences:
    inputs = tokenizer(
        sentence,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=-1)
    pred = torch.argmax(probabilities, dim=-1).item()
    confidence = probabilities[0][pred].item()

    label = cefr_levels[pred]

    results.append(
        f"Sentence: {sentence}\n"
        f"Readability level: {label}\n"
        f"Confidence: {confidence:.4f}\n"
        f"{'-' * 40}\n"
    )

output_file = current_dir / "readabert-en-output.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write("Readabert Results\n\n")
    file.writelines(results)

print(f"Results saved to: {output_file}")