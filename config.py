# re pattern
chinanet = 'china ?telecom|chinanet| ct'
cmcc = '(?:(?:china|henan|ZheJiang|YunNan|ShangHai|TianJin|BeiJing|ChongQing|AnHui|FuJian|GuangDong|GuangXi|GuiZhou|GanSu|HaiNan|HeBei|HeiLongJiang|HuBei|HuNan|JiLin|JiangSu|JiangXi|LiaoNing|NeiMengGu|NingXia|QingHai|ShanXi|ShanXi|ShanDong|SiChuan|XinJiang|YunNan|XiZang) ?mobile)|cmnet|tietong|CHINA ?RAILWAY'
unicom = 'unicom|cnc'
cernet = 'cngi|cernet|China ?Education'
cstnet = 'cstne|CNIC-CAS'


asn_list = ['chinanet', 'cmcc', 'unicom', 'cernet', 'cstnet']

# if set to false, output comma between ASN instead
output_newline = False


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
