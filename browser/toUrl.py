import sys
import webbrowser

args = sys.argv
if len(args) != 2:
    raise Exception('参数有误')

chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

if args[1] == 'test':
    webbrowser.get('chrome').open('http://120.26.209.59:8080/cdsq-manage')
elif args[1] == 'demo':
    webbrowser.get('chrome').open('http://120.26.209.59:8081/demo')
elif args[1] == 'product':
    webbrowser.get('chrome').open('http://120.26.61.219:8080/cdsq-manage')
elif args[1] =='jdk':
    webbrowser.get('chrome').open('http://docs.oracle.com/javase/8/docs/api/')
elif args[1] == 'jq' or args[1] == 'jquery':
    webbrowser.get('chrome').open('http://jquery.cuishifeng.cn/')
elif args[1] == 'bug':
    webbrowser.open('https://www.tracup.com')
elif args[1] == 'scala':
    webbrowser.get('chrome').open('http://docs.scala-lang.org/api/all.html')

