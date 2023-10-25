# re pattern
chinanet = 'china ?telecom|chinanet'
cmcc = 'china ?mobile|cmnet|tietong|CHINA ?RAILWAY'
unicom = 'unicom|cnc'
cernet = 'cngi|cernet'
cstnet = 'cstnet'

asn_list = ['chinanet', 'cmcc', 'unicom', 'cernet', 'cstnet']

# if set to false, output comma between ASN instead
output_newline = True


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Ch-Ua-Platform': "Windows",
    'Cache-Control': 'no-cache',
}
