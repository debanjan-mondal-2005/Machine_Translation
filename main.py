from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from eng_tam_model import eng_tam
from eng_spa_model import eng_spa
from eng_fre_model import eng_fre

app = FastAPI(title="Language Translator API")

app.mount("/static", StaticFiles(directory="static"), name="static")


class TranslateRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.post("/translate")
def translate(req: TranslateRequest):
    text = req.text.strip()
    src = req.source_lang
    tgt = req.target_lang

    if not text:
        return {"error": "Input text is empty."}

    pair = (src, tgt)
    try:
        if pair == ("English", "Tamil"):
            inp, out = eng_tam(text)
        elif pair == ("English", "Spanish"):
            inp, out = eng_spa(text)
        elif pair == ("English", "French"):
            inp, out = eng_fre(text)
        else:
            return {"error": f"Translation from {src} to {tgt} is not supported. Only English → Tamil / Spanish / French is available."}
    except Exception as e:
        return {"error": str(e)}

    return {"input": inp, "translation": out, "source": src, "target": tgt}

