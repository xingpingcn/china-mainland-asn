import asyncio
import requests
import threading
import re,os
from config import *


class main():
    def __init__(self) -> None:
        self.num = 0
        self.lock = threading.Lock()
        # 填写函数名，此函数能将asn和name写入self.asn_dict
        #input the name of the func which has ability of writing asn and name from website or db to self.asn_dict
        self.requset_url_func_list = [
            self.res_from_ipip_net]
        # asn_dict: {asn:name}
        self.asn_dict = dict() 
        self.queue_list = []

    # 线程模式运行   run in threading
    def res_from_ipip_net(self):
        url = 'https://whois.ipip.net/iso/CN'
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        re_pattern = re.compile(r'<tr>(.*?)</tr>', re.S)
        re_pattern_asn_name = re.compile(
            r'<td> ?<a.*?title="(.*?)AS([0-9]+)</a>\s?</td>', re.S)
        tr_list = re.findall(re_pattern, response.text)
        for tr in tr_list:
            try:
                res = re.search(re_pattern_asn_name, tr)
                asn = res.group(2)
                name = res.group(1)
                with self.lock:
                    self.asn_dict[asn] = name
            except:
                pass
    # 线程模式运行   run in threading

    def res_from_he_net(self):
        url = 'https://bgp.he.net/country/CN'
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        re_pattern = re.compile(r'<tr>(.*?)</tr>', re.S)
        re_pattern_asn_name = re.compile(
            r'<td> ?<a.*?title="(.*?)AS([0-9]+)</a>\s?</td>', re.S)
        tr_list = re.findall(re_pattern, response.text)
        for tr in tr_list:
            try:
                res = re.search(re_pattern_asn_name, tr)
                asn = res.group(2)
                name = res.group(1)
                with self.lock:
                    self.asn_dict[asn] = name
            except:
                pass

    async def worker(self, file_name, queue):

        with open(os.path.join('asn_txt',f'{file_name}'), 'w', encoding='utf8') as f:
            asn = await queue.get()
            f.write(f'{asn}')
            queue.task_done()
            while 1:
                asn = await queue.get()
                if output_newline:
                    f.write(f'\n{asn}')
                else:
                    f.write(f',{asn}')
                queue.task_done()

    async def run(self):
        await asyncio.gather(*(asyncio.to_thread(func) for func in self.requset_url_func_list))
        tasks = []
        try:
            os.makedirs('asn_txt')
        except Exception as e:
            print(e)
        names = self.__dict__  # add class variable dynamicly
        for isp in asn_list:
            if eval(isp):
                file_name = f'{isp}.txt'
                names['queue_'+isp] = asyncio.Queue()
                self.queue_list.append(names['queue_'+isp])
                names['pattern_'+isp] = re.compile(f'{eval(isp)}', re.I)
                tasks.append(asyncio.create_task(
                    self.worker(file_name, names['queue_'+isp])))

        for key in self.asn_dict.keys():
            for isp in asn_list:
                if re.search(names['pattern_'+isp], self.asn_dict[key]):
                    names['queue_'+isp].put_nowait(key)
                    break
        for queue in self.queue_list:
            await queue.join()
        for task in tasks:
            task.cancel()

        # Wait until all worker tasks are cancelled.
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main().run())
