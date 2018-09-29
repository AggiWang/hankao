import requests,json
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
# cur_105.execute('CREATE TABLE IF NOT EXISTS hanban (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), model varchar(10), part varchar(16), tests_type varchar(16), num varchar(16), title varchar(512), choice varchar(1024), choice_type varchar(28), answer varchar(8), interpretation varchar(10240),  audio varchar(512))')

a = {"tf":{"0":"T", "1":"F"}, "choice":{"0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G",}}


sql_exams = "SELECT exam_id,title FROM hskonline_exam_id WHERE level_id=2"
cur_105.execute(sql_exams)
exams = cur_105.fetchall()
print(len(exams))
for exam in exams[:1]:
    print(exam)
    url = 'http://api.hskonline.com/v1/exam/exercise?access_token=c9_Mh5xlemaCXAlv5CL7Ae9Hb_Lk_z5s&exam_id={}'.format(exam[0])
    response = requests.get(url)
    data = json.loads(response.text)
    HSKlevel = 'HSK二级'
    test_name = 'ho_' + exam[0] + '_' + exam[1]

    model_1 = "听力"
    print('111111')
    listening_part1 = ['第一部分'] * 10
    listening_exam_name1 = [data['sections'][0]['items'][0]['items'][0]['name']] * 10
    listening_type1 = ['判断题'] * 10
    listening_title1 = [''] * 10
    listening_title1_type = [''] * 10
    listening_choice1 = []
    listening_choice1_type = ['image'] * 10
    listening_answer1 = []
    listening_interpretation1 = []
    listening_audio1 = []
    for exam_info in data['sections'][0]['items'][0]['items'][0]['exercises']:
        listening_choice1.append(exam_info['image'])
        # listening_answer1.append(a['tf'][exam_info['answer']])
        try:
            listening_answer1.append(a['tf'][exam_info['answer']])
        except:
            listening_answer1.append('F')
        listening_interpretation1.append('subject:' + exam_info['subject'])
        listening_audio1.append(exam_info['audio'])
    # print(listening_exam_name1)
    # print(listening_choice1)
    # print(listening_answer1)
    # print(listening_interpretation1)
    # print(listening_audio1)

    print('222222')
    listening_part2 = ['第二部分'] * 10
    listening_exam_name2 = [data['sections'][0]['items'][2]['items'][0]['name']] * 10
    listening_type2 = ['选择题'] * 10
    listening_title2 = [''] * 10
    listening_title2_type = [''] * 10
    listening_choice2 = []
    listening_choice2_type = ['image'] * 10
    listening_answer2 = []
    listening_interpretation2 = []
    listening_audio2 = []
    for listening_part2_choice_data in data['sections'][0]['items'][1]['items'][0]['exercises']:
        listening_part2_choices_str = listening_part2_choice_data['items'].split('|')
        listening_part2_choices = []
        for choice, listening_part2_choice in zip(['A.', 'B.', 'C.', 'D.', 'E.'], listening_part2_choices_str):
            listening_part2_choice_one = choice + listening_part2_choice
            listening_part2_choices.append(listening_part2_choice_one)
        listening_choice2 += ['   '.join(listening_part2_choices)] * 5
        for exam_info in listening_part2_choice_data['children']:
            listening_answer2.append(a['choice'][exam_info['answer']])
            listening_interpretation2.append('subject:' + exam_info['subject'])
            listening_audio2.append(exam_info['audio'].split('|')[0])
    # print(listening_exam_name2)
    # print(listening_choice2)
    # print(listening_answer2)
    # print(listening_interpretation2)
    # print(listening_audio2)
    # for listening_interpretation in listening_interpretation2:
    #     print(listening_interpretation)

    print('333333')
    listening_part3 = ['第三部分'] * 10
    listening_exam_name3 = [data['sections'][0]['items'][2]['items'][0]['name']] * 10
    listening_type3 = ['选择题'] * 10
    listening_title3 = [''] * 10
    listening_title3_type = [''] * 10
    listening_choice3 = []
    listening_choice3_type = ['txt'] * 10
    listening_answer3 = []
    listening_interpretation3 = []
    listening_audio3 = []
    for exam_info in data['sections'][0]['items'][2]['items'][0]['exercises']:
        listening_part3_choices_str = exam_info['items'].split('|')
        listening_part3_choices = []
        for choice, listening_part3_choice in zip(['A.', 'B.', 'C.'], listening_part3_choices_str):
            listening_part3_choice_one = choice + listening_part3_choice
            listening_part3_choices.append(listening_part3_choice_one)
        listening_choice3.append('   '.join(listening_part3_choices))
        listening_answer3.append(a['choice'][exam_info['answer']])
        listening_interpretation3.append('subject:' + exam_info['subject'] + 'question:' + exam_info['question'])
        listening_audio3.append(exam_info['audio'].split('|')[0])
    # print(listening_exam_name3)
    # print(listening_choice3)
    # print(listening_answer3)
    # print(listening_interpretation3)
    # print(listening_audio3)
    # for listening_interpretation in listening_interpretation3:
    #     print(listening_interpretation)

    print('444444')
    listening_part4 = ['第四部分'] * 5
    listening_exam_name4 = [data['sections'][0]['items'][3]['items'][0]['name']] * 5
    listening_type4 = ['选择题'] * 5
    listening_title4 = [''] * 5
    listening_title4_type = [''] * 5
    listening_choice4 = []
    listening_choice4_type = ['txt'] * 5
    listening_answer4 = []
    listening_interpretation4 = []
    listening_audio4 = []
    for exam_info in data['sections'][0]['items'][3]['items'][0]['exercises']:
        listening_part4_choices_str = exam_info['items'].split('|')
        listening_part4_choices = []
        for choice, listening_part4_choice in zip(['A.', 'B.', 'C.'], listening_part4_choices_str):
            listening_part4_choice_one = choice + listening_part4_choice
            listening_part4_choices.append(listening_part4_choice_one)
        listening_choice4.append('   '.join(listening_part4_choices))
        listening_answer4.append(a['choice'][exam_info['answer']])
        listening_interpretation4.append('subject:' + exam_info['subject'] + 'question:' + exam_info['question'])
        listening_audio4.append(exam_info['audio'].split('|')[0])
    # print(listening_exam_name4)
    # print(listening_choice4)
    # print(listening_answer4)
    # print(listening_interpretation4)
    # print(listening_audio4)
    # for listening_interpretation in listening_interpretation4:
    #     print(listening_interpretation)

    model_2 = '阅读'
    print('555555666666')
    reading_part5 = ['第一部分'] * 5 + ['第二部分'] * 5
    reading_exam_name5 = []
    reading_type5 = ['选择题'] * 10
    reading_title5 = []
    reading_title5_type = ['txt'] * 10
    reading_choice5 = []
    reading_choice5_type = ['image']*5 + ['txt']*5
    reading_answer5 = []
    reading_interpretation5 = ['']*10
    reading_audio5 = [''] * 10

    for exam_data in data['sections'][1]['items'][:2]:
        reading_exam_name5_one = [exam_data['items'][0]['name']] * 5
        reading_exam_name5 += reading_exam_name5_one
        reading_part5_choices_str = exam_data['items'][0]['exercises'][0]['items'].split('|')
        reading_part5_choices = []
        for choice, reading_part5_choice in zip(['A.', 'B.', 'C.', 'D.', 'E.'], reading_part5_choices_str):
            reading_part5_choice_one = choice + reading_part5_choice
            reading_part5_choices.append(reading_part5_choice_one)
        reading_choice5 += ['   '.join(reading_part5_choices)]*5
        for exam_info in exam_data['items'][0]['exercises'][0]['children']:
            reading_answer5.append(a['choice'][exam_info['answer']])
            # try:
            #     reading_answer6.append(a['choice'][exam_info['answer']])
            # except:
            #     reading_answer6.append('C')
            reading_title5.append(exam_info['subject'])
    # print(reading_exam_name5)
    # print(reading_choice5)
    # print(len(reading_choice5))
    # print(reading_answer5)
    # print(reading_title5)
    # print(len(reading_title5))
    # print(reading_audio5)

    print('777777')
    reading_part7 = ['第三部分'] * 5
    reading_type7 = ['选择题'] * 5
    reading_title7 = []
    reading_title7_type = ['txt'] * 5
    reading_choice7 = []
    reading_choice7_type = ['txt'] * 5
    reading_answer7 = []
    reading_exam_name7 = [data['sections'][1]['items'][2]['items'][0]['name']] * 5
    for exam_info in data['sections'][1]['items'][2]['items'][0]['exercises']:
        reading_title7.append(exam_info['subject'] + '\n' + exam_info['question'])
        reading_part7_choices_str = exam_info['items']
        reading_part7_choices = []
        for choice, reading_part7_choice in zip(['A.', 'B.', 'C.'], reading_part7_choices_str):
            reading_part7_choice_one = choice + reading_part7_choice
            reading_part7_choices.append(reading_part7_choice_one)
        reading_choice7.append('   '.join(reading_part7_choices))
        reading_choice7.append(exam_info['items'].split('|'))
        reading_answer7.append(a['tf'][exam_info['answer']])
    print(reading_exam_name7)
    print(reading_title7)
    print(reading_choice7)
    print(reading_answer7)

    print('88888888')
    reading_part8 = ['第四部分'] * 10
    reading_type8 = ['选择题'] * 10
    reading_title8 = []
    reading_title8_type = ['txt'] * 10
    reading_choice8 = []
    reading_choice8_type = ['txt'] * 10
    reading_answer8 = []
    reading_exam_name8 = [data['sections'][1]['items'][3]['items'][0]['name']] * 10
    for exam_data in data['sections'][1]['items'][3]['items'][0]['exercises']:
        reading_part8_choices_str = exam_data['items'].split('|')
        reading_part8_choices = []
        for choice, reading_part8_choice in zip(['A.', 'B.', 'C.', 'D.', 'E.'], reading_part8_choices_str):
            reading_part8_choice_one = choice + reading_part8_choice
            reading_part8_choices.append(reading_part8_choice_one)
        reading_choice8 += ['   '.join(reading_part8_choices)]*5
        for exam_info in exam_data['children']:
            reading_title8.append(exam_info['subject'])
            reading_answer8.append(a['choice'][exam_info['answer']])
    # print(reading_exam_name8)
    # print(reading_title8)
    # print(reading_choice8)
    # print(reading_answer8)

    models = [model_1] * 35 + [model_2] * 25
    parts = listening_part1 + listening_part2 + listening_part3 + listening_part4 + reading_part5 + reading_part7 + reading_part8
    exam_names = listening_exam_name1 + listening_exam_name2 + listening_exam_name3 + listening_exam_name4 + reading_exam_name5 + reading_exam_name7 + reading_exam_name8
    exam_types = listening_type1 + listening_type2 + listening_type3 + listening_type4 + reading_type5 + reading_type7 + reading_type8
    numbers = [n for n in range(1, 61)]
    titles = listening_title1 + listening_title2 + listening_title3 + listening_title4 + reading_title5 + reading_title7 + reading_title8
    titles_type = listening_title1_type + listening_title2_type + listening_title3_type + listening_title4_type + reading_title5_type + reading_title7_type + reading_title8_type
    choices = listening_choice1 + listening_choice2 + listening_choice3 + listening_choice4 + reading_choice5 + reading_choice7 + reading_choice8
    choices_type = listening_choice1_type + listening_choice2_type + listening_choice3_type + listening_choice4_type + reading_choice5_type + reading_choice7_type + reading_choice8_type
    answers = listening_answer1 + listening_answer2 + listening_answer3 + listening_answer4 + reading_answer5 + reading_answer7 + reading_answer8
    interpretations = listening_interpretation1 + listening_interpretation2 + listening_interpretation3 + listening_interpretation4 + ['']*25
    audios = listening_audio1 + listening_audio2 + listening_audio3 + listening_audio4 + ['']*25
    print(len(models), len(parts), len(exam_names), len(exam_types), len(numbers), len(titles), len(choices), len(choices_type), len(answers), len(interpretations), len(audios))

    for model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio in zip(models, parts, exam_names, exam_types, numbers, titles, titles_type, choices, choices_type,answers, interpretations, audios):
        onedata = (
            HSKlevel, test_name, model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio)
        print(onedata)
        # sql = 'insert into hanban (HSKlevel, test_name, model, part, exam_name, exam_type, num, title, title_type, choice, choice_type, answer, interpretation, audio) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # cur_105.execute(sql, onedata)
        # con_105.commit()

cur_105.close()
con_105.close()
