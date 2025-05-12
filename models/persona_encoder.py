from sentence_transformers import SentenceTransformer
import torch

class PersonaEncoder:
    def __init__(self):
        self.encoder = SentenceTransformer('all-mpnet-base-v2')
        self.history = []

    def encode_static(self, persona_dict):
        text = " ".join([f"{k}: {v}" for k, v in persona_dict.items()])
        return self.encoder.encode(text)

    def update_dynamic(self, statement):
        self.history.append(statement)

    def get_dynamic_embedding(self):
        return self.encoder.encode(" ".join(self.history[-5:]))

