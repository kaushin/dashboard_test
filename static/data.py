import json
with open('/home/myu/Python/dashboard/dashboard/static/fake_test_results.json', 'r') as fp:
    data = json.loads(fp.read())
    lst = []
    ct = 11
    for line in data:
        dct = {}
        dct['model'] = 'graph_dash.TestResult'
        dct['pk'] = ct
        ct = ct + 1
        dct['fields'] = { 'date':line['date'], 'application':line['case'], 'result':line['pass'] }
        lst.append(dct)
    with open('/home/myu/Python/dashboard/dashboard/static/test.json','w') as wf:
        json.dump(lst, wf)
