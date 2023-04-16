from fastapi import FastAPI
from pyllamacpp.model import Model

app = FastAPI()

# loading model
model = Model(ggml_model='./gpt4all-converted.bin', n_ctx=512)


@app.post("/api/predict")
async def predict(payload: dict):
    prompt = payload["prompt"]
    temperature = payload["temperature"]
    top_p = payload["top_p"]
    top_k = payload["top_k"]
    num_beams = payload["num_beams"]
    # print(prompt, temperature, top_p, top_k, num_beams)
    generated_text = model.generate(prompt=prompt, n_predict=100, temp=temperature, top_k=top_k, top_p=top_p)
    # print(generated_text)
    # prediction = gpt4all.generate_text(prompt, temperature=temperature, top_p=top_p, top_k=top_k, num_beams=num_beams)

    return {"prediction": generated_text}
