import requests, json, re
import pymysql

con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306,
                          charset='utf8mb4')
cur_105 = con_105.cursor()
# cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), tests_type varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')

a = {"tf": {"0": "T", "1": "F"}, "choice": {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", }}

sql_exams = "SELECT exam_id,title FROM hskonline_exam_id WHERE level_id=6"
cur_105.execute(sql_exams)
exams = cur_105.fetchall()
print(len(exams))
for exam in exams[:]:
    print(exam)
    url = 'http://api.hskonline.com/v1/exam/exercise?access_token=c9_Mh5xlemaCXAlv5CL7Ae9Hb_Lk_z5s&exam_id={}'.format(
        exam[0])
    response = requests.get(url)
    data = json.loads(response.text)
    HSKlevel = 'HSK六级'
    test_name = 'ho_' + exam[0] + '_' + exam[1]

    model_1 = '听力'
    print('111111')
    listening_part1 = ['第一部分'] * 15
    listening_exam_name1 = [data['sections'][0]['items'][0]['items'][0]['name']] * 15
    listening_type1 = ['选择题'] * 15
    listening_title1 = [''] * 15
    listening_title1_type = [''] * 15
    listening_choice1 = []
    listening_choice1_type = ['txt'] * 15
    listening_answer1 = []
    listening_interpretation1 = []
    listening_audio1 = []
    for exam_info in data['sections'][0]['items'][0]['items'][0]['exercises']:
        listening_part1_choices_str = re.sub(r'\[\S+?\]', '', exam_info['items']).split('|')
        listening_part1_choices = []
        for choice, listening_part1_choice in zip(['A.', 'B.', 'C.', 'D.'], listening_part1_choices_str):
            listening_part1_choice_one = choice + listening_part1_choice
            listening_part1_choices.append(listening_part1_choice_one)
        listening_choice1.append('   '.join(listening_part1_choices))
        try:
            listening_answer1.append(a['choice'][exam_info['answer']])
        except:
            listening_answer1.append('')
        # listening_interpretation2.append('subject:' + re.sub(r'\[\S+?\]', '', exam_info['subject']) + '\nquestion:' + re.sub(r'\[\S+?\]', '',exam_info['question']) + '\nreviews:' + exam_info['reviews'])
        if '模拟' in exam[1]:
            listening_interpretation1.append(
                'subject:' + re.sub(r'\[\S+?\]', '', exam_info['subject']) + '\nreviews:' + exam_info['reviews'])
        else:
            listening_interpretation1.append('subject:' + re.sub(r'\[\S+?\]', '', exam_info['subject']))
        listening_audio1.append(exam_info['audio'].split('|')[0])
    # print(listening_exam_name1)
    # print(listening_choice1)
    # print(listening_answer1)
    # print(listening_interpretation1)
    # print(len(listening_choice1))
    # print(listening_audio1)

    print('222222')
    listening_part2 = ['第二部分'] * 15
    listening_type2 = ['选择题'] * 15
    listening_title2 = [''] * 15
    listening_title2_type = [''] * 15
    listening_choice2 = []
    listening_choice2_type = ['txt'] * 15
    listening_answer2 = []
    listening_interpretation2 = []
    listening_audio2 = []
    listening_exam_name2 = [data['sections'][0]['items'][1]['items'][0]['name']] * 15
    for exam_data in data['sections'][0]['items'][1]['items'][0]['exercises']:
        listening_part2_subject = re.sub(r'\[\S+?\]', '', exam_data['subject'])
        listening_part2_audio = exam_data['audio']
        for exam_info in exam_data['children']:
            listening_part2_choices_str = re.sub(r'\[\S+?\]', '', exam_info['items']).split('|')
            listening_part2_choices = []
            for choice, listening_part2_choice in zip(['A.', 'B.', 'C.', 'D.'], listening_part2_choices_str):
                listening_part2_choice_one = choice + listening_part2_choice
                listening_part2_choices.append(listening_part2_choice_one)
            listening_choice2.append('   '.join(listening_part2_choices))
            listening_answer2.append(a['choice'][exam_info['answer']])
            if '模拟' in exam[1]:
                listening_interpretation2.append(
                    'subject:' + listening_part2_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '', exam_info[
                        'question']) + '\nreviews:' + exam_info['reviews'])
            else:
                listening_interpretation2.append(
                    'subject:' + listening_part2_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '',
                                                                                  exam_info['question']))
            listening_audio2.append(listening_part2_audio + '|' + exam_info['audio'])
    # print(listening_exam_name2)
    # print(listening_choice2)
    # print(listening_answer2)
    # print(len(listening_interpretation2))
    # print(listening_interpretation2)
    # print(len(listening_choice2))
    # print(listening_audio2)
    # for listening_interpretation in listening_interpretation2:
    #     print(listening_interpretation)

    print('333333')
    listening_part3 = ['第二部分'] * 20
    listening_type3 = ['选择题'] * 20
    listening_title3 = [''] * 20
    listening_title3_type = [''] * 20
    listening_choice3 = []
    listening_choice3_type = ['txt'] * 20
    listening_answer3 = []
    listening_interpretation3 = []
    listening_audio3 = []
    listening_exam_name3 = [data['sections'][0]['items'][2]['items'][0]['name']] * 20
    for exam_data in data['sections'][0]['items'][2]['items'][0]['exercises']:
        listening_part3_subject = re.sub(r'\[\S+?\]', '', exam_data['subject'].replace('\u3000\u3000', '').strip())
        listening_part3_audio = exam_data['audio']
        # print(len(exam_data['children']))
        for exam_info in exam_data['children']:
            listening_part3_choices_str = re.sub(r'\[\S+?\]', '', exam_info['items']).split('|')
            listening_part3_choices = []
            for choice, listening_part3_choice in zip(['A.', 'B.', 'C.', 'D.'], listening_part3_choices_str):
                listening_part3_choice_one = choice + listening_part3_choice
                listening_part3_choices.append(listening_part3_choice_one)
            listening_choice3.append('   '.join(listening_part3_choices))
            try:
                listening_answer3.append(a['choice'][exam_info['answer']])
            except:
                listening_answer3.append('')
            if '模拟' in exam[1]:
                listening_interpretation3.append(
                    'subject:' + listening_part3_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '', exam_info[
                        'question']) + '\nreviews:' + exam_info['reviews'])
            else:
                listening_interpretation3.append(
                    'subject:' + listening_part3_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '',
                                                                                  exam_info['question']))
            listening_audio3.append(listening_part3_audio + '|' + exam_info['audio'])
    # print(listening_exam_name3)
    # print(listening_choice3)
    # print(listening_answer3)
    # print(listening_interpretation3)
    # print(listening_audio3)
    # print(len(listening_title3))
    # print(len(listening_choice3))
    # for listening_interpretation in listening_interpretation3:
    #     print(len(listening_interpretation))

    model_2 = '阅读'
    print('444444')
    reading_part4 = ['第一部分'] * 10
    reading_type4 = ['选择题'] * 10
    reading_title4 = [''] * 10
    reading_title4_type = [''] * 10
    reading_choice4 = []
    reading_choice4_type = ['txt'] * 10
    reading_answer4 = []
    reading_interpretation4 = []
    reading_exam_name4 = [data['sections'][1]['items'][0]['items'][0]['name']] * 10
    for exam_data in data['sections'][1]['items'][0]['items'][0]['exercises']:
        reading_part4_choices_str = re.sub(r'\[\S+?\]', '', exam_data['items']).split('|')
        reading_part4_choices = []
        for choice, reading_part4_choice in zip(['A.', 'B.', 'C.', 'D.'], reading_part4_choices_str):
            reading_part4_choice_one = choice + reading_part4_choice
            reading_part4_choices.append(reading_part4_choice_one)
        reading_choice4.append('   '.join(reading_part4_choices))
        try:
            reading_answer4.append(a['choice'][exam_data['answer']])
        except:
            reading_answer4.append('')
        if '模拟' in exam[1]:
            reading_interpretation4.append(exam_data['reviews'])
        else:
            reading_interpretation4.append('')
    # print(reading_exam_name4)
    # print(reading_choice4)
    # print(reading_answer4)
    # print(len(reading_title4))
    # print(len(reading_choice4))
    # for reading_interpretation in reading_interpretation4:
    #     print(reading_interpretation)

    print('555555')
    reading_part5 = ['第二部分'] * 10
    reading_type5 = ['选择题'] * 10
    reading_title5 = []
    reading_title5_type = ['txt'] * 10
    reading_choice5 = []
    reading_choice5_type = ['txt'] * 10
    reading_answer5 = []
    reading_interpretation5 = []
    reading_exam_name5 = [data['sections'][1]['items'][1]['items'][0]['name']] * 10
    for exam_data in data['sections'][1]['items'][1]['items'][0]['exercises']:
        reading_title5.append(re.sub(r'\[\S+?\]', '', exam_data['subject']))
        reading_part5_choices_str = re.sub(r'\[\S+?\]', '', exam_data['items']).split('|')
        reading_part5_choices = []
        for choice, reading_part5_choice in zip(['A.', 'B.', 'C.', 'D.'], reading_part5_choices_str):
            reading_part5_choice_one = choice + reading_part5_choice.replace('\u3000', ' ')
            reading_part5_choices.append(reading_part5_choice_one)
        reading_choice5.append('   '.join(reading_part5_choices))
        try:
            reading_answer5.append(a['choice'][exam_data['answer']])
        except:
            reading_answer5.append('')
        if '模拟' in exam[1]:
            reading_interpretation5.append(exam_data['reviews'])
        else:
            reading_interpretation5.append('')
    # print(reading_exam_name5)
    # print(reading_choice5)
    # print(reading_answer5)
    # print(len(reading_title5))
    # print(len(reading_choice5))
    # for reading_interpretation in reading_interpretation5:
    #     print(reading_interpretation)

    print('666666')
    reading_part6 = ['第三部分'] * 10
    reading_type6 = ['选择题'] * 10
    reading_title6 = []
    reading_title6_type = ['txt'] * 10
    reading_choice6 = []
    reading_choice6_type = ['txt'] * 10
    reading_answer6 = []
    reading_interpretation6 = []
    reading_exam_name6 = [data['sections'][1]['items'][2]['items'][0]['name']] * 10
    for exam_data in data['sections'][1]['items'][2]['items'][0]['exercises']:
        reading_part6_subject = re.sub(r'\[w=\d+\]', '',
                                       exam_data['subject'].replace('[/w]', '').replace('\u3000\u3000', ''))
        reading_part6_choices_str = re.sub(r'\[\S+?\]', '', exam_data['items']).split('|')
        reading_part6_choices = []
        for choice, reading_part6_choice in zip(['A.', 'B.', 'C.', 'D.', 'E.'], reading_part6_choices_str):
            reading_part6_choice_one = choice + reading_part6_choice
            reading_part6_choices.append(reading_part6_choice_one)
        reading_choice6 += ['   '.join(reading_part6_choices)] * 5
        for exam_info in exam_data['children']:
            reading_title6.append('subject:' + reading_part6_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '',
                                                                                              exam_info[
                                                                                                  'question']) + '( )')
            try:
                reading_answer6.append(a['choice'][exam_info['answer']])
            except:
                reading_answer6.append('')
            if '模拟' in exam[1]:
                reading_interpretation6.append(exam_info['reviews'])
            else:
                reading_interpretation6.append('')
    # print(reading_exam_name6)
    # print(reading_title6)
    # print(reading_choice6)
    # print(reading_answer6)
    # print(reading_interpretation6)
    # print(len(reading_interpretation6))

    print('777777')
    reading_part7 = ['第三部分'] * 20
    reading_type7 = ['选择题'] * 20
    reading_title7 = []
    reading_title7_type = ['txt'] * 20
    reading_choice7 = []
    reading_choice7_type = ['txt'] * 20
    reading_answer7 = []
    reading_interpretation7 = []
    reading_exam_name7 = [data['sections'][1]['items'][3]['items'][0]['name']] * 20
    for exam_data in data['sections'][1]['items'][3]['items'][0]['exercises']:
        reading_part7_subject = re.sub(r'\[\S+?\]', '', exam_data['subject'].replace('\u3000\u3000', ''))
        print(len(exam_data['children']))
        for exam_info in exam_data['children']:
            reading_title7.append('subject:' + reading_part7_subject + '\nquestion:' + re.sub(r'\[\S+?\]', '',
                                                                                              exam_info[
                                                                                                  'question']) + '( )')
            reading_part7_choices_str = re.sub(r'\[\S+?\]', '', exam_info['items']).split('|')
            reading_part7_choices = []
            for choice, reading_part7_choice in zip(['A.', 'B.', 'C.', 'D.'], reading_part7_choices_str):
                reading_part7_choice_one = choice + reading_part7_choice
                reading_part7_choices.append(reading_part7_choice_one)
            reading_choice7.append('   '.join(reading_part7_choices))
            try:
                reading_answer7.append(a['choice'][exam_info['answer']])
            except:
                reading_answer7.append('')
            if '模拟' in exam[1]:
                reading_interpretation7.append(exam_info['reviews'])
            else:
                reading_interpretation7.append('')
    # print(reading_exam_name7)
    # print(reading_title7)
    # print(reading_choice7)
    # print(reading_answer7)
    # print(reading_interpretation7)
    # print(len(reading_interpretation7))

    model_3 = '写作'
    print('888888')
    writing_part8 = ['第一部分']
    writing_exam_name8 = []
    writing_type8 = ['缩写题']
    writing_title8 = []
    writing_title8_type = ['txt']
    writing_choice8 = []
    writing_choice8_type = ['txt']
    writing_answer8 = []
    writing_interpretation8 = []
    exam_data = data['sections'][2]['items'][0]['items'][0]['exercises'][0]
    writing_exam_name8.append(data['sections'][2]['items'][0]['items'][0]['name'])
    writing_title8.append(exam_data['type_desc'].replace(' ', '').replace('\r\n', '').replace('（', '\n（')[1:])
    writing_choice8.append(re.sub(r'\[\S+?\]', '', exam_data['subject'].replace('\u3000\u3000', '')))
    if '模拟' in exam[1]:
        writing_answer8.append(exam_data['reviews'].replace('\u3000\u3000', ''))
        writing_interpretation8.append(exam_data['reviews'].replace('\u3000\u3000', ''))
    else:
        writing_answer8.append('')
        writing_interpretation8.append('')
    # print(writing_exam_name8)
    # print(writing_title8)
    # print(writing_choice8[0])
    # print(writing_answer8)
    # print(writing_interpretation8)

    models = [model_1] * 50 + [model_2] * 50 + [model_3]
    parts = listening_part1 + listening_part2 + listening_part3 + reading_part4 + reading_part5 + reading_part6 + reading_part7 + writing_part8
    exam_names = listening_exam_name1 + listening_exam_name2 + listening_exam_name3 + reading_exam_name4 + reading_exam_name5 + reading_exam_name6 + reading_exam_name7 + writing_exam_name8
    exam_types = listening_type1 + listening_type2 + listening_type3 + reading_type4 + reading_type5 + reading_type6 + reading_type7 + writing_type8
    numbers = [n for n in range(1, 102)]
    titles = listening_title1 + listening_title2 + listening_title3 + reading_title4 + reading_title5 + reading_title6 + reading_title7 + writing_title8
    titles_type = listening_title1_type + listening_title2_type + listening_title3_type + reading_title4_type + reading_title5_type + reading_title6_type + reading_title7_type + writing_title8_type
    choices = listening_choice1 + listening_choice2 + listening_choice3 + reading_choice4 + reading_choice5 + reading_choice6 + reading_choice7 + writing_choice8
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + reading_choice4_type + reading_choice5_type + reading_choice6_type + reading_choice7_type + writing_choice8_type
    answers = listening_answer1 + listening_answer2 + listening_answer3 + reading_answer4 + reading_answer5 + reading_answer6 + reading_answer7 + writing_answer8
    interpretations = listening_interpretation1 + listening_interpretation2 + listening_interpretation3 + reading_interpretation4 + reading_interpretation5 + reading_interpretation6 + reading_interpretation7 + writing_interpretation8
    audios = listening_audio1 + listening_audio2 + listening_audio3 + [''] * 51
    print(len(models), len(parts), len(exam_names), len(exam_types), len(numbers), len(titles), len(choices), len(choices_type), len(answers), len(interpretations), len(audios))

    for model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio in zip(
            models, parts, exam_names, exam_types, numbers, titles, titles_type, choices, choices_type, answers, interpretations, audios):
        onedata = (
            HSKlevel, test_name, model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio)
        print(onedata)
        sql = 'insert into hanban (HSKlevel, test_name, model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur_105.execute(sql, onedata)
        con_105.commit()

cur_105.close()
con_105.close()
