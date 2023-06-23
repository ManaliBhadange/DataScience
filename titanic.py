import pandas as pd
df=pd.read_csv("C:/Users/admin/Downloads/tested.csv")
print(df)
df.head()
from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import GradientBoostingClassifier

# le=LabelEncoder()
# le.fit(df['Age'])
# df['Age']=le.transform(df['Age'])
#
# le=LabelEncoder()
# le.fit(df['Sex'])
# df['Sex']=le.transform(df['Sex'])
#
# le=LabelEncoder()
# le.fit(df['Cabin'])
# df['Cabin']=le.transform(df['Cabin'])

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

x=df.drop(['Survived','Name','Age','Sex','Ticket','Cabin','Embarked'],axis=1)
y=df['Survived']

print(x)
print(y)

x=pd.DataFrame(x)
print(x)

print(x.isnull().sum())








