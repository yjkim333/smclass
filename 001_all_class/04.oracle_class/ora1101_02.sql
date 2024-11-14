-- 입사일의 마지막 날짜를 출력 10/1 -> 10/31
select hire_date,last_day(hire_date) from employees;

-- 등록일
select sdate from students;

-- 1년 후 날짜
select sdate+365 from students;
select add_months(sdate,12) from students;

-- 현재일 기준 등록일이 6개월 이내의 회원 출력
select * from students where sdate >= add_months(sysdate,-6) order by sdate;

-- 월별로 가입인원 그룹핑
select * from member;
select substr(mdate,4,2) from member;
select substr(mdate,1,5) m,count(substr(mdate,1,5)) from member group by substr(mdate,1,5) order by m;

select last_day(mdate) md from member order by md;
select substr(last_day(mdate),1,5) md, count(*) from member group by last_day(mdate) order by md;

select department_id,count(department_id) from employees group by department_id;


create table emp3 as select * from employees;
create table emp4 as select * from employees where 1=2;
select * from emp3;
select * from emp4;

-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
insert into emp4 select * from employees;
-- 테이블 구조의 제약조건을 확인해야함. (null 값 때문)
insert into emp4(employee_id,emp_name,hire_date) select employee_id,emp_name,hire_date from employees;

--insert, update, delete => commit / rollback;
rollback;


--------------------------------------
-- 테이블
-- CREATE - 생성
-- ALTER - 변경
-- DROP - 삭제

-- ALTER -- 테이블 구조변경 - 컬럼 추가 - add column / 수정 - modify column / 삭제 - drop column
select * from emp4;
-- 테이블 컬럼 추가
alter table emp4 add(hire_date2 date);

-- 테이블 컬럼 변경 - 컬럼 안에 데이터가 있다면 제약조건 
-- -> 65 길이의 문자가 있을 경우 50으로 변경 불가 / 타입 변경 - 다른 타입의 경우 불가 -> null 일땐 가능, 바꿀수있는 타입일땐 가능.
alter table emp4 modify(email varchar2(70)); 
alter table emp4 modify email varchar2(50);
select emp_name from emp4;
alter table emp4 modify emp_name varchar2(20);

alter table emp4 modify(email number(6));

-- 다른 컬럼의 내용 복사해서 입력
-- employee_id 값을 email 컬럼에 복사
update emp4 set email = employee_id;
select * from emp4;

-- employee_id 값을 phone_number 컬럼에 복사
-- phone_number는 문자형 타입, employee_id는 숫자형타입
update emp4 set phone_number = employee_id;

commit;
-- 문자형 타입을 숫자형 타입에 복사
-- 문자형 타입 안에 있는 데이터가 숫자형이기때문에 가능 => 문자가 있다면 불가능
update emp4 set manager_id = phone_number;

update emp4 set phone_number = '198a' where employee_id = 198;
rollback;

alter table emp4 modify emp_name number(3);
desc emp4;

-- 컬럼 이름 변경
alter table emp4 rename column phone_number to p_number;

-- 컬럼 속성 변경
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4 drop column hire_date2;

-- 테이블 삭제
drop table emp3;

-- 테이블 이름 변경
rename emp4 to emp44;

--
desc emp44;


--===============================================================
-- 무결성 제약 조건 - 테이블에 부적절한 자료가 입력되는 것을 방지하기 위해서 테이블을 생성할때 각 컬럼에 대해 정의하는 여러가지 규칙
-- not null - null 값을 허용하지 않음
-- unique - 중복된 값을 허용하지 않음, 항상 유일한 값을 갖도록 한다.
-- primary key - not null 과 unique를 합친 형태
-- foreign key - 참조되는 테이블 컬럼의 값이 존재하면 허용.
-- check - 저장가능한 데이터 값의 범위나 조건 설정하여 설정한 값만 허용


-----
--primary key - 중복불가, null 값 불가
--unique - 중복불가, null 값 허용
--not null - 중복가능, null 값 허용
--default - 값이 입력되지 않았을 때 디폴트 값 지정


create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in ('Male','Female')),
email varchar2(20),
bdate date default sysdate
);
desc bmember;

insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate
);
insert into bmember(id,pw,name,nicname,gender,email) values(
'bbb','1111','유관순','관순쓰','Female','bbb@bbb.com'
);
-- check -> gender => Male, Female 이 2가지 형태 외에는 안됨 - male,female 안됨
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'ccc','1111','이순신','거북선',20,'Male','ccc@ccc.com',sysdate
);

-- not null -> 중복허용, null 은 허용하지 않음, 사이공백은 가능
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'ddd',' ','강감찬','감아차기',20,'Male','ddd@ddd.com','2024/01/01'
);

-- primary key -> 중복불가, null 불가
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'eee',' ','김구','김구찌',20,'Male','eee@eee.com','2024/02/21'
);

commit;

create table emp3(
empno number(3) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1,'홍길동','01','01'
);
insert into emp3 values(
2,'유관순','02','02'
);
insert into emp3 (ename,job,deptno) values(
'이','03','03'
);
-- unique - 중복불가, null 값 허용
insert into emp3 values(
2,'강','04','04'
);

select * from emp3;

select * from bmember;

---------
-- 테이블에 primary key 제약조건 추가 / 삭제
-- primary key 추가시 null, 중복 값이 있으면 안됨/
-- constraint -> 이름설정, constraint id_pk -> 
desc member;
-- 추가
ALTER TABLE member add CONSTRAINT id_pk primary key(id);

insert into member(id) values ('aaa');

-- 삭제
alter table member drop constraint id_pk;


---------------------------------------------------------------
-- foreign key

create table board (
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile VARCHAR2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목5','내용5','ddd',board_seq.currval,0,0,0,sysdate,''
);
commit;

delete board;
rollback;

select * from board; -- 개수 : 5 / bno,btitle,bcontent,nicname,email,bgroup,bstep,bhit,bfile
select * from bmember; -- 개수 : 5 / id,pw,name,nicname,age,gender,email,bdate

-- 관계형 db
-- bmember 의 id 는 primary key, board의 id 는 foreign key
select bno,btitle,bcontent,nicname,age,gender,pw,email,bgroup,bstep,bhit,bfile from board,bmember where board.id = bmember.id;

--
select employee_id,emp_name,email,salary,employees.department_id,department_name from employees;

select employee_id,emp_name,email,salary,employees.department_id,department_name from employees,departments where employees.department_id = departments.department_id;

-- foreign key 추가,변경
desc board;

-- 닉네임 -> id_fk, foreign key :id -> bmember 테이블의 primary key:id 등록
alter table board add constraint id_fk foreign key (id) references bmember(id);

--foreign key 삭제
--alter table board drop constraint id_fk;


select * from board;
select * from bmember; -- id - aaa,bbb,ccc,ddd,eee

-- abc가 글을 등록하면 등록이 안됨.
insert into board values(
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,''
);

-- 테이블 create할때, foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
bcontent clob,
id varchar2(30)
constraint fk_board2_id foreign key(id) references bmember(id)
);

-- foreign key 삭제
alter table board drop constraint id_fk;
select * from board;
select * from bmember;  -- aaa,bbb,ccc,ddd,eee

-- abc글을 등록하면, 등록이 안됨
insert into board values(
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,' '
);

delete board where bno = 13;

-- [foreign key 등록된 id 삭제방법 ]
-- bmember테이블 id, foreign key로 board,board2에 등록
-- foreign key : 외래키
-- 원본의 primary key에 데이터를 지우려면, 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨.
-- foreign key를 해제해야 삭제 가능
-- primary key : 기본키

delete bmember where id='aaa';
delete board where id='aaa';
select * from bmember;
select * from board;
alter table board drop constraint id_fk;

-- foreign key 로 등록이 되면, 프라이머리 키를 삭제 할때 foreign key에 데이터가 있으면 삭제가 안됨.
-- on delete cascade -> primary key가 삭제되면,foreign key로 등록된 모든 글을 삭제시킴
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;

rollback;


alter table board add constraint fk_board_id foreign key(id) references bmember(id) on delete cascade;

-- 1. on delete restricted
-- 기본값 - 입력하지 않을시, 자식데이터가 있을 경우, 부모데이터가 삭제가 되지 않음.
alter table board add constraint id_fk foreign key(id) references bmember(id);
select * from board;
--자식테이블 에 aaa로 만든 데이터를 삭제해야 id를 삭제할 수 있음.
delete bmember where id = 'bbb';
delete board where bno = 3;

-- 2. on delete cascade
-- 부모데이터 삭제시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;
-- 부모데이터를 삭제하면, 자식데이터의 모든 글이 삭제 됨
delete bmember where id = 'bbb';


-- 33 on delete set null
-- 부모데이터 삭제시, 자식 데이터에 해당되는 값이 null로 표시
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete set null;
-- 부모데이터를 삭제하면 자식데이터의 해당 컬럼만 null로 변경되고, 데이터는 그대로 존재.
delete bmember where id = 'bbb';

-- 외래키 삭제
alter table board drop constraint id_fk;

rollback;





-----------------------------------------------
-- check 구문
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in ('Male','Female'))
);

-- check가 지정되어있는 컬럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary에 있는 범위를 벗어나면 에러, Male,Female 이외 단어 입력시 에러
insert into emp01 values(
2,'유관순',2000,'Female'
);
insert into emp01 values(
3,'이순신',20000,'Male'
);


-- default -> insert 시 값이 입력되지 않으면, 디폴트값 문자, 숫자, 날짜가 들어감
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in ('Male','Female')),
edate date default sysdate
);

insert into emp02 (empno,salary,gender) values(
1,5000,'Male'
);

select * from emp02;

commit;



--drop table datetable;





create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check(gender in('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values(
'aaa','1111','홍길동','22','2000/05/05','Male','golf',sysdate
);

insert into mem values(
'bbb','1111','유관순','22','2000/06/25','Female','book',sysdate
);

insert into mem values(
'ccc','1111','이순신','23','2001/12/25','Male','war',sysdate
);

commit;

select * from mem;


select count(*) from mem;


----------------------------------------

--select * from mem2;
--commit;
--update mem2 set id='abc', pw='1111', name='김용준',email='kyjoon0105@gmail.com' where id ='Trineman';
--desc member;
--select * from member;
--delete member;
--commit;
--insert into member select * from mem2;

--============================================





select count(emp_name) person, department_id from employees where department_id = 50 group by department_id;
select a.department_id,department_name from employees a,departments b where a.department_id = b.department_id;

select count(*) no, a.department_id dept, department_name deptname from employees a,departments b where a.department_id = b.department_id and a.department_id = 50 group by a.department_id,department_name;

desc mem;

select * from students;

desc students;