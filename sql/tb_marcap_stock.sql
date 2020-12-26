-- Table: public.tb_marcap_stock

-- DROP TABLE public.tb_marcap_stock;

CREATE TABLE public.tb_marcap_stock
(
    stock_dt character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stock_cd character varying(255) COLLATE pg_catalog."default" NOT NULL,
    changes_amt integer,
    changes_rt double precision,
    cls_amt integer,
    crt_dtm timestamp without time zone NOT NULL,
    frgn_cnt bigint,
    frgn_rt double precision,
    high_amt integer,
    low_amt integer,
    rnk integer,
    start_amt integer,
    stock_cnt bigint,
    stock_nm character varying(45) COLLATE pg_catalog."default",
    total_mrkt_amt bigint,
    total_mrkt_amt_rt double precision,
    trade_amt bigint,
    trade_qty bigint,
    updt_dtm timestamp without time zone NOT NULL,
    CONSTRAINT tb_marcap_stock_pkey PRIMARY KEY (stock_dt, stock_cd)
)

TABLESPACE ts_stock_data;

ALTER TABLE public.tb_marcap_stock
    OWNER to postgres;
-- Index: unique_tb_marcap_stock_stock_cd_stockdt

-- DROP INDEX public.unique_tb_marcap_stock_stock_cd_stockdt;

CREATE INDEX unique_tb_marcap_stock_stock_cd_stockdt
    ON public.tb_marcap_stock USING btree
    (stock_dt COLLATE pg_catalog."default" ASC NULLS LAST, stock_cd COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE ts_stock_data;