from transformers import pipeline

# Load summarization model only once
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)
print("✅ Model Loaded Successfully!")

from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

print("✅ Model Loaded Successfully!")

text = """
Artificial Intelligence is transforming healthcare by helping doctors diagnose diseases,
predict patient outcomes, and improve medical treatments.
"""

summary = summarizer(
    text,
    max_length=40,
    min_length=15,
    do_sample=False
)

print("\nSummary:")
print(summary[0]["summary_text"])