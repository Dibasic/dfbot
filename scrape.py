from lxml import html
import io, re, requests, string

clause_pattern = re.compile(r'(?:[.,;] +|\n{2,})')
date_pattern = re.compile(r'^ *\d\d/\d\d/\d\d\d\d')
release_pattern = re.compile(r'^[\n\t\s]*Released ')
file = open('notes.txt', 'w')

def handle_year(year):
    return handle_url(f'http://www.bay12games.com/dwarves/dev_{year}.html')

def handle_url(url):
    page = requests.get(url)
    if page.status_code == 200:
        handle_content(page.content)
        return True
    else:
        return False

def handle_content(content):
    tree = html.fromstring(content)
    posts = tree.xpath('//li')
    for post in posts:
        try:
            handle_text(post.text_content())
        except Exception as e:
            handle_text(''.join(filter(lambda x: x in string.printable, post.text_content())))

def handle_text(text):
    file.write(clause_pattern.sub('\n', (text + '\n')))

def main():
    global file
    year = 2004
    while True:
        status = handle_year(year)
        if (status):
            year += 1
        else:
            break
    handle_url('http://www.bay12games.com/dwarves/index.html')
    file.close()

    file = open('notes.txt', 'r')
    lines = []
    for line in file.readlines():
        if len(line) > 12 and not re.match(date_pattern, line) and not re.match(release_pattern, line):
            lines.append(line.strip('\t').strip('\n').lstrip(' '))
    file.close()
    file = open('notes.txt', 'w')
    for line in lines:
        file.write(line + '\n')
    file.close()

main()