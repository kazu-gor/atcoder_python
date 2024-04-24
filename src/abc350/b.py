"""
高橋君には、穴 1,2,…,N に 1 本ずつ、全部で N 本の歯が生えています。
歯医者の青木君は、これらの歯と穴に対して、 Q 回の治療を行います。
i 回目の治療では、穴 T iを治療します。治療内容は次の通りです。
穴 T iに歯が生えている場合、穴 T iから歯を抜く。
そうでない ( 穴 T iに歯が生えていない) 場合、穴 T iに歯を生やす。
全ての治療が終わった後、高橋君に生えている歯の本数は何本ですか?
"""

N,  Q = map(int, input().split())
T = list(map(int, input().split()))

extraction = []
for t in T:
    if t not in extraction:
        extraction.append(t)
    else:
        extraction.remove(t)

print(N - len(extraction))

