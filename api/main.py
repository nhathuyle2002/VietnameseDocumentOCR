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
    print(link_sound)

    return{'link': link_sound}



# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import FileResponse
# from Vbee import soundlink_end2end
# import ocr_end2end
# #import wget

# #host_link = '127.0.0.1:8000'
# app = FastAPI()

# @app.post('/convert_img_to_sound/')
# async def convert_img_to_sound(file: UploadFile = File(...)):
#     content = file.file.read()
#     name = file.filename.split('.')[0]

#     file_location = f"files/images/{name}.jpg"
#     with open(file_location, "wb+") as file:
#         file.write(content)

#     texts = ocr_end2end.img_to_txt(file_location)
#     print(type(texts))
#     print(texts)
#     with open(f"files/texts/{name}.txt", "w", encoding="utf-8") as file:
#         file.write(texts)

#     print('converting text to sound')
#     link_sound = soundlink_end2end.txt_to_wav(texts)
#     print(link_sound)
#     if link_sound == False:
#         return {'Error': 'Can not get direct link from Vbee!'}
#     with open(f"files/links/{name}.txt", "w") as file:
#         file.write(link_sound)

#     return{'link_wav': link_sound}

# @app.post('/convert_txt_to_sound/')
# async def convert_img_to_sound(file: UploadFile = File(...)):
#     texts = file.file.read().decode("utf-8")
#     print(texts)
#     name = file.filename.split('.')[0]
#     link_sound = soundlink_end2end.txt_to_wav(texts)
#     print(link_sound)
#     if link_sound == False:
#         return {'Error': 'Can not get direct link from Vbee!'}
#     with open(f"files/links/{name}.txt", "w") as file:
#         file.write(link_sound)
#     return{'link_wav': link_sound}

# # @app.post('/convert_img_to_sound/')
# # async def convert_img_to_sound(file: UploadFile = File(...)):
# #     content = file.file.read()
# #     name = file.filename.split('.')[0]

# #     file_location = f"files/images/{name}.jpg"
# #     with open(file_location, "wb+") as file:
# #         file.write(content)

# #     texts = ocr_end2end.img_to_txt(file_location)
# #     print(type(texts))
# #     print(texts)
# #     with open(f"files/texts/{name}.txt", "w", encoding="utf-8") as file:
# #         file.write(texts)

# #     print('converting text to sound')
# #     link_sound = soundlink_end2end.txt_to_wav(texts)
# #     print(link_sound)
# #     if link_sound == False:
# #         return {'Error': 'Can not get direct link from Vbee!'}
# #     with open(f"files/links/{name}.txt", "w") as file:
# #         file.write(link_sound)

# #     wget.download(link_sound, f"files/sounds/{name}.wav")
# #     await response_sound(f"{name}.wav")
# #     return{'link_wav': f"http://{host_link}/files/sounds/"}

# # @app.post('/convert_img_to_text/')
# # async def convert_img_to_text(file: UploadFile = File(...)):
# #     content = file.file.read()
# #     name = file.filename.split('.')[0]

# #     file_location = f"files/images/{name}.jpg"
# #     with open(file_location, "wb+") as file:
# #         file.write(content)

# #     texts = ocr_end2end.img_to_txt(file_location)
# #     print(type(texts))
# #     print(texts)
# #     with open(f"files/texts/response_text.txt", "w", encoding="utf-8") as file:
# #         file.write(texts)

# #     await response_text(f"{name}.txt")
# #     return{'link_txt': f"http://{host_link}/files/texts/"}

# # @app.get('/files/texts/')
# # async def response_text(filename = 'response_text.txt'):
# #     return FileResponse(f'files/texts/{filename}')

# # @app.get('/files/sounds/')
# # async def response_sound(filename = 'response_sound.wav'):
# #     return FileResponse(f'files/sounds/{filename}')