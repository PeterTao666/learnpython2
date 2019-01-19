# 持续化案例三
import pickle
a = [19, 'Peter', "I miss jingjing!", [178, 65]]
with open(r'test04.txt','wb') as f:
    pickle.dump(a, f)

with open(r'test04.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)