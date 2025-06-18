import whisper

model = whisper.load_model("medium")
result = model.transcribe("teste.webm", language='pt', word_timestamps=True)
print(result["text"])
