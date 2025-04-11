# # Step 1 : import module
import pymysql as p

# # # Step 2 : connect to database
santhoshdb = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'santhosh')
print("connected successfully")
#
#
# # # # Step3  : create cursor
# mypage = santhoshdb.cursor()
#
#
# # # # # # # #### selelect query ....
# # # # Step 4 : Prepare the query
# q1 = [
#         'select * from login;',
#         # 'select count(*) from login;',
#         # 'select email,password from login where name = "sandy";',
#         # 'select * from login where name = "santhosh";',
#         # 'select * from login where id = 5;',
#         # 'select * from login where id = 15;',
#         # 'select email,password from login where name = "yugesh";'
#       ]
#
# for query in q1:
#
#     # Step 5 : execute the query
#     mypage.execute(query)
#
#     # Step 6 : fetch all result
#     res = mypage.fetchall()
#     print("\n", res, "\n")
#
#
#
# # Step7 : close DB
# santhoshdb.close()
#
# #
# # for x in res:
# #     # print(x[1] + "#" + x[3])
# #     print(list(x))












#### dml statements





# step 1
import pymysql as p

# Step 2 : connect to database
db = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'santhosh')

print("connected successfully")

# Step3  : create cursor
mypage = db.cursor()

##### insert query

# Step 4 : insert the data


q1 = [
   """
CREATE TABLE Faiz (
    name varchar(255),
    age varchar(255),
    salary varchar(255)
);
""",
'drop table netaji',
"INSERT INTO login (id, name, email, password) VALUES (34, 'shwetha','shwetha@gmail.com','shwetha@987');",
"INSERT INTO login (id, name, email, password) VALUES (35, 'akash','akash@gmail.com','akash@987');"
     ]


# q1 = ['CREATE DATABASE production;', 'CREATE DATABASE development;']


# Step 5 : execute the query
for x in q1:
    try:
        mypage.execute(x)
    except Exception as err:
        print("error msg was = ", err)

# Step 6 : commit
db.commit()

# Step 7 : Close DB
db.close()

print("successfully inserted ")























