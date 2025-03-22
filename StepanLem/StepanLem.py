import whisper

model = whisper.load_model("turbo")
result = model.transcribe("TestVideo.mp4")
print(result["text"])