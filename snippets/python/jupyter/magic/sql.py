# !pip3 install --user ipython-sql
%load_ext sql

%sql postgresql://postgres:postgres@localhost/postgres
%sql select 1;
