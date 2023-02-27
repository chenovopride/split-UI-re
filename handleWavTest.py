'''
pred for denoiser
'''
import torch
import denoiser.demucs 
# import hydra
from denoiser.demucs import Demucs
# import torch.onnx 
import librosa
import os
# import torch
import torchaudio
import numpy as np


model_path = "model_c2_dep4_db18.pth"

def get_estimate(model, noisy):
    with torch.no_grad():
        estimate = model(noisy)
        # estimate = (1 - args.dry) * estimate + args.dry * noisy
    return estimate


        
def save_wav(estimate, music_path, sr):
    file_path = music_path[0:-4]+'_eff.wav'
    write(estimate, file_path, sr = sr)


def write(wav, filename, sr=16_000):
    # Normalize audio if it prevents clipping
    wav = wav / max(wav.abs().max().item(), 1)
    wav = wav[0] # 在这里把第一维的1去掉，变成(2,len)
    torchaudio.save(filename, wav.cpu(), sr)
    # mus_path = filename
    # sf.write(mus_path, y_eff.T, 44100, subtype='PCM_16')
    
def splitwavAI(music_path):
    device = torch.device("cpu")
    model =Demucs(sample_rate=44100,hidden=64,chin=2,chout=2,depth=4)
    PATH = model_path
    # PATH = "model_c2epo100.pth"
    model.load_state_dict(torch.load(PATH, map_location='cpu'))
    model.eval()
    
    y, sr = librosa.load(music_path,sr=44100, mono=False)
    y_1 = np.expand_dims(y, axis=0)
    y_1 = torch.from_numpy(y_1)
    estimate = get_estimate(model, y_1)
    print(estimate.shape)
    save_wav(estimate, music_path, sr=44100)
    # save_wavs(estimate,  filenames, out_dir, sr=model.sample_rate)
    

# splitwavAI('/root/metalSlug.mp4')

    
