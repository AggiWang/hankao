import requests,time,re
from lxml import etree
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), tests_type varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')


sql_cookies = "SELECT * FROM hanban_cookies WHERE HSKlevel='HSK六级'"
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
    listening_part1 = ['第一部分'] * 15
    listening_type1 = ['选择题'] * 15
    listening_title1 = [''] * 15
    listening_choice1 = []
    listening_choice1_type = ['txt']*15
    for url_str in urls_str[:15]:
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
    listening_choice2_type = ['txt']*15
    for url_str in urls_str[15:30][0::5]:
        listening_part2_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part2_html = requests.get(listening_part2_url, headers=headers).text
        sel = etree.HTML(listening_part2_html)
        listening_part2_choice_texts = sel.xpath('//td[@class="tdColumns1"]/text()')
        for i in range(5):
            listening_choice2.append('    '.join(listening_part2_choice_texts[4*i:4*(i+1)]))
    print(len(listening_choice2))

    print('333333')
    listening_part3 = ['第三部分'] * 20
    listening_type3 = ['选择题'] * 20
    listening_title3 = [''] * 20
    listening_choice3 = []
    listening_choice3_type = ['txt'] * 20
    # for url_str in [urls_str[30], urls_str[33], urls_str[36], urls_str[39], urls_str[43], urls_str[47]]:
    for url_str in [urls_str[30], urls_str[33], urls_str[37], urls_str[40], urls_str[43], urls_str[47]]:
        listening_part3_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part3_html = requests.get(listening_part3_url, headers=headers).text
        sel = etree.HTML(listening_part3_html)
        listening_part3_choice_texts = sel.xpath('//td[@class="tdColumns1"]/text()')
        for i, listening_part3_choice_text in zip(range(int(len(listening_part3_choice_texts)/4)), listening_part3_choice_texts):
            listening_choice3.append('    '.join(listening_part3_choice_texts[4 * i:4 * (i + 1)]))
    print(len(listening_choice3))

    model_2 = '阅读'
    print('444444555555')
    reading_part4 = ['第一部分']*10 + ['第二部分']*10
    reading_type4 = ['选择题']*20
    reading_title4 = []
    reading_choice4 = []
    reading_choice4_type = ['txt']*20
    for url_str in urls_str[50:70]:
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

    print('666666')
    reading_part6 = ['第三部分'] * 10
    reading_type6 = ['选择题'] * 10
    reading_title6 = []
    reading_choice6 = []
    reading_choice6_type = ['txt'] * 10
    nums_part6 = [[n for n in range(71,76)], [n for n in range(76,81)]]
    for num_part6,url_str in zip(nums_part6,urls_str[70:80][0::5]):
        reading_part6_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part6_html = requests.get(reading_part6_url, headers=headers).text
        # print(reading_part6_html)
        sel = etree.HTML(reading_part6_html)
        reading_part6_title_texts = []
        reading_part6_title_strs = re.findall(r'&nbsp[\s\S]+?<br />A', reading_part6_html)[0][:-1]
        reading_part6_title_text = re.sub(r'&[\S]+?;', '', re.sub(r'<[\s\S]+?/>', '' ,re.sub(r'<input[\s\S]+?>', '____{}____',reading_part6_title_strs.replace('<br />', '').replace(' ', ''))))
        reading_part6_title = reading_part6_title_text.format(num_part6[0],num_part6[1],num_part6[2],num_part6[3],num_part6[4])
        reading_title6 += [reading_part6_title] * 5
        reading_part6_choice_texts = sel.xpath('//div[@class="readingPromptHorizontal"]/text()')
        reading_part6_choice = '  '.join(reading_part6_choice_texts[-5:])
        # reading_choice6 += [re.sub(r'(\xa0)', '、', reading_part6_choice)] * 5
        reading_choice6 += [reading_part6_choice.replace('\xa0', ' ').replace('   ', '、')] * 5
    print(len(reading_title6))
    print(len(reading_choice6))

    print('777777')
    reading_part7 = ['第四部分'] * 20
    reading_type7 = ['选择题'] * 20
    reading_title7 = []
    reading_choice7 = []
    reading_choice7_type = ['txt'] * 20
    for url_str in urls_str[80:100][0::4]:
        reading_part7_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part7_html = requests.get(reading_part7_url, headers=headers).text
        sel = etree.HTML(reading_part7_html)
        reading_part7_title_strs_1 = sel.xpath('//div[@class="readingPromptHorizontal"]/text()')
        reading_part7_title_1 = re.sub('\xa0', '', ''.join(reading_part7_title_strs_1))
        reading_part7_title_strs_2 = sel.xpath('//div[@class="readingSubItemPrompt"]/text()')
        for reading_part7_title_str_2 in reading_part7_title_strs_2:
            reading_part7_title_2 = reading_part7_title_str_2.replace('\r\n', '').replace('\xa0', '').replace(' ', '')[3:]
            reading_part7_title = reading_part7_title_1 + '&&' + reading_part7_title_2
            reading_title7.append(reading_part7_title)
        reading_part7_choice_texts = sel.xpath('//td[@class="tdColumns1"]/text()')
        for i in range(4):
            reading_choice7.append('    '.join(reading_part7_choice_texts[4*i:4*(i+1)]))
    print(len(reading_title7))
    print(len(reading_choice7))

    model_3 = '写作'
    print('888888')
    writing_part8 = ['第一部分']
    writing_type8 = ['缩写短文']
    writing_title8 = []
    writing_choice8 = []
    writing_choice8_type = ['txt']
    for url_str in urls_str[100:]:
        writing_part8_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:-21]
        print(writing_part8_url)
        writing_part8_html = requests.get(writing_part8_url, headers=headers).text
        sel = etree.HTML(writing_part8_html)
        writing_part8_text = sel.xpath('//div[@id="divPromptArea"]/text()')
        writing_title8.append(''.join(writing_part8_text[:5]))
        writing_part8_choice = ''.join(writing_part8_text[5:])
        writing_choice8.append(writing_part8_choice.replace('\xa0', ''))
    print(writing_title8)
    print(writing_choice8)
    print(len(writing_choice8[0]))

    response_text = requests.get(audios_url).text
    audios_str = re.findall(r'<url>(.+?)</url>', response_text)
    audio_urls = []
    for audio_str in audios_str:
        if 'AssessmentItems' in audio_str:
            audio_url = 'http://mnks.cnhsk.org/mnks/' + audio_str
            audio_urls.append(audio_url)
    audios = audio_urls[:15] + [audio_urls[15]]*5 + [audio_urls[16]]*5 + [audio_urls[17]]*5 + [audio_urls[18]]*3 + [audio_urls[19]]*3 + [audio_urls[20]]*3 + [audio_urls[21]]*4 + [audio_urls[22]]*4 + [audio_urls[23]]*3 + ['']*51
    print(len(audios))

    models = [model_1]*50 + [model_2]*50 + [model_3]
    parts = listening_part1 + listening_part2 + listening_part3 + reading_part4 + reading_part6 + reading_part7 + writing_part8
    types = listening_type1 + listening_type2 + listening_type3 + reading_type4 + reading_type6 + reading_type7 + writing_type8
    numbers = [n for n in range(1,102)]
    titles = listening_title1 + listening_title2 + listening_title3 + reading_title4 + reading_title6 + reading_title7 + writing_title8
    choices = listening_choice1 + listening_choice2 + listening_choice3 + reading_choice4 + reading_choice6 + reading_choice7 + writing_choice8
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + reading_choice4_type + reading_choice6_type + reading_choice7_type + writing_choice8_type
    print(len(models), len(parts), len(types), len(numbers), len(titles), len(choices), len(choices_type))

    for model, part, type, num, title, choice, choice_type, answer_str, audio in zip(models,parts,types,numbers,titles,choices,choices_type,answers_str,audios):
    # for model, part, type, num, title, choice, choice_type, answer_str, audio in zip(models[100:], parts[100:], types[100:], numbers[100:],titles[100:], choices[100:], choices_type[100:],answers_str[100:], audios[100:]):
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




