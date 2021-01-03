-- Table: public.tb_st_marcap

-- DROP TABLE public.tb_st_marcap;

CREATE TABLE public.tb_st_marcap
(
    stock_dt character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stock_cd character varying(255) COLLATE pg_catalog."default" NOT NULL,
    changes_amt integer,
    changes_rt double precision,
    cls_amt integer,
    crt_dtm timestamp without time zone NOT NULL,
    frgn_cnt double precision,
    frgn_rt double precision,
    high_amt integer,
    low_amt integer,
    rnk integer,
    start_amt integer,
    stock_cnt double precision,
    stock_nm character varying(45) COLLATE pg_catalog."default",
    total_mrkt_amt bigint,
    total_mrkt_amt_rt double precision,
    trade_amt bigint,
    trade_qty bigint,
    updt_dtm timestamp without time zone NOT NULL,
    CONSTRAINT tb_marcap_stock_pkey PRIMARY KEY (stock_dt, stock_cd)
)

TABLESPACE pg_default;

ALTER TABLE public.tb_st_marcap
    OWNER to postgres;