import platform
import fire
import requests




class Config():
    def __init__(self):
        pass


    def pc_bench_cpu(self, *args):
        ### arg should be seperated
        url = "https://www.pcgamebenchmark.com/api/cpus?name="
        for x in args:
            new = x + "%20"
        new_url = url + new
        print(new_url)
        data = requests.get(url)
        data.content


        print(data.content)





if __name__ == "__main__":
    Config().pc_bench_cpu("intel")



