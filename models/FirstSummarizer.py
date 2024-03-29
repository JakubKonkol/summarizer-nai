from transformers import pipeline

class FirstSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn", max_length=110, min_length=8):
        self.summarizer = pipeline("summarization", model=model_name)
        self.max_length = max_length
        self.min_length = min_length

    def generate_summary(self, text):
        return self.summarizer(text, max_length=self.max_length, min_length=self.min_length)


