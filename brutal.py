from urllib.request import urlopen
from bs4 import BeautifulSoup
import pathlib

def main():
  # base contains the head element and the first two boxes
  base = ''''''
  soup = BeautifulSoup(urlopen('http://brutalistwebsites.com').read(), 'html.parser')
  soup.head.append(soup.new_tag('meta', charset='utf-8'))
  base += str(soup.head) + '\n'
  boxes = soup('div', {'class', 'box'});
  base += str(boxes[0]) + '\n' + str(boxes[1]) + '\n'
  del boxes[0]
  mainBody = ''''''
  pagenum = 1;
  for index, box in enumerate(boxes):
    # skip the first two entries, since i'm already adding those via the base var
    if index < 1:
      continue

    print('index ' + str(index))
    mainBody += str(box) + '\n';
    # every 10 entries, make a new page
    if index % 10 == 0:
      print('page ' + str(pagenum))
      generatePage(base, mainBody, pagenum, False)
      mainBody = ''''''
      pagenum += 1

  generatePage(base, mainBody, pagenum, True)
  pass

def generatePage(head, body, number, last):
  # print(body)
  pathlib.Path('./' + str(number)).mkdir(parents=True, exist_ok=True)
  prevPage = '<div class="box"><a href="/' + str(number - 1) + '">Previous</a></div>\n'
  nextPage = '<div class="box"><a href="/' + str(number + 1) + '">Next</a></div>\n'
  html = head + '<body>\n' + body
  if number > 1:
    html += prevPage
  if not last:
    html += nextPage
  html += '</body>'
  with open('./' + str(number) + "/index.html", "w") as file:
    file.write(html)
  if number == 1:
    with open('./index.html', 'w') as file:
      file.write(html)

  # generate html
  pass

if __name__ == "__main__":
  main()