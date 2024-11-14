select * from member;

update member set id = 'abc', pw = '1111' where id = 'abc';
commit;
update member set pw = '1111' where id = 'Towell';

commit;


--------------------------------------------------------------------------
-- 날짜 함수

select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;

select hire_date,trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- 요금제 변경 시 다음 달 1일 부터 적용됨.
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;


-- 입사일 기준 다음달 1일 부터 혜택 적용.
select hire_date,to_char(add_months(trunc(hire_date,'month'),1),'yy-mm-dd.dy') from employees;

-- 입사일 기준 1년 후 날짜를 출력
select hire_date,add_months(hire_date,12),hire_date+365 from employees;

-- 달의 마지막 날짜 출력
select last_day(sysdate) from dual;

-- 입사달의 1년 후 날짜와 1년 후 달의 마지막 날짜
select hire_date,hire_date+365,add_months(last_day(hire_date),12) from employees;


-- 입력일 기준 1년후 달의 마지막 날짜가 8월 31일 9월 30일 또는 10월 31일인 학생들을 출력
select sdate from students;

select * from students where last_day(add_months(sdate,12)) in ('24/08/31','24/09/30','24/10/31','25/08/31','25/09/30','25/10/31');

-----------------------------------------------------------------------------
-- extract() => 년월일시분초 중 원하는 것을 추출해서 가져올 수 있다.
select sysdate from dual;
-- extract -> sysdate - 년 월 일 까지 가능
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

select systimestamp from dual;
-- extract -> systimestamp - 년 월 일 시 분 초 까지 가능
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

-- 입력일 기준 1년후 달의 마지막 날짜가 8월 31일 11월 30일 또는 12월 31일인 학생들을 출력
select * from students where extract(month from last_day(add_months(sdate,12))) in (8,11,12);

select * from students where extract(year from last_day(add_months(sdate,12)))=2025 and extract(month from last_day(add_months(sdate,12))) in (8,11,12);

------------------------------------------------------------------------------
-- substr(문자,시작위치,가져올개수) => 문자에서 시작 위치, 가져올 개수
select sysdate from dual;
select substr(sysdate,4,2) from dual;

select * from students where substr(sdate,4,2) = 8;
select sdate,last_day(sdate+365) sdate2 from students where substr(last_day(sdate+365),4,2) in (8,11,12) order by sdate2;

------------------------------------------------------------------------------
-- 날짜->문자 : to_char    -- 날짜포맷변경
-- 문자->날짜 : to_date    -- 날짜 사칙연산
-- 숫자->문자 : to_char    -- 천단위, 숫자앞 0표시, 통화표시 
-- 문자->숫자 : to_number  -- 천단위표시, 천단위 삭제해서 사칙연산

-- 날짜 형변환
-- date타입을 char타입으로 변경해서 포맷변경.
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy.mm.dd.dy') from dual;
select sysdate,to_char(sysdate, 'dl') from dual;
select sysdate,to_char(sysdate,'yyyy.mon.dd.dy') from dual;
select sysdate,to_char(sysdate,'yyyy/mm/mm hh24:mi:ss') from dual;
select sysdate,to_char(sysdate,'yyyy/mm/mm.dy am hh:mi:ss') from dual;

select hire_date,to_char(hire_date,'yyyy-mm-dd.dy am hh:mi:ss') from employees;

-- students테이블에 sdate 2024/01/01 변경
select to_char(sdate, 'yyyy/mm/dd') from students;


select kor from students where kor = 70;
select kor from students where to_char(kor) = 70;


-- 숫자타입 -> 문자타입 변경해서 포맷 변경
-- 숫자에 천단위 , 표시
select salary*1382.86*12 연봉 from employees;
select to_char(salary*1382.86*12,'999,999,999') 연봉 from employees; -- 9 => 빈자릿수를 공백으로 채움
select to_char(salary*1382.86*12,'$000,000,000') 연봉 from employees; -- 0 => 빈자릿수를 0으로 채움
-- L : 국가 통화기호 표시, $:$표시
select to_char(salary*1382.86*12,'L000,000,000') 연봉 from employees; -- 0 => 빈자릿수를 0으로 채움

select 1 from dual;
select to_char(1,'000') from dual;
select to_char(1,'999') from dual;



select to_char(123456,'0000000'),to_char(123456,'999,999,999') from dual;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

-- 문자형 타입에는 숫자형 타입 입력 가능 -> 타입은 문자형으로.
-- number,number,str에 number 타입 넣어도 입력,str
insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

insert into chartable values(
1,10000,10000,10000
);

-- 숫자형타입과 숫자형문자타입은 사칙연산 오라클에서만 가능
select kor+kor_char from chartable;
-- 천단위 표시가 들어간 숫자형문자타입은 사칙연산 불가능
select kor+kor_mark from chartable;

select * from chartable;

desc chartable;

desc chartable2;
-- 모든 타입 number
create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);
-- 숫자형 타입은 숫자 앞에 0이 있어도 입력되지 않음 => 문자형 타입에만 가능
-- 숫자형 타입은 천단위 자릿점 , 표시도 안됨. => 문자형 타입에만 가능
insert into chartable2 values(
6,06000000,006000000,0006000000
);

select * from chartable2;
commit;

-----------------------------------------------------------------------
select '20241031' from dual;
-- '20241031'의 2일 뒤 날짜 출력
-- 문자형 타입을 date타입으로 변경 => to_date
select to_date('20241031')+2 from dual;
select to_char(to_date('20241031')+2,'dl') from dual;

select to_char(to_date('20241031'),'yy-mm-dd') from dual;

-- 숫자형 타입을 date타입으로 변경 => to_date
select sysdate - to_date(20231101) from dual;

----------------------------------------------------------------------
-- 문자형타입 -> 숫자형타입으로
select '20,000' from dual;
-- 천단위 문자형 타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select kor,kor_mark from chartable;
select kor,to_number(kor_mark,'999,999,999') from chartable;

-- 숫자형 타입이기에 사칙 연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;

delete chartable;
insert into chartable values(
3,30000,'0030000','3,000,000'
);
commit;

select * from chartable;

-------------------------------------------------------------------------


select department_id from employees;

select department_id from employees where department_id is null;
select commission_pct from employees where commission_pct is not null;

-- 월급*커미션을 계산하시오
select emp_name,salary+(salary*nvl(commission_pct,0)) from employees;

select department_id from employees;
-- null 인경우 ceo로 표시
select nvl(department_id,0) from employees;

-------**----***----****----*****----******----******----
select nvl(to_char(department_id),'ceo') from employees;


--=============================================================================

-- 그룹함수
-- sum-합계, avg-평균, count()-개수, count(*), min-최소값, max-최대값, median-중간값

-- 모든 직원 월급의 총 합계
select salary from employees;
select sum(salary) from employees;
select to_char(sum(salary),'$999,999') from employees;
-- 모든 직원 월급 평균
select avg(salary) from employees;
select round(avg(salary),2) from employees;
select trunc(avg(salary),4) from employees;
--직원 월급 최대값,최소값
select max(salary) from employees;
select min(salary) from employees;


-- 평균값 보다 월급이 높은 사원 출력
select avg(salary) from employees;

select emp_name,salary from employees where salary > (select avg(salary) from employees);
select count(emp_name) from employees where salary > (select avg(salary) from employees);

-- emp_name -> 단일함수 / avg(salary) -> 그룹함수
-- 그룹함수와 단일함수를 같이 쓸 수 없다.
-- select emp_name,avg(salary) from employees; --에러
-- select department_id,max(salary) from employees; --에러

-- students 테이블 모든 학생의kor점수합계,평균,최대,최소
select kor from students;
-- median
select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;


-- 부서번호가 50인 사원들의 월급 합계와 평균 최대 최소 출력
select sum(salary),avg(salary),min(salary),max(salary),median(salary) from employees where department_id = 50;
select sum(salary),avg(salary),min(salary),max(salary),median(salary) from employees where department_id = 30;

-- # group by -> 그룹함수과 단일함수를 같이 쓰는 법 => 단일 함수를 출력하고 싶을때 ,단일함수 입력
select department_id,max(salary) from employees group by department_id;

select emp_name,salary from employees;

select avg(salary) from employees;

select department_id,avg(salary) from employees group by department_id;

-- 평균 월급보다 높은 사람 수를 출력
select count(emp_name),min(salary),max(salary) from employees where salary > (select avg(salary) from employees);

-- 수학함수
-- abs - 절대값, ceil-올림, floor-버림, round-반올림, mod-나머지, trunc-절사, power-제곱, sqrt-제곱근
-- 제곱
select power(3,2) from dual;


----------------------

select '2',to_number('2') from dual;
select '240101',to_number('240101') from dual;

-- 날짜형 -> 문자형
select sysdate,to_char(sysdate) from dual;
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 년 월 일 특수문자 입력
select to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;
select to_char(sysdate, 'dl') from dual;

------------------------------------------------------------------------
--========================================================================

-- 문자형 함수

select email,emp_name from employees;


-- || , concat() 함수 : 문자 합치기
-- || -> 속도가 좀 더 빠름
--select emp_name+email from employees;
select emp_name || email from employees;
select concat(emp_name,email) from employees;

select name from member;

select * from member where name = 'Bryan';
--
-- lower -> 소문자 치환, upper -> 대문자 치환, initcap -> 첫글자 대문자 치환
select * from member where lower(name) = 'bryan';
select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

--
-- lpad('문자',자릿수,'채우는 문자') => 왼쪽 자리채움
select 'john',lpad('jhon',10,'#') from dual;
-- rpad('문자',자릿수,'채우는 문자') => 오른쪽 자리채움
select 'john',rpad('jhon',10,'#') from dual;

--
-- trim - 앞뒤공백 없애기, ltrim,rtrim
select '    aaa  ' from dual;
select '    aaa  ',trim('    aaa  ') from dual;
select length('    aaa  '),length(trim('    aaa  ')) from dual;

--
-- replace - 치환
select '  a a a  ',trim('  a a a  '),replace('  a a a  ',' ','') from dual;

--
-- substr - 특정위치 자르기 substr(대상,시작위치,자르는개수)
select 'abcdefg',substr('abcdefg',1,3) from dual;
select 'abcdefg',substr('abcdefg',3,3) from dual;

-- 입사일이 3,8,10월 인 사원을 출력하시오.
select * from employees;
select * from employees where substr(hire_date,4,2) in ('03','8','10');

-- 입사일이 7월 이상인 사원을 출력하시오.

select * from employees where substr(hire_date,4,2) > '07';


-- translate -치환
select 'axyazx',translate('axyazx','xyz','abc') from dual;
--translate('axyzx','xy','ab') 에서 'xyj','ab' => x는 a로 치환, y는 b로 치환, j(대응되는 것이 없는것)는 삭제, xy가 연달아 있는거를 바꾸라는 의미가 아님.


-- length() - 문자의 길이
-- students 테이블에서 name 글자 길이가 5자 이상인 학생 출력
select name,length(name) from students where length(name) >=5;


-- 사원 월급 합 평균 구하시오
select sum(salary), avg(salary) from employees;

-- 영어점수 합 평균 최대값 최소값
select sum(eng),avg(eng),max(eng),min(eng) from students;

-- students 에서 등록일 홍길동 2023년 12월 02일 

select name || to_char(sdate, '", 등록일 : "yyyy"년 "mm"월 "dd"일"') from students;







