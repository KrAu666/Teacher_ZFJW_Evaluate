import json
import sys
import requests
from lxml import etree

def get_teacher_message():
    i = 0
    totalPage = 999
    teacher_list_data = []
    while i < totalPage:
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Origin': 'https://jwxt.gcc.edu.cn',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'doType': 'query',
            'gnmkdm': 'N401605',
        }

        data = {
            '_search': 'false',
            'nd': '1718518825707',
            'queryModel.showCount': '15',
            f'queryModel.currentPage': {i+1},
            'queryModel.sortName': 'kcmc,jzgmc ',
            'queryModel.sortOrder': 'asc',
            'time': '0',
        }

        response = requests.post(
            'https://jwxt.gcc.edu.cn/xspjgl/xspj_cxXspjIndex.html',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        datas = json.loads(response.text)
        teacher_list_data.append(datas)
        totalPage = datas['totalPage']
        i += 1

    return teacher_list_data


def fill_form(datas):
    for i in range(len(datas['items'])):
        jxh_id = datas['items'][i]['jgh_id']
        jxb_id = datas['items'][i]['jxb_id']
        kch_id = datas['items'][i]['kch_id']
        xsdm = datas['items'][i]['xsdm']
        jgh_id = datas['items'][i]['jgh_id']
        sfcjlrjs = datas['items'][i]['sfcjlrjs']
        tjzt = datas['items'][i]['tjzt']

        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Origin': 'https://jwxt.gcc.edu.cn',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'gnmkdm': 'N401605',
        }

        data = {
            'jxb_id': jxb_id,
            'kch_id':  kch_id,
            'xsdm': xsdm,
            'jgh_id': jgh_id,
            'tjzt': tjzt,
            'sfcjlrjs': sfcjlrjs,
        }

        response = requests.post(
            'https://jwxt.gcc.edu.cn/xspjgl/xspj_cxXspjDisplay.html',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        e = etree.HTML(response.text)
        try:
            data_pfdjdmxmb_id_value = e.xpath('//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[1]/tbody/tr/td[2]/div/div[1]/label/input/@data-pfdjdmxmb_id')[0]
        except:
            print('该老师已填写完毕')
            continue
        name_value = e.xpath('//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[1]/tbody/tr/td[2]/div/div[1]/label/input//@name')[0]
        name_value = name_value.split('_')
        pjzbxm_id = e.xpath('//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table/tbody/tr/@data-pjzbxm_id')
        xspfb_id = e.xpath('//*[@id="ajaxForm1"]/div[2]/div[@data-xspfb_id]')
        for element in xspfb_id:
            xspfb_id = element.get('data-xspfb_id')

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            # 'Cookie': 'route=eb50131048d7e112b90dc25102786a8d; JSESSIONID=61D94B2D094D1183A2CA0F22D6A5216F',
            'Origin': 'https://jwxt.gcc.edu.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://jwxt.gcc.edu.cn/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'gnmkdm': 'N401605',
        }

        data = {
            'ztpjbl': '100',
            'jszdpjbl': '0',
            'xykzpjbl': '0',
            'jxb_id': jxb_id,
            'kch_id': kch_id,
            'jgh_id': jxh_id,
            'xsdm': xsdm,
            'modelList[0].pjmbmcb_id': name_value[0],
            'modelList[0].pjdxdm': '01',
            'modelList[0].fxzgf': '',
            'modelList[0].py': '',
            'modelList[0].xspfb_id': xspfb_id,
            'modelList[0].xspjList[0].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[0].childXspjList[0].pjzbxm_id': pjzbxm_id[0],
            'modelList[0].xspjList[0].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[0].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[0].pjzbxm_id': pjzbxm_id[0],
            'modelList[0].xspjList[1].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[1].childXspjList[0].pjzbxm_id': pjzbxm_id[1],
            'modelList[0].xspjList[1].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[1].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[1].pjzbxm_id': pjzbxm_id[1],
            'modelList[0].xspjList[2].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[2].childXspjList[0].pjzbxm_id': pjzbxm_id[2],
            'modelList[0].xspjList[2].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[2].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[2].pjzbxm_id': pjzbxm_id[2],
            'modelList[0].xspjList[3].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[3].childXspjList[0].pjzbxm_id': pjzbxm_id[3],
            'modelList[0].xspjList[3].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[3].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[3].pjzbxm_id': pjzbxm_id[3],
            'modelList[0].xspjList[4].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[4].childXspjList[0].pjzbxm_id': pjzbxm_id[4],
            'modelList[0].xspjList[4].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[4].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[4].pjzbxm_id': pjzbxm_id[4],
            'modelList[0].xspjList[5].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[5].childXspjList[0].pjzbxm_id': pjzbxm_id[5],
            'modelList[0].xspjList[5].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[5].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[5].pjzbxm_id': pjzbxm_id[5],
            'modelList[0].xspjList[6].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[6].childXspjList[0].pjzbxm_id': pjzbxm_id[6],
            'modelList[0].xspjList[6].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[6].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[6].pjzbxm_id': pjzbxm_id[6],
            'modelList[0].xspjList[7].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[7].childXspjList[0].pjzbxm_id': pjzbxm_id[7],
            'modelList[0].xspjList[7].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[7].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[7].pjzbxm_id': pjzbxm_id[7],
            'modelList[0].xspjList[8].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[8].childXspjList[0].pjzbxm_id': pjzbxm_id[8],
            'modelList[0].xspjList[8].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[8].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[8].pjzbxm_id': pjzbxm_id[8],
            'modelList[0].xspjList[9].childXspjList[0].pfdjdmxmb_id': data_pfdjdmxmb_id_value,
            'modelList[0].xspjList[9].childXspjList[0].pjzbxm_id': pjzbxm_id[9],
            'modelList[0].xspjList[9].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[9].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[9].pjzbxm_id': pjzbxm_id[9],
            'modelList[0].xspjList[10].childXspjList[0].zgpj': '',
            'modelList[0].xspjList[10].childXspjList[0].pjzbxm_id': pjzbxm_id[10],
            'modelList[0].xspjList[10].childXspjList[0].pfdjdmb_id': name_value[2],
            'modelList[0].xspjList[10].childXspjList[0].zsmbmcb_id': name_value[0],
            'modelList[0].xspjList[10].pjzbxm_id': pjzbxm_id[10],
            'modelList[0].pjzt': '1',
            'tjzt': '1',
        }

        response = requests.post(
            'https://jwxt.gcc.edu.cn/xspjgl/xspj_tjXspj.html',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        print(response.text)


if __name__ == '__main__':

    """
    本脚本为添加js逆向部分，请自行抓包获取cookie
    浏览器抓包教程视频：
        https://www.bilibili.com/video/BV1G24y1o75g/
    只需要把route和JSESSIONID冒号后面的内容填写至冒号中间即可
    """

    # 请填写cookie
    cookies = {
        'route': '请填写cookie',
        'JSESSIONID': '请填写cookie',
    }

    if '请填写cookie' in str(cookies):
        print('请填写cookie后再进行操作')
        sys.exit()

    teacher_list_data = get_teacher_message()
    for datas in teacher_list_data:
        fill_form(datas)

    print('所有老师均已填写完毕')

