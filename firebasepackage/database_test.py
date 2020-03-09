from firebasepackage.database import Database

db = Database()
name='Jack'
temp=37.5
state='fever'
db.insert(name,temp,state) #建立資料測試
update('575507',name,temp,'normal') #更新資料測試
db.searchAll() #搜尋全部資料測試
db.search('575507') #搜尋資料測試
db.delete('575507') #刪除資料測試