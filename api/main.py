from fastapi import FastAPI
from pydantic import BaseModel
import torch
import fasttext
from model import POSTagger
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


ft = fasttext.load_model('model/cc.az.300.bin')


EMBEDDING_DIM = 300  # FastText embedding size
HIDDEN_DIM = 256

tag_to_ix = {'bağlayıcı': 0,
 'durğu işarəsi': 1,
 'zərf': 2,
 'say': 3,
 'isim': 4,
 'qoşma': 5,
 'əvəzlik': 6,
 'sifət': 7,
 'modal': 8,
 'fel': 9,
 'ədat': 10,
 'nida': 11}

def load_model():
    model = POSTagger(EMBEDDING_DIM, HIDDEN_DIM, len(tag_to_ix))  # Recreate the model
    model.load_state_dict(torch.load('model/pos_tagger_model.pth'))
    model.eval()  # Set the model to evaluation mode
    return model

model = load_model()

def sentence_to_embedding(sentence, fasttext_model):
    embeddings = [fasttext_model.get_word_vector(word) for word in sentence]
    return torch.tensor(embeddings, dtype=torch.float)



def predict_tags(sentence, model):
    with torch.no_grad():
        test_sentence = sentence.split()
        test_embeddings = sentence_to_embedding(test_sentence, ft)
        tag_scores = model(test_embeddings)
        predicted_tags = [list(tag_to_ix.keys())[tag_scores[i].argmax().item()] for i in range(len(test_sentence))]
    return predicted_tags


class Sentence(BaseModel):
    text: str

@app.post("/tag/")
def tag_sentence(sentence: Sentence):
    tags = predict_tags(sentence.text, model)
    return {"sentence": sentence.text, "tags": tags}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)