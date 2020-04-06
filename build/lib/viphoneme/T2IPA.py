#Grapheme
Rime_tone=[    "a","ă","â","e","ê","i","o","ô","ơ","u","ư","y","iê","oa","oă","oe","oo","uâ","uê","uô","uơ","uy","ươ","uyê","yê", #blank
          "á","ắ","ấ","é","ế","í","ó","ố","ớ","ú","ứ","ý","iế","óa","oắ","óe","oó","uấ","uế","uố","ướ","úy","ướ","uyế","yế", #grave
                                                               "oá",     "oé","óo",                    "uý",      
          "à","ằ","ầ","è","ề","ì","ò","ồ","ờ","ù","ừ","ỳ","iề","òa","oằ","òe","oò","uầ","uề","uồ","ườ","ùy","ườ","uyề","yề", #acute
                                                               "oà",     "oè","òo",                    "uỳ",            
          "ả","ẳ","ẩ","ẻ","ể","ỉ","ỏ","ổ","ở","ủ","ử","ỷ","iể","ỏa","oẳ","ỏe","oỏ","uẩ","uể","uổ","ưở","ủy","ưở","uyể","yể", #hook
                                                               "oả",     "oẻ","ỏo",                    "uỷ", 
          "ã","ẵ","ẫ","ẽ","ễ","ĩ","õ","ỗ","ỡ","ũ","ữ","ỹ","iễ","õa","oẵ","õe","oõ","uẫ","uễ","uỗ","ưỡ","ũy","ưỡ","uyễ","yễ", #tilde
                                                               "oã",     "oẽ","õo",                    "uỹ",            
          "ạ","ặ","ậ","ẹ","ệ","ị","ọ","ộ","ợ","ụ","ự","ỵ","iệ","ọa","oặ","ọe","oọ","uậ","uệ","uệ","ượ","ụy","ượ","uyệ","yệ", #dot
                                                               "oạ",     "oẹ","ọo",                    "uỵ"]

Onset=["b","d","h","l","m","n","p","r","s","t","v","x","đ","p",
        "tr", "th", "ch", "ph","nh","kh","gi","qu",
        "ngh","ng","gh","g","k","c"]
#coding: utf-8
#Custom phoneme follow the https://vi.wikipedia.org/wiki/%C3%82m_v%E1%BB%8B_h%E1%BB%8Dc_ti%E1%BA%BFng_Vi%E1%BB%87t
#Improve pronoune between N C S

Cus_onsets = { u'b' : u'b', u't' : u't', u'th' : u'tʰ', u'đ' : u'd', u'ch' : u'c', 
				u'kh' : u'x', u'g' : u'ɣ', u'l' : u'l', u'm' : u'm', u'n': u'n', 
				u'ngh': u'ŋ', u'nh' : u'ɲ', u'ng' : u'ŋ', u'ph' : u'f', u'v' : u'v', 
				u'x' : u's', u'd' : u'z', u'h' : u'h', u'p' : u'p', u'qu' : u'kw',
				u'gi' : u'j', u'tr' : u'ʈ', u'k' : u'k', u'c' : u'k', u'gh' : u'ɣ', 
				u'r' : u'ʐ', u's' : u'ʂ', u'gi': u'j'}
				
			  
Cus_nuclei = { u'a' : u'a', u'á' : u'a', u'à' : u'a', u'ả' : u'a', u'ã' : u'a', u'ạ' : u'a', 
				u'â' : u'ɤ̆', u'ấ' : u'ɤ̆', u'ầ' : u'ɤ̆', u'ẩ' : u'ɤ̆', u'ẫ' : u'ɤ̆', u'ậ' : u'ɤ̆',
				u'ă' : u'ă', u'ắ' : u'ă', u'ằ' : u'ă', u'ẳ' : u'ă', u'ẵ' : u'ă', u'ặ' : u'ă',
				u'e' : u'ɛ', u'é' : u'ɛ', u'è' : u'ɛ', u'ẻ' : u'ɛ', u'ẽ' : u'ɛ', u'ẹ' : u'ɛ',
				u'ê' : u'e', u'ế' : u'e', u'ề' : u'e', u'ể' : u'e', u'ễ' : u'e', u'ệ' : u'e',
				u'i' : u'i', u'í' : u'i', u'ì' : u'i', u'ỉ' : u'i', u'ĩ' : u'i', u'ị' : u'i',
				u'o' : u'ɔ', u'ó' : u'ɔ', u'ò' : u'ɔ', u'ỏ' : u'ɔ', u'õ' : u'ɔ', u'ọ' : u'ɔ',
				u'ô' : u'o', u'ố' : u'o', u'ồ' : u'o', u'ổ' : u'o', u'ỗ' : u'o', u'ộ' : u'o',
				u'ơ' : u'ɤ', u'ớ' : u'ɤ', u'ờ' : u'ɤ', u'ở' : u'ɤ', u'ỡ' : u'ɤ', u'ợ' : u'ɤ',
				u'u' : u'u', u'ú' : u'u', u'ù' : u'u', u'ủ' : u'u', u'ũ' : u'u', u'ụ' : u'u',
				u'ư' : u'ɯ', u'ứ' : u'ɯ', u'ừ' : u'ɯ', u'ử' : u'ɯ', u'ữ' : u'ɯ', u'ự' : u'ɯ',
				u'y' : u'i', u'ý' : u'i', u'ỳ' : u'i', u'ỷ' : u'i', u'ỹ' : u'i', u'ỵ' : u'i',
				
				u'eo' : u'eo', u'éo' : u'eo', u'èo' : u'eo', u'ẻo' : u'eo', u'ẽo': u'eo', u'ẹo' : u'eo',
				u'êu' : u'ɛu', u'ếu' : u'ɛu', u'ều' : u'ɛu', u'ểu' : u'ɛu', u'ễu': u'ɛu', u'ệu' : u'ɛu',
				u'ia' : u'iə', u'ía' : u'iə', u'ìa' : u'iə', u'ỉa' : u'iə', u'ĩa' : u'iə', u'ịa' : u'iə',
				u'ia' : u'iə', u'iá' : u'iə', u'ià' : u'iə', u'iả' : u'iə', u'iã' : u'iə', u'iạ' : u'iə',
				u'iê' : u'iə', u'iế' : u'iə', u'iề' : u'iə', u'iể' : u'iə', u'iễ' : u'iə', u'iệ' : u'iə',
				u'oo' : u'ɔ', u'óo' : u'ɔ', u'òo' : u'ɔ', u'ỏo' : u'ɔ', u'õo' : u'ɔ', u'ọo' : u'ɔ',
				u'oo' : u'ɔ', u'oó' : u'ɔ', u'oò' : u'ɔ', u'oỏ' : u'ɔ', u'oõ' : u'ɔ', u'oọ' : u'ɔ',
				u'ôô' : u'o', u'ốô' : u'o', u'ồô' : u'o', u'ổô' : u'o', u'ỗô' : u'o', u'ộô' : u'o',				                 
                u'ôô' : u'o', u'ôố' : u'o', u'ôồ' : u'o', u'ôổ' : u'o', u'ôỗ' : u'o', u'ôộ' : u'o',				                  
                u'ua' : u'uə', u'úa' : u'uə', u'ùa' : u'uə', u'ủa' : u'uə', u'ũa' : u'uə', u'ụa' : u'uə',
				u'uô' : u'uə', u'uố' : u'uə', u'uồ' : u'uə', u'uổ' : u'uə', u'uỗ' : u'uə', u'uộ' : u'uə',
				u'ưa' : u'ɯə', u'ứa' : u'ɯə', u'ừa' : u'ɯə', u'ửa' : u'ɯə', u'ữa' : u'ɯə', u'ựa' : u'ɯə',
				u'ươ' : u'ɯə', u'ướ' : u'ɯə', u'ườ' : u'ɯə', u'ưở' : u'ɯə', u'ưỡ' : u'ɯə', u'ượ' : u'ɯə',
				u'yê' : u'iɛ', u'yế' : u'iɛ', u'yề' : u'iɛ', u'yể' : u'iɛ', u'yễ' : u'iɛ', u'yệ' : u'iɛ', 
                u'uơ' : u'uə',  u'uở' : u'uə', u'uờ': u'uə', u'uở' : u'uə', u'uỡ' : u'uə', u'uợ' : u'uə',
				}
				         
	         
Cus_offglides =  { u'ai' : u'aj', u'ái' : u'aj', u'ài' : u'aj', u'ải' : u'aj', u'ãi' : u'aj', u'ại' : u'aj',
				  u'ay' : u'ăj', u'áy' : u'ăj', u'ày' : u'ăj', u'ảy' : u'ăj', u'ãy' : u'ăj', u'ạy' : u'ăj',
				  u'ao' : u'aw', u'áo' : u'aw', u'ào' : u'aw', u'ảo' : u'aw', u'ão' : u'aw', u'ạo' : u'aw',
				  u'au' : u'ăw', u'áu' : u'ăw', u'àu' : u'ăw', u'ảu' : u'ăw', u'ãu' : u'ăw', u'ạu' : u'ăw',
				  u'ây' : u'ɤ̆j',  u'ấy' : u'ɤ̆j',  u'ầy' : u'ɤ̆j', u'ẩy' : u'ɤ̆j', u'ẫy' : u'ɤ̆j', u'ậy' : u'ɤ̆j', 
				  u'âu' : u'ɤ̆w', u'ấu' : u'ɤ̆w', u'ầu': u'ɤ̆w', u'ẩu' : u'ɤ̆w', u'ẫu' : u'ɤ̆w', u'ậu' : u'ɤ̆w',
				  u'eo' : u'ew', u'éo' : u'ew', u'èo' : u'ew', u'ẻo' : u'ew', u'ẽo' : u'ew', u'ẹo' : u'ew',
				  u'iu' : u'iw', u'íu' : u'iw', u'ìu' : u'iw', u'ỉu' : u'iw', u'ĩu' : u'iw', u'ịu' : u'iw',
				  u'oi' : u'ɔj', u'ói' : u'ɔj', u'òi' : u'ɔj', u'ỏi' : u'ɔj', u'õi' : u'ɔj', u'ọi' : u'ɔj',
				  u'ôi' : u'oj', u'ối' : u'oj', u'ồi' : u'oj', u'ổi' : u'oj', u'ỗi' : u'oj', u'ội' : u'oj',
				  u'ui' : u'uj', u'úi' : u'uj', u'ùi' : u'uj', u'ủi' : u'uj', u'ũi' : u'uj', u'ụi' : u'uj', 
				  #u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj', 
                  u'uy' : u'ʷi', u'uý' : u'ʷi', u'uỳ' : u'ʷi', u'uỷ' : u'ʷi', u'uỹ' : u'ʷi', u'uỵ' : u'ʷi',
				  u'ơi' : u'ɤj', u'ới' : u'ɤj', u'ời' : u'ɤj', u'ởi' : u'ɤj', u'ỡi' : u'ɤj', u'ợi' : u'ɤj', 
				  u'ưi' : u'ɯj', u'ứi' : u'ɯj', u'ừi' : u'ɯj', u'ửi' : u'ɯj', u'ữi' : u'ɯj', u'ựi' : u'ɯj', 
				  u'ưu' : u'ɯw', u'ứu' : u'ɯw', u'ừu' : u'ɯw', u'ửu' : u'ɯw', u'ữu' : u'ɯw', u'ựu' : u'ɯw',

				  u'iêu' : u'iəw', u'iếu' : u'iəw', u'iều' : u'iəw', u'iểu' : u'iəw', u'iễu' : u'iəw', u'iệu' : u'iəw',
				  u'yêu' : u'iəw', u'yếu' : u'iəw', u'yều' : u'iəw', u'yểu' : u'iəw', u'yễu' : u'iəw', u'yệu' : u'iəw', 
				  u'uôi' : u'uəj', u'uối' : u'uəj', u'uồi' : u'uəj', u'uổi' : u'uəj', u'uỗi' : u'uəj', u'uội' : u'uəj', 
				  u'ươi' : u'ɯəj', u'ưới' : u'ɯəj', u'ười' : u'ɯəj', u'ưởi' : u'ɯəj', u'ưỡi' : u'ɯəj', u'ượi' : u'ɯəj', 
				  u'ươu' : u'ɯəw', u'ướu' : u'ɯəw', u'ườu' : u'ɯəw', u'ưởu' : u'ɯəw', 'ưỡu' : u'ɯəw', u'ượu' : u'ɯəw'	 
			    }
#Các âm vòng ở đây i chang không vòm: không có w ở trước		=> Try to add ʷ	
Cus_onglides =   { u'oa' : u'ʷa', u'oá' : u'ʷa', u'oà' : u'ʷa', u'oả' : u'ʷa', u'oã' : u'ʷa', u'oạ' : u'ʷa', 
		              u'óa' : u'ʷa', u'òa' : u'ʷa', u'ỏa' : u'ʷa', u'õa' : u'ʷa', u'ọa' : u'ʷa', 
			      u'oă' : u'ʷă', u'oắ' : u'ʷă', u'oằ' : u'ʷă', u'oẳ' : u'ʷă', u'oẵ' : u'ʷă', u'oặ' : u'ʷă', 	
			      u'oe' : u'ʷɛ', u'oé' : u'ʷɛ', u'oè' : u'ʷɛ', u'oẻ' : u'ʷɛ', u'oẽ' : u'ʷɛ', u'oẹ' : u'ʷɛ', 	
			      u'oe' : u'ʷɛ', u'óe' : u'ʷɛ', u'òe' : u'ʷɛ', u'ỏe' : u'ʷɛ', u'õe' : u'ʷɛ', u'ọe' : u'ʷɛ', 	
			      u'ua' : u'ʷa', u'uá' : u'ʷa', u'uà' : u'ʷa', u'uả' : u'ʷa', u'uã' : u'ʷa', u'uạ' : u'ʷa', 
			      u'uă' : u'ʷă', u'uắ' : u'ʷă', u'uằ' : u'ʷă', u'uẳ' : u'ʷă', u'uẵ' : u'ʷă', u'uặ' : u'ʷă', 	
			      u'uâ' : u'ʷɤ̆', u'uấ' : u'ʷɤ̆', u'uầ' : u'ʷɤ̆', u'uẩ' : u'ʷɤ̆', u'uẫ' : u'ʷɤ̆', u'uậ' : u'ʷɤ̆', 
			      u'ue' : u'ʷɛ', u'ué' : u'ʷɛ', u'uè' : u'ʷɛ', u'uẻ' : u'ʷɛ', u'uẽ' : u'ʷɛ', u'uẹ' : u'ʷɛ', 
			      u'uê' : u'ʷe', u'uế' : u'ʷe', u'uề' : u'ʷe', u'uể' : u'ʷe', u'uễ' : u'ʷe', u'uệ' : u'ʷe', 
			      u'uơ' : u'ʷɤ', u'uớ' : u'ʷɤ', u'uờ' : u'ʷɤ', u'uở' : u'ʷɤ', u'uỡ' : u'ʷɤ', u'uợ' : u'ʷɤ', 
			      u'uy' : u'ʷi', u'uý' : u'ʷi', u'uỳ' : u'ʷi', u'uỷ' : u'ʷi', u'uỹ' : u'ʷi', u'uỵ' : u'ʷi',
		          u'uya' : u'ʷiə', u'uyá' : u'ʷiə', u'uyà' : u'ʷiə', u'uyả' : u'ʷiə', u'uyã' : u'ʷiə', u'uyạ' : u'ʷiə', 
				  u'uyê' : u'ʷiə', u'uyế' : u'ʷiə', u'uyề' : u'ʷiə', u'uyể' : u'ʷiə', u'uyễ' : u'ʷiə', u'uyệ' : u'ʷiə', 
				  u'uyu' : u'ʷiu', u'uyú' : u'ʷiu', u'uyù' : u'ʷiu', u'uyủ' : u'ʷiu', u'uyũ' : u'ʷiu', u'uyụ' : u'ʷiu', 
				  u'uyu' : u'ʷiu', u'uýu' : u'ʷiu', u'uỳu' : u'ʷiu', u'uỷu' : u'ʷiu', u'uỹu' : u'ʷiu', u'uỵu' : u'ʷiu',
                  u'oen' : u'ʷen', u'oén' : u'ʷen', u'oèn' : u'ʷen', u'oẻn' : u'ʷen', u'oẽn' : u'ʷen', u'oẹn' : u'ʷen', 	
                  u'oet' : u'ʷet', u'oét' : u'ʷet', u'oèt' : u'ʷet', u'oẻt' : u'ʷet', u'oẽt' : u'ʷet', u'oẹt' : u'ʷet' 	
				}

Cus_onoffglides = { u'oe' : u'ɛj', u'oé' : u'ɛj', u'oè' : u'ɛj', u'oẻ' : u'ɛj', u'oẽ' : u'ɛj', u'oẹ' : u'ɛj', 
				   u'oai' : u'aj', u'oái' : u'aj', u'oài' : u'aj', u'oải' : u'aj', u'oãi' : u'aj', u'oại' : u'aj',
				   u'oay' : u'ăj', u'oáy' : u'ăj', u'oày' : u'ăj', u'oảy' : u'ăj', u'oãy' : u'ăj', u'oạy' : u'ăj',
				   u'oao' : u'aw', u'oáo' : u'aw', u'oào' : u'aw', u'oảo' : u'aw', u'oão' : u'aw', u'oạo' : u'aw',
				   u'oeo' : u'ew', u'oéo' : u'ew', u'oèo' : u'ew', u'oẻo' : u'ew', u'oẽo' : u'ew', u'oẹo' : u'ew',
				   u'oeo' : u'ew', u'óeo' : u'ew', u'òeo' : u'ew', u'ỏeo' : u'ew', u'õeo' : u'ew', u'ọeo' : u'ew',
				   u'ueo' : u'ew', u'uéo' : u'ew', u'uèo' : u'ew', u'uẻo' : u'ew', u'uẽo' : u'ew', u'uẹo' : u'ew',
				   u'uai' : u'aj', u'uái' : u'aj', u'uài' : u'aj', u'uải' : u'aj', u'uãi' : u'aj', u'uại' : u'aj',
				   u'uay' : u'ăj', u'uáy' : u'ăj', u'uày' : u'ăj', u'uảy' : u'ăj', u'uãy' : u'ăj', u'uạy' : u'ăj',
				   u'uây' : u'ɤ̆j', u'uấy' : u'ɤ̆j', u'uầy' : u'ɤ̆j', u'uẩy' : u'ɤ̆j', u'uẫy' : u'ɤ̆j', u'uậy' : u'ɤ̆j'
				 }

Cus_codas = { u'p' : u'p', u't' : u't', u'c' : u'k', u'm' : u'm', u'n' : u'n', u'ng' : u'ŋ', u'nh' : u'ɲ', u'ch' : u'tʃ' }

Cus_tones_p =     { u'á' : 5, u'à' : 2, u'ả' : 4, u'ã' : 3, u'ạ' : 6, 
				u'ấ' : 5, u'ầ' : 2, u'ẩ' : 4, u'ẫ' : 3, u'ậ' : 6,
				u'ắ' : 5, u'ằ' : 2, u'ẳ' : 4, u'ẵ' : 3, u'ặ' : 6,
				u'é' : 5, u'è' : 2, u'ẻ' : 4, u'ẽ' : 3, u'ẹ' : 6,
				u'ế' : 5, u'ề' : 2, u'ể' : 4, u'ễ' : 3, u'ệ' : 6,
				u'í' : 5, u'ì' : 2, u'ỉ' : 4, u'ĩ' : 3, u'ị' : 6,
				u'ó' : 5, u'ò' : 2, u'ỏ' : 4, u'õ' : 3, u'ọ' : 6,
				u'ố' : 5, u'ồ' : 2, u'ổ' : 4, u'ỗ' : 3, u'ộ' : 6,
				u'ớ' : 5, u'ờ' : 2, u'ở' : 4, u'ỡ' : 3, u'ợ' : 6,
				u'ú' : 5, u'ù' : 2, u'ủ' : 4, u'ũ' : 3, u'ụ' : 6,
				u'ứ' : 5, u'ừ' : 2, u'ử' : 4, u'ữ' : 3, u'ự' : 6,
				u'ý' : 5, u'ỳ' : 2, u'ỷ' : 4, u'ỹ' : 3, u'ỵ' : 6,
			  }
			  
Cus_gi = { u'gi' : u'zi', u'gí': u'zi', u'gì' : u'zi', u'gì' : u'zi', u'gĩ' : u'zi', u'gị' : u'zi'}

Cus_qu = {u'quy' : u'kwi', u'qúy' : u'kwi', u'qùy' : u'kwi', u'qủy' : u'kwi', u'qũy' : u'kwi', u'qụy' : u'kwi'}


#######################################################
# North
# #coding: utf-8

N_onsets = { u'b' : u'b', u't' : u't', u'th' : u'tʰ', u'đ' : u'd', u'ch' : u'c', 
				u'kh' : u'x', u'g' : u'ɣ', u'l' : u'l', u'm' : u'm', u'n': u'n', 
				u'ngh': u'ŋ', u'nh' : u'ɲ', u'ng' : u'ŋ', u'ph' : u'f', u'v' : u'v', 
				u'x' : u's', u'd' : u'z', u'h' : u'h', u'p' : u'p', u'qu' : u'kw',
				u'gi' : u'z', u'tr' : u'c', u'k' : u'k', u'c' : u'k', u'gh' : u'ɣ', 
				u'r' : u'z', u's' : u's', u'gi': u'z'}
				
			  
N_nuclei = { u'a' : u'a', u'á' : u'a', u'à' : u'a', u'ả' : u'a', u'ã' : u'a', u'ạ' : u'a', 
				u'â' : u'ɤ̆', u'ấ' : u'ɤ̆', u'ầ' : u'ɤ̆', u'ẩ' : u'ɤ̆', u'ẫ' : u'ɤ̆', u'ậ' : u'ɤ̆',
				u'ă' : u'ă', u'ắ' : u'ă', u'ằ' : u'ă', u'ẳ' : u'ă', u'ẵ' : u'ă', u'ặ' : u'ă',
				u'e' : u'ɛ', u'é' : u'ɛ', u'è' : u'ɛ', u'ẻ' : u'ɛ', u'ẽ' : u'ɛ', u'ẹ' : u'ɛ',
				u'ê' : u'e', u'ế' : u'e', u'ề' : u'e', u'ể' : u'e', u'ễ' : u'e', u'ệ' : u'e',
				u'i' : u'i', u'í' : u'i', u'ì' : u'i', u'ỉ' : u'i', u'ĩ' : u'i', u'ị' : u'i',
				u'o' : u'ɔ', u'ó' : u'ɔ', u'ò' : u'ɔ', u'ỏ' : u'ɔ', u'õ' : u'ɔ', u'ọ' : u'ɔ',
				u'ô' : u'o', u'ố' : u'o', u'ồ' : u'o', u'ổ' : u'o', u'ỗ' : u'o', u'ộ' : u'o',
				u'ơ' : u'ɤ', u'ớ' : u'ɤ', u'ờ' : u'ɤ', u'ở' : u'ɤ', u'ỡ' : u'ɤ', u'ợ' : u'ɤ',
				u'u' : u'u', u'ú' : u'u', u'ù' : u'u', u'ủ' : u'u', u'ũ' : u'u', u'ụ' : u'u',
				u'ư' : u'ɯ', u'ứ' : u'ɯ', u'ừ' : u'ɯ', u'ử' : u'ɯ', u'ữ' : u'ɯ', u'ự' : u'ɯ',
				u'y' : u'i', u'ý' : u'i', u'ỳ' : u'i', u'ỷ' : u'i', u'ỹ' : u'i', u'ỵ' : u'i',
				
				u'eo' : u'eo', u'éo' : u'eo', u'èo' : u'eo', u'ẻo' : u'eo', u'ẽo': u'eo', u'ẹo' : u'eo',
				u'êu' : u'ɛu', u'ếu' : u'ɛu', u'ều' : u'ɛu', u'ểu' : u'ɛu', u'ễu': u'ɛu', u'ệu' : u'ɛu',
				u'ia' : u'iə', u'ía' : u'iə', u'ìa' : u'iə', u'ỉa' : u'iə', u'ĩa' : u'iə', u'ịa' : u'iə',
				u'ia' : u'iə', u'iá' : u'iə', u'ià' : u'iə', u'iả' : u'iə', u'iã' : u'iə', u'iạ' : u'iə',
				u'iê' : u'iə', u'iế' : u'iə', u'iề' : u'iə', u'iể' : u'iə', u'iễ' : u'iə', u'iệ' : u'iə',
				u'oo' : u'ɔ', u'óo' : u'ɔ', u'òo' : u'ɔ', u'ỏo' : u'ɔ', u'õo' : u'ɔ', u'ọo' : u'ɔ',
				u'oo' : u'ɔ', u'oó' : u'ɔ', u'oò' : u'ɔ', u'oỏ' : u'ɔ', u'oõ' : u'ɔ', u'oọ' : u'ɔ',
				u'ôô' : u'o', u'ốô' : u'o', u'ồô' : u'o', u'ổô' : u'o', u'ỗô' : u'o', u'ộô' : u'o',				                 
                u'ôô' : u'o', u'ôố' : u'o', u'ôồ' : u'o', u'ôổ' : u'o', u'ôỗ' : u'o', u'ôộ' : u'o',				                  
                u'ua' : u'uə', u'úa' : u'uə', u'ùa' : u'uə', u'ủa' : u'uə', u'ũa' : u'uə', u'ụa' : u'uə',
				u'uô' : u'uə', u'uố' : u'uə', u'uồ' : u'uə', u'uổ' : u'uə', u'uỗ' : u'uə', u'uộ' : u'uə',
				u'ưa' : u'ɯə', u'ứa' : u'ɯə', u'ừa' : u'ɯə', u'ửa' : u'ɯə', u'ữa' : u'ɯə', u'ựa' : u'ɯə',
				u'ươ' : u'ɯə', u'ướ' : u'ɯə', u'ườ' : u'ɯə', u'ưở' : u'ɯə', u'ưỡ' : u'ɯə', u'ượ' : u'ɯə',
				u'yê' : u'iɛ', u'yế' : u'iɛ', u'yề' : u'iɛ', u'yể' : u'iɛ', u'yễ' : u'iɛ', u'yệ' : u'iɛ', 
                                u'uơ' : u'uə',  u'uở' : u'uə', u'uờ': u'uə', u'uở' : u'uə', u'uỡ' : u'uə', u'uợ' : u'uə',
				}
				         
				         
N_offglides =  { u'ai' : u'aj', u'ái' : u'aj', u'ài' : u'aj', u'ải' : u'aj', u'ãi' : u'aj', u'ại' : u'aj',
				  u'ay' : u'ăj', u'áy' : u'ăj', u'ày' : u'ăj', u'ảy' : u'ăj', u'ãy' : u'ăj', u'ạy' : u'ăj',
				  u'ao' : u'aw', u'áo' : u'aw', u'ào' : u'aw', u'ảo' : u'aw', u'ão' : u'aw', u'ạo' : u'aw',
				  u'au' : u'ăw', u'áu' : u'ăw', u'àu' : u'ăw', u'ảu' : u'ăw', u'ãu' : u'ăw', u'ạu' : u'ăw',
				  u'ây' : u'ɤ̆j',  u'ấy' : u'ɤ̆j',  u'ầy' : u'ɤ̆j', u'ẩy' : u'ɤ̆j', u'ẫy' : u'ɤ̆j', u'ậy' : u'ɤ̆j', 
				  u'âu' : u'ɤ̆w', u'ấu' : u'ɤ̆w', u'ầu': u'ɤ̆w', u'ẩu' : u'ɤ̆w', u'ẫu' : u'ɤ̆w', u'ậu' : u'ɤ̆w',
				  u'eo' : u'ew', u'éo' : u'ew', u'èo' : u'ew', u'ẻo' : u'ew', u'ẽo' : u'ew', u'ẹo' : u'ew',
				  u'iu' : u'iw', u'íu' : u'iw', u'ìu' : u'iw', u'ỉu' : u'iw', u'ĩu' : u'iw', u'ịu' : u'iw',
				  u'oi' : u'ɔj', u'ói' : u'ɔj', u'òi' : u'ɔj', u'ỏi' : u'ɔj', u'õi' : u'ɔj', u'ọi' : u'ɔj',
				  u'ôi' : u'oj', u'ối' : u'oj', u'ồi' : u'oj', u'ổi' : u'oj', u'ỗi' : u'oj', u'ội' : u'oj',
				  u'ui' : u'uj', u'úi' : u'uj', u'ùi' : u'uj', u'ủi' : u'uj', u'ũi' : u'uj', u'ụi' : u'uj', 
				  u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj', 
				  u'ơi' : u'ɤj', u'ới' : u'ɤj', u'ời' : u'ɤj', u'ởi' : u'ɤj', u'ỡi' : u'ɤj', u'ợi' : u'ɤj', 
				  u'ưi' : u'ɯj', u'ứi' : u'ɯj', u'ừi' : u'ɯj', u'ửi' : u'ɯj', u'ữi' : u'ɯj', u'ựi' : u'ɯj', 
				  u'ưu' : u'ɯw', u'ứu' : u'ɯw', u'ừu' : u'ɯw', u'ửu' : u'ɯw', u'ữu' : u'ɯw', u'ựu' : u'ɯw',

				  u'iêu' : u'iəw', u'iếu' : u'iəw', u'iều' : u'iəw', u'iểu' : u'iəw', u'iễu' : u'iəw', u'iệu' : u'iəw',
				  u'yêu' : u'iəw', u'yếu' : u'iəw', u'yều' : u'iəw', u'yểu' : u'iəw', u'yễu' : u'iəw', u'yệu' : u'iəw', 
				  u'uôi' : u'uəj', u'uối' : u'uəj', u'uồi' : u'uəj', u'uổi' : u'uəj', u'uỗi' : u'uəj', u'uội' : u'uəj', 
				  u'ươi' : u'ɯəj', u'ưới' : u'ɯəj', u'ười' : u'ɯəj', u'ưởi' : u'ɯəj', u'ưỡi' : u'ɯəj', u'ượi' : u'ɯəj', 
				  u'ươu' : u'ɯəw', u'ướu' : u'ɯəw', u'ườu' : u'ɯəw', u'ưởu' : u'ɯəw', 'ưỡu' : u'ɯəw', u'ượu' : u'ɯəw'	 
			    }
N_onglides =   { u'oa' : u'a', u'oá' : u'a', u'oà' : u'a', u'oả' : u'a', u'oã' : u'a', u'oạ' : u'a', 
		              u'óa' : u'a', u'òa' : u'a', u'ỏa' : u'a', u'õa' : u'a', u'ọa' : u'a', 
			      u'oă' : u'ă', u'oắ' : u'ă', u'oằ' : u'ă', u'oẳ' : u'ă', u'oẵ' : u'ă', u'oặ' : u'ă', 	
			      u'oe' : u'e', u'oé' : u'e', u'oè' : u'e', u'oẻ' : u'e', u'oẽ' : u'e', u'oẹ' : u'e', 	
			      u'oe' : u'e', u'óe' : u'e', u'òe' : u'e', u'ỏe' : u'e', u'õe' : u'e', u'ọe' : u'e', 	
			      u'ua' : u'a', u'uá' : u'a', u'uà' : u'a', u'uả' : u'a', u'uã' : u'a', u'uạ' : u'a', 
			      u'uă' : u'ă', u'uắ' : u'ă', u'uằ' : u'ă', u'uẳ' : u'ă', u'uẵ' : u'ă', u'uặ' : u'ă', 	
			      u'uâ' : u'ɤ̆', u'uấ' : u'ɤ̆', u'uầ' : u'ɤ̆', u'uẩ' : u'ɤ̆', u'uẫ' : u'ɤ̆', u'uậ' : u'ɤ̆', 
			      u'ue' : u'ɛ', u'ué' : u'ɛ', u'uè' : u'ɛ', u'uẻ' : u'ɛ', u'uẽ' : u'ɛ', u'uẹ' : u'ɛ', 
			      u'uê' : u'e', u'uế' : u'e', u'uề' : u'e', u'uể' : u'e', u'uễ' : u'e', u'uệ' : u'e', 
			      u'uơ' : u'ɤ', u'uớ' : u'ɤ', u'uờ' : u'ɤ', u'uở' : u'ɤ', u'uỡ' : u'ɤ', u'uợ' : u'ɤ', 
			      u'uy' : u'i', u'uý' : u'i', u'uỳ' : u'i', u'uỷ' : u'i', u'uỹ' : u'i', u'uỵ' : u'i',
		              u'uya' : u'iə', u'uyá' : u'iə', u'uyà' : u'iə', u'uyả' : u'iə', u'uyã' : u'iə', u'uyạ' : u'iə', 
				  u'uyê' : u'iə', u'uyế' : u'iə', u'uyề' : u'iə', u'uyể' : u'iə', u'uyễ' : u'iə', u'uyệ' : u'iə', 
				  u'uyu' : u'iu', u'uyú' : u'iu', u'uyù' : u'iu', u'uyủ' : u'iu', u'uyũ' : u'iu', u'uyụ' : u'iu', 
				  u'uyu' : u'iu', u'uýu' : u'iu', u'uỳu' : u'iu', u'uỷu' : u'iu', u'uỹu' : u'iu', u'uỵu' : u'iu',
                  u'oen' : u'en', u'oén' : u'en', u'oèn' : u'en', u'oẻn' : u'en', u'oẽn' : u'en', u'oẹn' : u'en', 	
                  u'oet' : u'et', u'oét' : u'et', u'oèt' : u'et', u'oẻt' : u'et', u'oẽt' : u'et', u'oẹt' : u'et' 	
				}

N_onoffglides = { u'oe' : u'ej', u'oé' : u'ej', u'oè' : u'ej', u'oẻ' : u'ej', u'oẽ' : u'ej', u'oẹ' : u'ej', 
				   u'oai' : u'aj', u'oái' : u'aj', u'oài' : u'aj', u'oải' : u'aj', u'oãi' : u'aj', u'oại' : u'aj',
				   u'oay' : u'ăj', u'oáy' : u'ăj', u'oày' : u'ăj', u'oảy' : u'ăj', u'oãy' : u'ăj', u'oạy' : u'ăj',
				   u'oao' : u'aw', u'oáo' : u'aw', u'oào' : u'aw', u'oảo' : u'aw', u'oão' : u'aw', u'oạo' : u'aw',
				   u'oeo' : u'ew', u'oéo' : u'ew', u'oèo' : u'ew', u'oẻo' : u'ew', u'oẽo' : u'ew', u'oẹo' : u'ew',
				   u'oeo' : u'ew', u'óeo' : u'ew', u'òeo' : u'ew', u'ỏeo' : u'ew', u'õeo' : u'ew', u'ọeo' : u'ew',
				   u'ueo' : u'ew', u'uéo' : u'ew', u'uèo' : u'ew', u'uẻo' : u'ew', u'uẽo' : u'ew', u'uẹo' : u'ew',
				   u'uai' : u'aj', u'uái' : u'aj', u'uài' : u'aj', u'uải' : u'aj', u'uãi' : u'aj', u'uại' : u'aj',
				   u'uay' : u'ăj', u'uáy' : u'ăj', u'uày' : u'ăj', u'uảy' : u'ăj', u'uãy' : u'ăj', u'uạy' : u'ăj',
				   u'uây' : u'ɤ̆j', u'uấy' : u'ɤ̆j', u'uầy' : u'ɤ̆j', u'uẩy' : u'ɤ̆j', u'uẫy' : u'ɤ̆j', u'uậy' : u'ɤ̆j'
				 }

N_codas = { u'p' : u'p', u't' : u't', u'c' : u'k', u'm' : u'm', u'n' : u'n', u'ng' : u'ŋ', u'nh' : u'ɲ', u'ch' : u'k' }
			

#tones   =     { u'a' : 33, u'á' : 24, u'à' : 32, u'ả' : 312, u'ã' : u'35g', u'ạ' : u'21g', 
#				u'â' : 33, u'ấ' : 24, u'ầ' : 32, u'ẩ' : 312, u'ẫ' : u'35g', u'ậ' : u'21g',
#				u'ă' : 33, u'ắ' : 24, u'ằ' : 32, u'ẳ' : 312, u'ẵ' : u'35g', u'ặ' : u'21g',
#				u'e' : 33, u'é' : 24, u'è' : 32, u'ẻ' : 312, u'ẽ' : u'35g', u'ẹ' : u'21g',
#				u'ê' : 33, u'ế' : 24, u'ề' : 32, u'ể' : 312, u'ễ' : u'35g', u'ệ' : u'21g',
#				u'i' : 33, u'í' : 24, u'ì' : 32, u'ỉ' : 312, u'ĩ' : u'35g', u'ị' : u'21g',
#				u'o' : 33, u'ó' : 24, u'ò' : 32, u'ỏ' : 312, u'õ' : u'35g', u'ọ' : u'21g',
#				u'ô' : 33, u'ố' : 24, u'ồ' : 32, u'ổ' : 312, u'ỗ' : u'35g', u'ộ' : u'21g',
#				u'ơ' : 33, u'ớ' : 24, u'ờ' : 32, u'ở' : 312, u'ỡ' : u'35g', u'ợ' : u'21g',
#				u'u' : 33, u'ú' : 24, u'ù' : 32, u'ủ' : 312, u'ũ' : u'35g', u'ụ' : u'21g',
#				u'ư' : 33, u'ứ' : 24, u'ừ' : 32, u'ử' : 312, u'ữ' : u'35g', u'ự' : u'21g',
#				u'y' : 33, u'ý' : 24, u'ỳ' : 32, u'ỷ' : 312, u'ỹ' : u'35g', u'ỵ' : u'21g',
#			  }

N_tones   =     { u'á' : 24, u'à' : 32, u'ả' : 312, u'ã' : u'35g', u'ạ' : u'21g', 
				u'ấ' : 24, u'ầ' : 32, u'ẩ' : 312, u'ẫ' : u'35g', u'ậ' : u'21g',
				u'ắ' : 24, u'ằ' : 32, u'ẳ' : 312, u'ẵ' : u'35g', u'ặ' : u'21g',
				u'é' : 24, u'è' : 32, u'ẻ' : 312, u'ẽ' : u'35g', u'ẹ' : u'21g',
				u'ế' : 24, u'ề' : 32, u'ể' : 312, u'ễ' : u'35g', u'ệ' : u'21g',
				u'í' : 24, u'ì' : 32, u'ỉ' : 312, u'ĩ' : u'35g', u'ị' : u'21g',
				u'ó' : 24, u'ò' : 32, u'ỏ' : 312, u'õ' : u'35g', u'ọ' : u'21g',
				u'ố' : 24, u'ồ' : 32, u'ổ' : 312, u'ỗ' : u'35g', u'ộ' : u'21g',
				u'ớ' : 24, u'ờ' : 32, u'ở' : 312, u'ỡ' : u'35g', u'ợ' : u'21g',
				u'ú' : 24, u'ù' : 32, u'ủ' : 312, u'ũ' : u'35g', u'ụ' : u'21g',
				u'ứ' : 24, u'ừ' : 32, u'ử' : 312, u'ữ' : u'35g', u'ự' : u'21g',
				u'ý' : 24, u'ỳ' : 32, u'ỷ' : 312, u'ỹ' : u'35g', u'ỵ' : u'21g',
			  }
# used to use \u02C0 for the unicode raised glottal character

N_tones_p =     { u'á' : 5, u'à' : 2, u'ả' : 4, u'ã' : 3, u'ạ' : 6, 
				u'ấ' : 5, u'ầ' : 2, u'ẩ' : 4, u'ẫ' : 3, u'ậ' : 6,
				u'ắ' : 5, u'ằ' : 2, u'ẳ' : 4, u'ẵ' : 3, u'ặ' : 6,
				u'é' : 5, u'è' : 2, u'ẻ' : 4, u'ẽ' : 3, u'ẹ' : 6,
				u'ế' : 5, u'ề' : 2, u'ể' : 4, u'ễ' : 3, u'ệ' : 6,
				u'í' : 5, u'ì' : 2, u'ỉ' : 4, u'ĩ' : 3, u'ị' : 6,
				u'ó' : 5, u'ò' : 2, u'ỏ' : 4, u'õ' : 3, u'ọ' : 6,
				u'ố' : 5, u'ồ' : 2, u'ổ' : 4, u'ỗ' : 3, u'ộ' : 6,
				u'ớ' : 5, u'ờ' : 2, u'ở' : 4, u'ỡ' : 3, u'ợ' : 6,
				u'ú' : 5, u'ù' : 2, u'ủ' : 4, u'ũ' : 3, u'ụ' : 6,
				u'ứ' : 5, u'ừ' : 2, u'ử' : 4, u'ữ' : 3, u'ự' : 6,
				u'ý' : 5, u'ỳ' : 2, u'ỷ' : 4, u'ỹ' : 3, u'ỵ' : 6,
			  }
			  
N_gi = { u'gi' : u'zi', u'gí': u'zi', u'gì' : u'zi', u'gì' : u'zi', u'gĩ' : u'zi', u'gị' : u'zi'}

N_qu = {u'quy' : u'kwi', u'qúy' : u'kwi', u'qùy' : u'kwi', u'qủy' : u'kwi', u'qũy' : u'kwi', u'qụy' : u'kwi'}
#######################################################
#central.py
#coding: utf-8

C_onsets = { u'b' : u'b', u't' : u't', u'th' : u'tʰ', u'đ' : u'd', u'ch' : u'c', 
u'kh' : u'x', u'g' : u'ɣ', u'l' : u'l', u'm' : u'm', u'n': u'n', 
u'ngh': u'ŋ', u'nh' : u'ɲ', u'ng' : u'ŋ', u'ph' : u'f', u'v' : u'j', 
u'x' : u's', u'd' : u'j', u'h' : u'h', u'p' : u'p', u'qu' : u'w',
u'gi' : u'j', u'tr' : u'ʈ', u'k' : u'k', u'c' : u'k', u'gh' : u'ɣ',
u'r' : u'ʐ', u's' : u'ʂ', u'gi' : u'j'
}
			  
C_nuclei = { u'a' : u'a', u'á' : u'a', u'à' : u'a', u'ả' : u'a', u'ã' : u'a', u'ạ' : u'a', 
u'â' : u'ɤ̆', u'ấ' : u'ɤ̆', u'ầ' : u'ɤ̆', u'ẩ' : u'ɤ̆', u'ẫ' : u'ɤ̆', u'ậ' : u'ɤ̆',
u'ă' : u'ă', u'ắ' : u'ă', u'ằ' : u'ă', u'ẳ' : u'ă', u'ẵ' : u'ă', u'ặ' : u'ă',
u'e' : u'ɛ', u'é' : u'ɛ', u'è' : u'ɛ', u'ẻ' : u'ɛ', u'ẽ' : u'ɛ', u'ẹ' : u'ɛ',
u'ê' : u'e', u'ế' : u'e', u'ề' : u'e', u'ể' : u'e', u'ễ' : u'e', u'ệ' : u'e',
u'i' : u'i', u'í' : u'i', u'ì' : u'i', u'ỉ' : u'i', u'ĩ' : u'i', u'ị' : u'i',
u'o' : u'ɔ', u'ó' : u'ɔ', u'ò' : u'ɔ', u'ỏ' : u'ɔ', u'õ' : u'ɔ', u'ọ' : u'ɔ',
u'ô' : u'o', u'ố' : u'o', u'ồ' : u'o', u'ổ' : u'o', u'ỗ' : u'o', u'ộ' : u'o',
u'ơ' : u'ɤ', u'ớ' : u'ɤ', u'ờ' : u'ɤ', u'ở' : u'ɤ', u'ỡ' : u'ɤ', u'ợ' : u'ɤ',
u'u' : u'u', u'ú' : u'u', u'ù' : u'u', u'ủ' : u'u', u'ũ' : u'u', u'ụ' : u'u',
u'ư' : u'ɯ', u'ứ' : u'ɯ', u'ừ' : u'ɯ', u'ử' : u'ɯ', u'ữ' : u'ɯ', u'ự' : u'ɯ',
u'y' : u'i', u'ý' : u'i', u'ỳ' : u'i', u'ỷ' : u'i', u'ỹ' : u'i', u'ỵ' : u'i',
				
u'eo' : u'eo', u'éo' : u'eo', u'èo' : u'eo', u'ẻo' : u'eo', u'ẽo': u'eo', u'ẹo' : u'eo',
u'êu' : u'ɛu', u'ếu' : u'ɛu', u'ều' : u'ɛu', u'ểu' : u'ɛu', u'ễu': u'ɛu', u'ệu' : u'ɛu',
u'ia' : u'iə', u'ía' : u'iə', u'ìa' : u'iə', u'ỉa' : u'iə', u'ĩa' : u'iə', u'ịa' : u'iə',
u'ia' : u'iə', u'iá' : u'iə', u'ià' : u'iə', u'iả' : u'iə', u'iã' : u'iə', u'iạ' : u'iə',
u'iê' : u'iə', u'iế' : u'iə', u'iề' : u'iə', u'iể' : u'iə', u'iễ' : u'iə', u'iệ' : u'iə',
u'oo' : u'ɔ', u'óo' : u'ɔ', u'òo' : u'ɔ', u'ỏo' : u'ɔ', u'õo' : u'ɔ', u'ọo' : u'ɔ',
u'oo' : u'ɔ', u'oó' : u'ɔ', u'oò' : u'ɔ', u'oỏ' : u'ɔ', u'oõ' : u'ɔ', u'oọ' : u'ɔ',
u'ôô' : u'o', u'ốô' : u'o', u'ồô' : u'o', u'ổô' : u'o', u'ỗô' : u'o', u'ộô' : u'o',				                 
u'ôô' : u'o', u'ôố' : u'o', u'ôồ' : u'o', u'ôổ' : u'o', u'ôỗ' : u'o', u'ôộ' : u'o',				                  
u'ua' : u'uə', u'úa' : u'uə', u'ùa' : u'uə', u'ủa' : u'uə', u'ũa' : u'uə', u'ụa' : u'uə',
u'uô' : u'uə', u'uố' : u'uə', u'uồ' : u'uə', u'uổ' : u'uə', u'uỗ' : u'uə', u'uộ' : u'uə',
u'ưa' : u'ɯə', u'ứa' : u'ɯə', u'ừa' : u'ɯə', u'ửa' : u'ɯə', u'ữa' : u'ɯə', u'ựa' : u'ɯə',
u'ươ' : u'ɯə', u'ướ' : u'ɯə', u'ườ' : u'ɯə', u'ưở' : u'ɯə', u'ưỡ' : u'ɯə', u'ượ' : u'ɯə',
u'yê' : u'iɛ', u'yế' : u'iɛ', u'yề' : u'iɛ', u'yể' : u'iɛ', u'yễ' : u'iɛ', u'yệ' : u'iɛ', 
u'uơ' : u'uə',  u'uở' : u'uə', u'uờ': u'uə', u'uở' : u'uə', u'uỡ' : u'uə', u'uợ' : u'uə',
}
				         
C_offglides =  { u'ai' : u'aj', u'ái' : u'aj', u'ài' : u'aj', u'ải' : u'aj', u'ãi' : u'aj', u'ại' : u'aj',
u'ay' : u'ăj', u'áy' : u'ăj', u'ày' : u'ăj', u'ảy' : u'ăj', u'ãy' : u'ăj', u'ạy' : u'ăj',
u'ao' : u'aw', u'áo' : u'aw', u'ào' : u'aw', u'ảo' : u'aw', u'ão' : u'aw', u'ạo' : u'aw',
u'au' : u'ăw', u'áu' : u'ăw', u'àu' : u'ăw', u'ảu' : u'ăw', u'ãu' : u'ăw', u'ạu' : u'ăw',
u'ây' : u'ɤ̆j',  u'ấy' : u'ɤ̆j',  u'ầy' : u'ɤ̆j', u'ẩy' : u'ɤ̆j', u'ẫy' : u'ɤ̆j', u'ậy' : u'ɤ̆j', 
u'âu' : u'ɤ̆w', u'ấu' : u'ɤ̆w', u'ầu': u'ɤ̆w', u'ẩu' : u'ɤ̆w', u'ẫu' : u'ɤ̆w', u'ậu' : u'ɤ̆w',
u'eo' : u'ew', u'éo' : u'ew', u'èo' : u'ew', u'ẻo' : u'ew', u'ẽo' : u'ew', u'ẹo' : u'ew',
u'iu' : u'iw', u'íu' : u'iw', u'ìu' : u'iw', u'ỉu' : u'iw', u'ĩu' : u'iw', u'ịu' : u'iw',
u'oi' : u'ɔj', u'ói' : u'ɔj', u'òi' : u'ɔj', u'ỏi' : u'ɔj', u'õi' : u'ɔj', u'ọi' : u'ɔj',
u'ôi' : u'oj', u'ối' : u'oj', u'ồi' : u'oj', u'ổi' : u'oj', u'ỗi' : u'oj', u'ội' : u'oj',
u'ui' : u'uj', u'úi' : u'uj', u'ùi' : u'uj', u'ủi' : u'uj', u'ũi' : u'uj', u'ụi' : u'uj', 
u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj', 
u'ơi' : u'ɤj', u'ới' : u'ɤj', u'ời' : u'ɤj', u'ởi' : u'ɤj', u'ỡi' : u'ɤj', u'ợi' : u'ɤj', 
u'ưi' : u'ɯj', u'ứi' : u'ɯj', u'ừi' : u'ɯj', u'ửi' : u'ɯj', u'ữi' : u'ɯj', u'ựi' : u'ɯj', 
u'ưu' : u'ɯw', u'ứu' : u'ɯw', u'ừu' : u'ɯw', u'ửu' : u'ɯw', u'ữu' : u'ɯw', u'ựu' : u'ɯw',

u'iêu' : u'iəw', u'iếu' : u'iəw', u'iều' : u'iəw', u'iểu' : u'iəw', u'iễu' : u'iəw', u'iệu' : u'iəw',
u'yêu' : u'iəw', u'yếu' : u'iəw', u'yều' : u'iəw', u'yểu' : u'iəw', u'yễu' : u'iəw', u'yệu' : u'iəw', 
u'uôi' : u'uəj', u'uối' : u'uəj', u'uồi' : u'uəj', u'uổi' : u'uəj', u'uỗi' : u'uəj', u'uội' : u'uəj', 
u'ươi' : u'ɯəj', u'ưới' : u'ɯəj', u'ười' : u'ɯəj', u'ưởi' : u'ɯəj', u'ưỡi' : u'ɯəj', u'ượi' : u'ɯəj', 
u'ươu' : u'ɯəw', u'ướu' : u'ɯəw', u'ườu' : u'ɯəw', u'ưởu' : u'ɯəw', 'ưỡu' : u'ɯəw', u'ượu' : u'ɯəw'	 
}
				
C_onglides =   { u'oa' : u'a', u'oá' : u'a', u'oà' : u'a', u'oả' : u'a', u'oã' : u'a', u'oạ' : u'a', 
u'óa' : u'a', u'òa' : u'a', u'ỏa' : u'a', u'õa' : u'a', u'ọa' : u'a', 
u'oă' : u'ă', u'oắ' : u'ă', u'oằ' : u'ă', u'oẳ' : u'ă', u'oẵ' : u'ă', u'oặ' : u'ă', 	
u'oe' : u'e', u'oé' : u'e', u'oè' : u'e', u'oẻ' : u'e', u'oẽ' : u'e', u'oẹ' : u'e', 	
u'oe' : u'e', u'óe' : u'e', u'òe' : u'e', u'ỏe' : u'e', u'õe' : u'e', u'ọe' : u'e', 	
u'ua' : u'a', u'uá' : u'a', u'uà' : u'a', u'uả' : u'a', u'uã' : u'a', u'uạ' : u'a', 
u'uă' : u'ă', u'uắ' : u'ă', u'uằ' : u'ă', u'uẳ' : u'ă', u'uẵ' : u'ă', u'uặ' : u'ă', 	
u'uâ' : u'ɤ̆', u'uấ' : u'ɤ̆', u'uầ' : u'ɤ̆', u'uẩ' : u'ɤ̆', u'uẫ' : u'ɤ̆', u'uậ' : u'ɤ̆', 
u'ue' : u'ɛ', u'ué' : u'ɛ', u'uè' : u'ɛ', u'uẻ' : u'ɛ', u'uẽ' : u'ɛ', u'uẹ' : u'ɛ', 
u'uê' : u'e', u'uế' : u'e', u'uề' : u'e', u'uể' : u'e', u'uễ' : u'e', u'uệ' : u'e', 
u'uơ' : u'ɤ', u'uớ' : u'ɤ', u'uờ' : u'ɤ', u'uở' : u'ɤ', u'uỡ' : u'ɤ', u'uợ' : u'ɤ', 
u'uy' : u'i', u'uý' : u'i', u'uỳ' : u'i', u'uỷ' : u'i', u'uỹ' : u'i', u'uỵ' : u'i',
u'uya' : u'iə', u'uyá' : u'iə', u'uyà' : u'iə', u'uyả' : u'iə', u'uyã' : u'iə', u'uyạ' : u'iə', 
u'uyê' : u'iə', u'uyế' : u'iə', u'uyề' : u'iə', u'uyể' : u'iə', u'uyễ' : u'iə', u'uyệ' : u'iə', 
u'uyu' : u'iu', u'uyú' : u'iu', u'uyù' : u'iu', u'uyủ' : u'iu', u'uyũ' : u'iu', u'uyụ' : u'iu', 
u'uyu' : u'iu', u'uýu' : u'iu', u'uỳu' : u'iu', u'uỷu' : u'iu', u'uỹu' : u'iu', u'uỵu' : u'iu',
u'oen' : u'en', u'oén' : u'en', u'oèn' : u'en', u'oẻn' : u'en', u'oẽn' : u'en', u'oẹn' : u'en', 	
u'oet' : u'et', u'oét' : u'et', u'oèt' : u'et', u'oẻt' : u'et', u'oẽt' : u'et', u'oẹt' : u'et' 	
}

C_onoffglides = { u'oe' : u'ej', u'oé' : u'ej', u'oè' : u'ej', u'oẻ' : u'ej', u'oẽ' : u'ej', u'oẹ' : u'ej', 
u'oai' : u'aj', u'oái' : u'aj', u'oài' : u'aj', u'oải' : u'aj', u'oãi' : u'aj', u'oại' : u'aj',
u'oay' : u'ăj', u'oáy' : u'ăj', u'oày' : u'ăj', u'oảy' : u'ăj', u'oãy' : u'ăj', u'oạy' : u'ăj',
u'oao' : u'aw', u'oáo' : u'aw', u'oào' : u'aw', u'oảo' : u'aw', u'oão' : u'aw', u'oạo' : u'aw',
u'oeo' : u'ew', u'oéo' : u'ew', u'oèo' : u'ew', u'oẻo' : u'ew', u'oẽo' : u'ew', u'oẹo' : u'ew',
u'oeo' : u'ew', u'óeo' : u'ew', u'òeo' : u'ew', u'ỏeo' : u'ew', u'õeo' : u'ew', u'ọeo' : u'ew',
u'ueo' : u'ew', u'uéo' : u'ew', u'uèo' : u'ew', u'uẻo' : u'ew', u'uẽo' : u'ew', u'uẹo' : u'ew',
u'uai' : u'aj', u'uái' : u'aj', u'uài' : u'aj', u'uải' : u'aj', u'uãi' : u'aj', u'uại' : u'aj',
u'uay' : u'ăj', u'uáy' : u'ăj', u'uày' : u'ăj', u'uảy' : u'ăj', u'uãy' : u'ăj', u'uạy' : u'ăj',
u'uây' : u'ɤ̆j', u'uấy' : u'ɤ̆j', u'uầy' : u'ɤ̆j', u'uẩy' : u'ɤ̆j', u'uẫy' : u'ɤ̆j', u'uậy' : u'ɤ̆j'
}

C_codas = { u'p' : u'p', u't' : u'k', u'c' : u'k', u'm' : u'm', u'n' : u'ŋ', u'ng' : u'ŋ', u'nh' : u'n', u'ch' : u'k' }

# See Alves 2007 (SEALS XII), Vũ 1982
C_tones = { u'á' : 13, u'à' : 42, u'ả' : 312, u'ã' : 312, u'ạ' : u'21g', 
          u'ấ' : 13, u'ầ' : 42, u'ẩ' : 312, u'ẫ' : 312, u'ậ' : u'21g',
          u'ắ' : 13, u'ằ' : 42, u'ẳ' : 312, u'ẵ' : 312, u'ặ' : u'21g',
          u'é' : 13, u'è' : 42, u'ẻ' : 312, u'ẽ' : 312, u'ẹ' : u'21g',
          u'ế' : 13, u'ề' : 42, u'ể' : 312, u'ễ' : 312, u'ệ' : u'21g',
          u'í' : 13, u'ì' : 42, u'ỉ' : 312, u'ĩ' : 312, u'ị' : u'21g',
          u'ó' : 13, u'ò' : 42, u'ỏ' : 312, u'õ' : 312, u'ọ' : u'21g',
          u'ố' : 13, u'ồ' : 42, u'ổ' : 312, u'ỗ' : 312, u'ộ' : u'21g',
          u'ớ' : 13, u'ờ' : 42, u'ở' : 312, u'ỡ' : 312, u'ợ' : u'21g',
          u'ú' : 13, u'ù' : 42, u'ủ' : 312, u'ũ' : 312, u'ụ' : u'21g',
          u'ứ' : 13, u'ừ' : 42, u'ử' : 312, u'ữ' : 312, u'ự' : u'21g',
          u'ý' : 13, u'ỳ' : 42, u'ỷ' : 312, u'ỹ' : 312, u'ỵ' : u'21g',
          }

# used to use \u02C0 for raised glottal instead of g

C_tones_p = { u'á' : 5, u'à' : 2, u'ả' : 4, u'ã' : 4, u'ạ' : 6,
u'ấ' : 5, u'ầ' : 2, u'ẩ' : 4, u'ẫ' : 4, u'ậ' : 6,
u'ắ' : 5, u'ằ' : 2, u'ẳ' : 4, u'ẵ' : 4, u'ặ' : 6,
u'é' : 5, u'è' : 2, u'ẻ' : 4, u'ẽ' : 4, u'ẹ' : 6,
u'ế' : 5, u'ề' : 2, u'ể' : 4, u'ễ' : 4, u'ệ' : 6,
u'í' : 5, u'ì' : 2, u'ỉ' : 4, u'ĩ' : 4, u'ị' : 6,
u'ó' : 5, u'ò' : 2, u'ỏ' : 4, u'õ' : 4, u'ọ' : 6,
u'ố' : 5, u'ồ' : 2, u'ổ' : 4, u'ỗ' : 4, u'ộ' : 6,
u'ớ' : 5, u'ờ' : 2, u'ở' : 4, u'ỡ' : 4, u'ợ' : 6, 
u'ú' : 5, u'ù' : 2, u'ủ' : 4, u'ũ' : 4, u'ụ' : 6,
u'ứ' : 5, u'ừ' : 2, u'ử' : 4, u'ữ' : 4, u'ự' : 6, 
u'ý' : 5, u'ỳ' : 2, u'ỷ' : 4, u'ỹ' : 4, u'ỵ' : 6,
}

C_gi = { u'gi' : u'ji', u'gí': u'ji', u'gì' : u'ji', u'gì' : u'ji', u'gĩ' : u'ji', u'gị' : u'ji' }

C_qu = {u'quy' : u'wi', u'qúy' : u'wi', u'qùy' : u'wi', u'qủy' : u'wi', u'qũy' : u'wi', u'qụy' : u'wi'}
############################################

#south.py
#coding: utf-8

S_onsets = { u'b' : u'b', u't' : u't', u'th' : u'tʰ', u'đ' : u'd', u'ch' : u'c', 
				u'kh' : u'x', u'g' : u'ɣ', u'l' : u'l', u'm' : u'm', u'n': u'n', 
				u'ngh': u'ŋ', u'nh' : u'ɲ', u'ng' : u'ŋ', u'ph' : u'f', u'v' : u'j', 
				u'x' : u's', u'd' : u'j', u'h' : u'h', u'p' : u'p', u'qu' : u'w',
				u'gi' : u'j', u'tr' : u'ʈ', u'k' : u'k', u'c' : u'k', u'gh' : u'ɣ',
				u'r' : u'ʐ', u's' : u'ʂ', u'gi' : u'j'
			  }
			  
				         
S_nuclei = { u'a' : u'a', u'á' : u'a', u'à' : u'a', u'ả' : u'a', u'ã' : u'a', u'ạ' : u'a', 
				u'â' : u'ɤ̆', u'ấ' : u'ɤ̆', u'ầ' : u'ɤ̆', u'ẩ' : u'ɤ̆', u'ẫ' : u'ɤ̆', u'ậ' : u'ɤ̆',
				u'ă' : u'ă', u'ắ' : u'ă', u'ằ' : u'ă', u'ẳ' : u'ă', u'ẵ' : u'ă', u'ặ' : u'ă',
				u'e' : u'ɛ', u'é' : u'ɛ', u'è' : u'ɛ', u'ẻ' : u'ɛ', u'ẽ' : u'ɛ', u'ẹ' : u'ɛ',
				u'ê' : u'e', u'ế' : u'e', u'ề' : u'e', u'ể' : u'e', u'ễ' : u'e', u'ệ' : u'e',
				u'i' : u'i', u'í' : u'i', u'ì' : u'i', u'ỉ' : u'i', u'ĩ' : u'i', u'ị' : u'i',
				u'o' : u'ɔ', u'ó' : u'ɔ', u'ò' : u'ɔ', u'ỏ' : u'ɔ', u'õ' : u'ɔ', u'ọ' : u'ɔ',
				u'ô' : u'o', u'ố' : u'o', u'ồ' : u'o', u'ổ' : u'o', u'ỗ' : u'o', u'ộ' : u'o',
				u'ơ' : u'ɤ', u'ớ' : u'ɤ', u'ờ' : u'ɤ', u'ở' : u'ɤ', u'ỡ' : u'ɤ', u'ợ' : u'ɤ',
				u'u' : u'u', u'ú' : u'u', u'ù' : u'u', u'ủ' : u'u', u'ũ' : u'u', u'ụ' : u'u',
				u'ư' : u'ɯ', u'ứ' : u'ɯ', u'ừ' : u'ɯ', u'ử' : u'ɯ', u'ữ' : u'ɯ', u'ự' : u'ɯ',
				u'y' : u'i', u'ý' : u'i', u'ỳ' : u'i', u'ỷ' : u'i', u'ỹ' : u'i', u'ỵ' : u'i',
				
				u'eo' : u'eo', u'éo' : u'eo', u'èo' : u'eo', u'ẻo' : u'eo', u'ẽo': u'eo', u'ẹo' : u'eo',
				u'êu' : u'ɛu', u'ếu' : u'ɛu', u'ều' : u'ɛu', u'ểu' : u'ɛu', u'ễu': u'ɛu', u'ệu' : u'ɛu',
				u'ia' : u'iə', u'ía' : u'iə', u'ìa' : u'iə', u'ỉa' : u'iə', u'ĩa' : u'iə', u'ịa' : u'iə',
				u'ia' : u'iə', u'iá' : u'iə', u'ià' : u'iə', u'iả' : u'iə', u'iã' : u'iə', u'iạ' : u'iə',
				u'iê' : u'iə', u'iế' : u'iə', u'iề' : u'iə', u'iể' : u'iə', u'iễ' : u'iə', u'iệ' : u'iə',
				u'oo' : u'ɔ', u'óo' : u'ɔ', u'òo' : u'ɔ', u'ỏo' : u'ɔ', u'õo' : u'ɔ', u'ọo' : u'ɔ',
				u'oo' : u'ɔ', u'oó' : u'ɔ', u'oò' : u'ɔ', u'oỏ' : u'ɔ', u'oõ' : u'ɔ', u'oọ' : u'ɔ',
				u'ôô' : u'o', u'ốô' : u'o', u'ồô' : u'o', u'ổô' : u'o', u'ỗô' : u'o', u'ộô' : u'o',				                                 u'ôô' : u'o', u'ôố' : u'o', u'ôồ' : u'o', u'ôổ' : u'o', u'ôỗ' : u'o', u'ôộ' : u'o',				                              u'ua' : u'uə', u'úa' : u'uə', u'ùa' : u'uə', u'ủa' : u'uə', u'ũa' : u'uə', u'ụa' : u'uə',
				u'uô' : u'uə', u'uố' : u'uə', u'uồ' : u'uə', u'uổ' : u'uə', u'uỗ' : u'uə', u'uộ' : u'uə',
				u'ưa' : u'ɯə', u'ứa' : u'ɯə', u'ừa' : u'ɯə', u'ửa' : u'ɯə', u'ữa' : u'ɯə', u'ựa' : u'ɯə',
				u'ươ' : u'ɯə', u'ướ' : u'ɯə', u'ườ' : u'ɯə', u'ưở' : u'ɯə', u'ưỡ' : u'ɯə', u'ượ' : u'ɯə',
				u'yê' : u'iɛ', u'yế' : u'iɛ', u'yề' : u'iɛ', u'yể' : u'iɛ', u'yễ' : u'iɛ', u'yệ' : u'iɛ', 
                u'uơ' : u'uə',  u'uở' : u'uə', u'uờ': u'uə', u'uở' : u'uə', u'uỡ' : u'uə', u'uợ' : u'uə',
				}
				         
				         
S_offglides =  { u'ai' : u'aj', u'ái' : u'aj', u'ài' : u'aj', u'ải' : u'aj', u'ãi' : u'aj', u'ại' : u'aj',
				  u'ay' : u'ăj', u'áy' : u'ăj', u'ày' : u'ăj', u'ảy' : u'ăj', u'ãy' : u'ăj', u'ạy' : u'ăj',
				  u'ao' : u'aw', u'áo' : u'aw', u'ào' : u'aw', u'ảo' : u'aw', u'ão' : u'aw', u'ạo' : u'aw',
				  u'au' : u'ăw', u'áu' : u'ăw', u'àu' : u'ăw', u'ảu' : u'ăw', u'ãu' : u'ăw', u'ạu' : u'ăw',
				  u'ây' : u'ɤ̆j',  u'ấy' : u'ɤ̆j',  u'ầy' : u'ɤ̆j', u'ẩy' : u'ɤ̆j', u'ẫy' : u'ɤ̆j', u'ậy' : u'ɤ̆j', 
				  u'âu' : u'ɤ̆w', u'ấu' : u'ɤ̆w', u'ầu': u'ɤ̆w', u'ẩu' : u'ɤ̆w', u'ẫu' : u'ɤ̆w', u'ậu' : u'ɤ̆w',
				  u'eo' : u'ew', u'éo' : u'ew', u'èo' : u'ew', u'ẻo' : u'ew', u'ẽo' : u'ew', u'ẹo' : u'ew',
				  u'iu' : u'iw', u'íu' : u'iw', u'ìu' : u'iw', u'ỉu' : u'iw', u'ĩu' : u'iw', u'ịu' : u'iw',
				  u'oi' : u'ɔj', u'ói' : u'ɔj', u'òi' : u'ɔj', u'ỏi' : u'ɔj', u'õi' : u'ɔj', u'ọi' : u'ɔj',
				  u'ôi' : u'oj', u'ối' : u'oj', u'ồi' : u'oj', u'ổi' : u'oj', u'ỗi' : u'oj', u'ội' : u'oj',
				  u'ui' : u'uj', u'úi' : u'uj', u'ùi' : u'uj', u'ủi' : u'uj', u'ũi' : u'uj', u'ụi' : u'uj', 
				  u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj', 
				  u'ơi' : u'ɤj', u'ới' : u'ɤj', u'ời' : u'ɤj', u'ởi' : u'ɤj', u'ỡi' : u'ɤj', u'ợi' : u'ɤj', 
				  u'ưi' : u'ɯj', u'ứi' : u'ɯj', u'ừi' : u'ɯj', u'ửi' : u'ɯj', u'ữi' : u'ɯj', u'ựi' : u'ɯj', 
				  u'ưu' : u'ɯw', u'ứu' : u'ɯw', u'ừu' : u'ɯw', u'ửu' : u'ɯw', u'ữu' : u'ɯw', u'ựu' : u'ɯw',

				  u'iêu' : u'iəw', u'iếu' : u'iəw', u'iều' : u'iəw', u'iểu' : u'iəw', u'iễu' : u'iəw', u'iệu' : u'iəw',
				  u'yêu' : u'iəw', u'yếu' : u'iəw', u'yều' : u'iəw', u'yểu' : u'iəw', u'yễu' : u'iəw', u'yệu' : u'iəw', 
				  u'uôi' : u'uəj', u'uối' : u'uəj', u'uồi' : u'uəj', u'uổi' : u'uəj', u'uỗi' : u'uəj', u'uội' : u'uəj', 
				  u'ươi' : u'ɯəj', u'ưới' : u'ɯəj', u'ười' : u'ɯəj', u'ưởi' : u'ɯəj', u'ưỡi' : u'ɯəj', u'ượi' : u'ɯəj', 
				  u'ươu' : u'ɯəw', u'ướu' : u'ɯəw', u'ườu' : u'ɯəw', u'ưởu' : u'ɯəw', 'ưỡu' : u'ɯəw', u'ượu' : u'ɯəw'	 
			    }
				
S_onglides =   { u'oa' : u'a', u'oá' : u'a', u'oà' : u'a', u'oả' : u'a', u'oã' : u'a', u'oạ' : u'a', 
		              u'óa' : u'a', u'òa' : u'a', u'ỏa' : u'a', u'õa' : u'a', u'ọa' : u'a', 
			      u'oă' : u'ă', u'oắ' : u'ă', u'oằ' : u'ă', u'oẳ' : u'ă', u'oẵ' : u'ă', u'oặ' : u'ă', 	
			      u'oe' : u'e', u'oé' : u'e', u'oè' : u'e', u'oẻ' : u'e', u'oẽ' : u'e', u'oẹ' : u'e', 	
			      u'oe' : u'e', u'óe' : u'e', u'òe' : u'e', u'ỏe' : u'e', u'õe' : u'e', u'ọe' : u'e', 	
			      u'ua' : u'a', u'uá' : u'a', u'uà' : u'a', u'uả' : u'a', u'uã' : u'a', u'uạ' : u'a', 
			      u'uă' : u'ă', u'uắ' : u'ă', u'uằ' : u'ă', u'uẳ' : u'ă', u'uẵ' : u'ă', u'uặ' : u'ă', 	
			      u'uâ' : u'ɤ̆', u'uấ' : u'ɤ̆', u'uầ' : u'ɤ̆', u'uẩ' : u'ɤ̆', u'uẫ' : u'ɤ̆', u'uậ' : u'ɤ̆', 
			      u'ue' : u'ɛ', u'ué' : u'ɛ', u'uè' : u'ɛ', u'uẻ' : u'ɛ', u'uẽ' : u'ɛ', u'uẹ' : u'ɛ', 
			      u'uê' : u'e', u'uế' : u'e', u'uề' : u'e', u'uể' : u'e', u'uễ' : u'e', u'uệ' : u'e', 
			      u'uơ' : u'ɤ', u'uớ' : u'ɤ', u'uờ' : u'ɤ', u'uở' : u'ɤ', u'uỡ' : u'ɤ', u'uợ' : u'ɤ', 
			      u'uy' : u'i', u'uý' : u'i', u'uỳ' : u'i', u'uỷ' : u'i', u'uỹ' : u'i', u'uỵ' : u'i',
		          u'uya' : u'iə', u'uyá' : u'iə', u'uyà' : u'iə', u'uyả' : u'iə', u'uyã' : u'iə', u'uyạ' : u'iə', 
				  u'uyê' : u'iə', u'uyế' : u'iə', u'uyề' : u'iə', u'uyể' : u'iə', u'uyễ' : u'iə', u'uyệ' : u'iə', 
				  u'uyu' : u'iu', u'uyú' : u'iu', u'uyù' : u'iu', u'uyủ' : u'iu', u'uyũ' : u'iu', u'uyụ' : u'iu', 
				  u'uyu' : u'iu', u'uýu' : u'iu', u'uỳu' : u'iu', u'uỷu' : u'iu', u'uỹu' : u'iu', u'uỵu' : u'iu',
                  u'oen' : u'en', u'oén' : u'en', u'oèn' : u'en', u'oẻn' : u'en', u'oẽn' : u'en', u'oẹn' : u'en', 	
                  u'oet' : u'et', u'oét' : u'et', u'oèt' : u'et', u'oẻt' : u'et', u'oẽt' : u'et', u'oẹt' : u'et' 	
				}

S_onoffglides = { u'oe' : u'ej', u'oé' : u'ej', u'oè' : u'ej', u'oẻ' : u'ej', u'oẽ' : u'ej', u'oẹ' : u'ej', 
				   u'oai' : u'aj', u'oái' : u'aj', u'oài' : u'aj', u'oải' : u'aj', u'oãi' : u'aj', u'oại' : u'aj',
				   u'oay' : u'ăj', u'oáy' : u'ăj', u'oày' : u'ăj', u'oảy' : u'ăj', u'oãy' : u'ăj', u'oạy' : u'ăj',
				   u'oao' : u'aw', u'oáo' : u'aw', u'oào' : u'aw', u'oảo' : u'aw', u'oão' : u'aw', u'oạo' : u'aw',
				   u'oeo' : u'ew', u'oéo' : u'ew', u'oèo' : u'ew', u'oẻo' : u'ew', u'oẽo' : u'ew', u'oẹo' : u'ew',
				   u'oeo' : u'ew', u'óeo' : u'ew', u'òeo' : u'ew', u'ỏeo' : u'ew', u'õeo' : u'ew', u'ọeo' : u'ew',
				   u'ueo' : u'ew', u'uéo' : u'ew', u'uèo' : u'ew', u'uẻo' : u'ew', u'uẽo' : u'ew', u'uẹo' : u'ew',
				   u'uai' : u'aj', u'uái' : u'aj', u'uài' : u'aj', u'uải' : u'aj', u'uãi' : u'aj', u'uại' : u'aj',
				   u'uay' : u'ăj', u'uáy' : u'ăj', u'uày' : u'ăj', u'uảy' : u'ăj', u'uãy' : u'ăj', u'uạy' : u'ăj',
				   u'uây' : u'ɤ̆j', u'uấy' : u'ɤ̆j', u'uầy' : u'ɤ̆j', u'uẩy' : u'ɤ̆j', u'uẫy' : u'ɤ̆j', u'uậy' : u'ɤ̆j'
				 }

S_codas = { u'p' : u'p', u't' : u't', u'c' : u'k', u'm' : u'm', u'n' : u'ŋ', u'ng' : u'ŋ', u'nh' : u'n', u'ch' : u't' }

S_tones =   { u'á' : 45, u'à' : 32, u'ả' : 214, u'ã' : 214, u'ạ' : 212, 
		    u'ấ' : 45, u'ầ' : 32, u'ẩ' : 214, u'ẫ' : 214, u'ậ' : 212,
		    u'ắ' : 45, u'ằ' : 32, u'ẳ' : 214, u'ẵ' : 214, u'ặ' : 212,
		    u'é' : 45, u'è' : 32, u'ẻ' : 214, u'ẽ' : 214, u'ẹ' : 212,
            u'ế' : 45, u'ề' : 32, u'ể' : 214, u'ễ' : 214, u'ệ' : 212,
            u'í' : 45, u'ì' : 32, u'ỉ' : 214, u'ĩ' : 214, u'ị' : 212,
            u'ó' : 45, u'ò' : 32, u'ỏ' : 214, u'õ' : 214, u'ọ' : 212,
            u'ố' : 45, u'ồ' : 32, u'ổ' : 214, u'ỗ' : 214, u'ộ' : 212,
            u'ớ' : 45, u'ờ' : 32, u'ở' : 214, u'ỡ' : 214, u'ợ' : 212,
            u'ú' : 45, u'ù' : 32, u'ủ' : 214, u'ũ' : 214, u'ụ' : 212,
            u'ứ' : 45, u'ừ' : 32, u'ử' : 214, u'ữ' : 214, u'ự' : 212,
            u'ý' : 45, u'ỳ' : 32, u'ỷ' : 214, u'ỹ' : 214, u'ỵ' : 212,
			  }

S_tones_p = { u'á' : 5, u'à' : 2, u'ả' : 4, u'ã' : 4, u'ạ' : 6, 
		    u'ấ' : 5, u'ầ' : 2, u'ẩ' : 4, u'ẫ' : 4, u'ậ' : 6,
			u'ắ' : 5, u'ằ' : 2, u'ẳ' : 4, u'ẵ' : 4, u'ặ' : 6,
			u'é' : 5, u'è' : 2, u'ẻ' : 4, u'ẽ' : 4, u'ẹ' : 6,
			u'ế' : 5, u'ề' : 2, u'ể' : 4, u'ễ' : 4, u'ệ' : 6,
			u'í' : 5, u'ì' : 2, u'ỉ' : 4, u'ĩ' : 4, u'ị' : 6,
			u'ó' : 5, u'ò' : 2, u'ỏ' : 4, u'õ' : 4, u'ọ' : 6,
			u'ố' : 5, u'ồ' : 2, u'ổ' : 4, u'ỗ' : 4, u'ộ' : 6,
			u'ớ' : 5, u'ờ' : 2, u'ở' : 4, u'ỡ' : 4, u'ợ' : 6,
			u'ú' : 5, u'ù' : 2, u'ủ' : 4, u'ũ' : 4, u'ụ' : 6,
			u'ứ' : 5, u'ừ' : 2, u'ử' : 4, u'ữ' : 4, u'ự' : 6,
			u'ý' : 5, u'ỳ' : 2, u'ỷ' : 4, u'ỹ' : 4, u'ỵ' : 6,
			}


S_gi = { u'gi' : u'ji', u'gí': u'ji', u'gì' : u'ji', u'gì' : u'ji', u'gĩ' : u'ji', u'gị' : u'ji' }

S_qu = {u'quy' : u'wi', u'qúy' : u'wi', u'qùy' : u'wi', u'qủy' : u'wi', u'qũy' : u'wi', u'qụy' : u'wi'}

################################################3
import sys, codecs, re
from io import StringIO
from optparse import OptionParser
from string import punctuation

def trans(word, dialect, glottal, pham, cao, palatals):

    # This looks ugly, but newer versions of python complain about "from x import *" syntax
    if dialect == 'n':
        onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi = N_onsets, N_nuclei, N_codas, N_tones, N_onglides, N_offglides, N_onoffglides, N_qu, N_gi
    elif dialect == 'c':
        onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi = C_onsets, C_nuclei, C_codas, C_tones, C_onglides, C_offglides, C_onoffglides, C_qu, C_gi
    elif dialect == 's':
        onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi = S_onsets, S_nuclei, S_codas, S_tones, S_onglides, S_offglides, S_onoffglides, S_qu, S_gi


    #Custom
    onsets, nuclei, codas, onglides, offglides, onoffglides, qu, gi = Cus_onsets, Cus_nuclei, Cus_codas,  Cus_onglides, Cus_offglides, Cus_onoffglides, Cus_qu, Cus_gi



    if pham or cao:
        if dialect == 'n': tones_p = N_tones_p
        if dialect == 'c': tones_p = C_tones_p
        if dialect == 's': tones_p = S_tones_p

        #Custom
        tones_p = Cus_tones_p


        tones = tones_p

    ons = ''
    nuc = ''
    cod = ''
    ton = 0
    oOffset = 0
    cOffset = 0 
    l = len(word)

    if l > 0:
        if word[0:3] in onsets:         # if onset is 'ngh'
            ons = onsets[word[0:3]]
            oOffset = 3
        elif word[0:2] in onsets:       # if onset is 'nh', 'gh', 'kʷ' etc
            ons = onsets[word[0:2]]
            oOffset = 2
        elif word[0] in onsets:         # if single onset
            ons = onsets[word[0]]
            oOffset = 1

        if word[l-2:l] in codas:        # if two-character coda
            cod = codas[word[l-2:l]]
            cOffset = 2
        elif word[l-1] in codas:        # if one-character coda
            cod = codas[word[l-1]]
            cOffset = 1
                            

        #if word[0:2] == u'gi' and cod and len(word) == 3:  # if you just have 'gi' and a coda...
        if word[0:2] in gi and cod and len(word) == 3:  # if you just have 'gi' and a coda...
            nucl = u'i'
            ons = u'z'
        else:
            nucl = word[oOffset:l-cOffset]

        if nucl in nuclei:
            if oOffset == 0:
                if glottal == 1:
                    if word[0] not in onsets:   # if there isn't an onset....  
                        ons = u'ʔ'+nuclei[nucl] # add a glottal stop
                    else:                       # otherwise...
                        nuc = nuclei[nucl]      # there's your nucleus 
                else: 
                    nuc = nuclei[nucl]          # there's your nucleus 
            else:                               # otherwise...
                nuc = nuclei[nucl]              # there's your nucleus
        
        elif nucl in onglides and ons != u'kw': # if there is an onglide...
            nuc = onglides[nucl]                # modify the nuc accordingly
            if ons:                             # if there is an onset...
                ons = ons+u'w'                  # labialize it, but...
            else:                               # if there is no onset...
                ons = u'w'                      # add a labiovelar onset 

        elif nucl in onglides and ons == u'kw': 
            nuc = onglides[nucl]
                
        elif nucl in onoffglides:
            cod = onoffglides[nucl][-1]
            nuc = onoffglides[nucl][0:-1]
            if ons != u'kw':
                if ons:
                    ons = ons+u'w'
                else:
                    ons = u'w'
        elif nucl in offglides:
            cod = offglides[nucl][-1]
            nuc = offglides[nucl][:-1]
                
        elif word in gi:      # if word == 'gi', 'gì',...
            ons = gi[word][0]
            nuc = gi[word][1]

        elif word in qu:      # if word == 'quy', 'qúy',...
            ons = qu[word][:-1]
            nuc = qu[word][-1]
                
        else:   
            # Something is non-Viet
            return (None, None, None, None)


        # Velar Fronting (Northern dialect)
        if dialect == 'n':
            if nuc == u'a':
                if cod == u'k' and cOffset == 2: nuc = u'ɛ'
                if cod == u'ɲ' and nuc == u'a': nuc = u'ɛ'

            # Final palatals (Northern dialect)
            if nuc not in [u'i', u'e', u'ɛ']:
                if cod == u'ɲ': 
                    cod = u'ɲ' # u'ŋ'
            elif palatals != 1 and nuc in [u'i', u'e', u'ɛ']:
                if cod == u'ɲ': 
                    cod = u'ɲ'#u'ŋ'
            if palatals == 1:
                if cod == u'k' and nuc in [u'i', u'e', u'ɛ']: 
                    cod = u'c'

        # Velar Fronting (Southern and Central dialects)
        else:
            if nuc in [u'i', u'e']:
                if cod == u'k': cod = u't'
                if cod == u'ŋ': cod = u'n'

            # There is also this reverse fronting, see Thompson 1965:94 ff.
            elif nuc in [u'iə', u'ɯə', u'uə', u'u', u'ɯ', u'ɤ', u'o', u'ɔ', u'ă', u'ɤ̆']:
                if cod == u't': 
                    cod = u'k'
                if cod == u'n': cod = u'ŋ'

        # Monophthongization (Southern dialects: Thompson 1965: 86; Hoàng 1985: 181)
        if dialect == 's':
            if cod in [u'm', u'p']:
                if nuc == u'iə': nuc = u'i'
                if nuc == u'uə': nuc = u'u'
                if nuc == u'ɯə': nuc = u'ɯ'

        # Tones 
        # Modified 20 Sep 2008 to fix aberrant 33 error
        tonelist = [tones[word[i]] for i in range(0,l) if word[i] in tones]
        if tonelist:
            ton = str(tonelist[len(tonelist)-1])
        else:
            if not (pham or cao):
                if dialect == 'c':
                    ton = str('35')
                else:
                    ton = str('33')
            else:
                ton = str('1')
            
        # Modifications for closed syllables
        if cOffset !=0:

            # Obstruent-final nang tones are modal voice
            if (dialect == 'n' or dialect == 's') and ton == u'21g' and cod in ['p', 't', 'k']:
                #if ton == u'21\u02C0' and cod in ['p', 't', 'k']: # fixed 8 Nov 2016
                ton = u'21'

            # Modification for sắc in closed syllables (Northern and Central only)
            if ((dialect == 'n' and ton == u'24') or (dialect == 'c' and ton == u'13')) and cod in ['p', 't', 'k']:
                ton = u'45'

            # Modification for 8-tone system
            if cao == 1:
                if ton == u'5' and cod in ['p', 't', 'k']:
                    ton = u'5b'
                if ton == u'6' and cod in ['p', 't', 'k']:
                    ton = u'6b'

            # labialized allophony (added 17.09.08)
            if nuc in [u'u', u'o', u'ɔ']:
                if cod == u'ŋ':
                    cod = u'ŋ͡m' 
                if cod == u'k':
                    cod = u'k͡p'

        return (ons, nuc, cod, ton)
    
def convert(word, dialect, glottal, pham, cao, palatals, delimit):
    """Convert a single orthographic string to IPA."""

    ons = ''
    nuc = ''
    cod = ''
    ton = 0
    seq = ''

    try:
        (ons, nuc, cod, ton) = trans(word, dialect, glottal, pham, cao, palatals)
        if None in (ons, nuc, cod, ton):
            seq = u'['+word+u']'
        else:
            seq = delimit+delimit.join(filter(None, (ons, nuc, cod, ton)))+delimit
    except (TypeError):
        pass

    return seq
            


########################333
from vinorm import *
from underthesea import word_tokenize
import eng_to_ipa


SET=[S_onsets, S_nuclei, S_codas#, S_tones
    , S_onglides, S_offglides, S_onoffglides, S_qu, S_gi,     C_onsets, C_nuclei, C_codas#, C_tones
    , C_onglides, C_offglides, C_onoffglides, C_qu, C_gi,     N_onsets, N_nuclei, N_codas#, N_tones
    , N_onglides, N_offglides, N_onoffglides, N_qu, N_gi,     Cus_onsets, Cus_nuclei, Cus_codas#, N_tones
    , Cus_onglides, Cus_offglides, Cus_onoffglides, Cus_qu, Cus_gi]
DICT={}

#118 in total
syms=['ʷiə', 'ɯəw', 'iəw', 'ŋ͡m', 'ʷiu', 'k͡p', 'ɤ̆w', 'ɤ̆j', 'kwi', 'ʷɤ̆', 'ʷen', 'ɯəj', 'ʷet', 'uəj', 'iɛ', 't∫', 'ɑ:', 'tʰ', 'ɔj', 'ʷɛ', 'ɪə', 'tʃ', 'ɛj', 'iə', 'aɪ', 'əʊ', 'ɔɪ', 'ɯə', 'ɤ̆', 'aj', 'ɛu', 'ʷa', 'i:', 'ʷă', 'dʒ', 'ăw', 'oj', 'iw', 'aw', 'ʊə', 'eɪ', 'ɯw', 'ɯj', 'kw', 'uə', 'ɤj', 'ɜ:', 'uj', 'ɔ:', 'u:', 'eə', 'ăj', 'ew', 'ʷe', 'ʷi', 'zi', 'aʊ', 'ʷɤ', '?', 'd', 'ɔ', 'o', '.', 'k', 'p', 'η', 't', ',', 'g', ';', '2', 'θ', 'l', 'z', "'", 'n', 'ʒ', 's', 'f', 'm', 'e', 'ɛ', ':', '1', '4', 'ʂ', 'w', ' ', 'ɪ', 'ɲ', 'ð', 'ɣ', '_', 'æ', 'ʊ', 'ə', 'a', 'x', '6', 'v', 'r', 'ɯ', '∫', '!', 'ʈ', 'u', 'i', 'ɤ', 'j', 'ʐ', '5', 'ɒ', '3', 'ă', 'b', 'ŋ', 'h', 'ʌ']
def getSymbol():
    for s in SET:
        DICT.update(s)
    list_phoneme=DICT.values()
    list_phoneme=list(list_phoneme)
    English_phoneme=["p","b","t","d","t∫","dʒ","k","g","f","v","ð","θ","s","z","∫","ʒ","m","n","η","l","r","w","j","ɪ","i:","ʊ","u:","e","ə","ɜ:","ɒ","ɔ:","æ","ʌ","ɑ:","ɪə","ʊə","eə","eɪ","ɔɪ","aɪ","əʊ","aʊ"]
    word_pad = ["_"]
    space = [" "]
    tone=["1","2","3","4","5","6"]
    punctuation = [".",",","!",":","?",";","'"] #" ' ( ) Have been removed due to none sound

    modifi = ["k͡p","ŋ͡m"]

    symbols = list_phoneme + space+word_pad + English_phoneme + punctuation + tone + modifi
    symbols = list(set(symbols))
    symbols.sort(reverse = True,key=len) 
    return symbols

def vi2IPA_pitrain(text):
    epi = epitran.Epitran('vie-Latn')
    r=epi.transliterate(text)
    return r


def T2IPA(text):
    sys.path.append('./Rules')      # make sure we can find the Rules files
    #Setup option
    glottal = 0
    pham = 0 
    cao = 0
    palatals = 0
    tokenize = 0
    delimit = ''
    dialect='n' #"c""s"
    tone_type=0
    if tone_type==0:
        pham=1
    else:
        cao=1
    #Input text
    line = text
    if line =='\n':
        return ""
    else:
        compound = u''
        ortho = u'' 
        words = line.split()
        ## toss len==0 junk
        words = [word for word in words if len(word)>0]
        ## hack to get rid of single hyphens or underscores
        words = [word for word in words if word!=u'-']
        words = [word for word in words if word!=u'_']
        for i in range(0,len(words)):
            word = words[i].strip()
            ortho += word
            word = word.strip(punctuation).lower()
            ## 29.03.16: check if tokenize is true
            ## if true, call this routine for each substring
            ## and re-concatenate 
            if (tokenize and '-' in word) or (tokenize and '_' in word):
                substrings = re.split(r'(_|-)', word)
                values = substrings[::2]
                delimiters = substrings[1::2] + ['']
                ipa = [convert(x, dialect, glottal, pham, cao, palatals, delimit).strip() for x in values]
                seq = ''.join(v+d for v,d in zip(ipa, delimiters))
            else:
                seq = convert(word, dialect, glottal, pham, cao, palatals, delimit).strip()
            # concatenate
            if len(words) >= 2:
                ortho += ' '
            if i < len(words)-1:
                seq = seq+u' '
            compound = compound + seq
        return compound
EN={"a":"ây","ă":"á","â":"ớ","b":"bi","c":"si","d":"đi","đ":"đê","e":"i","ê":"ê","f":"ép","g":"giy","h":"ếch","i":"ai","j":"giây","k":"cây","l":"eo","m":"em","n":"en","o":"âu","ô":"ô","ơ":"ơ","p":"pi","q":"kiu","r":"a","s":"ét","t":"ti","u":"diu","ư":"ư","v":"vi","w":"đắp liu","x":"ít","y":"quai","z":"giét"}
import re
def vi2IPA(text):
    print("------------------------------------------------------")
    TN= TTSrawUpper_punc_unknown(text)
    print("------------------------------------------------------")
    print("Text normalize:              ",TN)
    TK= word_tokenize(TN)
    print("Vietnamese Tokenize:         ",TK)
    IPA=""
    for tk in TK:
        ipa = T2IPA(tk).replace(" ","_")
        if ipa =="":
            IPA+=tk+" "
        elif ipa[0]=="[" and ipa[-1]=="]":
            eng = eng_to_ipa.convert(tk)
            if eng[-1] == "*":
                if tk.lower().upper() == tk:
                    #Đọc tiếng anh từng chữ
                    letter2sound=""
                    for char in tk:
                        CHAR = str(char).lower()
                        if CHAR in list(EN.keys()):
                            letter2sound+=EN[CHAR]+" "
                        else:
                            letter2sound+=char+" "
                    IPA+=T2IPA(letter2sound)+" "
                else:
                    #Giữ nguyên
                    IPA+=tk+" "
            else:
                IPA+=eng+" "
            #Check tu dien tieng anh Etrain bưc
            #Neu co Mapping
            #Neu khong, check co nguyen am
            #Neu co de nguyen
            #Neu khong danh van
            print("                                    ..................Out of domain word: " ,ipa)
        else:
            IPA+=ipa+" "
    IPA=re.sub(' +', ' ', IPA)
    print("IPA Vietnamese:             ",IPA)
    print("------------------------------------------------------")
    return IPA

def checkDict():
    cout=0
    trung=0
    List_token=[]
    List_pair = []
    with open("Popular.txt", encoding="utf-8") as f:
        content=f.read().splitlines()
        for line in content:
            #nor_tr = vi2IPA_pitrain(line)
            #nor = vi2IPA(line)
            nor = T2IPA(line)
            if nor in List_token:
                print(line + "  -> "+nor)
                trung +=1
                List_pair.append(line)
            List_token.append(nor)
            if nor=="":
                cout+=1
                print(line)
    print("Number of token can not convert: ",cout)
    print("Number of token in the same mapping:",trung)
    List_token = list(set(List_token))
    #print(List_token)
    print(len(List_token))
    ################################
    #Looking for pair
    Pair = {}
    for lt in List_pair:
        Pair[T2IPA(lt)] = lt
    cout_same=0
    with open("Popular.txt", encoding="utf-8") as f:
        content=f.read().splitlines()
        for line in content:
            if T2IPA(line) in Pair:
                lin2 =Pair[T2IPA(line)]
                if line != lin2:
                    if (lin2[0]=="k" and line[0]=="c") or (lin2[-1] in ['i','í','ì','ĩ','ỉ','ị'] and line[-1] in ['y','ý','ỳ','ỷ','ỹ','ỵ']) or (lin2[-1] in ['y','ý','ỳ','ỷ','ỹ','ỵ'] and line[-1] in ['i','í','ì','ĩ','ỉ','ị']):
                        continue
                    cout_same+=1
                    print(line+ "  <-> " + lin2 +"\t\t:\t\t"+T2IPA(line))
    print("Same pair:" , cout_same)

    #Các trường hợp dẫn đến trùng âm là:  
    # Phương ngữ khác nhau đã thống nhất ở list custom  
    # Các trường hợp có cách bỏ dấu khác nhau đều gộp chung làm một 

    #Disable convert from 'ɲ' to 'ɲ'' in north
    #Các âm vòng ở đây i chang không vòm: không có w ở trước như: "oa,ua,a" đều như một > must consider (nhưng nếu thêm vào ảnh hưởng chữ qu cũng ra w)
                #Try to add ʷ to all start o and u as in wiki
    
    #Same positive
    #k <-> c
    #g <-> gh
    #i <-> y

    #Same negative / need to fix
    #oe <-> uê   -> fix oe from e to ɛ
    #âm cuối: ch : k theo bắc : t theo nam -> custom k vì nó giảm trùng nhiều hơn 241->153 case
              #Tuy nhiên cuối cùng "ch" "c" "t" không phân âm được => ý tưởng mượn "tʃ" trong teach and watch để thay thế => k for c , t for t, tʃ for ch
    #Thay offglide: úy -> wi để phân biệt với úi


    #Remain
    '''
    di  <-> gi              :               zi1
    dìm  <-> gìm            :               zim2
    din  <-> gin            :               zin1
    díp  <-> gíp            :               zip5
    gen  <-> ghen           :               ɣɛn1
    ghì  <-> gì             :               ɣi2
    ghích  <-> gích         :               ɣitʃ5
    ia  <-> iê              :               iə1
    iêu  <-> yêu            :               iəw1
    khoắng  <-> khuắng              :               xwʷăŋ5
    khỏe  <-> khoẻ          :               xwʷɛ4
    khua  <-> khuơ          :               xuə1
    lóe  <-> loé            :               lwʷɛ5
    ngét  <-> nghét         :               ŋɛt5
    ngễu  <-> nghễu         :               ŋɛu3
    nghía  <-> ngía         :               ŋiə5
    nghịu  <-> ngịu         :               ŋiw6
    nghoèo  <-> ngoèo               :               ŋwew2
    quít  <-> quýt          :               kwit5
    thủa  <-> thuở          :               tʰuə4
    tòe  <-> toè            :               twʷɛ2
    ua  <-> uơ              :               uə1
    ưa  <-> ươ              :               ɯə1
    xõa  <-> xoã            :               swʷa3
    '''

    #Ở đây tiết kiệm chi phí chạy máy không normal phoneme về cường độ âm sắc chỉ dừng từ 1->6
    #học ác cho kết quả "c" khác nhau



###################################################

#checkDict()
print(vi2IPA("Ngày hôm nay phải làm xong cái vinorm kết hợp vái viegraph WTO và wro"))

#print(len(getSymbol()))
#print(getSymbol())

'''
test="t"
if test in syms:
    print(test)
else:
    print("none")
'''

###################################################

#Step
#Vinorm
#Underthesea
#For each Convert to phoneme
#Nếu không được check phoneme tiếng anh
#Nếu không có trong từ tiếng anh -> đọc từng kí tự



#Now
#+Thêm kí tự IPA của tiếng ANH
#+Thêm xử lí case không có cũng như case Tiếng anh: => dùng etrain cho tiếng anh
#+Deal case thống nhất âm vực phoneme -> ok
#+Get lại bộ symbol