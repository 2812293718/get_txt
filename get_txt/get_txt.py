
import re
import requests
import os
"""
    
    从笔趣阁中获取玄化小说
    
    """
def get_page_data(url, headers):
    t = 0
    page_text = requests.get(url=url, headers=headers).text
    obj1 = re.compile(r'<span class=.*?href="(.*?)"',re.S)
    obj_title = re.compile(r'<span class=.*?target="_blank">(.*?)</a>',re.S)
    # print(page_text)
    # 首页玄幻板块小说
    page_url_list = obj1.findall(page_text)
    page_title_list = obj_title.findall(page_text)
    # 遍历到每一部小说
    for page_url in page_url_list[:-2]:
        t += 1
        page_download_url = 'https://www.biqudu.net' + page_url
        # print(page_download_url)
        in_page_text = requests.get(url=page_download_url, headers=headers).text
        obj = re.compile(r'<a style=.*?href="(.*?)"', re.S)
        ps_url_list = obj.findall(in_page_text)
        # print(ps_url_list)
        # 遍历到每一章节
        for ps_url in ps_url_list:
            "https://www.biqudu.net/63_63147/3570545.html"
            ps_download_url = 'https://www.biqudu.net' + ps_url
            # print(ps_download_url)
            every_text = requests.get(url=ps_download_url, headers=headers).text
            obj1 = re.compile(r'<div id="content">(.+?)</div>', re.S)
            obj_in_page_title = re.compile(r'<div class=.*?<h1>(.*?)</h1>', re.S)
            in_page = obj1.findall(every_text)
            in_page_title = obj_in_page_title.findall(every_text)
            page_title = page_title_list[t]
            print(page_title)
            # print(in_page_title)
            # print(in_page)
            # 文件名不可用特殊符号，将章节标题中的文件名替换。
            in_page_title = in_page_title[0].replace('?','').replace('!','').replace('.','').replace('、','').replace('|','').replace('*','').replace('/','').replace('\\','').replace('<','').replace('>','').replace('\"','').replace('`','')

            # print(in_page_title)
            writeToFile( in_page[0],page_title,in_page_title)



def writeToFile(in_page, title,in_page_title):
    path = 'txt/' + title
    name = '/'+ in_page_title + ".txt"
    if not os.path.exists(path):
        os.mkdir(path)
    real_text = in_page.replace('<br/>', '''
    ''')  # 替换换行
    real_text = real_text.replace('\r\n\t\t\t\t\u3000\u3000一秒记住【笔趣阁\u3000】为您提供最快更新！', '').replace('<script>chaptererror();</script>','')
    real_text = real_text.replace('u3000', '	')  # 替换制表
    real_text = real_text.replace('&nbsp;', ' ')  # 替换空格
    with open(r'txt/' + title + '/'+ in_page_title + "a.txt", 'w', encoding='utf-8') as f:
        f.write(real_text)
        f.close()
    print(in_page_title+"  下载完成！！")


if __name__ == '__main__':
    # 创建文件夹
    if not os.path.exists('txt'):
        os.mkdir('txt')
    # 遍历每一页--{page}
    for p in range(3):

        url = 'https://www.biqudu.net/searchbook.php?keyword=%E7%8E%84%E5%B9%BB&page={}'.format(p)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/67.0.396.99 Safari/537.36',
            'Cookie': 'BIDUPSID=502200AFB81FE7181B1A8833BA3AA17B; PSTM=1648018908; BAIDUID=502200AFB81FE718C397DD42E9B34BD9:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31254_36005_35909_36165_34584_36120_36232_26350_36300_36315_36061; BA_HECTOR=0k01208lag0g0124mg1h6hj490r; delPer=0; PSINO=1; BAIDU_WISE_UID=wapp_1651035318851_663; BAIDUID_BFESS=897EE5B4436C0007AC03A853F722680C:FG=1; BCLID=10457401896746647562; BDSFRCVID=260OJexroG01VTjDeXVJMWG1yEJ4OdoTDYrEOwXPsp3LGJLVg1mDEG0PtHM7R2DbY6ONogKKW2OTHT8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbPO_C-yJID3fn74bKTahjoLjmT22jna-tj9aJ5nJDoAjtoG3jJUbqvyWtcU05o85R6ahDJlQpP-eCOKhpLBQ5KzDUKHK4vHJ2bnKl0MLnjWbb0xyTOY36FiXfnMBMnUteOnaU-y3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4j58WDT3LDHRf-b-X-Kb0QnT8MJnhHJrd5tQ_q4tHePjNtURZ5mAqoD375UJ8jlbNWhJEXq-1DqrpWUrg3K7naIQqahbKhl3EhpnkW4DUQM6HWt743bRTWbLy5KJvfJoE3pQhhP-UyntHWh37QnblMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD_-MK_xD58MePDyqx5Ka43tHD7yWCvKWpQcOR59K4nnD5_Z3M6RKlvgbejUKKjX3lFM8nbv3MOZKxLg5n7Tbb8eBgvZ2UQjtR6Usq0x0bO1Xj-wD4OaX659BDOMahv6tq7xOM-9QlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXjG8HJT8JJn3y0JQVKbK_qbbIq4b_eUAOMPnZKRvHa2kjoxQm2qbqoM8lXqJnDJFkyGO9KPRn3N5HKC5V3C5x84c1-t5M34bLhtO405OTbgbu_M_-3noZMl78hPJvypbXXnO7LTvlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_KJI_2hK-meP55q4D_MfOtetJyaR0H_DJvWJ5WqR7jD5Q43-IvbJ7pBfrU3b68KlF2BbboShbXKxoc5pkrKp0eWUbZBNcMoR6g3l02V-bSXjJCDx0VWHj9WtRMW23Uoq7mWU-WsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKDHAHJjJP; BCLID_BFESS=10457401896746647562; BDSFRCVID_BFESS=260OJexroG01VTjDeXVJMWG1yEJ4OdoTDYrEOwXPsp3LGJLVg1mDEG0PtHM7R2DbY6ONogKKW2OTHT8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbPO_C-yJID3fn74bKTahjoLjmT22jna-tj9aJ5nJDoAjtoG3jJUbqvyWtcU05o85R6ahDJlQpP-eCOKhpLBQ5KzDUKHK4vHJ2bnKl0MLnjWbb0xyTOY36FiXfnMBMnUteOnaU-y3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4j58WDT3LDHRf-b-X-Kb0QnT8MJnhHJrd5tQ_q4tHePjNtURZ5mAqoD375UJ8jlbNWhJEXq-1DqrpWUrg3K7naIQqahbKhl3EhpnkW4DUQM6HWt743bRTWbLy5KJvfJoE3pQhhP-UyntHWh37QnblMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD_-MK_xD58MePDyqx5Ka43tHD7yWCvKWpQcOR59K4nnD5_Z3M6RKlvgbejUKKjX3lFM8nbv3MOZKxLg5n7Tbb8eBgvZ2UQjtR6Usq0x0bO1Xj-wD4OaX659BDOMahv6tq7xOM-9QlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXjG8HJT8JJn3y0JQVKbK_qbbIq4b_eUAOMPnZKRvHa2kjoxQm2qbqoM8lXqJnDJFkyGO9KPRn3N5HKC5V3C5x84c1-t5M34bLhtO405OTbgbu_M_-3noZMl78hPJvypbXXnO7LTvlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_KJI_2hK-meP55q4D_MfOtetJyaR0H_DJvWJ5WqR7jD5Q43-IvbJ7pBfrU3b68KlF2BbboShbXKxoc5pkrKp0eWUbZBNcMoR6g3l02V-bSXjJCDx0VWHj9WtRMW23Uoq7mWU-WsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKDHAHJjJP; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1651056973; hkpcSearch=%u5C0F%u54C1; av1_switch_v3=0; PC_TAB_LOG=video_details_page; COMMON_LID=d95acc0d964aadb22746d1be2db1d76e; ab_sr=1.0.1_M2M3MDU3YTllNjgyN2I2ODhlMzg1NWNhMDcyNWY4NGNlMDZlOGRmNGUxYjU4NzBkNTM1NGE0MjhlZWQyMDU2Mzk4Yzc1ZDk5YzQ5Y2E0YjViNzU2MDhkMmNiZmViYzliNWUzNmQ3ZGZmZTI3ZThhNWQ2NmZmYTg4YTAxNWM3ZTExM2U1NjQxYjVkYTcwNzNjZmE2N2MwNzU0ZTY0YjA3Ng==; reptileData=%7B%22data%22%3A%22d6c9cda39b2af4ed4c6d81ebc2c13c0d3228503c5218bfdc699e05a251439274085a3a6b1dea3f610e8e1368853dc70f9a2704811e037a7ada52d9a9febbf9f5c80914fdf16b96a4907b8da1172f2fe0de72bfa65f6d0ff87d77b5503c7429ec%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%229cebdc98%22%7D; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1651058134; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=lyfi30665ga&ss=l2hgozt4&sl=5&tt=3gpp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=pmjl"'
        }
        page_text = get_page_data(url, headers)

