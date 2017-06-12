# Xpath_Generator
Generate Xpath list after giving tag, attribute and attribute' value.

## Dependences

* [requests](http://docs.python-requests.org/en/master/)
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Install

* With pip: `pip install xpath_generator`
* With git: 
  1. `git clone https://github.com/Terryhung/Xpath_Generator.git`
  2. `pip install -r requirements.txt`

## Usage

```python
from xpath_generator.xpath_generator import XpathGEN

url = 'https://guides.github.com/activities/hello-world/'

element = {
    'tag': 'a',
    'attr': 'id',
    'attr_value': 'intro'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4)\
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/58.0.3029.96 Safari/537.36'
}

# default parent_layers is 5
xpath_gen = XpathGEN(url, element, parent_layers=3, headers=headers)
xpaths = xpath_gen.get_xpaths()

```
Return Value:

```
{
  'xpaths': 
    [
      '//div[@class="wrap"]/div[@class="markdown-body content-body "]/p/a[@id="intro"]'
    ]
}
```
