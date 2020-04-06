# Project Custom from vPhon for convert Raw text to IPA

* Use for embeding TTS model using Tacotron2

* By using IPA, tacotron2 can deal with cases cross language as a proposal from futre paper

* Include diary research in phoneme of Vietnamese, painful and character of Viet

* Function include: Convert Grapheme to IPA, List same token output, normalize text with vinorm and wordtoken

* Requirment: vinorm, underthesea, eng_to_ipa

```python
from viphoneme import vi2IPA
phoneme = vi2IPA("hải quay xe")
```