--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;


-- create - 테이블 생성
-- alter - 테이블 수정
-- drop - 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert, select, update, delete
-- insert, update, delete => 임시저장소에 저장 => commit 이나 rollback

-- insert - 데이터 입력 
insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
-- 문자는 '' 홑따옴표!!
);

-- 입력데이터 확정
commit;

insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);

-- commit 지점까지 롤백
rollback;


-- select 데이터 검색
select * from member;


-- delete 데이터 삭제
-- delete member; -- 모든데이터 삭제
-- delete member where no = 2;


-- update 데이터 수정
--update member set name = '홍길자' where no = 1;
--update member set name = '홍길자'; -- 모든 데이터 수정

select * from member;

---------------------------------------------------------------------

-- create 테이블 생성
create table students(
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

-- sysdate - 현재날짜,시간
insert into students values(
1,'홍길동',100,100,100+100,sysdate
);

commit;

-- 모든 컬럼 검색
select * from students;

-- 특정 컬럼을 입력하면 특정 컬럼만 검색
select name,sdate from students;

-- 특정 컬럼만 입력하면 특정 컬럼만 입력
insert into students(stuno,name) values(
2,'유관순'
);

-----------------------------------------------

select * from employees;

-- 테이블 복사 -> 테이블 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;

select * from emp2;

-- count - 데이터 개수
select count(*) from emp2;

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
-- => 데이터 내용이 같을때만 복사하라는 건데 데이터가 다르니까 구조만 복사해옴

select * from emp3;


-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
select * from member;
select * from member2;

insert into member2 select * from member;
select * from member2;
commit;


-- 테이블 컬럼
-- 컬럼 데이터 타입의 길이를 변경
desc member;
-- alter - 변경 member 테이블 no 컬럼의 타입길이 변경
-- NO       NUMBER(4) - > number(10)
alter table member modify no number(10);


-- 다른 타입으로 변경 시에는 타입과 길이를 맞춰주던지 비워놓고(null) 해야함
update member set no = '';
commit;
alter table member modify no varchar2(10);
select * from member;


-- alter 변경 - 컬럼 이름 변경
alter table member rename column no to memberNo;


-- 대소문자 구분
-- 명령어는 대소문자 구분하지 않지만,
-- 데이터의 대소문자는 구분해야함.
SELECT * FROM MEMBER;
select * from member;
select memberno from member;
select MEMBERNO from member;
select memberNo from member;

select * from member;
select * from member where id = 'aaa';
SELECT * FROM MEMBER WHERE ID = 'AAA';



-- desc - 테이블 구조
desc employees;


-- employees 테이블에서 사원번호, 사원이름(emp_name), 입사일(hire_date) 출력
select employee_id,emp_name,hire_date from employees;


-- 연산자 :  산술 연산자  + - * /

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);

select * from member;

drop table students;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select * from students;

commit;

select kor,eng,kor+eng from students;
select kor,eng,kor+eng,abs(kor-eng) from students;

-- concat 명령어, ||
select concat(employee_id, emp_name) from employees;
select employee_id||emp_name from employees;


-- 달러 원화환산
select salary*1384 from employees;
-- 문자 변환 후 천단위 , 표시
select to_char(salary*1384,'999,999,999.00') from employees;

select emp_name,salary,salary*1384 from employees;


-------------------------------------------
-- Null
-- 0 도 아니고 빈공간도 아니다. 미확정(undefined),알수없는(unknown) 값을 의미(? 혹은 무한대의 의미)
-- 연산, 할당 비교가 불가능

CREATE TABLE stu(
no number(4),
name varchar2(20),
kor NUMBER(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;

-- null 검색 - is null
select * from stu where name = ''; -- null은 빈공백이 아니라 못 찾음
select * from stu where name = null; -- null 못 찾음
select * from stu where name is null; -- is null 해야 null 값을 찾을 수 있음

-- null 아닌 것 검색 - is not null
select commission_pct from employees where commission_pct is not null;


---------------------------------------------
select salary from employees;
-- 연봉계산
select salary,salary*12 from employees;
select salary,salary*12,salary*12*1384 from employees;

-- 커미션이 없는 사원은 null - null에 연산하면 null이 출력. => null 값을 대체해줘야 함 (nvl()함수사용)
select salary,salary*12,salary*12+(salary*12)*commission_pct*0.01 from employees;
-- 컬럼별 별칭 사용 - as 별칭
-- -> ""사용하면 특수문자, 사이공간 까지 쓰는 데로 사용가능
select salary,salary*12 as "연  봉" ,salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as real_yearsalary from employees;

-- nvl() 함수
-- nvl(kor,0) => kor컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;


select * from students;
-- 컬럼별 별칭 사용 (as 생략 가능)
select no as 번호, name as 이름, kor 국어, eng 영어, math 수학, total 총점, avg as 평균, rank  등수, sdate as 입력일 from students;

select * from employees;
-- 사원번호, 이름, 이메일을 합쳐서 출력하시오
select employee_id||emp_name||email from employees;
-- concat 은 2가지만 합칠 수 있음
select concat(concat(employee_id,emp_name),email) from employees;
-- 합지는 중간에 글 넣기
select emp_name||' is a '||job_id from employees;



-- distinct - 중복제거
select department_id from employees;
select distinct department_id from employees;



-- 정렬
-- 순차정렬 => order by 컬럼명 (asc(생략가능))
select distinct department_id from employees order by department_id;
-- 역순정렬 => order by 컬럼명 desc
select distinct department_id from employees order by department_id desc;


-- job_id 중복제거 출력
select job_id from employees;
select distinct job_id from employees;

-- substr(0,2) - 문자열 자르기 => 0,1 출력
select substr(job_id,4) from employees;
-- 문자열 잘라와서 중복제거
select distinct(substr(job_id,4)) from employees;

-- where 절 - 조건 비교 연산자
select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id > 100 and employee_id < 150;

-- students 합계 250점 이상 출력
select * from students;
select * from students where total >= 250;

-- 합계 250 이상이면서 kor 가 90점 이상인것 출력
select * from students where total >= 250 and kor >= 90;

-- 영어점수 70점 이상 90점 이하 출력
select * from students where eng >= 70 and eng <= 90;


-- 월급 5000이상 8000이하
select * from employees where salary >= 5000 and salary <= 8000;

-- 월급이 7000 아닌것
-- 아닌 것 => <>,!=,^=
select * from employees where salary<>7000;

-- 부서가 50 , 50 아닌것 개수
select count(*) from employees where department_id != 50;
select count(*) from employees where department_id = 50;
select count(*) from employees;
select count(*) from employees where department_id is null;
select * from employees where department_id is null;

-- null 은 count에 포함되지 않음
select count(employee_id) from employees;  -- 107개
select count(department_id) from employees; -- 106개 -> null 이 1개 있음.

-- 급여가 4000 이하 사원번호,사원명,급여컬럼 출력
select employee_id 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자 가능
select emp_name,hire_date from employees;

select emp_name,hire_date from employees where hire_date >= '2008/01/01';

-- 1999년 12월 31일 이전에 입사한 사람 출력
select emp_name,hire_date from employees where hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31 까지 입사한 사람 출력
select emp_name,hire_date from employees where hire_date >= '2001-01-01' and hire_date <= '20041231';

--------------------------------------------------------------
-- 논리연산자, between, in

-- 국어 90 이상 또는 영어 90 이상 출력
select * from students where kor >=90 or eng >=90;
select count(*) from students where kor >=90 or eng >=90;
select count(*) from students;
select count(*) from students where not kor >= 90;

-- 부서번호 80 이면서 job_id 가 MAN
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';

-- 0.2,0.3,0.5 만 출력
-- or 연산자
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- in 연산자
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);

-- 사원번호 employee_id = 110,120,130
select * from employees where employee_id in (110,120,130);
select * from employees where employee_id = 110 or employee_id = 120 or employee_id=130;

-- 사원번호 150-170 출력
-- and 연산자
select * from employees where employee_id >=150 and employee_id <= 170;
-- between and 연산자 => <= >= 등호가 포함되어있음.
select * from employees where employee_id between 150 and 170;
-- 날짜 in, between
select hire_date from employees where hire_date between '2001-02-17' and '2002-06-07';
select hire_date from employees where hire_date in('20040217','2002/06/07');

-----------------------------------------------------
-- LIKE => %(문자가 없거나, 하나 이상의 문자가 어떤 값이와도 상관없다), _(공간) 같이 사용

-- job- MAN 출력
select * from employees where substr(job_id,4) = 'MAN';

-- like 사용 => 들어가있는(포함되어있는) 글자 검색할 때 씀
-- like '%'  => '%MAN' -> MAN으로 끝나는 단어  'ST%' -> ST로 시작하는 단어 검색
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

-- emp_name 에서 a가 들어가있는 사람 출력
select emp_name from employees where emp_name not like '%a%';

-- 2번째 글자가 t인 사람 검색
select * from employees where emp_name like '_t%';

-- 4번째 글자가 e인 사람 검색
select * from employees where emp_name like '___e%';

-- 뒤에서 두번째에 l이 들어간 사람 검색
select * from employees where emp_name like '%l_';

-- 첫번째 D가 들어간 이름 검색
select * from employees where emp_name like 'D%';













