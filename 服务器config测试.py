import pickle

with open("config.pkl", "rb") as f:
        print("发现config文件，自动使用文件补全信息")
        config = pickle.load(f)
        test1 = config.get('PublicIP')
        print(test1)