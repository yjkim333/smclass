select sysdate from dual;
-- dual => 임시로 넣어두는 가상 테이블

select sysdate,sysdate-30,sysdate+30 from dual;


-- emlpoyees 테이블의 hire_date 컬럼
select hire_date,hire_date-1,hire_date+1 from employees;

-- 날짜 범위 검색 / 정렬 order by , asc : 순차정렬(생략가능), desc : 역순정렬
select emp_name,hire_date from employees where hire_date>='02-01-01' and hire_date<='04-12-31' order by hire_date desc;
select emp_name,hire_date from employees where hire_date between '02-01-01' and '04-12-31' order by hire_date;

-- LIKE
select emp_name from employees where emp_name like '___a%';
select emp_name from employees where emp_name like '%a_';

--------------------------------------------
-- 정렬
-- desc => null 값이 제일 위에 검색, asc => 제일 아래에 검색
select department_id from employees order by department_id desc;

-- 월급 역순 정렬
select emp_name,salary from employees order by salary desc;

-- students 에서 total 역순정렬
select no,name,total from students order by total desc;

-- hire_date 기준으로 순차정렬
select emp_name,hire_date from employees order by hire_date;

select name,kor,eng,math from students order by kor desc, eng desc;
-- 기준점은 kor 이고! kor 값이 동일할 경우 그 중에서 eng 기준으로 역순 정렬.

-- 한국어 순차정렬 : ㄱㄴㄷㄹ...ㅎ 역순정렬 : ㅎ,ㅍ,ㅌ,ㅋ...ㄱ
select name from students order by name desc;

-- 입사일이 빠른순으로 정렬하는데, 이름은 역순으로 정렬하시오.
select emp_name,hire_date from employees order by hire_date, emp_name desc;


---------------------------------------------
-- 숫자함수
--
-- abs : 절대값
SELECT -10 as val ,abs(-10) as abs from dual;

select kor,kor-eng,abs(kor-eng) abs from students order by abs desc;

--
-- floor : 소수점 이하 버림
select 3.141592, floor(3.141592) from dual;

--
-- trunc : 버림, 자릿수 지정 가능
-- 소수점 둘째자리까지 출력,소수점셋째자리부터 버려
select 34.5678, trunc(34.5678,2) from dual;
select 34.5678, trunc(34.5678,-1) from dual;

--
-- ceil : 올림
select 3.141592, ceil(3.141592) from dual;

--
-- round : 반올림, 자릿수 범위 지정 가능
-- 소수점 첫째자리 반올림
select 34.5678, round(34.5678) from dual;
-- 소수점 둘째자리 까지 출력, 셋째자리 반올림
select 34.5678, round(34.5678,2) from dual;
-- 소수점 한칸 앞(일의 자리) 반올림
select 34.5678, round(34.5678,-1) from dual;

--
-- mod : 나머지
select 31/2, mod(31,2) from dual;
select 30/3, mod(30,3) from dual;

-- 사원번호가 홀수 인 사원을 출력하시오
select employee_id,emp_name from employees where mod(employee_id,2) = 1 order by employee_id;

-- 최종 연봉 계산 = 월급*12+(월급*12)*커미션  => 소수점 둘째자리에서 반올림
select emp_name,salary,round((salary*12+(salary*12)*nvl(commission_pct,0))*1381.86795,1) ysalary from employees; 


-----------------------------------------------
-- 시퀀스 : 자동으로 중복되지 않는 순차적인 고유 번호 부여 primary key
select * from students;
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
-- varchar2 최대 = 4000
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa',1,sysdate
);

insert into board values(
2,'제목2입니다.','내용2입니다.','aaa',10,sysdate
);

insert into board values(
stu_seq.nextval,'제목2입니다.','내용2입니다.','aaa',10,sysdate
);

select * from board;
commit;


select * from board;

create sequence board_seq
start with 8  -- 시작번호
increment by 1   -- 증감숫자
minvalue 1    -- 최소값
maxvalue 9999 -- 최대값
nocycle       -- cycle -> 1-9999 이상이 되면, 다시 1부터
nocache       -- cache 메모리에 시쿼스값을 미리 할당
;

desc board;

insert into board values(
board_seq.nextval,'제목8','내용8','aaa',100,sysdate
);
commit;


--drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, -- 대용량 글자 타입
id varchar2(20),
bgroup number(4),  -- 답변달기 그룹필
bstep number(4),   -- 답변달기 경우 순서정의
bindent number(4), -- 답변달기 들여쓰기
bhit number(10),   -- 조회수
bdate date         -- 등록일
);

select board_seq.currval form dual;

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100 -> 101
-- 101,'홍길순',100,99,90,total,avg,rank,날짜

select * from students;
desc students;

create sequence students_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

insert into students values(
students_seq.nextval,'홍길순',99,99,90,99+99+90,(99+99+90)/3,0,sysdate
);
commit;
select no,name,kor,eng,math,total,round(avg,2) avg,rank,sdate from students;

select round(avg,2) from students;
select s.*,round(avg,2) from students s;


select dept_seq.nextval from dual;

-- s_seq
-- 시작 1 증분 1 최대값 99999

create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

select s_seq.nextval from dual;

-- 시퀀스 생성, nextval:다음 시퀀스번호 생성, currval : 현재 시퀀스번호 리턴
select emp_seq.nextval from dual;
select emp_seq.currval from dual;

-----------------------------------------------------
-- 형 변환 함수

-- 문자형, 숫자형, 날짜형
-- 문자형 - car, varchar2, nchar, nvarchar2, long, clob
-- 한글 문자 입력시 3byte 사용
-- char - 고정길이 문자형
-- varchar2 - 가변길이 문자형  ex) varchar2(6) -> 2글자
-- nvarchar2(5) - 한글 5자리까지 입력가능 - 2byte

-- 숫자형 - number

-- 날짜형 - date, timestamp
-- date - 세기 년 월 일 요일 시 분 초 까지 입력
-- timestamp - 밀리세컨드까지 입력


select '홍길동' from dual;

-- length - 문자 길이
select length('홍길동') from dual;

-- 이름(문자)길이로 역순 정렬
select length(name) n from students order by n desc;

-- lengthb - byte 크기
select lengthb('홍길동') from dual;

-- 합계 200점 이상, 번호가 10이상 50이하, 이름 두번째자리에 e가 들어가 있는 모든 학생 출력
select * from students;
select * from students where total >= 200 and no >= 10 and no <= 50 and name like '_e%';

select * from students where total >= 200;

-- select * from 테이블
-- 이중쿼리
select * from (select * from students where total >= 200) where name like '_e%' and no >= 30;

rollback;

select * from students;

select no,name,total,rank from students;

-- rank 만들기
-- 등수함수 - rank()
-- rank() over(기준점입력)
-- no 는 중복이 없음, 유일키, 기본키, primary key
select no,rank() over(order by total desc) ranks from students;
select ranks from (select no,rank() over(order by total desc) ranks from students);

select no,name,total,rank from students order by total desc;

select * from students;

-- update - 수정 
update students a set rank = 1 where a.no = 101;

update students a set rank = (select ranks from (select no,rank() over(order by total desc) ranks from students) b
where a.no = b.no);

select * from students order by rank;

rollback;

select no,rank() over(order by total desc) as ranks from students;

update students set rank = 1 where no = 101;
update students set rank = 2 where no = 96;
update students set rank = 3 where no = 64;
update students set rank = 4 where no = 49;
update students set rank = 5 where no = 14;

select * from students;

-- 사원번호가 높은 순으로 등수를 생성하시오.

select employee_id,emp_name, from employees order by employee_id desc;

select employee_id,rank() over(order by employee_id desc) as ranks from employees;

-- emp2 테이블 employees 복사 생성
create table emp2 as select * from employees;

-- rank()실행
select rank() over(order by employee_id desc) ranks from employees;

-- 테이블 컬럼 추가
alter table emp2 add rank number(4);

desc emp2;

select * from emp2;

-- rank() 등수를 rank에 입력
update emp2 e set rank = (select ranks from(select employee_id,rank() over(order by employee_id desc) ranks from employees) e2
where e.employee_id = e2.employee_id);

-- 출력
select employee_id,rank from emp2 order by rank;

select * from emp2;

-----------------------------------------------------
-- 컬럼 순서 변경
-- emp_name 뒤에 rank 컬럼을 이동배치
desc emp2;
-- 1. emp_name 뒤부터 rank 컬럼 앞까지 invisible
alter table emp2 modify email invisible;
alter table emp2 modify PHONE_NUMBER invisible;
alter table emp2 modify PHONE_NUMBER invisible;
alter table emp2 modify HIRE_DATE invisible;
alter table emp2 modify SALARY invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

select * from emp2;

-- 2. invisible한 컬럼 다시 visible
alter table emp2 modify email visible;
alter table emp2 modify PHONE_NUMBER visible;
alter table emp2 modify PHONE_NUMBER visible;
alter table emp2 modify HIRE_DATE visible;
alter table emp2 modify SALARY visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;

select * from emp2;

-- 원상복귀 (맨뒤로)
alter table emp2 modify rank invisible;
alter table emp2 modify rank visible;
-----------------------------------------------------

-- 컬럼 삭제
desc emp2;

alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column HIRE_DATE;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;

select * from emp2;

-----------------------------------------------------

select * from departments;
desc departments;

alter table emp2 add DEPARTMENT_NAME varchar2(80);

-- emp2에는 부서명(DEPARTMENT_NAME)이 없음 -> departments 테이블에 있음
select * from emp2;
select department_id, department_name from emp2;
select department_id, department_name from departments;

update emp2 set department_name = '배송부' where department_id = 50;

update emp2 e set department_name =(select d from(select department_id,department_name d from departments)e2 where e.department_id = e2.department_id);

select department_id,department_name from emp2;



-- 테이블 복사
create table stu as select * from students;

alter table stu drop column rank;
desc stu;

select * from stu;
-- total avg 컬럼 추가

alter table stu add total number(3);
alter table stu add avg number;
alter table stu add rank number(3);
alter table stu modify sdate invisible;
alter table stu modify sdate visible;

desc stu;
-- 합계 평균 계산 추가
update stu set total = kor+eng+math;
update stu set avg = (kor+eng+math)/3;

select rank() over(order by total desc) from stu;
update stu s set rank = (select ranks from(select no,rank() over(order by total desc) ranks from stu)r where s.no = r.no);
select * from stu order by rank;

commit;

-------------------------------------------------------

-- 날짜 함수

-- sysdate - 현재날짜
select sysdate from dual;
-- 현재날짜 +30일 뒤 날짜
select sysdate+30 from dual;
-- 현재날짜 1일 전 날짜
select sysdate-1 from dual;

create table datetable(
no number(4),
predate date,
today date,
nextdate date
);

-- 1개월, 6개월, 1년 회원권
insert into datetable values(
1,sysdate-30,sysdate,sysdate+180
);

select no,predate,today 가입일,nextdate 만료일 from datetable;

select * from member;
select id,name,mdate,sysdate,round(sysdate-mdate) from member;
select id,name,mdate,sysdate,round(sysdate-mdate) from member where sysdate >= mdate+180;

-- 현재 날짜와 입사일 기준으로 몇일 지났는지 출력하시오.
select emp_name,hire_date,sysdate,round(sysdate-hire_date) from employees;

-- 달 기준 반올림 - 15일 이상이면 월을 1올림, 15일 미만이면 내림(1일로)
select hire_date,round(hire_date,'month') from employees;

-- 달 기준 버림 - 모든 날짜를 1일로.
select hire_date,trunc(hire_date,'month') from employees;

-- months_between() - 두가지 날짜와 날짜 사이의 개월 수를 알려줌
select hire_date,sysdate,months_between(sysdate,hire_date) from employees;
select hire_date,sysdate,round(months_between(sysdate,hire_date)) 개월수,round(sysdate-hire_date) 일수 from employees;

-- add_months 달수 추가
select hire_date,add_months(hire_date,3) from employees;

-- next_day - 다가오는 요일의 날짜 알려줌
select sysdate 오늘,next_day(sysdate,'목요일') from dual;
select sysdate 오늘,next_day(sysdate,'월요일') from dual;

-- last_day - 달의 마지막 날짜를 알려줌
select sysdate,last_day(sysdate) from dual;

----------------------------------------------------------------------
-- 형 변환
-- to_char, to_date, to_number

select sysdate from dual;
select to_char(sysdate,'yyyy.mm.dd hh24:mi:ss') from dual;

select hire_date,to_char(hire_date,'yyyy.mm.dd') from employees;
select '24-07-07',to_char(to_date('24-07-07'),'yyyy.mm.dd') from dual;
-------------------------------------------------------------------------

select * from member where id='aaa' and pw = '1111';

update member set id = 'abc', pw = '1111', name = '김용준', email = 'kyjoon0105@gmail.com' where id = 'Trineman';
commit;
select * from member;

select * from member where id = 'eee';

desc member;

alter table member modify pw varchar2(8);













