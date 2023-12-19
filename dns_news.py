import requests
from  bs4 import  BeautifulSoup
import json



cookies = {
    'phonesIdent': '64fb6da82d0cac0181567c176bb6f1c1e92fa155349270e943fe1c00e51be1ffa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2286122bdb-482e-4f39-8023-102565c3593f%22%3B%7D',
    'ipp_uid': '1659096199693/SNHVxOSk4O2e1Jbe/BmICJpUCdC/3Na4VmIoTXQ==',
    'rrpvid': '913447649970503',
    '_ym_uid': '1659096200764281073',
    'rcuid': '62e3cc88914df6fecdb80e3d',
    '_gcl_au': '1.1.329208953.1678538831',
    '_ym_d': '1678538832',
    'spid': '1678539818984_f24876ddb3573c55f2f8f63667e4b06f_b4mipj94uscfbk0i',
    'tmr_lvid': 'ffcebd6afc3342323ff3d4b65a44cefd',
    'tmr_lvidTS': '1659096200515',
    '_ga': 'GA1.2.840501745.1659096200',
    '_ga_FLS4JETDHW': 'GS1.1.1678615699.3.1.1678615746.13.0.0',
    'rerf': 'AAAAAGQOwGlt0wiLAzv9Ag==',
    'date-user-last-order-v2': '8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D',
    'spid': '1679167274112_bb45707de92881c0b0746690c39aba15_62qo5lawari6mwn1',
    '_gaexp': 'GAX1.2.Uth_b8BjS4eYr9UxIE_0Vg.19524.1!Uo8OYhgyRvyI9jNbUapMXA.19523.1',
    'auth_public_uid': '2b691755a239463b42743c024b6786b9',
    'cartUserCookieIdent_v3': 'f92c99f81818ff722f667336ea096280a2cebfca88fe0138944d4a44add81363a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2250a14851-e959-321f-b9fb-0e72ca4e41a5%22%3B%7D',
    'current_path': '195e323377f5c16c96618a93cd6f774fe46f6aa38c334480a0f2c9c2f89c18fea%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A121%3A%22%7B%22city%22%3A%22e3ff7ef2-92b6-4ab7-b2ff-4d58cab73dbc%22%2C%22cityName%22%3A%22%5Cu041f%5Cu0435%5Cu0440%5Cu0435%5Cu0432%5Cu043e%5Cu0437%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'cf_avails': 'now-today-tomorrow',
    'ipp_sign': '26e3e3593ef8f81f8472a0efe83eb069_790980369_ca0330eaefc95b5ccdf9b32154ddcb51',
    'auth_access_token': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6ImZmYjRhN2U3ZTIxZGM3MWNkMjQ2YjUxZjZlMThiYzczOTI3YjIyNTBjNzVkZmIyNDJiZDEyZGIxMWM3MTJmYTgiLCJleHAiOjE2ODEyMzMyNTUsInJuZCI6IjYxMDExOTZjYWZiNjY2OWRiYTM0MGQwYTJmMTExNzIxNGQwODRkZTU3NjJhMTE1YmVmMjYwYzA0YmJiYmY2N2EiLCJ1c2VySWQiOiI5NzM5NGM1MC1hNWMwLTU4OTUtY2Y5Yi0yNmUzMGVmNzE5NGQiLCJ1c2VyTmFtZSI6IiJ9.MEQCIDgccMLo5z-tsnXwicShYGgjWbehSgVwFQwbEuXRZzF9AiALMd36zaNQwcvg59qPv8V0QBgrJFAr5NpXGZTcadaR7A',
    'auth_refresh_token': '6ca798d3ed42704616a6feecbdc6a3de74b20226e4a412e58050807bf50b5795',
    'auth_ssid': 'ffb4a7e7e21dc71cd246b51f6e18bc73927b2250c75dfb242bd12db11c712fa8',
    'PHPSESSID': '86aa73611ccc2088e7c4d59463fd8d42',
    'lang': 'ru',
    '_ab_': '%7B%22search-design%22%3A%22new%22%2C%22search-checkbox%22%3A%22SEARCH_OUT_OF_STOCK%22%7D',
    '_csrf': 'a7dd54ab7836a71bc5f6d937de1447f342143685b004041efe5d292efaa81fc3a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22kIIfCBmJrpIi3vSTIl6gff0w5W8EahHA%22%3B%7D',
    '_gid': 'GA1.2.596071058.1681232357',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'tmr_detect': '0%7C1681232359627',
    '_gat_UA-8349380-2': '1',
    'ipp_key': 'v1681232392760/v33947245ba5adc7a72e273/x7eQGfxqwSy4h4VTCbl5pA==',
    'rr-testCookie': 'testvalue',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'phonesIdent=64fb6da82d0cac0181567c176bb6f1c1e92fa155349270e943fe1c00e51be1ffa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2286122bdb-482e-4f39-8023-102565c3593f%22%3B%7D; ipp_uid=1659096199693/SNHVxOSk4O2e1Jbe/BmICJpUCdC/3Na4VmIoTXQ==; rrpvid=913447649970503; _ym_uid=1659096200764281073; rcuid=62e3cc88914df6fecdb80e3d; _gcl_au=1.1.329208953.1678538831; _ym_d=1678538832; spid=1678539818984_f24876ddb3573c55f2f8f63667e4b06f_b4mipj94uscfbk0i; tmr_lvid=ffcebd6afc3342323ff3d4b65a44cefd; tmr_lvidTS=1659096200515; _ga=GA1.2.840501745.1659096200; _ga_FLS4JETDHW=GS1.1.1678615699.3.1.1678615746.13.0.0; rerf=AAAAAGQOwGlt0wiLAzv9Ag==; date-user-last-order-v2=8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D; spid=1679167274112_bb45707de92881c0b0746690c39aba15_62qo5lawari6mwn1; _gaexp=GAX1.2.Uth_b8BjS4eYr9UxIE_0Vg.19524.1!Uo8OYhgyRvyI9jNbUapMXA.19523.1; auth_public_uid=2b691755a239463b42743c024b6786b9; cartUserCookieIdent_v3=f92c99f81818ff722f667336ea096280a2cebfca88fe0138944d4a44add81363a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2250a14851-e959-321f-b9fb-0e72ca4e41a5%22%3B%7D; current_path=195e323377f5c16c96618a93cd6f774fe46f6aa38c334480a0f2c9c2f89c18fea%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A121%3A%22%7B%22city%22%3A%22e3ff7ef2-92b6-4ab7-b2ff-4d58cab73dbc%22%2C%22cityName%22%3A%22%5Cu041f%5Cu0435%5Cu0440%5Cu0435%5Cu0432%5Cu043e%5Cu0437%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; cf_avails=now-today-tomorrow; ipp_sign=26e3e3593ef8f81f8472a0efe83eb069_790980369_ca0330eaefc95b5ccdf9b32154ddcb51; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6ImZmYjRhN2U3ZTIxZGM3MWNkMjQ2YjUxZjZlMThiYzczOTI3YjIyNTBjNzVkZmIyNDJiZDEyZGIxMWM3MTJmYTgiLCJleHAiOjE2ODEyMzMyNTUsInJuZCI6IjYxMDExOTZjYWZiNjY2OWRiYTM0MGQwYTJmMTExNzIxNGQwODRkZTU3NjJhMTE1YmVmMjYwYzA0YmJiYmY2N2EiLCJ1c2VySWQiOiI5NzM5NGM1MC1hNWMwLTU4OTUtY2Y5Yi0yNmUzMGVmNzE5NGQiLCJ1c2VyTmFtZSI6IiJ9.MEQCIDgccMLo5z-tsnXwicShYGgjWbehSgVwFQwbEuXRZzF9AiALMd36zaNQwcvg59qPv8V0QBgrJFAr5NpXGZTcadaR7A; auth_refresh_token=6ca798d3ed42704616a6feecbdc6a3de74b20226e4a412e58050807bf50b5795; auth_ssid=ffb4a7e7e21dc71cd246b51f6e18bc73927b2250c75dfb242bd12db11c712fa8; PHPSESSID=86aa73611ccc2088e7c4d59463fd8d42; lang=ru; _ab_=%7B%22search-design%22%3A%22new%22%2C%22search-checkbox%22%3A%22SEARCH_OUT_OF_STOCK%22%7D; _csrf=a7dd54ab7836a71bc5f6d937de1447f342143685b004041efe5d292efaa81fc3a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22kIIfCBmJrpIi3vSTIl6gff0w5W8EahHA%22%3B%7D; _gid=GA1.2.596071058.1681232357; _gat=1; _gat_%5Bobject%20Object%5D=1; _ym_isad=2; _ym_visorc=b; tmr_detect=0%7C1681232359627; _gat_UA-8349380-2=1; ipp_key=v1681232392760/v33947245ba5adc7a72e273/x7eQGfxqwSy4h4VTCbl5pA==; rr-testCookie=testvalue',
    'Origin': 'https://www.dns-shop.ru',
    'Referer': 'https://www.dns-shop.ru/catalog/actions/no-referrer',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.895 Yowser/2.5 Safari/537.36',
    'X-CSRF-Token': 'AIj977LXRawHhLBtn20DgXrIAiUGyZeW8Bhd5_vtGBBrwbSJ8ZUo5nX0-QSsG1DVM6Q0QmCvp-HFT2WimoVQUQ==',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'data={"type":"product-buy","containers":[{"id":"as-uZxSsd","data":{"id":"5338749"}},{"id":"as-qvEsci","data":{"id":"5066856"}},{"id":"as-XlL8ar","data":{"id":"8122103"}},{"id":"as-R9g1Yu","data":{"id":"9945668"}},{"id":"as--Mzj7N","data":{"id":"5352198"}},{"id":"as-4Gw00i","data":{"id":"1103154"}},{"id":"as-gDoJ9U","data":{"id":"5360867"}},{"id":"as-2ibra3","data":{"id":"5365397"}},{"id":"as-oqyTou","data":{"id":"9927200"}},{"id":"as-onTaRh","data":{"id":"9909797"}},{"id":"as-2xRsuJ","data":{"id":"5300666"}},{"id":"as-obTy_H","data":{"id":"4787374"}},{"id":"as-IvoQ3Q","data":{"id":"5321301"}},{"id":"as-NaBJfh","data":{"id":"1216153"}},{"id":"as-1OfmYw","data":{"id":"9901518"}},{"id":"as-INN3Om","data":{"id":"4828799"}},{"id":"as-QI0You","data":{"id":"5370937"}},{"id":"as-9hcgCI","data":{"id":"1136205"}}]}'

response = requests.get('https://www.dns-shop.ru/catalog/actions/?stock=now-today-tomorrow&category', cookies=cookies, headers=headers, data=data)



with open('res2.json', 'w', encoding='utf-8') as file:
    cart = file.write(response.text)



# with open('res2.json', 'r', encoding='utf-8') as file:
#     cart2 = json.load(file)
# d = cart2['data']['states']
# for i in d:
#
#     print(i['data']['name'], i['data']['price']['current'])

# for i in cart[data]:
#     print(i['name']["containers"])