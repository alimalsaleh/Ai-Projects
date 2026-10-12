"""
سكريبت تحميل بيانات OneStopEnglish Corpus
"""

from datasets import load_dataset


def load_readability_data():
    """تحميل البيانات من Hugging Face"""
    print("📥 جارٍ تحميل البيانات...")
    dataset = load_dataset("agentlans/one-stop-english")
    print(f"\n✅ نصوص التدريب: {len(dataset['train'])}")
    return dataset


if __name__ == "__main__":
    dataset = load_readability_data()
    print(f"\n📊 مثال:")
    print(f"   {dataset['train'][0]['text'][:150]}...")
