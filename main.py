from fastapi import FastAPI
import googletrans as g

app = FastAPI()
translator = g.Translator()

@app.get("/translate/{text_to_translate}/{lang_to_translate}")
def op(text_to_translate, lang_to_translate):
    detector = translator.detect(lang_to_translate)
    return {f"  Text that To translate:  '{text_to_translate}'  " : f"  The translationed text:  '{str(translator.translate(text_to_translate, dest=str(detector.lang)).text)}'  "}
