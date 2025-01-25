import pandas as pd

df=pd.read_csv("read_csv.csv")
print(df)

dict_sample= {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
dict_key = pd.DataFrame(dict_sample)
dict_key.to_csv("sample_dictionary.csv",mode='a',index=False)