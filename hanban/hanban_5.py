import requests,time,re
from lxml import etree
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), tests_type varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')


sql_cookies = "SELECT * FROM hanban_cookies WHERE HSKlevel='HSK五级'"
cur_105.execute(sql_cookies)
hanban_cookies = cur_105.fetchall()
print(len(hanban_cookies))
for hanban_cookie in hanban_cookies[8:]:
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
    print('111111222222')
    listening_part1 = ['第一部分'] * 20 + ['第二部分']*10
    listening_type1 = ['选择题'] * 30
    listening_title1 = [''] * 30
    listening_choice1 = []
    listening_choice1_type = ['txt']*30
    for url_str in urls_str[:30]:
        listening_part1_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part1_html = requests.get(listening_part1_url, headers=headers).text
        sel = etree.HTML(listening_part1_html)
        listening_part1_choice_texts = sel.xpath('//td/text()')
        listening_part1_choice = []
        for listening_part1_choice_text in listening_part1_choice_texts[2::2]:
            listening_part1_choice.append(listening_part1_choice_text.replace('\r\n', ' ').replace('\xa0', ' ').replace(' ', ''))
        listening_choice1.append('    '.join(listening_part1_choice))
    print(len(listening_choice1))

    print('22222')
    listening_part2 = ['第二部分']*15
    listening_type2 = ['选择题'] * 15
    listening_title2 = [''] * 15
    listening_choice2 = []
    listening_choice2_type = ['txt']*25
    for url_str in [urls_str[30],urls_str[32],urls_str[35],urls_str[38],urls_str[41],urls_str[43]]:
        listening_part2_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part2_html = requests.get(listening_part2_url, headers=headers).text
        sel = etree.HTML(listening_part2_html)
        listening_part2_choice_texts = sel.xpath('//td[@class="tdColumns2"]/text()')
        listening_part2_choice_one = []
        if len(listening_part2_choice_texts) == 8:
            listening_choice2.append('    '.join(listening_part2_choice_texts[:4]))
            listening_choice2.append('    '.join(listening_part2_choice_texts[4:]))
        else:
            listening_choice2.append('    '.join(listening_part2_choice_texts[:4]))
            listening_choice2.append('    '.join(listening_part2_choice_texts[4:8]))
            listening_choice2.append('    '.join(listening_part2_choice_texts[8:]))
    print(len(listening_choice2))

    model_2 = '阅读'
    print('333333')
    listening_part3 = ['第一部分'] * 15
    listening_type3 = ['选择题'] * 15
    listening_title3 = []
    listening_choice3 = []
    listening_choice3_type = ['txt'] * 15
    nums_part3 = [n for n in range(46,61)]
    texts_values = [nums_part3[:3], nums_part3[3:7], nums_part3[7:11], nums_part3[11:15]]
    for text_values,url_str in zip(texts_values,[urls_str[45]] + [urls_str[48]] + [urls_str[52]] + [urls_str[56]]):
        listening_part3_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part3_html = requests.get(listening_part3_url, headers=headers).text
        sel = etree.HTML(listening_part3_html)
        listening_part3_title_texts = []
        listening_part3_title_strs = re.findall(r'&nbsp[\s\S]+?</div>', listening_part3_html)[0]
        listening_part3_title_text = re.sub(r'&[\S]+?;', '', re.sub(r'<[\s\S]+?>', '____{}____',listening_part3_title_strs.replace('<br />', '').replace(' ', '')[:-6]))
        if len(text_values) ==3:
            listening_part3_title = listening_part3_title_text.format(text_values[0], text_values[1], text_values[2])
        else:
            listening_part3_title = listening_part3_title_text.format(text_values[0], text_values[1], text_values[2], text_values[3])
        listening_title3 += [listening_part3_title] * len(text_values)
        listening_part3_choice_texts = sel.xpath('//td[@class="tdColumns1"]/text()')
        listening_part3_choice_one = []
        for i in range(len(text_values)):
            listening_choice3.append('    '.join(listening_part3_choice_texts[4*i:4*(i+1)]))
    print(len(listening_title3))
    print(len(listening_choice3))

    print('444444')
    reading_part4 = ['第二部分']*10
    reading_type4 = ['选择题']*10
    reading_title4 = []
    reading_choice4 = []
    reading_choice4_type = ['txt']*10
    for url_str in urls_str[60:70]:
        reading_part4_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part4_html = requests.get(reading_part4_url, headers=headers).text
        sel = etree.HTML(reading_part4_html)
        reading_part4_title = sel.xpath('//div[@class="singleChoicePrompt"]/text()')[0]
        reading_title4.append(reading_part4_title)
        reading_part4_choice_strs = sel.xpath('//td/text()')
        reading_part4_choice = []
        for reading_part4_choice_text in reading_part4_choice_strs[2::2]:
            reading_part4_choice.append(reading_part4_choice_text.replace('\r\n', ' ').replace('\xa0', ' ').replace(' ', ''))
        reading_choice4.append('    '.join(reading_part4_choice))
    print(len(reading_title4))
    print(len(reading_choice4))

    print('555555')
    reading_part5 = ['第二部分'] * 20
    reading_type5 = ['选择题'] * 20
    reading_title5 = []
    reading_choice5 = []
    reading_choice5_type = ['txt'] * 20
    for url_str in urls_str[70:90][0::4]:
        reading_part5_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part5_html = requests.get(reading_part5_url, headers=headers).text
        sel = etree.HTML(reading_part5_html)
        reading_part5_title_strs_1 = sel.xpath('//div[@class="readingPromptHorizontal"]/text()')
        reading_part5_title_1 = re.sub('\xa0', '', ''.join(reading_part5_title_strs_1))

        reading_part5_title_strs_2 = sel.xpath('//div[@class="readingSubItemPrompt"]/text()')
        for reading_part5_title_str_2 in reading_part5_title_strs_2:
            reading_part5_title_2 = reading_part5_title_str_2.replace('\r\n', '').replace('\xa0', '').replace(' ', '')[3:]
            reading_part5_title = reading_part5_title_1 + '&&' + reading_part5_title_2
            reading_title5.append(reading_part5_title)
        reading_part5_choice_texts = sel.xpath('//td[@class="tdColumns1"]/text()')
        for i in range(4):
            reading_choice5.append('    '.join(reading_part5_choice_texts[4*i:4*(i+1)]))
    print(len(reading_title5))
    print(len(reading_choice5))

    model_3 = '写作'
    print('666666')
    writing_part6 = ['第一部分'] * 8
    writing_type6 = ['词条排序'] * 8
    writing_title6 = ['']*8
    writing_choice6 = []
    writing_choice6_type = ['txt']*8
    choices_1 = ['A', 'B', 'C', 'D']
    choices_2 = ['A', 'B', 'C', 'D', 'E']
    for url_str in urls_str[90:98]:
        writing_part6_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        writing_part6_html = requests.get(writing_part6_url, headers=headers).text
        sel = etree.HTML(writing_part6_html)
        writing_part6_choice_strs = sel.xpath('//div[@class="DragBox"]/text()')
        writing_part6_choices = []
        if len(writing_part6_choice_strs) ==4:
            for choice,writing_part6_choice_str in zip(choices_1,writing_part6_choice_strs):
                writing_part6_choice = choice + '、' + writing_part6_choice_str
                writing_part6_choices.append(writing_part6_choice)
            writing_choice6.append('    '.join(writing_part6_choices))
        else:
            for choice,writing_part6_choice_str in zip(choices_2,writing_part6_choice_strs):
                writing_part6_choice = choice + '、' + writing_part6_choice_str
                writing_part6_choices.append(writing_part6_choice)
            writing_choice6.append('    '.join(writing_part6_choices))
    print(len(writing_choice6))

    print('777777')
    writing_part7 = ['第二部分']
    writing_type7 = ['用词语写短文']
    writing_title7 = []
    writing_choice7 = []
    writing_choice7_type = ['txt']
    for url_str in urls_str[98:99]:
        writing_part7_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:-21]
        writing_part7_html = requests.get(writing_part7_url, headers=headers).text
        sel = etree.HTML(writing_part7_html)
        writing_part7_title = sel.xpath('//div[@id="divPromptArea"]/text()')[0]
        writing_title7.append(writing_part7_title)
        writing_part7_choice = sel.xpath('//div[@id="divPromptArea"]/text()')[1].replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', '、')
        writing_choice7.append(writing_part7_choice)
    print(writing_title7)
    print(writing_choice7)

    print('888888')
    writing_part8 = ['第二部分']
    writing_type8 = ['结合图片写短文']
    writing_title8 = []
    writing_choice8 = []
    writing_choice8_type = ['image']
    for url_str in urls_str[99:]:
        writing_part8_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:-21]
        writing_part8_html = requests.get(writing_part8_url, headers=headers).text
        sel = etree.HTML(writing_part8_html)
        writing_part8_title = sel.xpath('//div[@id="divPromptArea"]/text()')[0]
        writing_title8.append(writing_part8_title)
        writing_part8_choice = 'http://mnks.cnhsk.org' + sel.xpath('//img/@src')[0]
        writing_choice8.append(writing_part8_choice)
    print(writing_title8)
    print(writing_choice8)

    response_text = requests.get(audios_url).text
    audios_str = re.findall(r'<url>(.+?)</url>', response_text)
    audio_urls = []
    for audio_str in audios_str:
        if 'AssessmentItems' in audio_str:
            audio_url = 'http://mnks.cnhsk.org/mnks/' + audio_str
            audio_urls.append(audio_url)
    audios = audio_urls[:20] + audio_urls[20:30] + [audio_urls[30]]*2 + [audio_urls[31]]*3 + [audio_urls[32]]*3 + [audio_urls[33]]*3 + [audio_urls[34]]*2 + [audio_urls[35]]*2 + ['']*55
    print(len(audios))

    models = [model_1]*45 + [model_2]*45 + [model_3]*10
    parts = listening_part1 + listening_part2 + listening_part3 + reading_part4 + reading_part5 + writing_part6 + writing_part7 + writing_part8
    types = listening_type1 + listening_type2 + listening_type3 + reading_type4 + reading_type5 + writing_type6 + writing_type7 + writing_type8
    numbers = [n for n in range(1,101)]
    titles = listening_title1 + listening_title2 + listening_title3 + reading_title4 + reading_title5 + writing_title6 + writing_title7 + writing_title8
    choices = listening_choice1 + listening_choice2 + listening_choice3 + reading_choice4 + reading_choice5 + writing_choice6 + writing_choice7 + writing_choice8
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + reading_choice4_type + reading_choice5_type + writing_choice6_type + writing_choice7_type + writing_choice8_type
    print(len(models), len(parts), len(types), len(numbers), len(titles), len(choices), len(choices_type))

    for model, part, type, num, title, choice, choice_type, answer_str, audio in zip(models,parts,types,numbers,titles,choices,choices_type,answers_str,audios):
    # for model, part, type, num, title, choice, choice_type, answer_str, audio in zip(models[98:], parts[98:], types[98:], numbers[98:],titles[98:], choices[98:], choices_type[98:],answers_str[98:], audios[98:]):
        try:
            answer = answer_str.xpath('td[{}]/text()'.format(str(len(answer_str.xpath('td')) - 2)))[0]
        except:
            answer = '略'
        onedata = (
        HSKlevel, test_name, model, part, type, num, title, choice, choice_type, answer, audio)
        print(onedata)
        sql = 'insert into hanban (HSKlevel, test_name, model, part, tests_type, num, title, choice, choice_type, answer, audio) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur_105.execute(sql, onedata)
        con_105.commit()

cur_105.close()
con_105.close()




