create or replace procedure CreateTableAndIndex(year in varchar2,outStr out varchar2)
authid current_user
as
begin
  execute immediate 'create table fct_lims_result'||year||' as select * from fct_lims_result2017 where 1=2';
  execute immediate 'create table fct_lims_sample'||year||' as select * from fct_lims_sample2017 where 1=2';
  execute immediate 'create table fct_lims_test'||year||' as select * from fct_lims_test2017 where 1=2';
  execute immediate 'create table fct_mes_result'||year||' as select * from fct_mes_result2017 where 1=2';
  outStr:='success';
EXCEPTION 
  WHEN OTHERS THEN 
     outStr:='fail';
end;
/
