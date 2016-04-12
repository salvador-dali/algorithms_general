# https://www.interviewbit.com/problems/pretty-json/

def pretty(s):
    num_of_tabs = 0
    res, line = [], ''
    for i in s:
        line = line.strip()
        if i in ['{', '[']:
            if line:
                res.append('\t' * num_of_tabs + line)
            res.append('\t' * num_of_tabs + i)
            num_of_tabs += 1
            line = ''
        elif i in ['}', ']']:
            if line:
                res.append('\t' * num_of_tabs + line)
            num_of_tabs -= 1
            res.append('\t' * num_of_tabs + i)

            line = ''
        elif i == ',':
            if res[-1][-1] in [']', '}']:
                res[-1] += ','
            else:
                res.append('\t' * num_of_tabs + line + ',')
            line = ''
        else:
            line += i

    return res

s = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
# s = '["foo", {"bar":["baz",null,1.0,2]}]'
s = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
for i in pretty(s):
    print i