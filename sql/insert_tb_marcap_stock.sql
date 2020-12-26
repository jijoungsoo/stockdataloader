-- PROCEDURE: public.insert_tb_marcap_stock(character varying, character varying, integer, integer, double precision, bigint, bigint, integer, integer, integer, bigint, double precision, bigint, bigint, double precision, integer, character varying)

-- DROP PROCEDURE public.insert_tb_marcap_stock(character varying, character varying, integer, integer, double precision, bigint, bigint, integer, integer, integer, bigint, double precision, bigint, bigint, double precision, integer, character varying);

CREATE OR REPLACE PROCEDURE public.insert_tb_marcap_stock(
	p_stock_cd character varying,
	p_stock_nm character varying,
	p_cls_amt integer,
	p_changes_amt integer,
	p_changes_rt double precision,
	p_trade_qty bigint,
	p_trade_amt bigint,
	p_start_amt integer,
	p_high_amt integer,
	p_low_amt integer,
	p_total_mrkt_amt bigint,
	p_total_mrkt_amt_rt double precision,
	p_stock_cnt bigint,
	p_frgn_cnt bigint,
	p_frgn_rt double precision,
	p_rnk integer,
	p_stock_dt character varying)
LANGUAGE 'plpgsql'

AS $BODY$
declare
begin
  ---tb_stock 입력
  insert into tb_marcap_stock
  		(
            stock_cd,
            stock_dt,
            stock_nm,
            cls_amt,
            changes_amt,
            changes_rt,
            trade_qty,
            trade_amt,
            start_amt,
            high_amt,
            low_amt,
            total_mrkt_amt,
            total_mrkt_amt_rt,
            stock_cnt,
            frgn_cnt,
            frgn_rt,
            rnk,
            crt_dtm,
            updt_dtm
        )
  values (
            p_stock_cd,
            p_stock_dt,
            p_stock_nm,
            p_cls_amt,
            p_changes_amt,
            p_changes_rt,
            p_trade_qty,
            p_trade_amt,
            p_start_amt,
            p_high_amt,
            p_low_amt,
            p_total_mrkt_amt,
            p_total_mrkt_amt_rt,
            p_stock_cnt,
            p_frgn_cnt,
            p_frgn_rt,
            p_rnk,
            now(),
            now()
		 )
  ON CONFLICT (stock_cd,stock_dt)
  DO
     UPDATE
     SET
            stock_cd=EXCLUDED.stock_cd,
            stock_dt=EXCLUDED.stock_dt,
            stock_nm=EXCLUDED.stock_nm,
            cls_amt=EXCLUDED.cls_amt,
            changes_amt=EXCLUDED.changes_amt,
            changes_rt=EXCLUDED.changes_rt,
            trade_qty=EXCLUDED.trade_qty,
            trade_amt=EXCLUDED.trade_amt,
            start_amt=EXCLUDED.start_amt,
            high_amt=EXCLUDED.high_amt,
            low_amt=EXCLUDED.low_amt,
            total_mrkt_amt=EXCLUDED.total_mrkt_amt,
            total_mrkt_amt_rt=EXCLUDED.total_mrkt_amt_rt,
            stock_cnt=EXCLUDED.stock_cnt,
            frgn_cnt=EXCLUDED.frgn_cnt,
            frgn_rt=EXCLUDED.frgn_rt,
            rnk=EXCLUDED.rnk,
		    updt_dtm = now();

end $BODY$;
