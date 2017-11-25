import konlpy
import sys
from PyQt5.QtWidgets import *

def yaminList(p0):
    rep_arr_small = [

        ["대", "머"],
        ["머", "대"],

        ["파", "과"],
        ["과", "파"],

        ["댕", "멍"],
        ["멍", "댕"],

        ["피", "괴"],
        ["괴", "피"],

        ["커", "귀"],
        ["귀", "커"],
        ["멋", "댓"],
        ["댓", "멋"],
        ["괏", "팟"],
        ["팟", "괏"],


        ["늒", "뉴"],
        ["앟", "왕"],
        ["팡", "광"],
        ["비", "네"],
        ["ㄹ", "근"],
        ["흑", "후"],
        ["맣", "싸"],
        ["늑", "누"],
        ["띠", "며"],
        ["며", "띠"],
        ["빅", "넥"],
        ["윽", "우"],
        ["판", "관"],
        ["믁", "무"],
        ["㕦", "못"],
        ["거", "지"],
        ["븍", "부"],
        ["지", "거"],
        ["거", "지"],
        ["싀", "식"],
        ["튽", "장"],
        ["넨", "빈"],
        ["띵", "명"],
        ["극", "구"],
        ["긘", "리"],
        ["뫼", "민"],
        ["익", "의"],
        ["읶", "위"],
        ["돠", "단"],
        ["뫄", "만"],
        ["E", "든"],
        ["네", "비"],
        ["화", "한"],
        ["틴", "된"],
        ["즉", "주"],
        ["화", "한"],
        ["슥", "수"],
        ["티", "되"],
        ["뢰", "린"],
        ["외", "인"],
        ["믂", "뮤"],
        ["윾", "유"],
        ["봐", "반"],
    ]
    rep_arr = rep_arr_small * 10
    rep_arr2 = [
        ["01", "이"],
        ["7ㅣ", "기"],
        ["SE", "또"],
    ]

    for i in range(0, len(rep_arr)):
       for j in range(0, len(p0)):
            temp = p0[j]
            for k in range(0, len(p0[j])):
                if temp[k] == rep_arr[i][0]:
                    temp = temp[:k] + rep_arr[i][1] + temp[k + 1:]
                    isex = False
                    for f in range(0, len(p0)):
                        if p0[f] == temp:
                            isex = True
                    if not isex:
                        p0.append(temp)

    for i in range(0, len(rep_arr2)):
        for j in range(0, len(p0)):
            temp = p0[j]
            for k in range(0, len(temp) - 1):
                try:
                    if (temp[k] + temp[k + 1]) == rep_arr2[i][0]:
                        temp = temp[:k] + rep_arr2[i][1] + temp[k + 2:]
                        isex = False
                        for f in range(0, len(p0)):
                            if p0[f] == temp:
                                isex = True
                        if not isex:
                            p0.append(temp)
                except:
                    pass

    return p0


def yamin(p0):
    rtn = []
    rtn.append(p0)
    rtn = yaminList(rtn)

    return rtn


def nounNext(p0):
    if not (p0.find('SC') == -1) or \
            not (p0.find('MAJ') == -1) or \
            not (p0.find('JKS') == -1) or \
            not (p0.find('JKC') == -1) or \
            not (p0.find('JKG') == -1) or \
            not (p0.find('JKO') == -1) or \
            not (p0.find('JKB') == -1) or \
            not (p0.find('JKV') == -1) or \
            not (p0.find('JKQ') == -1) or \
            not (p0.find('JC') == -1) or \
            not (p0.find('JC') == -1) or \
            not (p0.find('XSN') == -1):
        return 4
    return 0


def adjNext(p0):
    if not (p0.find('ETM') == -1) or \
            not (p0.find('EP') == -1) or \
            not (p0.find('EC') == -1):
        return 4
    return 0


def verbNext(p0):
    if not (p0.find('EP') == -1) or \
            not (p0.find('ETM') == -1) or \
            not (p0.find('NNB') == -1):
        return 4
    return 0


def gwanNext(p0):
    if not (p0.find('NNG') == -1) or \
            not (p0.find('NNP') == -1) or \
            not (p0.find('NNB') == -1) or \
            not (p0.find('NR') == -1) or \
            not (p0.find('NP') == -1):
        return 4
    return 0


def VCPNext(p0):
    if not (p0.find('EF') == -1):
        return 4
    return 0


def XRNext(p0):
    if not (p0.find('XSV') == -1) or \
            not (p0.find('XSA') == -1):
        return 4
    return 0


def longscore(p0):
    if len(p0) == 1:
        return 0
    elif len(p0) == 2:
        return 4
    elif len(p0) == 3:
        return 16
    elif len(p0) == 4:
        return 64
    else:
        return 256



def comfile(p0):
    words = []
    score = []
    for arr in p0:
        words.append(konlpy.tag.Mecab().pos(arr))
        score.append(0)
    for i in range(0, len(p0)):
        print(words[i])
        for j in range(0, len(words[i])):
            for k in words[i][j][1].split('+'):

                if words[i][j][0] == '슥':
                    score[i] -= 4

                if words[i][j][0] == '머':
                    score[i] -= 1

                if words[i][j][0] == '지':
                    score[i] += 4
                    try:
                        if words[i][j + 1][0] == '게':
                            score[i] += 4
                    except:
                        pass
                try:
                    if words[i][j][0] == '이':
                        if words[i][j + 1][1] == "SN":
                            score[i] -= 4
                except:
                    pass
                try:
                    if words[i][j][0] + words[i][j + 1][0] == '이며':
                        score[i] += 6

                except:
                    pass
                if words[i][j][0] == '멍멍이':
                    score[i] += 8
                if k == 'NNG':
                    if words[i][j][0] == '현지':
                        score[i] += 4
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += 2 * longscore(words[i][j][0])

                if k == 'NNP':
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += longscore(words[i][j][0])

                if k == 'NNB':
                    try:
                        if words[i][j][0] == "거":
                            if words[i][j + 1][0] == "에서":
                                score[i] += 4
                            if words[i][j + 1][0] == "라":
                                score[i] += 4
                    except:
                        pass
                    if words[i][j][0] == "건지":
                        score[i] += 6
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'NR':
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'NP':
                    if words[i][j][0] == "누구":
                        score[i] += 4
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += longscore(words[i][j][0])

                if k == 'VV':
                    try:
                        score[i] += verbNext(words[i][j][1].split('+')[1])
                        score[i] += verbNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += 2 * longscore(words[i][j][0])

                if k == 'VA':
                    if words[i][j][0] == "귀엽":
                        score[i] += 8
                    try:
                        score[i] += adjNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += longscore(words[i][j][0])

                if k == 'VCP':
                    try:
                        score[i] += VCPNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'VCN':
                    try:
                        score[i] += VCPNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'MM':
                    try:
                        score[i] += gwanNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += longscore(words[i][j][0])

                if k == 'MAG':
                    score[i] += longscore(words[i][j][0])
                    if words[i][j][0] == '단지':
                        score[i] += 6
                if k == 'EC':
                    if words[i][j][0] == '지만':
                        score[i] += 10
                    if words[i][j][0] == '라며':
                        score[i] += 4
                    if words[i][j][0] == '인지':
                        score[i] += 4
                    if words[i][j][0] == '네요':
                        score[i] += 10
                if k == 'XSN':
                    try:
                        score[i] += nounNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += 2 * longscore(words[i][j][0])

                if k == 'XSV':
                    if words[i][j][0] == '되':
                        score[i] += 4
                    try:
                        score[i] += verbNext(words[i][j][1].split('+')[1])
                        score[i] += verbNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'XSA':
                    try:
                        score[i] += adjNext(words[i][j + 1][1])
                    except:
                        pass

                if k == 'XR':
                    try:
                        score[i] += XRNext(words[i][j + 1][1])
                    except:
                        pass
                    score[i] += longscore(words[i][j][0])
                if k == 'SH':
                    score[i] -= 64

                if k == 'SL':
                    score[i] -= longscore(words[i][j][0])
                    score[i] -= 4
                if k == 'XPN':
                    if words[i][j][0] == "명":
                        score[i] += 4
                if k == 'SN':
                    try:
                        if words[i][j + 1][0] == '이':
                            score[i] -= 4
                    except:
                        pass
                    score[i] -= 6

                if k == 'UNKNOWN':
                    score[i] -= longscore(words[i][j][0])
                    score[i] -= 4

    highscore = score[0]

    for i in range(0, len(p0)):
        if highscore <= score[i]:
            highscore = score[i]

    high = []
    for i in range(0, len(p0)):
        if highscore == score[i]:
            high.append(i)
    rtn = []
    for i in high:
        rtn.append(p0[i])

    return rtn




class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(640, 360, 640, 360)
        self.setWindowTitle("아민정음 해독기")
        global lineEdit
        lineEdit = QLineEdit("", self)
        lineEdit.setGeometry(20,20,520,20)
        lineEdit.returnPressed.connect(self.btn1_clicked)

        btn1 = QPushButton("입력", self)
        btn1.setGeometry(560, 20, 60, 20)
        btn1.clicked.connect(self.btn1_clicked)
        global viewresult
        viewresult = QLabel("결과: ", self)
        viewresult.setGeometry(20,40,600,300)

    def btn1_clicked(self):
        global viewresult
        global lineEdit
        viewr = "결과: "
        result = comfile(yamin(lineEdit.text()))
        for arr in result:
            viewr += "\n"+arr

        viewresult.setText(viewr)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()



