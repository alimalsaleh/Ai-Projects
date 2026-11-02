import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification

current_dir = Path(__file__).resolve().parent
model_dir = current_dir / "readability-model"

print("جاري تحميل الموديل...")

tokenizer = AutoTokenizer.from_pretrained(
    str(model_dir),
    local_files_only=True
)

model = AutoModelForSequenceClassification.from_pretrained(
    str(model_dir),
    local_files_only=True
)

print("تم تحميل الموديل بنجاح!")

sentences = [
    "الشمس مشرقة اليوم. ذهب الطفل إلى المدرسة ولعب مع أصدقائه.",
    "تُسهم التحولات التكنولوجية المتسارعة في إعادة تشكيل البُنى المعرفية والاجتماعية للمجتمعات المعاصرة."
]

levels = []

for sentence in sentences:
    inputs = tokenizer(
        sentence,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=-1).item() + 1
    levels.append(pred)

doc_level = max(levels)

# حفظ النتيجة في ملف output.txt
output_path = current_dir / "readability-ab-output.txt"

result = f"Document readability level: {doc_level}"

output_path.write_text(result, encoding="utf-8")

print("تم حفظ النتيجة في output.txt بنجاح!")
print(result)