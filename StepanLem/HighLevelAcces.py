import whisper
import time

start_time = time.time()

model = whisper.load_model("turbo")
result = model.transcribe("StepanLem/lfs/TestVideo.mp4")
print(result["text"])

print("--- %s seconds ---" % (time.time() - start_time))
