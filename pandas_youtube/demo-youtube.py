import pandas as pd 

df = pd.read_csv("youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)
# 2- İkinci 5 kaydı getiriniz.
result = df[5:15].head()
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
#df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis = 1)
result = df
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df[["likes","dislikes"]].mean()
# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["likes","dislikes"]].head(50)
# 7- En çok görüntülenen video hangisidir ?
result = df[df["views"] == df["views"].max()]
# 8- En düşük görüntülenen video hangisidir?
result = df[df["views"] == df["views"].min()]
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views",ascending = False).head(10)[["title","views"]]
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean()["likes"]
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count")["comment_count"]
# 12- Her kategoride kaç video vardır ?
result = df.groupby("category_id")["title"].count()
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"]=df["title"].apply(len)
result= df
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

def ayırma(x):
    return len(x.split("|"))
    

df["tag_count"] = df["tags"].apply(ayırma)
result = df
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

df["oran"] = df["likes"]/df["dislikes"]
result = df.sort_values("oran", ascending= True)[["title","likes","dislikes","oran"]].head(10)

print(result)
