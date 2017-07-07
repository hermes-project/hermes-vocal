import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

print ("Model path : "+model_path)

speech = LiveSpeech(
	verbose=True,
	sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'fr-fr'),
    lm=os.path.join(model_path, 'fr-small.lm'),
    dic=os.path.join(model_path, 'fr.dict')
)

for phrase in speech:
    print(phrase)

#from pocketsphinx import LiveSpeech

#hmdir = "/usr/share/pocketsphinx/model/fr/fr"
#lmd = "/usr/share/pocketsphinx/model/fr/fr-small.lm"
#dictd = "/usr/share/pocketsphinx/model/fr/fr.dict"

#for phrase in LiveSpeech(): print(phrase)
