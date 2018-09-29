import requests, time, re
from lxml import etree
from selenium import webdriver
import pymysql

con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
cur_105.execute(
    'CREATE TABLE IF NOT EXISTS hanban_cookies (id int not null auto_increment primary key, HSKlevel varchar(16), test_name varchar(16), audios_url varchar(256), cookies varchar(1024))')

hsklevels = 'HSK一级,' * 10 + 'HSK二级,' * 10 + 'HSK三级,' * 10 + 'HSK四级,' * 10 + 'HSK五级,' * 10 + 'HSK六级,' * 10
HSKlevels = hsklevels.split(',')[:-1]
print(len(HSKlevels))
for i, HSKlevel in zip([j for j in range(30,40)], HSKlevels[30:40]):
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    url = 'http://mnks.cnhsk.org/Mnks/Simulate/LoginNew.aspx?lang=zh-CN'
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_id('ctl00_CphMain_TxtUsername').send_keys('aggi')
    driver.find_element_by_id('ctl00_CphMain_TxtPassword').send_keys('gyj1325GYJ')
    driver.find_element_by_id('ctl00_CphMain_BtnOk').click()
    time.sleep(2)
    # driver.current_window_handle.click(635,70)
    start_url = 'http://mnks.cnhsk.org/Mnks/Simulate/Default.aspx'
    driver.get(start_url)
    time.sleep(2)

    # HSKlevel = 'HSK一级'
    PaperId = driver.find_elements_by_xpath('//div[@class="listtwoul"]/div/ul/li/a')[i]
    test_name = PaperId.get_attribute("textContent")
    print(test_name)
    PaperId_str = PaperId.get_attribute("href").split('PaperId=')[1]
    audios_url = 'http://mnks.cnhsk.org/mnks//ExamData/TestPaper/examdata/4/ASM_{}.xml'.format(PaperId_str)
    response_text = requests.get(audios_url).text
    audios_str = re.findall(r'<url>(.+?)</url>', response_text)
    PaperId.click()
    driver.find_element_by_id('ctl00_CphMain_BtnLogin').click()
    driver.find_element_by_id('ctl00_CphMain_btnInit').click()
    time.sleep(3)
    driver.find_element_by_id('btnFinish').click()
    driver.find_element_by_id('ctl00_CphMain_BtnExam').click()
    # time.sleep(3)

    # print('1111111')
    # a = '第一部分,' * 7
    # part1 = a.split(',')[:-1]
    # number1 = ['例1','例2',1,2,3,4,5]
    # part1_titles = ['','','','','','','']
    # part1_choices = []
    # a = 0
    # while a < 7:
    #     driver.find_element_by_id('btnNext').click()
    #     time.sleep(0.8)
    #     img_url = driver.find_elements_by_xpath('//img')[3].get_attribute('src')
    #     part1_choices.append(img_url)
    #     a += 1
    # print(len(part1_choices))
    #
    # print('222222')
    # b = '第二部分,' * 6
    # part2 = b.split(',')[:-1]
    # number2 = ['例1', 6, 7, 8, 9, 10]
    # part2_titles = ['', '', '', '', '', '']
    # part2_choices = []
    # b= 0
    # while b < 6:
    #     driver.find_element_by_id('btnNext').click()
    #     time.sleep(1)
    #     img_urls = driver.find_elements_by_xpath('//img')
    #     choices = ['A','B','C']
    #     part2_choice = []
    #     for choice,imgurl in zip(choices,img_urls[3:6]):
    #         img_url = imgurl.get_attribute('src')
    #         one_choice = choice + '、' + img_url
    #         part2_choice.append(one_choice)
    #
    #     part2_choices.append('  '.join(part2_choice))
    #     b += 1
    # print(len(part2_choices))
    #
    # print('3333333')
    # c = '第三部分,' * 6
    # part3 = c.split(',')[:-1]
    # number3 = ['例1', 11, 12, 13, 14, 15]
    # part3_choices = []
    # time.sleep(1)
    # driver.find_element_by_id('btnNext').click()
    # time.sleep(2)
    # response_text = driver.page_source
    # try:
    #     title_str = re.findall(r'><br[\s\S]*）</div>', response_text)[0]
    #     title_text = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(' ', '')[1:])
    #     part3_title_0 = re.findall(r'F(.+?)（', title_text)[0]
    #     part3_titles = [part3_title_0] + ['', '', '', '', '']
    #     part3_answer0 = re.findall(r'[A-Z]',title_text)[-1]
    # except:
    #     part3_title_0 = driver.find_elements_by_xpath('//img')[10].get_attribute('src')
    #     part3_titles = [part3_title_0] + ['', '', '', '', '']
    #     part3_answer0 = ''
    # img_urls = driver.find_elements_by_xpath('//img')
    # choices = ['A', 'B', 'C', 'D', 'E', 'F']
    # for choice, imgurl in zip(choices, img_urls[3:9]):
    #     img_url = imgurl.get_attribute('src')
    #     part3_choices.append(img_url)
    # print(len(part3_choices))
    #
    # print('444444')
    # d = '第四部分,' * 6
    # part4 = d.split(',')[:-1]
    # number4 = ['例1', 16, 17, 18, 19, 20]
    # part4_titles = []
    # part4_choices = []
    # time.sleep(1)
    # d = 0
    # while d < 6:
    #     driver.find_element_by_id('btnNext').click()
    #     time.sleep(1)
    #     response_text = driver.page_source
    #     try:
    #         title_str = re.findall(r'<ruby>[\s\S]*</ruby></div>',response_text )[0]
    #         part4_title = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(' ', ''))
    #     except:
    #         part4_title = ''
    #     part4_titles.append(part4_title)
    #     choices_str = re.findall(r'singleChoiceResponseTable">[\s\S]*</tr></tbody></table>', response_text)[0]
    #     part4_choice = []
    #     for choice_str in choices_str.split('</label')[1:4]:
    #         one_choice = re.sub(r'<(.+?)>', '', choice_str.replace('\n','').replace(' ',''))[1:]
    #         part4_choice.append(one_choice)
    #     part4_choices.append('  '.join(part4_choice))
    #     d += 1
    #     # time.sleep(1)
    # print(len(part4_choices))
    #

    # driver.find_element_by_id('btnFinish').click()
    # time.sleep(2)
    # driver.find_element_by_id('btnFinish').click()
    # time.sleep(2)
    # driver.find_element_by_id('btnFinish').click()
    # time.sleep(2)

    #
    # module_2 = '阅读'
    # print('555555555')
    # e = '第一部分,' * 7
    # reading_part1 = e.split(',')[:-1]
    # reading_number1 = ['例1', '例2', 21, 22, 23, 24, 25]
    # reading_part1_titles = ['', '', '', '', '', '', '']
    # reading_part1_choices = []
    # e = 0
    # while e < 7:
    #     time.sleep(1)
    #     img_url = driver.find_elements_by_xpath('//img')[3].get_attribute('src')
    #     reading_part1_choices.append(img_url)
    #     driver.find_element_by_id('btnNext').click()
    #     e += 1
    # print(len(reading_part1_choices))
    #
    # print('6666666666')
    # time.sleep(1)
    # f_str = '第二部分,' * 6
    # reading_part2 = f_str.split(',')[:-1]
    # reading_number2 = ['例1', 26, 27, 28, 29, 30]
    # reading_part2_titles = []
    # time.sleep(3)
    # response_text = driver.page_source
    # title_strs = re.findall(r'<ruby>[\s\S]+?</div>', response_text)
    # print(len(title_strs))
    # if len(title_strs) == 6:
    #     for title_str in title_strs:
    #         title_text = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(' ', ''))
    #         print(title_text)
    #         part2_title_text = re.sub(r'\xa0([A-Z])\xa0', '', title_text)
    #         reading_part2_titles.append(part2_title_text.replace('\xa0', ' '))
    #         print(re.findall(r'\xa0([A-Z])\xa0', title_text))
    #         if len(re.findall(r'\xa0([A-Z])\xa0', title_text)) > 0:
    #             part2_answer_0 = re.findall(r'\xa0([A-Z])\xa0', title_text)
    #         else:
    #             continue
    # else:
    #     reading_part2_titles_1 = []
    #     part3_title_0 = driver.find_elements_by_xpath('//img')[9].get_attribute('src')
    #     for title_str in title_strs:
    #         title_text = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(' ', ''))
    #         print(title_text)
    #         part2_title_text = re.sub(r'\xa0([A-Z])\xa0', '', title_text)
    #         reading_part2_titles_1.append(part2_title_text.replace('\xa0', ' '))
    #         print(re.findall(r'\xa0([A-Z])\xa0', title_text))
    #         # if len(re.findall(r'\xa0([A-Z])\xa0', title_text)) > 0:
    #         #     part2_answer_0 = re.findall(r'\xa0([A-Z])\xa0', title_text)
    #         # else:
    #         #     continue
    #     reading_part2_titles = [part3_title_0] + reading_part2_titles_1
    #     part2_answer_0 = ['']
    #
    # img_urls = driver.find_elements_by_xpath('//img')
    # choices = ['A', 'B', 'C', 'D', 'E', 'F']
    # reading_part2_choice = []
    # for choice, imgurl in zip(choices, img_urls[3:9]):
    #     img_url = imgurl.get_attribute('src')
    #     one_choice = choice + '、' + img_url
    #     reading_part2_choice.append(one_choice)
    # reading_part2_choice_str = '  '.join(reading_part2_choice)
    # reading_part2_choice_text = (reading_part2_choice_str + ',') * 6
    # reading_part2_choices = reading_part2_choice_text.split(',')[:-1]
    # print(len(reading_part2_choices))
    #
    # print('777777777')
    # time.sleep(1)
    # g_str = '第三部分,' * 6
    # reading_part3 = g_str.split(',')[:-1]
    # reading_number3 = ['例1', 31, 32, 33, 34,35]
    # reading_part3_titles = []
    # driver.find_element_by_id('btnNext').click()
    # time.sleep(3)
    # response_text = driver.page_source
    # title_strs = re.findall(r'<ruby>[\s\S]+?</div>', response_text.split('例如：')[1])
    # # print(len(title_strs))
    # # print(title_strs)
    # for title_str in title_strs:
    #     # print(title_str)
    #     title_text = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(' ', ''))
    #     reading_part3_titles.append(title_text)
    #     try:
    #         part2_answer = re.findall(r'[A-Z]', title_text.split('（')[1])
    #     except:
    #         pass
    # chocie_strs = re.findall(r'<ruby>[\s\S]+?</div>', response_text)[0]
    # chocie_str_li = chocie_strs.split('<br>')
    # chocies_str = ''.join(chocie_str_li)
    # chocie_strs = re.findall(r'<ruby>[\s\S]+?<br', chocies_str.replace('\n', '').replace(' ', ''))
    # choices = ['A', 'B', 'C', 'D', 'E', 'F']
    # reading_part3_choice = []
    # for choice, chocie_str in zip(choices, chocie_strs):
    #     chocie_text = re.sub(r'<(.+?)>', '', chocie_str.replace('\n', '').replace(' ', ''))
    #     one_choice = choice + '、' + chocie_text[:-3]
    #     reading_part3_choice.append(one_choice)
    # reading_part3_choice_str = '  '.join(reading_part3_choice)
    # reading_part3_choice_text = (reading_part3_choice_str + ',') * 6
    # reading_part3_choices = reading_part2_choice_text.split(',')[:-1]
    # print(len(reading_part3_choices))
    #
    # print('888888888')
    # time.sleep(1)
    # h_str = '第四部分,' * 6
    # reading_part4 = h_str.split(',')[:-1]
    # reading_number4 = ['例1', 36, 37, 38, 39, 40]
    # reading_part4_titles = []
    # driver.find_element_by_id('btnNext').click()
    # time.sleep(3)
    # response_text = driver.page_source
    # title_strs = re.findall(r'<ruby>[\s\S]+?</div>', response_text.split('例如：')[1])
    # for title_str in title_strs:
    #     title_text = re.sub(r'<(.+?)>', '', title_str.replace('\n', '').replace(r' ', ''))
    #     part4_title_text = re.sub(r'\xa0([A-Z])\xa0', '', title_text).replace('\xa0', ' ')
    #     reading_part4_titles.append(''.join(part4_title_text))
    #     if len(re.findall(r'\xa0([A-Z])\xa0', title_text)) > 0:
    #         part4_answer_0 = re.findall(r'\xa0([A-Z])\xa0', title_text)
    #     else:
    #         continue
    # chocie_strs = re.findall(r'<ruby>[\s\S]+?例如', response_text.replace('\n', '').replace(' ', ''))[0]
    # # print(chocie_strs)
    # choices_str = re.split('</ruby>[A-Z]<ruby>', ''.join(chocie_strs[:-2].split('\xa0')))
    # # print(len(choices_str))
    # # print(choices_str)
    # choices = ['A', 'B', 'C', 'D', 'E', 'F']
    # reading_part4_choice = []
    # for choice, choice_str in zip(choices, choices_str):
    #     chocie_text = re.sub(r'<(.+?)>', '', choice_str.replace('\n', '').replace('\xa0', ''))
    #     # print(chocie_text)
    #     one_choice = choice + '、' + chocie_text
    #     # print(one_choice)
    #     reading_part4_choice.append(one_choice)
    # reading_part4_choice_str = '  '.join(reading_part4_choice)
    # reading_part4_choice_text = (reading_part4_choice_str + ',') * 6
    # reading_part4_choices = reading_part4_choice_text.split(',')[:-1]
    # print(len(reading_part4_choices))

    # 提交试题得到答案

    # driver.find_element_by_id('btnsubmitTest').click()
    # time.sleep(2)
    # driver.find_element_by_id('ctl00_CphMain_LblSubmit').click()
    # time.sleep(2)

    cookie_list = driver.get_cookies()
    cookies_list = []
    for cookie in cookie_list:
        cookie_str = cookie['name'] + '=' + cookie['value']
        cookies_list.append(cookie_str)
    cookies = '; '.join(cookies_list)
    print(cookies)

    onedata = (HSKlevel, test_name, audios_url, cookies)
    sql = 'insert into hanban_cookies (HSKlevel, test_name, audios_url, cookies) value (%s,%s,%s,%s)'
    cur_105.execute(sql, onedata)
    con_105.commit()
    # time.sleep(1)
    # driver.find_element_by_id('ctl00_CphMain_BtnOk').click()
    # time.sleep(1)
    # driver.find_element_by_id('ctl00_CphMain_BtnClose').click()
    # time.sleep(2)

    # driver.close()
    driver.quit()
