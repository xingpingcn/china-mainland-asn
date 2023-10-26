# re pattern
chinanet = 'china ?telecom|chinanet'
cmcc = 'china ?mobile|cmnet|tietong|CHINA ?RAILWAY'
unicom = 'unicom|cnc'
cernet = 'cngi|cernet|China ?Education'
cstnet = 'cstne|CNIC-CAS'


asn_list = ['chinanet', 'cmcc', 'unicom', 'cernet', 'cstnet']

# if set to false, output comma between ASN instead
output_newline = True


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
