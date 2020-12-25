import prosodic as p
def getSymEnglish():
    PHO=[]
    with open("english.txt", encoding="utf-8") as f:
        content=f.read().splitlines()
        for line in content:
            x= p.Text(line)
            x.parse()
            PAR = x.bestParses()[0]
            PHO.extend(x.phonemes())
    print(PHO)
    PHO=set(PHO)
    return PHO

ENG_SYM=["ʧ", "f", "θ", "k", "uː", "h", "b", "v", "ɔ", "t", "ɛ", "p", "ŋ", "ð", "iː", "ʌ", "j", "ʒ", "w", "ʊ", "n", "s", "ɛː", "g", "l", "d", "r", "æ", "ɑ", "ʤ", "ɪ", "ɔː", "m", "z", "ə", "a", "o", "e", "ʃ", "i"]

ExceptReplaceSym=['uː', 'iː', 'ɑ', 'ɛː', 'zi', 'kwi', 'ɔː']

symbols =['ɯəj', 'ɤ̆j', 'ʷiə', 'ɤ̆w', 'ɯəw', 'ʷet', 'iəw', 'uəj', 'ʷen', 'tʰw', 'ʷɤ̆', 'ʷiu', 'kwi', 'ŋ͡m', 'k͡p', 'cw', 'jw', 'uə', 'eə', 'bw', 'oj', 'ʷi', 'vw', 'ăw', 'ʈw', 'ʂw', 'aʊ', 'fw', 'ɛu', 'tʰ', 'tʃ', 'ɔɪ', 'xw', 'ʷɤ', 'ɤ̆', 'ŋw', 'ʊə', 'zi', 'ʷă', 'dw', 'eɪ', 'aɪ', 'ew', 'iə', 'ɣw', 'zw', 'ɯj', 'ʷɛ', 'ɯw', 'ɤj', 'ɔ:', 'əʊ', 'ʷa', 'mw', 'ɑ:', 'hw', 'ɔj', 'uj', 'lw', 'ɪə', 'ăj', 'u:', 'aw', 'ɛj', 'iw', 'aj', 'ɜ:', 'kw', 'nw', 't∫', 'ɲw', 'eo', 'sw', 'tw', 'ʐw', 'iɛ', 'ʷe', 'i:', 'ɯə', 'dʒ', 'ɲ', 'θ', 'ʌ', 'l', 'w', '1', 'ɪ', 'ɯ', 'd', '∫', 'p', 'ə', 'u', 'o', '3', 'ɣ', '!', 'ð', 'ʧ', '6', 'ʒ', 'ʐ', 'z', 'v', 'g', 'ă', '_', 'æ', 'ɤ', '2', 'ʤ', 'i', '.', 'ɒ', 'b', 'h', 'n', 'ʂ', 'ɔ', 'ɛ', 'k', 'm', '5', ' ', 'c', 'j', 'x', 'ʈ', ',', '4', 'ʊ', 's', 'ŋ', 'a', 'ʃ', '?', 'r', ':', 'η', 'f', ';', 'e', 't', "'"]

def normEng (eng,delemit):
    x= p.Text(eng)
    x.parse()
    PAR = str(x.bestParses()[0]).split("|")
    SYL = x.syllables()
    if len(PAR) != len(SYL):
        print("check dif len: ", eng)
    result=""
    for i,syl in enumerate(SYL):
        syllable = str(syl).replace("'","").replace("ː","").replace("ɑ","a")
        if PAR[i].lower().upper() == PAR[i]:
            result+=syllable+"'5"+" "
        else:
            result+=syllable+"'1"+" "
    result=result.rstrip(" ")
    if delemit !="":
        takemore=""
        for r in result:
            if r in symbols:
                takemore+=delemit+r
        result=takemore
    return result

Sen="string Sentence Examples. Someone tried to string him The violin string is first drawn on one side A piece of string she found in the kitchen would suffice".split(" ")
sen=""
for w in Sen:
    sen+=normEng(w,"/")
print(sen)

#Chạy qua các từ tiếng anh -> lọc ra các phoneme đặc thù tiếng anh => ExceptReplaceSym=['uː', 'iː', 'ɑ', 'ɛː', 'zi', 'kwi', 'ɔː']
#Chạy lọc các cau trong LDspeech -> chứa các từ riêng biệt: khoảng 500 câu
#Đưa đống hàm normEng vào tacotron đang train xem dọcđược không
#có nên thêm kí tự đánh dấu tiếng anh như Zalo nói

# Xử lí ngắt ngẫu nhiên của zalo * và ~ => tìm hiểu ý nghĩa 2 đấu đó  => thay bằng phẩy
#Chạy lọc qua dict tiengs aanh với hàm normEng => check xem có kí tự mới nào không