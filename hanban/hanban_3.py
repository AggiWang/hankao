import requests,time,re
from lxml import etree
# from selenium import webdriver
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), tests_type varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')


sql_cookies = "SELECT * FROM hanban_cookies WHERE HSKlevel='HSK三级'"
cur_105.execute(sql_cookies)
hanban_cookies = cur_105.fetchall()
print(len(hanban_cookies))
for hanban_cookie in hanban_cookies[:1]:
    HSKlevel = hanban_cookie[1]
    test_name = hanban_cookie[2]
    print(test_name)
    audios_url = hanban_cookie[3]
    cookies = hanban_cookie[4]

    url = 'http://mnks.cnhsk.org/Mnks/Exam/Result.aspx'
    headers = {
        'Cookie': cookies,
    }
    html = requests.get(url, headers=headers).text
    sel = etree.HTML(html)
    urls_str = sel.xpath('//tr[@align="center"]/td/a/@href')
    answers_str = sel.xpath('//tr[@align="center"]')

    model_1 = '听力'
    print('111111')
    listening_part1 = ['第一部分'] * 10
    listening_type1 = ['选择题'] * 10
    listening_title1 = [''] * 10
    listening_choice1 = []
    listening_choice1_type = ['image']*10
    choices = ['A', 'B', 'C', 'D', 'E', 'F'] * 2
    for url_str in urls_str[:10]:
        listening_part1_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part1_html = requests.get(listening_part1_url, headers=headers).text
        sel = etree.HTML(listening_part1_html)
        listening_part1_imgs_str = sel.xpath('//img/@src')
        listening_choice1_one = []
        for choice, listening_part1_img_str in zip(choices, listening_part1_imgs_str):
            listening_part1_img = choice + '、' + 'http://mnks.cnhsk.org' + listening_part1_img_str
            listening_choice1_one.append(listening_part1_img)
        listening_choice1.append('    '.join(listening_choice1_one))
    print(len(listening_choice1))

    print('222222')
    listening_part2 = ['第二部分'] * 10
    listening_type2 = ['判断题'] * 10
    listening_title2 = [''] * 10
    listening_choice2 = []
    listening_choice2_type = ['txt']*10
    for url_str in urls_str[10:20]:
        listening_part2_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part2_html = requests.get(listening_part2_url, headers=headers).text
        sel = etree.HTML(listening_part2_html)
        listening_part2_text = sel.xpath('//div[@class="judgementPrompt"]/text()')[0]
        # print(listening_part2_text.replace('\xa0', ' ').replace(' ', ''))
        listening_choice2.append(listening_part2_text.replace('\xa0', ' ').replace(' ', ''))
    print(len(listening_choice2))

    print('333333444444')
    listening_part3 = ['第三部分']*10 + ['第四部分']*10
    listening_type3 = ['选择题'] * 20
    listening_title3 = [''] * 20
    listening_choice3 = []
    listening_choice3_type = ['txt']*20
    for url_str in urls_str[20:40]:
        listening_part3_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part3_html = requests.get(listening_part3_url, headers=headers).text
        sel = etree.HTML(listening_part3_html)
        listening_part3_texts = sel.xpath('//td/text()')
        listening_part3_choice_one = []
        for listening_part3_text in listening_part3_texts[2::2]:
            listening_part3_choice_one.append(listening_part3_text.replace('\n', '').replace('\r', '').replace(' ', ''))
        listening_choice3.append('    '.join(listening_part3_choice_one))
    print(len(listening_choice3))

    model_2 = '阅读'
    print('555555666666')
    reading_part5 = ['第一部分']*10 + ['第二部分']*10
    reading_type5 = ['选择题']*20
    reading_title5 = []
    reading_choice5 = []
    reading_choice5_type = ['txt']*20
    choices_1 = ['A', 'B', 'C', 'D', 'E', 'F']
    choices_2 = ['A', 'B', 'C', 'D', 'E']
    for e,url_str in zip([n for n in range(20)], urls_str[40:60]):
        reading_part5_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part5_html = requests.get(reading_part5_url, headers=headers).text
        sel = etree.HTML(reading_part5_html)
        reading_part5_title_strs = sel.xpath('//div[@class="readingSubItemsVertical"]/div[{}]/div/div/text()'.format(e%5+1))
        reading_part5_title = '    '.join(reading_part5_title_strs)[3:]
        reading_title5.append(reading_part5_title.replace('\n', '').replace('\r', '').replace(' ', '').replace('\xa0', ' '))
        reading_part5_choice_strs = sel.xpath('//div[@class="readingPromptVertical"]/text()')
        reading_part5_choice = ' '.join(reading_part5_choice_strs).split('例')[0]
        reading_part5_choice_texts = re.split(r'[A-Z]', reading_part5_choice)
        if len(reading_part5_choice_texts) == 7:
            reading_part5_choices = []
            for choice_1, reading_part5_choice_text in zip(choices_1, reading_part5_choice_texts[1:]):
                reading_part5_choice = choice_1 + '、' + re.sub(r'(\xa0)+?', '', reading_part5_choice_text.replace(r' ', ''))
                reading_part5_choices.append(reading_part5_choice)
        else:
            reading_part5_choices = []
            for choice_2, reading_part5_choice_text in zip(choices_2, reading_part5_choice_texts[1:]):
                reading_part5_choice = choice_2 + '、' + re.sub(r'(\xa0)+?', '', reading_part5_choice_text.replace(r' ', ''))
                reading_part5_choices.append(reading_part5_choice)
        reading_choice5.append('    '.join(reading_part5_choices))
    print(len(reading_title5))
    print(len(reading_choice5))

    print('777777')
    reading_part7 = ['第三部分'] * 10
    reading_type7 = ['选择题'] * 10
    reading_title7 = []
    reading_choice7 = []
    reading_choice7_type = ('txt,' * 10).split(',')[:-1]
    for url_str in urls_str[60:70]:
        reading_part7_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part7_html = requests.get(reading_part7_url, headers=headers).text
        sel = etree.HTML(reading_part7_html)
        reading_part7_title_strs = sel.xpath('//div[@class="singleChoicePrompt"]/text()')
        reading_part7_title = ''.join(reading_part7_title_strs).replace('\xa0', '')
        reading_title7.append(reading_part7_title)
        reading_part7_choice_strs = sel.xpath('//td/text()')
        reading_part7_choices = []
        reading_part7_choice = '&'.join(reading_part7_choice_strs[2::2])
        reading_choice7.append(re.sub('\r\n', '', reading_part7_choice).replace(' ', '').replace('&', '    '))
    print(len(reading_title7))
    print(len(reading_choice7))

    model_3 = '写作'
    print('888888')
    writing_part8 = ['第一部分'] * 5
    writing_type8 = ['词条排序'] * 5
    writing_title8 = ['']*5
    writing_choice8 = []
    writing_choice8_type = ('txt,' * 5).split(',')[:-1]
    choices = ['A', 'B', 'C', 'D']
    for url_str in urls_str[70:75]:
        writing_part8_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        writing_part8_html = requests.get(writing_part8_url, headers=headers).text
        sel = etree.HTML(writing_part8_html)
        writing_part8_choice_strs = sel.xpath('//div[@class="DragBox"]/text()')
        writing_part8_choices = []
        for choice,writing_part8_choice_str in zip(choices,writing_part8_choice_strs):
            writing_part8_choice = choice + '、' + writing_part8_choice_str
            writing_part8_choices.append(writing_part8_choice)
        writing_choice8.append('    '.join(writing_part8_choices))
    print(len(writing_choice8))

    print('999999')
    writing_part9 = ['第二部分'] * 5
    writing_type9 = ['填空题'] * 5
    writing_title9 = []
    writing_choice9 = ['']*5
    writing_choice9_type = ('image,' * 5).split(',')[:-1]
    for url_str in urls_str[75:80]:
        writing_part9_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:-21]
        writing_part9_html = requests.get(writing_part9_url, headers=headers).content
        sel = etree.HTML(writing_part9_html)
        writing_part9_title = 'http://mnks.cnhsk.org' + sel.xpath('//img/@src')[0]
        writing_title9.append(writing_part9_title)
    print(len(writing_title9))


    response_text = requests.get(audios_url).text
    audios_str = re.findall(r'<url>(.+?)</url>', response_text)
    audio_urls = []
    for audio_str in audios_str:
        if 'AssessmentItems' in audio_str:
            audio_url = 'http://mnks.cnhsk.org/mnks/' + audio_str
            audio_urls.append(audio_url)
    audios = [audio_urls[0]]*5 + [audio_urls[1]]*5 + audio_urls[4:14] + audio_urls[15:25] + audio_urls[26:36] + (','*40).split(',')[:-1]
    print(len(audios))

    models = [model_1]*40 + [model_2]*30 + [model_3]*10
    parts = listening_part1 + listening_part2 + listening_part3  + reading_part5 + reading_part7 + writing_part8 + writing_part9
    types = listening_type1 + listening_type2 + listening_type3 + reading_type5 + reading_type7 + writing_type8 + writing_type9
    numbers = [n for n in range(1,81)]
    titles = listening_title1 + listening_title2 + listening_title3  + reading_title5 + reading_title7 + writing_title8 + writing_title9
    choices = listening_choice1 + listening_choice2 + listening_choice3  + reading_choice5 + reading_choice7 + writing_choice8 + writing_choice9
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + reading_choice5_type + reading_choice7_type + writing_choice8_type + writing_choice9_type
    print(len(models), len(parts), len(types), len(numbers), len(titles), len(choices), len(choices_type))

    for model, part, type, num, title, choice, choice_type, answer_str, audio in zip(models,parts,types,numbers,titles,choices,choices_type,answers_str,audios):
        answer = answer_str.xpath('td[{}]/text()'.format(str(len(answer_str.xpath('td')) - 2)))[0]
        onedata = (
        HSKlevel, test_name, model, part, type, num, title, choice, choice_type, answer, audio)
        print(onedata)
        sql = 'insert into hanban (HSKlevel, test_name, model, part, tests_type, num, title, choice, choice_type, answer, audio) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur_105.execute(sql, onedata)
        con_105.commit()

cur_105.close()
con_105.close()




