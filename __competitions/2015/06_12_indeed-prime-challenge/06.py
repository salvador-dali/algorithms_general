from sklearn import linear_model
def analysis(arr, window):
    X, Y = [], []
    for i in xrange(len(arr) - window):
        X.append(arr[i: i + window])
        Y.append(arr[i + window])

    model = linear_model.LogisticRegression(C=1e5)
    model.fit(X, Y)

    s = 0
    answers = []
    for i in xrange(50):
        last = arr[-window:]
        ans = model.predict(last)[0]
        arr.append(ans)
        answers.append(ans)

    return s, answers


arr = [int(raw_input().split()[3]) for i in xrange(545)]
e, ans1 = analysis([i for i in arr], 5)
e, ans2 = analysis([i for i in arr], 25)
e, ans3 = analysis([i for i in arr], 40)
e, ans4 = analysis([i for i in arr], 50)

for i in xrange(50):
    print int(round( (ans1[i] + ans1[i] + ans1[i] + ans1[i]) / 4.0 ))
