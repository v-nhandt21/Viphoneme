import re
symbols =['ɯəj', 'ɤ̆j', 'ʷiə', 'ɤ̆w', 'ɯəw', 'ʷet', 'iəw', 'uəj', 'ʷen', 'tʰw', 'ʷɤ̆', 'ʷiu', 'kwi', 'ŋ͡m', 'k͡p', 'cw', 'jw', 'uə', 'eə', 'bw', 'oj', 'ʷi', 'vw', 'ăw', 'ʈw', 'ʂw', 'aʊ', 'fw', 'ɛu', 'tʰ', 'tʃ', 'ɔɪ', 'xw', 'ʷɤ', 'ɤ̆', 'ŋw', 'ʊə', 'zi', 'ʷă', 'dw', 'eɪ', 'aɪ', 'ew', 'iə', 'ɣw', 'zw', 'ɯj', 'ʷɛ', 'ɯw', 'ɤj', 'ɔ:', 'əʊ', 'ʷa', 'mw', 'ɑ:', 'hw', 'ɔj', 'uj', 'lw', 'ɪə', 'ăj', 'u:', 'aw', 'ɛj', 'iw', 'aj', 'ɜ:', 'kw', 'nw', 't∫', 'ɲw', 'eo', 'sw', 'tw', 'ʐw', 'iɛ', 'ʷe', 'i:', 'ɯə', 'dʒ', 'ɲ', 'θ', 'ʌ', 'l', 'w', '1', 'ɪ', 'ɯ', 'd', '∫', 'p', 'ə', 'u', 'o', '3', 'ɣ', '!', 'ð', 'ʧ', '6', 'ʒ', 'ʐ', 'z', 'v', 'g', 'ă', '_', 'æ', 'ɤ', '2', 'ʤ', 'i', '.', 'ɒ', 'b', 'h', 'n', 'ʂ', 'ɔ', 'ɛ', 'k', 'm', '5', ' ', 'c', 'j', 'x', 'ʈ', ',', '4', 'ʊ', 's', 'ŋ', 'a', 'ʃ', '?', 'r', ':', 'η', 'f', ';', 'e', 't', "'"]
abortsym =["","[","]","/"]
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}
from viphoneme import syms, vi2IPA_split

def text_to_sequence(text,delimit):
    text=re.sub(re.compile(r'\s+'), ' ', text)
    text=text.rstrip(".").rstrip("?").rstrip("!").rstrip(" ")
    ipa = vi2IPA_split(text,delimit)
    print("Phoneme: ",ipa)
    #*****************************************8Xử lí vụ cuối câu phải có simple dot : chưa làm
    sequence = []
    phonemes =ipa.split(delimit)
    for pho in phonemes:
        if pho in _symbol_to_id and pho not in abortsym:
            sequence.append(_symbol_to_id[pho])
    return sequence
def sequence_to_text(sequence,delimit):
    result = ''
    for symbol_id in sequence:
        if symbol_id in _id_to_symbol:
            s = _id_to_symbol[symbol_id]
            result += delimit+s
    return result




print(text_to_sequence("tui yêu em từ thuở nào.", "/"))
print("-----------------------------------------------------")
#print(sequence_to_text(text_to_sequence("tui yêu em từ thuở nào.","/"),"/"))


#max_decoder_steps=2000,
#batch_size=32, ???
#drop_out =0.5, ???