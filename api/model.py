import torch
import torch.nn as nn
import torch.optim as optim

class POSTagger(nn.Module):
    def __init__(self, embedding_dim, hidden_dim, tagset_size):
        super(POSTagger, self).__init__()
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

    def forward(self, sentence_embeddings):
        lstm_out, _ = self.lstm(sentence_embeddings.view(len(sentence_embeddings), 1, -1))
        tag_space = self.hidden2tag(lstm_out.view(len(sentence_embeddings), -1))
        tag_scores = torch.log_softmax(tag_space, dim=1)
        return tag_scores