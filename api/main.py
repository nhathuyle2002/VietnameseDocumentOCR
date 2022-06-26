from fastapi import FastAPI, UploadFile, File
from Vbee import soundlink_end2end
import ocr_end2end

app = FastAPI()
@app.post('/ocr/')
async def perform_ocr(file: UploadFile = File(...)):
    content = file.file.read()
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(content)

    texts = ocr_end2end.img_to_txt(file_location)
    link_sound = soundlink_end2end.txt_to_wav(texts)
    #link_sound = texts
    print(link_sound)

    return{'link': link_sound}
