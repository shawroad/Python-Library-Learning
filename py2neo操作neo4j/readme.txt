1. 创造一个节点
   create (n:Person {name:"我", age=21})     
2. 创建关系
   create (p:Person {name:"我", age:"23"})-[:包工程{金额:10000}]->(n:Person {name:"好大哥", age:"35"})
3. 删除节点    注意 删除有连接的节点时  必须先删掉关系  
   create (n:Person {name:"XL", age:23})
   match (n:Person {name:"XL"}) delete n
4. 删除关系
  match  (p:Person {name:"我", age:"23"})-[f:包工程{金额:10000}]->(n:Person {name:"好大哥", age:"35"}) delete f
5. 加上标签
  match (t:Person) where id(t)=2 set t:好人 return t
  同个某个节点的id   找到它   然后给其设置一个好人的标签  
6. 额外增加属性
   match (a:好人) where id(a)=2 set a.战斗力=200 return a
   在好人标签中找一个节点的id为2  然后给其加一个战斗力属性  并设置其值为200
7. 查找
  create (:Person {name:"唐僧", age:"79"})-[:师傅 {s_time:"2020-11-23"}]->(:Person {name:"孙悟空", age:"1w"})
  match (a:Person)-[:师傅]->(b:Person) return a,b
  创建了唐僧和孙悟空是师傅关系 然后  找关系为师傅的两个节点。
8. 快速清空数据库
   match (n) detach delete n