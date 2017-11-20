import konlpy

def yamin():
    print("입력 : ")
    __input = input()
    __input = __input.replace('ㄹ','근')

    rtn = []

    rtn.append(__input)

    return rtn

_input = yamin()

words = []
for arr in _input:
    words.append(konlpy.tag.Mecab().pos(arr))


print("Mecab")
for i in range(0,len(words)):
    print(words[i])
    for j in range(0, len(words[i])):
        for k in words[i][j][1].split('+'):

            if k == 'NNG':
                print('일반 명사 : ' + words[i][j][0])

            if k == 'NNP':
                print('고유 명사 : ' + words[i][j][0])

            if k == 'NNB':
                print('의존 명사 : ' + words[i][j][0])

            if k == 'NR':
                print('사 : ' + words[i][j][0])

            if k == 'NP':
                print('대명사 : ' + words[i][j][0])

            if k == 'VV':
                print('동사 : ' + words[i][j][0])

            if k == 'VA':
                print('형용 : ' + words[i][j][0])

            if k == 'VX':
                print('보조 용언 : ' + words[i][j][0])

            if k == 'VCP':
                print('긍정 지정사 : ' + words[i][j][0])

            if k == 'VCN':
                print('부정 지정사 : ' + words[i][j][0])

            if k == 'MM':
                print('관형사 : ' + words[i][j][0])

            if k == 'MAG':
                print('일반 부사 : ' + words[i][j][0])

            if k == 'MAJ':
                print('접속 부사 : ' + words[i][j][0])

            if k == 'IC':
                print('감탄사 : ' + words[i][j][0])

            if k == 'JKS':
                print('주격 조사 : ' + words[i][j][0])

            if k == 'JKC':
                print('보격 조사 : ' + words[i][j][0])

            if k == 'JKG':
                print('관형격 조사 : ' + words[i][j][0])

            if k == 'JKO':
                print('목적격 조사 : ' + words[i][j][0])

            if k == 'JKB':
                print('부사격 조사 : ' + words[i][j][0])

            if k == 'JKV':
                print('호격 조사 : ' + words[i][j][0])

            if k == 'JKQ':
                print('인용격 조사 : ' + words[i][j][0])

            if k == 'JC':
                print('접속 조사 : ' + words[i][j][0])

            if k == 'JX':
                print('보조사 조사 : ' + words[i][j][0])

            if k == 'EP':
                print('선어말어미 : ' + words[i][j][0])

            if k == 'EF':
                print('종결 어미 : ' + words[i][j][0])

            if k == 'EC':
                print('연결 어미 : ' + words[i][j][0])

            if k == 'ETN':
                print('명사형 전성 어미 : ' + words[i][j][0])

            if k == 'ETM':
                print('관형형 전성 어미 : ' + words[i][j][0])

            if k == 'XPN':
                print('체언 접두사 : ' + words[i][j][0])

            if k == 'XSN':
                print('명사 파생 접미사 : ' + words[i][j][0])

            if k == 'XSV':
                print('동사 파생 접미사 : ' + words[i][j][0])

            if k == 'XSA':
                print('형용사 파생 접미사 : ' + words[i][j][0])

            if k == 'XR':
                print('어근 : ' + words[i][j][0])

            if k == 'SF':
                print('마침표 물음표 느낌표 : ' + words[i][j][0])

            if k == 'SE':
                print('줄임표 ... : ' + words[i][j][0])

            if k == 'SSO':
                print('여는 괄호 : ' + words[i][j][0])

            if k == 'SSC':
                print('닫는 괄호 : ' + words[i][j][0])

            if k == 'SC':
                print('구분자 : ' + words[i][j][0])

            if k == 'SY':
                print('기타 기호 : ' + words[i][j][0])

            if k == 'SH':
                print('한자 : ' + words[i][j][0])

            if k == 'SL':
                print('외국어 : ' + words[i][j][0])

            if k == 'SN':
                print('숫자 : ' + words[i][j][0])

