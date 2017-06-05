# news_crawler


### HOW TO USE
`python mongodb.py`


### HOW TO ADD A NEW MODULE
1. write your module `*.py` refer to `tech_164.py` or `auto_163.py`
2. add `import *` to `mongodb.py`
3. add your name of module to `mod = [tech_163, auto_163, *]`
* define a news item as:

```
item = {'title': title,
        'date': date,
        'content': content,
        'cate': 'tech',
        'src': '163',
        'link': link,
        }
```
