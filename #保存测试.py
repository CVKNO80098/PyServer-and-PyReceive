#保存测试
import pickle

a = "sad"
config = {
    "test1": "1asd",
    "test2": "2asd",
    "test3": a,
}
with open("config.pkl", "wb") as f:
    pickle.dump(config, f)
    print("保存完毕")

with open("config.pkl", "rb") as f:
        print("发现config文件，自动使用文件补全信息")
        config = pickle.load(f)
        test1 = config.get('test3')
        print(test1)