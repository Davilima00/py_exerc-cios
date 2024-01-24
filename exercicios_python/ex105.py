def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'boa'
        if r['media'] >= 5:
            r['situacao'] = 'rasoavel'
        if r['media'] >= 5:
            r['situacao'] = 'ruim'

    return r


resp = notas(5.6, 2, 5, 6, sit=True)
print(resp)