create table attendnum(
    entry_date DATE not null ,
    seq INT ,
    adult INT ,
    child INT ,
    primary key(entry_date,seq)
);
