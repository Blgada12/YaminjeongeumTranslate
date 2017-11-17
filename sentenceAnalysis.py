import konlpy
import nltk


a = u'아버지가 방에 들어가신다'
b = u'며용'

kkma_words_1 = konlpy.tag.Kkma().pos(a)
kkma_words_2 = konlpy.tag.Kkma().pos(b)

Twitter_words_1 = konlpy.tag.Twitter().pos(a)
Twitter_words_2 = konlpy.tag.Twitter().pos(b)

grammar = """
NP: {<N.*>*<Suffix>?}   
VP: {<V.*>*}            
AP: {<A.*>*}           
"""
parser = nltk.RegexpParser(grammar)

print("kkma 비교")
print(parser.parse(kkma_words_1).pprint())
print(parser.parse(kkma_words_2).pprint())

print("\nTwitter 비교")
print(parser.parse(Twitter_words_1).pprint())
print(parser.parse(Twitter_words_2).pprint())
