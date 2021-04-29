# Probabilistic Context-Free Grammar (PCFG)
확률에 기반하여 문장들의 규칙 추출 및 빈도수 분석

</br>

## 프로젝트 기간
- 대학원 2학기 전산언어학 수업의 파이널 프로젝트로 진행하였다.
- 프로젝트 기간 : 2019.12.05 ~ 2019.12.25

</br>

## 기술 스택
- Python 3.7.3

</br>

## CFG
### CFG의 정의
- CFG는 형식 문법의 한 종류이며 V -> w의 생성 규칙을 가지고 있다. 여기서 V는 비말단(non-terminal) 기호이며 w는 말단(terminal) 기호들로 구성된 문자열을 의미한다.  
- 예를들어, CFG는 S -> NP VP 또는 N -> king과 같은 규칙들로 표현이 된다.  
- CFG는 4개의 원소로 정의가 된다. G = (N, ∑, R, S)  
(1) N : 비말단 기호의 집합  
(2) ∑ : 말단기호의 집합  
(3) R : 생성 규칙의 집합  
(4) S : N의 원소이며 시작기호를 지정  
- CFG는 Phrase Structure Grammars(PSG) 또는 Backus Naur Form(BNF) 라고도 불러진다.  

</br>

### CFG의 문제점
- CFG는 모호성(ambiguity)을 가진 결과물을 만들어 낼 수 있다. 즉, 하나의 문장에서 여러 결과물이 나올 수 있다.  
- 사람은 언어적인 지식을 이용하여 어떤 것이 올바른 결과물인지 쉽게 알아낼 수 있지만 컴퓨터는 그러지 못하다.  
- 예를들어, “I saw the man with the telescope” 라는 문장이 주어졌을 때 두 개의 뜻으로 해석이 가능하다.  
(1) 나는 망원경으로 그 남자를 보았다.  
(2) 나는 망원경을 가지고 있는 남자를 보았다.  
- 따라서 모호성을 해소하기 위해서는 추가적인 작업이 필요하다.  

</br>

## PCFG
- PCFG는 CFG에 확률개념을 적용한 생성 문법이다.  
- CFG는 5개의 원소로 정의가 된다. G = (M,T,R,S,P)  
(1) M : 비말단 기호의 집합  
(2) T : 말단기호의 집합  
(3) R : 생성 규칙의 집합  
(4) S : M의 원소이며 시작기호를 지정  
(5) P : 생성 규칙의 확률

</br>

## 데이터
- 브라운 코퍼스를 사용했으며, 해당 코퍼스는 193개의 파일과 438,141개의 중복되는 생성 규칙을 가지고 있다.  
- 파일의 트리구조 예시
```
( (S (S (PP In
            (NP American romance))
        ,
        (NP-SBJ-2 almost nothing)
        (VP rates
            (S (NP-SBJ *-2)
                (ADJP-PRD (ADJP higher)
                    (PP than
                        (SBAR-NOM (WHNP-1 what)
                            (S (NP-SBJ the movie men)
                                (VP have
                                    (VP called
                                        (S (NP-SBJ *T*-1)
                                            ''
                                            (S-NOM-PRD (NP-SBJ *)
                                                (VP meeting
                                                    (NP cute)))
                                            ''))))))))))
```
</br>

## 알고리즘
- 스택을 이용하여 규칙 추출  
    - [소스코드 확인](https://github.com/biscayan/PCFG/blob/master/PCFG.py)  

        <details>
        <summary>수도코드</summary>
        <div markdown="1">

            def rule extraction ():

            input file = ‘brown.prd’
            output file = ‘brown rule.txt’

            token stack = Stack()
            rule stack = Stack()

            tokens = the elements which are separated as a blank

            for token in tokens:
                if token is not ‘)’:
                    push token into the token stack
                else:
                    while the element of token stack is not ‘(’:
                        popped token = the last element of the token stack
                        push popped token into the rule stack

                    remove ‘(’ from the token stack
                    extract left hand side from the rule stack

                    write left hand side in the output file
                    write ‘→’ in the output file

                    push left hand side into the token stack

                    while rule stack is not empty:
                        extract right hand side from the rule stack
                        write right hand side in the output file
                        write a space in the output file

                    write new line in the output file

        </div>
        </details>

</br>

## 수행 결과
- 193개의 파일로부터 96,906개의 중복되지 않는 규칙들을 추출하였다.  
- 생각보다 많은 규칙들이 추출되었는데, 이는 문법트리에서 단어들이 the(Det), cook(Verb), he(Pronoun)처럼 단어 단위로 품사 태깅이 세분화되어 있지 않고 the(NP), cook(VP), he(NP)처럼 구 단위로 태깅이 되어있기 때문으로 보인다.  
- Top 5 규칙

    |Rank|Rule|Frequency|
    |:---:|:---:|:---:|
    |1|S -> NP SBJ VP|30,112|
    |2|S -> |20,864|
    |3|PP -> of NP|10,313|
    |4|NP -> NP PP|8,983|
    |5|VP -> to VP|5,898|