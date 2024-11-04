select * from mem;

create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);
-- db에서 null 값은 최대한 지양한다.
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,'이순신','clerk',2
);

select * from emp02;

--drop table emp02;


-- unique - 중복 불가
create table emp02(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);


insert into emp02 values(
1,'홍길동','clerk',2
);

insert into emp02 values(
2,'유관순',null,null
);

insert into emp02 values(
3,'이순신',null,null
);

insert into emp02 values(
null,'강감찬',null,null
);
unique - 중복 에러
insert into emp02 values(
2,'김구',null,null
);

select * from emp02;

--drop table emp02;
delete emp02 where empno is null;
--commit;

-- 제약 조건 변경 alter - modify
alter table emp02 modify empno number(4) not null;
alter table emp02 modify empno;

desc emp02;


-- primary key - 중복불가, not null


--not null -> primary key - pk_emp02_empno(별칭)
alter table emp02 add constraint pk_emp_empno primary key(empno);
alter table emp02 drop constraint pk_emp02_empno;


create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);


-- foreign key
-- 부모테이블(primary key) <-> 자식테이블(foreign key)


--drop table mem;

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check(gender in('Male','Female'))
);

insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female'
);
--commit;
select * from mem;


create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);

select * from board2;
insert into board2 values(
1,'제목1','aaa'
);
insert into board2 values(
2,'제목2','bbb'
);
insert into board2 values(
3,'제목3','aaa'
);

-- 외래키(foreign key)로 등록시 부모키에 해당 값이 없을 시 에러가 남.
insert into board2 values(
4,'제목4','bbb'
);

-- 자식이 있는 경우 부모키 삭제가 안됨.
delete mem where id = 'aaa';

-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;

-- 부모키 삭제시 외래키로 등록된 값들을 모두 삭제.
alter table board2
add constraint fk_board2_id foreign key(id)
references mem(id) on delete cascade;
-- -> 부모 테이블의 aaa 삭제시 자식테이블의 aaa글이 모두 삭제.
delete mem where id = 'aaa';
-- -> mem의 aaa를 삭제 => board의 aaa도 삭제
select * from board2;

-- dafault => on delete restricted - 부모키 삭제시, 외래키에 등록된 값이 있으면 삭제가 안됨. -> 외래키 값 삭제후 삭제가능.
-- on delete set null : 부모키 삭제시, 외래키로 등록된 값을 삭제는 하지않도 , 해당되는 컬럼값(id값) null로!

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
-- 논리의 사용
-- DECODE

--drop table mem;
--drop table board2;

create table mem(
id varchar2(30) primary key,
pw varchar2(100) not null,
name varchar2(100),
deptno number(4)
);

insert into mem values(
'aaa','1111','홍길동',10
);
insert into mem values(
'ccc','1111','이순신',30
);
--commit;
select * from mem;

-- 10 '총무부', 20 '인사부', 30 '마케팅'
select id,pw,name,deptno,
decode (deptno,
10,'총무부',
20,'인사부',
30,'마케팅'
)
from mem;

select * from employees;

select job_id from employees;
--clerk -> 월급의 5% 인상, rep -> 10% , man -> 15%

-- 1. clerk rep man 인 직원 출력
select substr(job_id,1,3) from employees;
select * from employees where substr(job_id,4) in ('CLERK','REP','MAN');
select substr(job_id,4) j_id from employees where substr(job_id,4) in ('CLERK','REP','MAN');

select substr(job_id,4) j_id,salary,
decode(substr(job_id,4),
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15
)as sal
from employees
where substr(job_id,4) in ('CLERK','REP','MAN');




create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);
insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);

commit;

select * from lavel_data;

-- 1-100 2-1000 3-5000 4 -10000 5 -20000

select id,lavel,decode(lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000
)||' point' as point
from lavel_data;

---------------------------------------------------------
---------------------------------------------------------
-- CASE -> 비교연산자로 조건제시 가능
-- decode(일치하는 경우(=)만 사용 가능)와 같은 기능, 비교연산자를 사용할 수 있다는 차이점.
select id,pw,name,deptno,case
when deptno = 10 then '총무부' 
when deptno = 20 then '인사부'
when deptno = 30 then '마케팅'
end as deptName
from mem;


-- 1,2,3-5000 4,5-20000 포인트
select id,lavel,decode(lavel,
1,5000,
2,5000,
3,5000,
4,20000,
5,20000
)||' point' as point
from lavel_data;

select id,lavel,case
when lavel >= 1 and lavel <= 3 then 5000
when lavel >=4 and lavel <=5 then 20000
end ||' point' point
from lavel_data;


select * from students;
-- avg :90이상 A,80점이상 B,70C,60D,나머지F => result
select no,name,avg,case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end result
from students order by result;


create table stu as select * from students;
select * from stu;
-- 컬럼 추가
alter table stu add result varchar2(2);


--result 컬럼에 추가
update stu set result = (case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end);

select case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end
from stu;

-- 파이썬에서 if문 구현해서 처리하는 것 보다 오라클에서 하는 것이 속도가 빠르다.
-- rank() over => 순위 구현하는 함수 - 중복 순위 개수만큼 다음 순위 값을 증가해서 표시 _ex 2등이 2명이면 다음순위는 3등이 아닌 4등으로 표시.
select no,name,total, rank() over(order by total desc) from stu;
-- dense_rank() over => 중복 순위가 존재해도 순차적으로 다음 순위 표시
select no,name,total, dense_rank() over(order by total desc) from stu;

select ranks from (select rank() over(order by total desc) ranks from stu b);

--*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*--
-- 순위를 rank 컬럼에 추가하시오
update stu a set rank = (select ranks from(select no,rank() over(order by total desc) as ranks from stu) b where b.no = a.no);


rollback;
select * from stu;


-- case
-- salary 5000이하는 월급 15% 인상, 5000-8000 10%, 8000이상 5% 인상
select emp_name,salary,case
when salary < 5000 then salary*1.15
when salary >=5000 and salary <=8000 then salary*1.1
when salary >8000 then salary*1.05
end update_salary
from employees;

-- emp_name 대문자D가 포함되어있으면 10%인상 대문자M이 포함되어있으면 5%인상 그 외 그대로

select emp_name,salary,case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
when emp_name not like '%D%' and emp_name not like '%M%' then salary*1
end update_salary
from employees;

select emp_name,salary,case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary*1
end update_salary
from employees;


select * from employees;
select department_id,commission_pct from employees where commission_pct is not null;

-- 커미션이 있는 사원수를 출력하시오.
select count(commission_pct) from employees;
select count(*) from employees where commission_pct is not null;

-- 부서별 사원수 출력
select department_id,count(*) from employees group by department_id order by department_id;

-- 부서별 평균 월급 출력
select department_id,avg(salary) from employees group by department_id order by department_id;

-----------------------------------------------------------------------
-- 그룹함수에 조건을 사용하려면 - having
-- 부서별로 평균 월급이 7000 보다 높은 사원의 인원수
select department_id,avg(salary),count(salary) from employees group by department_id
having avg(salary) >= 7000;

-- 부서별로 전체 평균 월급 보다 적게 받는 사원수 출력
select department_id,avg(salary) from employees group by department_id;
select avg(salary) from employees;
select department_id,count(salary) from employees where salary<(select avg(salary) from employees) group by department_id;


-- 부서별 평균 월급이 6000이하인 부서별 인원수를 출력
select department_id,avg(salary),count(*) from employees group by department_id having avg(salary)>6000;


-- 부서별 평균월급 보다 적게 받는 사원 출력
select department_id,emp_name,salary from employees a
where salary <
(select salarys from(
select department_id,avg(salary) salarys from employees group by department_id
) b
where a.department_id = b.department_id
);

select department_id,avg(salary) salarys from employees group by department_id;


--*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/--
-- 부서별 평균월급 보다 적게 받는 사원수
select department_id,count(salary) from employees e 
where salary < (select avg(salary) from employees where e.department_id = department_id )
group by department_id;

select department_id,count(*) from employees a
where salary < (select salarys from(select department_id,avg(salary) salarys from employees group by department_id) b
where a.department_id = b.department_id)
group by department_id order by department_id;


-- 부서의 최대값 최소값 출력하되, 최대급여가 5000이상인 부서만 출력하시오.
select department_id,max(salary),min(salary) from employees group by department_id having max(salary)>=5000;






-----------------------------------------------------------------------------------
--===============================================================================--
-- JOIN

-- 학번,이름,전화번호,주소,성별,학년,학기,국어,영어,수학,합계,평균,등수
--1001,홍길동,010,서울,남자,1,1,100,100,100,300,1
--1001,홍길동,010,서울,남자,1,2,90,90,90,270,8
--1001,홍길동,010,서울,남자,1,3,95,95,95,285,15
--1001,홍길동,010,서울,남자,1,4,100,100,99,299,2
--1001,홍길동,010,서울,남자,2,1,100,100,100,300,1
--1001,홍길동,010,서울,남자,2,2,90,90,90,270,8
--1001,홍길동,010,서울,남자,2,3,95,95,95,285,15
--1001,홍길동,010,서울,남자,2,4,100,100,99,299,2
--1001,홍길동,010,서울,남자,3,1,100,100,100,300,1
--1001,홍길동,010,서울,남자,3,2,90,90,90,270,8
--1001,홍길동,010,서울,남자,3,3,95,95,95,285,15
--1001,홍길동,010,서울,남자,3,4,100,100,99,299,2



-- 부서명 departments
select * from departments;

select * from employees;

-- Donald OConnell 의 부서명을 알고싶어요.

select emp_name,department_id from employees where emp_name = 'Donald OConnell';

select department_id,department_name from departments where department_id = 50;

-- => JOIN을 사용해야 두개의 쿼리를 1개의 쿼리로 구성이 가능해짐.
-- join
-- 1. cross join - 특별한 키워드 없이 두개의 테이블을 검색하는 것
select * from employees;  -- 107개
select * from departments;  -- 27개
select count(*) from employees,departments;  -- 2889개  <- 107*27
select * from employees,departments;
--------------------------------------------------------------------------------------
-- 1-1. inner join
-- 1-1-1. equi join - 조인하려는 테이블에서 공통으로 존재하는 컬럼의 값으로 연결
select * from employees,departments; -- join
select * from employees,departments where employees.department_id = departments.department_id;
select emp_name,department_name from employees a,departments b where a.department_id = b.department_id;
select emp_name,department_name,a.department_id from employees a,departments b where a.department_id = b.department_id;


select * from member;
select * from board;
select id from member;
select bno,btitle,bcontent,id from board;

select bno,btitle,bcontent,b.id,email,phone,bgroup,bstep,bindent,bhit,bdate from member a,board b where a.id = b.id;


select * from jobs;

-- inner join - 사원번호,사원명,job_id,job_title
select employee_id,emp_name,a.job_id,job_title from employees a,jobs b where a.job_id = b.job_id and a.job_id = 'SH_CLERK';

-- 사원번호,사원명,부서번호,부서명,job_id,job_title출력
select employee_id,emp_name,a.department_id,department_name,a.job_id,job_title from employees a, departments b, jobs c 
where a.department_id = b.department_id and a.job_id = c.job_id;

-- member name / board 게시글
select * from member;
select * from board;
select bno,btitle,bcontent,name,bgroup,bstep,bindent,bhit,bdate,bfile from member a, board b where a.id = b.id;

-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 월급이 평균 월급보다 적은 사원 출력하시오.
select employee_id,emp_name,salary,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id and salary < (select avg(salary) from employees);

-- 월급이 부서별 평균 월급보다 적은 사원 출력하시오.
select employee_id,emp_name,salary,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id and salary < 
(select sal from (select department_id,avg(salary) sal from employees group by department_id) c where a.department_id = c.department_id);


--
select * from employees;
select * from jobs;
select * from departments;
-- job_id - CLERK 인 사원의 사원명, 사원번호, 부서명, 부서번호, job_id, job_title 출력
select employee_id,emp_name,a.department_id,department_name,a.job_id,job_title from employees a, departments b, jobs c 
where a.department_id = b.department_id and a.job_id = c.job_id and substr(a.job_id,4) in ('CLERK','MAN');

------------------------------------------------------------------------------------------------
-- 1-1-2. non-equi join - = 연산자 이외의 조건으로

select salary from employees order by salary; -- 2100-24000

-- 2000-4000-E등급,4000-6000-D,6000-8000-C,8000-10000-B,10000-100000-A
create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);
commit;

select * from salgrade;
select salary from employees;
-- salary , 등급 넣으려고함.
-- 등급은 salgrade에 있는데 salgrade 와 employees에는 공통 컬럼이 없음
-- => non-equi join을 사용해서 테이블 join을 하려고함.
-- => non-equi join - 테이블 간 같은 컬럼이 없으면서, 테이블의 값을 비교해서 출력
select emp_name, salary, grade from employees, salgrade
where salary between losal and hisal
;


-- students - avg ABCDF 등급을 출력하시오.
-- 100-90 A,89-80 B,79-70 C, 69-60 D, 60 미만 F
create table stu_grade(
grade varchar2(10),
loavg number(6),
hiavg number(6)
);

insert into stu_grade values(
'A등급',90.00,100.00
);
insert into stu_grade values(
'B등급',80.00,89.99
);
insert into stu_grade values(
'C등급',70.00,79.99
);
insert into stu_grade values(
'D등급',60.00,69.99
);
insert into stu_grade values(
'F등급',0.00,59.99
);
commit;


select * from stu_grade;

select name,total,avg,grade from students,stu_grade where avg between loavg and hiavg;


--
select * from stu;
-- result에 결과값을 non-equi join으로 입력하시오.
commit;

update stu set result = (
select grade from stu_grade where avg between loavg and hiavg
);

update stu set result = (
select results from(select no, grade as results from stu_grade where avg between loavg and hiavg) b
where a.no=b.no);


select * from stu order by result;


--alter table stu modify result varchar2(10);
--alter table stu_grade modify hiavg number(6,2);
--
--delete stu_grade;
--rollback;





-- 1-2. outer join

-----------------------------------------------------------------------------
-- 1-3. self join - 하나의 테이블 내에서 자기자신과 조인을 하는 경우
-- 자신의 테이블 2개를 join해서 결과값 출력
select employee_id,emp_name,manager_id from employees;
select employee_id,emp_name from employees where employee_id  = 124;

select a.employee_id,a.emp_name,a.manager_id,b.emp_name manager_name
from employees a, employees b
where a.manager_id = b.employee_id;
























