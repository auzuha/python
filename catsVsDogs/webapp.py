import torch 
from torchvision import models,transforms
import torch.nn as nn
import streamlit as st
import numpy as np
from PIL import Image
model = models.resnet18(pretrained=True)
model.fc = nn.Sequential(nn.Linear(model.fc.in_features , 1) , nn.Sigmoid())

model.load_state_dict(torch.load("catsvsdogsBCE_95_2",map_location=torch.device('cpu')))
model.eval()
img = st.file_uploader("Upload file.")

if img is not None:
    t = transforms.Compose([transforms.Resize(224),transforms.CenterCrop(200),transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5,)) ])

    img = Image.open(img)
    st.image(img,caption="You Uploaded:")
    img = t(img)
    img = torch.unsqueeze(img,0)
    prob = model(img)
    if prob > 0.5:
    	st.success(f"Predicted Dog with probability {prob.item():.4f}")
    else:
    	st.success(f"Predicted Cat with probability {1-prob.item():.4f}")