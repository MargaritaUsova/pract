import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_data():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
        'bIPs': '53593859',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '_gid': 'GA1.2.777481713.1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2433014794.20480.0000',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'JSESSIONID': '6xSnkThYPkyy6phMhdqpzvv1HJ2DrL7TkZD1Nsb2vHnyZspQZxg2!716989621',
        '_ym_isad': '2',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        '_sp_id.d61c': 'ae2f8cb0-62f2-402e-866a-f75052b0dada.1687034037.7.1687109413.1687106703.6b331e84-5892-4fe3-942b-fd86212fe5a3.98031e7a-8fa2-4a79-8d82-c94655fc1f5b.ea5a997e-a72a-4de7-a505-f690771440e8.1687109413163.7',
        '_ga': 'GA1.2.1990035478.1687034037',
        'tmr_detect': '0%7C1687109418997',
        'gssc218': '',
        'gsscgib-w-mvideo': 'eu/rVVzuS/yiRBDcNNqnR/Kx333bTuVS8cq8v+zTHWJkpb9ljOaVpWwMR7qx3FHJr4lObXTFT85kdceoz9VfTh4gJLCEkflpeg/jB1UAlM7t/Pm0DY8PCA7Y/trY92vPpxDuZg9c60X+SPneexWAl1ZSqrLSUyMBmVmhAIdtLNirthzV9Wb78VhL/GczWU7BZKrIjhJnjozX5G2cKORjkFqDKKre6Ou3tELE+oJ64CttwlohV0fc7rMn19OjYik=',
        'gsscgib-w-mvideo': 'eu/rVVzuS/yiRBDcNNqnR/Kx333bTuVS8cq8v+zTHWJkpb9ljOaVpWwMR7qx3FHJr4lObXTFT85kdceoz9VfTh4gJLCEkflpeg/jB1UAlM7t/Pm0DY8PCA7Y/trY92vPpxDuZg9c60X+SPneexWAl1ZSqrLSUyMBmVmhAIdtLNirthzV9Wb78VhL/GczWU7BZKrIjhJnjozX5G2cKORjkFqDKKre6Ou3tELE+oJ64CttwlohV0fc7rMn19OjYik=',
        'fgsscgib-w-mvideo': 'CP2k31ec4394da7966ffb477e75e073c64dfc892',
        'fgsscgib-w-mvideo': 'CP2k31ec4394da7966ffb477e75e073c64dfc892',
        'cfidsgib-w-mvideo': 'WFBio/KTGRMSxgHLGu9IXKvFrWfHt8EqD1f5nTmKrWQhXi7JIQW7AnMnGmmW5/ASAlVAO/1BooScTwKvRJjEUBkmPyIRH2X1pk6Q9XFhZxSWADYGJL/j75s2fhZZTfoCTgoaLTuYQoIz9ZEAYSOjvNLksrM93mB3Uftmkz4=',
        '__hash_': 'b8c2f7d8dc22cf32c7515dea1f745b35',
        '_ga_CFMZTSS5FM': 'GS1.1.1687111763.8.0.1687111763.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687111763.8.0.1687111763.60.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=81d92a5f1b39439c94fd7d61ca9545a6,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; _ym_uid=1687034037702065663; _ym_d=1687034037; _gid=GA1.2.777481713.1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2433014794.20480.0000; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; JSESSIONID=6xSnkThYPkyy6phMhdqpzvv1HJ2DrL7TkZD1Nsb2vHnyZspQZxg2!716989621; _ym_isad=2; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; _sp_id.d61c=ae2f8cb0-62f2-402e-866a-f75052b0dada.1687034037.7.1687109413.1687106703.6b331e84-5892-4fe3-942b-fd86212fe5a3.98031e7a-8fa2-4a79-8d82-c94655fc1f5b.ea5a997e-a72a-4de7-a505-f690771440e8.1687109413163.7; _ga=GA1.2.1990035478.1687034037; tmr_detect=0%7C1687109418997; gssc218=; gsscgib-w-mvideo=eu/rVVzuS/yiRBDcNNqnR/Kx333bTuVS8cq8v+zTHWJkpb9ljOaVpWwMR7qx3FHJr4lObXTFT85kdceoz9VfTh4gJLCEkflpeg/jB1UAlM7t/Pm0DY8PCA7Y/trY92vPpxDuZg9c60X+SPneexWAl1ZSqrLSUyMBmVmhAIdtLNirthzV9Wb78VhL/GczWU7BZKrIjhJnjozX5G2cKORjkFqDKKre6Ou3tELE+oJ64CttwlohV0fc7rMn19OjYik=; gsscgib-w-mvideo=eu/rVVzuS/yiRBDcNNqnR/Kx333bTuVS8cq8v+zTHWJkpb9ljOaVpWwMR7qx3FHJr4lObXTFT85kdceoz9VfTh4gJLCEkflpeg/jB1UAlM7t/Pm0DY8PCA7Y/trY92vPpxDuZg9c60X+SPneexWAl1ZSqrLSUyMBmVmhAIdtLNirthzV9Wb78VhL/GczWU7BZKrIjhJnjozX5G2cKORjkFqDKKre6Ou3tELE+oJ64CttwlohV0fc7rMn19OjYik=; fgsscgib-w-mvideo=CP2k31ec4394da7966ffb477e75e073c64dfc892; fgsscgib-w-mvideo=CP2k31ec4394da7966ffb477e75e073c64dfc892; cfidsgib-w-mvideo=WFBio/KTGRMSxgHLGu9IXKvFrWfHt8EqD1f5nTmKrWQhXi7JIQW7AnMnGmmW5/ASAlVAO/1BooScTwKvRJjEUBkmPyIRH2X1pk6Q9XFhZxSWADYGJL/j75s2fhZZTfoCTgoaLTuYQoIz9ZEAYSOjvNLksrM93mB3Uftmkz4=; __hash_=b8c2f7d8dc22cf32c7515dea1f745b35; _ga_CFMZTSS5FM=GS1.1.1687111763.8.0.1687111763.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687111763.8.0.1687111763.60.0.0',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205?from=homepage',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '81d92a5f1b39439c94fd7d61ca9545a6-a1f536fa80cc798f-1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-set-application-id': '28c161c7-01b9-443f-90c1-9188a1919ee4',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    products_id = response.get('body').get('products')

    with open('products_id_phones.json', 'w') as file:
        json.dump(products_id, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('phones_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    products_names = response.get('body').get('products')


    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('phone_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price' : item_base_price,
            'item_discount_price' : item_discount_price,
            'item_bonus' : item_bonus,
            'id' : item_id
        }


    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name' : item_name, 'id' : item_id}


    for i in item_prices:
        for j in item_names:
            if j['id'] == i['id']:
                item_prices[j['id']].update(item_names[j['id']])

    with open('phones_data.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)



def main():
    get_data()

if __name__ == '__main__':
    main()
