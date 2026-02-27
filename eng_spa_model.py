import pickle
import dill
import sys
import tf_keras as keras
import tf_keras.preprocessing.text
import numpy as np
from pathlib import Path

class _KerasUnpickler(dill.Unpickler):
    def find_class(self, module, name):
        if 'keras.src.preprocessing' in module:
            module = module.replace('keras.src.preprocessing', 'tf_keras.preprocessing')
        elif module.startswith('keras.preprocessing'):
            module = module.replace('keras.preprocessing', 'tf_keras.preprocessing', 1)
        return super().find_class(module, name)

def _safe_load(path):
    with open(path, 'rb') as f:
        return _KerasUnpickler(f).load()

def pad_sequences(sequences, maxlen, padding='pre', value=0):
    result = np.full((len(sequences), maxlen), value, dtype='int32')
    for i, seq in enumerate(sequences):
        seq = seq[:maxlen]
        if padding == 'pre':
            result[i, maxlen - len(seq):] = seq
        else:
            result[i, :len(seq)] = seq
    return result

_MODELS = Path(__file__).parent / "Models"
encoder_model = keras.models.load_model(str(_MODELS / "en-spencoder.h5"))
decoder_model = keras.models.load_model(str(_MODELS / "en-spdecoder.h5"))
input_tokenizer = _safe_load(str(_MODELS / "en-spInputTokenizer.pkl"))
output_tokenizer = _safe_load(str(_MODELS / "en-spOutputTokenizer.pkl"))


max_input_len = 4       
word2idx_inputs = input_tokenizer.word_index
word2idx_outputs = output_tokenizer.word_index
max_out_len = 9
idx2word_input = {v:k for k, v in word2idx_inputs.items()}
idx2word_target = {v:k for k, v in word2idx_outputs.items()}

def eng_spa(input_val):
        def translate_sentence(input_seq):
                states_value = encoder_model.predict(input_seq)
                target_seq = np.zeros((1, 1))
                target_seq[0, 0] = word2idx_outputs['<sos>']
                eos = word2idx_outputs['<eos>']
                output_sentence = []

                for _ in range(max_out_len):
                        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
                        idx = np.argmax(output_tokens[0, 0, :])

                        if eos == idx:
                                break

                        word = ''

                        if idx > 0:
                                word = idx2word_target[idx]
                                output_sentence.append(word)

                                target_seq[0, 0] = idx
                                states_value = [h, c]

                return ' '.join(output_sentence)

        # Assume 'input_sentence' is the sentence you want to translate
        input_sentence = input_val

        # Tokenize and pad the input sentence
        input_sequence = input_tokenizer.texts_to_sequences([input_sentence])
        input_sequence_padded = pad_sequences(input_sequence, maxlen=max_input_len)

        # Translate the sentence
        translation = translate_sentence(input_sequence_padded)

        # Print the results
        print('Input:', input_sentence)
        print('Translation:', translation)
        return input_sentence,translation


