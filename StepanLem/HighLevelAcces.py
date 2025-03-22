import whisper

model = whisper.load_model("turbo")
result = model.transcribe("StepanLem/lfs/TestVideo.mp4")
print(result["text"])
