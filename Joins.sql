--Sql Joins Interview Questions

null!=null

insert into t1 values(null);
insert into t2 values(null);

insert into t1 values(1);
insert into t2 values(2);
select * from t1;
select * from t2;
 
 select * from t1
 inner join t2 on t1.id1=t2.id2

 select * from t1
 left join t2 on t1.id1=t2.id2

 select * from t1
 right join t2 on t1.id1=tr.id2 

 select * from t1
 full outer join t1.id1=t2.id2