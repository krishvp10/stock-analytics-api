create table stock_data (
    id serial primary key,
    symbol varchar(10) NOT NULL,
    date date NOT NULL,
    open float,
    high float,
    low float,
    close float NOT NULL,
    volume bigint NOT NULL,
    UNIQUE(symbol, date)
);