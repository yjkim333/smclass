
-- 검색
-- select * from 
--select * from employees;
--select * from customers;
--select * from products;


-- 테이블 생성 -> create table 테이블명 
-- no,name,kor,eng,math,total,avg,rank
create table students (
no number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);


-- 데이터 입력  
-- insert => commit 명령어를 주지 않으면 임시저장소에 저장됨. roll back시 날라감.
insert into students (no,name,kor,eng,math,total,avg,rank) values(
 1,'홍길동',100,100,99,299,(299/3),1
);

insert into students (no,name,kor,eng,math,total,avg,rank) values(
 2,'유관순',100,90,99,289,(289/3),1
);


-- 테이블 검색
select no,name,kor,eng,math,total,avg,rank from students;

commit;

rollback;

select * from students;

select * from employees;




create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

-- aaa 1111 홍길동 010-1111-1111
insert into member (id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111'
);

select * from member;

commit;

insert into member values(
'bbb','1111','유관순','010-2222-2222'
);

commit;

insert into member values(
'ccc','이순신'
);

-- 일부만 입력시에는 입력할 것들을 적어줘야함
insert into member (id,name) values(
'ccc','이순신'
);

commit;

select * from member;

select id,phone from member;

select name,phone from member;

select name,id from member;

select emp_name,salary from employees;

select * from employees;

select * from member;

-- 데이터 수정 -- id가 aaa인 것을 찾아서 name을 홍길자로 변경해라
update member set name='홍길자' where id='aaa';

-- 데이터 삭제
delete member where id = 'ccc';

-- 데이터 확정 => commit, rollback
-- commit - 확정 , rollback - 되돌리기 commit 한 후엔 rollback해도 안돌아감.
commit;

rollback;

select * from member;






-- 테이블 삭제
-- drop table students;
