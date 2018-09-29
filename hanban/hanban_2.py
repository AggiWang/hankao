import requests,time,re
from lxml import etree
# from selenium import webdriver
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
# cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')


sql_cookies = "SELECT * FROM hanban_cookies WHERE HSKlevel='HSK二级'"
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
    answers_str = sel.xpath('//tr[@align="center"]/td/text()')
    answers = re.findall(r'[A-Z]', ''.join(answers_str))

    model_1 = '听力'
    print('111111')
    listening_part1 = ['第一部分'] * 10
    listening_type1 = ['判断题'] * 10
    listening_title1 = (',' * 10).split(',')[:-1]
    listening_choice1 = []
    listening_choice1_type = ('image,'*10).split(',')[:-1]
    for url_str in urls_str[:10]:
        listening_part1_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part1_html = requests.get(listening_part1_url, headers=headers).text
        sel = etree.HTML(listening_part1_html)
        listening_part1_img = 'http://mnks.cnhsk.org' + sel.xpath('//img/@src')[0]
        listening_choice1.append(listening_part1_img)
    print(len(listening_choice1))

    print('222222')
    listening_part2 = ['第二部分'] * 10
    listening_type2 = ['选择题'] * 10
    listening_title2 = (',' * 10).split(',')[:-1]
    listening_choice2 = []
    listening_choice2_type = ('image,' * 10).split(',')[:-1]
    choices = ['A', 'B', 'C', 'D', 'E', 'F']*2
    for url_str in urls_str[10:20]:
        listening_part2_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part2_html = requests.get(listening_part2_url, headers=headers).text
        sel = etree.HTML(listening_part2_html)
        listening_part2_imgs_str = sel.xpath('//img/@src')
        listening_choice2_one = []
        for choice,listening_part2_img_str in zip(choices,listening_part2_imgs_str):
            listening_part2_img = choice + '、' + 'http://mnks.cnhsk.org' + listening_part2_img_str
            listening_choice2_one.append(listening_part2_img)
        listening_choice2.append('    '.join(listening_choice2_one))
    print(len(listening_choice2))


    print('333333444444')
    listening_part3 = ['第三部分']*10 + ['第四部分']*5
    listening_type3 = ['选择题'] * 15
    listening_title3 = (',' * 15).split(',')[:-1]
    listening_choice3 = []
    listening_choice3_type = ('txt,' * 15).split(',')[:-1]
    for url_str in urls_str[20:35]:
        listening_part3_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        listening_part3_html = requests.get(listening_part3_url, headers=headers).text
        listening_part3_choices_str = listening_part3_html.split('</label>')[1:]
        listening_part3_choice_one = []
        for listening_part3_choice_str in listening_part3_choices_str:
            listening_part3_choice = re.sub(r'<(.+?)>', '', listening_part3_choice_str.replace('\n', '').replace('\r', '').replace(' ', '').replace('&nbsp;', ' '))
            listening_part3_choice_one.append(listening_part3_choice)
        listening_choice3.append('    '.join(listening_part3_choice_one))
    # print(listening_choice3)
    print(len(listening_choice3))

    model_2 = '阅读'
    print('555555')
    reading_part5 = ['第一部分'] * 5
    reading_type5 = ['选择题'] * 5
    reading_title5 = []
    reading_choice5 = []
    reading_choice5_type = ('image,' * 5).split(',')[:-1]
    choices = ['A', 'B', 'C', 'D', 'E', 'F']
    for e,url_str in zip([n for n in range(5)], urls_str[35:40]):
        reading_part5_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part5_html = requests.get(reading_part5_url, headers=headers).text
        reading_part5_titles_str = re.findall(r'<ruby>[\s\S]+?</div>', reading_part5_html)
        reading_part5_title = re.sub(r'<(.+?)>', '',reading_part5_titles_str[e].replace('\n', '').replace('\r', '').replace(' ','').replace('&nbsp;', ' '))
        reading_title5.append(reading_part5_title)
        sel = etree.HTML(reading_part5_html)
        reading_part5_imgs_str = sel.xpath('//img/@src')
        reading_choice5_one = []
        for choice,reading_part5_img_str in zip(choices,reading_part5_imgs_str):
            reading_part5_img = choice + '、' + 'http://mnks.cnhsk.org' + reading_part5_img_str
            reading_choice5_one.append(reading_part5_img)
        reading_choice5.append('    '.join(reading_choice5_one))
    print(len(reading_title5))
    print(len(reading_choice5))

    print('666666')
    reading_part6 = ['第二部分'] * 5
    reading_type6 = ['选择题'] * 5
    reading_title6 = []
    reading_choice6 = []
    reading_choice6_type = ('txt,' * 5).split(',')[:-1]
    for f, url_str in zip([n for n in range(1,6)], urls_str[40:45]):
        reading_part6_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part6_html = requests.get(reading_part6_url, headers=headers).text
        reading_part6_titles_str = re.findall(r'<ruby>[\s\S]+?</div>', reading_part6_html)
        reading_part6_title = re.sub(r'<(.+?)>', '',reading_part6_titles_str[f].replace('\n', '').replace('\r', '').replace(' ','').replace( '&nbsp;', ' '))
        reading_title6.append(reading_part6_title)
        reading_part6_choices_str = re.findall(r'<ruby>[\s\S]+?<br />', reading_part6_html)[0]
        reading_part6_choices_text = re.sub(r'<(.+?)>', '', reading_part6_choices_str.replace('\n', '').replace('\r', '').replace(r' ', ''))
        reading_part6_choices = re.split(r'&nbsp;[A-Z]&nbsp;', reading_part6_choices_text)
        reading_choice6_one = []
        for choice,reading_part6_choice in zip(['A','B','C','D','E','F'],reading_part6_choices):
            reading_part6_choice_one = choice + '、' + reading_part6_choice.replace('&nbsp;', '')
            reading_choice6_one.append(reading_part6_choice_one)
        reading_choice6.append('    '.join(reading_choice6_one))
    print(len(reading_title6))
    print(len(reading_choice6))

    print('777777')
    reading_part7 = ['第三部分'] * 5
    reading_type7 = ['判断题'] * 5
    reading_title7 = []
    reading_choice7 = []
    reading_choice7_type = ('txt,' * 5).split(',')[:-1]
    for url_str in urls_str[45:50]:
        reading_part7_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part7_html = requests.get(reading_part7_url, headers=headers).text
        reading_part7_titles_str = re.findall(r'<ruby>[\s\S]+?<br />', reading_part7_html)
        reading_part7_title = re.sub(r'<(.+?)>', '',reading_part7_titles_str[0].replace('\n', '').replace('\r', '').replace(' ','').replace( '&nbsp;', ' '))
        reading_title7.append(reading_part7_title)
        reading_part7_choices_str = re.findall(r'<br />[\s\S]+?</div>', reading_part7_html)[0]
        reading_part7_choice_one = re.sub(r'<(.+?)>', '', reading_part7_choices_str.replace('\n', '').replace('\r', '').replace(r' ', ''))
        reading_choice7.append(reading_part7_choice_one)
    print(len(reading_title7))
    print(len(reading_choice7))

    print('888888')
    reading_part8 = ['第四部分'] * 10
    reading_type8 = ['选择题'] * 10
    reading_title8 = []
    reading_choice8 = []
    reading_choice8_type = ('txt,' * 10).split(',')[:-1]
    nums = [n for n in range(1, 6)] + [n for n in range(1, 6)]
    for h, url_str in zip(nums, urls_str[50:60]):
        reading_part8_url = 'http://mnks.cnhsk.org/Mnks/' + 'WebServices/LoadQuestionContent.ashx' + url_str[17:]
        reading_part8_html = requests.get(reading_part8_url, headers=headers).text
        # print(reading_part8_html)
        reading_part8_titles_str = re.findall(r'<ruby>[\s\S]+?</div>', reading_part8_html)
        reading_part8_title = re.sub(r'<(.+?)>', '',reading_part8_titles_str[h].replace('\n', '').replace('\r', '').replace(' ', '').replace('&nbsp;', ' '))
        reading_title8.append(reading_part8_title)
        reading_part8_choices_str = re.findall(r'<ruby>[\s\S]+?</rp></ruby><', reading_part8_html)
        # print(reading_part8_choices_str)
        reading_choice8_one = []
        for choice, reading_part8_choice_str in zip(['A', 'B', 'C', 'D', 'E', 'F'], reading_part8_choices_str):
            # print(reading_part8_choice_str)
            reading_part8_choice_text = re.sub(r'<(.+?)>', '',reading_part8_choice_str[:-1].replace('\n', '').replace('\r', '').replace(r' ', ''))
            reading_part8_choice_one = choice + '、' + reading_part8_choice_text
            reading_choice8_one.append(reading_part8_choice_one)
        reading_choice8.append('    '.join(reading_choice8_one))
    print(len(reading_title8))
    print(reading_title8)
    print(len(reading_choice8))
    print(reading_choice8)

    response_text = requests.get(audios_url).text
    audios_str = re.findall(r'<url>(.+?)</url>', response_text)
    audio_urls = []
    for audio_str in audios_str:
        if 'AssessmentItems' in audio_str:
            audio_url = 'http://mnks.cnhsk.org/mnks/' + audio_str
            audio_urls.append(audio_url)
    audios = audio_urls[2:12] + [audio_urls[12]]*5 + [audio_urls[13]]*5 + audio_urls[15:25] + audio_urls[26:31] + (','*25).split(',')[:-1]
    print(len(audios))

    models = [model_1]*35 + [model_2]*25
    parts = listening_part1 + listening_part2 + listening_part3  + reading_part5 + reading_part6 + reading_part7 + reading_part8
    types = listening_type1 + listening_type2 + listening_type3 + reading_type5 + reading_type6 + reading_type7 + reading_type8
    numbers = [n for n in range(1,61)]
    titles = listening_title1 + listening_title2 + listening_title3  + reading_title5 + reading_title6 + reading_title7 + reading_title8
    choices = listening_choice1 + listening_choice2 + listening_choice3  + reading_choice5 + reading_choice6 + reading_choice7 + reading_choice8
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + reading_choice5_type + reading_choice6_type + reading_choice7_type + reading_choice8_type
    print(len(models), len(parts), len(types), len(numbers), len(titles), len(choices), len(choices_type), len(answers))

    # models = [model_1] * 25 + [model_2] * 25
    # parts = listening_part2 + listening_part3 + reading_part5 + reading_part6 + reading_part7 + reading_part8
    # type= listening_type2 + listening_part3 + reading_part5 + reading_part6 + reading_part7 + reading_part8
    # numbers = [n for n in range(11, 61)]
    # titles = listening_title2 + listening_title3 + reading_title5 + reading_title6 + reading_title7 + reading_title8
    # choices = listening_choice2 + listening_choice3 + reading_choice5 + reading_choice6 + reading_choice7 + reading_choice8
    # choices_type = listening_choice2_type + listening_choice3_type + reading_choice5_type + reading_choice6_type + reading_choice7_type + reading_choice8_type
    # print(len(models), len(parts), len(numbers), len(titles), len(choices), len(choices_type), len(answers[10:]))

    for model, part, type, num, title, choice, choice_type, answer, audio in zip(models,parts,types,numbers,titles,choices,choices_type,answers,audios):
        onedata = (
        HSKlevel, test_name, model, part, type, num, title, choice, choice_type, answer, audio)
        print(len(onedata))
        print(onedata)
        # sql = 'insert into hanban (HSKlevel, test_name, model, part, tests_type, num, title, choice, choice_type, answer, audio) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # cur_105.execute(sql, onedata)
        # con_105.commit()

cur_105.close()
con_105.close()




