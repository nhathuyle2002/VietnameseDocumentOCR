install libraries and download pretrained models:
  install.sh

run api:
  PS: uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
  link api:
    http://127.0.0.1:8000/docs
