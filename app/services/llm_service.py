class LLMService:
    def summarize(self, text: str):
        return f"Summary of file: {text[:200]}"