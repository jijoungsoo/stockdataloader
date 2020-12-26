#!/usr/bin/python
# -*- coding: utf-8 -*-
import gzip
import sys
import os
import psycopg2
import time

class Main():
    def __init__(self):
        print("실행할 메인 클래스")
        file_list = self.get_file_dir()
        print(file_list)
        self.start = time.time()


        #self.write_file_to_db(file_list[0])
        for f in file_list:
            self.write_file_to_db(f)

    def get_file_dir(self):
        print("gz파일가져오기")
        #print(os.getcwd())  #현재 폴더경로 가져오기
        #print(os.listdir(os.getcwd()))  #현재 폴더 파일리스트가져오기
        #print(os.listdir(os.getcwd()))
        tmp_dir = os.getcwd()
        self.stock_data_dir =tmp_dir+"\stock_data"
        #print(tmp_dir)

        os.chdir(self.stock_data_dir)  #작업디렉토리변경
        #print(os.getcwd())  # 현재 폴더경로 가져오기
        #print(os.listdir(os.getcwd()))
        return os.listdir(os.getcwd())

    def write_file_to_db(self,file_name):
        tmp = self.stock_data_dir+"\\"+file_name
        print("gz파일읽기 %s" % tmp)
        file_data = []
        try:
            with gzip.open(tmp, 'rb') as f:
                cnt=0;
                for line in f:
                    #첫번째라인은 건너 띄어야한다.
                    if cnt==0:
                        cnt+=1
                        continue
                    row_data=[]
                    tmp=line.decode('utf-8')  #라인별로 파일을 가져옴
                    arr_tmp=tmp.split(",");
                    Code= arr_tmp[0].strip()[1:-1]  #주식코드  #양옆에 " 이거 하나씩 제거
                    Name= arr_tmp[1].strip()[1:-1]  #주식명
                    #print("aaaa")             #종가 1997 코드 015545 종목명 핵심텔레텍(1우)  종가금액이 ""이다.
                    if arr_tmp[2].strip().replace('""',''):   #비어있지 않아야만 통과다!!
                        Close= float(arr_tmp[2])  #종가
                        Close= int(Close)
                    else:
                        Close= 0
                    Changes= int(arr_tmp[3])  #전일대비
                    ChagesRatio = float(arr_tmp[4])  # 전일비
                    Volume = int(arr_tmp[5])  # 거래량
                    Amount = int(arr_tmp[6])  # 거래대금
                    Open = int(arr_tmp[7])  # 시가
                    High = int(arr_tmp[8])  # 고가
                    Low = int(arr_tmp[9])  # 저가
                    Marcap = int(arr_tmp[10])  # 시가총액(백만원)
                    MarcapRatio = arr_tmp[11].strip().replace('"','')
                    if MarcapRatio:
                        MarcapRatio = float(MarcapRatio)  # 시가총액비중(%)
                    else:
                        MarcapRatio= 0
                    Stocks = int(arr_tmp[12])  # 상장주식수
                    ForeignShares = arr_tmp[13].strip().replace('"',"")   # 외국인 보유주식수
                    if ForeignShares:
                        ForeignShares = float(ForeignShares)  # 외국인 보유주식수
                        ForeignShares = int(ForeignShares)
                    else:
                        ForeignShares= 0
                    ForeignRatio = arr_tmp[14].strip().replace('"',"")   # 외국인 지분율(%)
                    if ForeignRatio:
                        ForeignRatio = float(ForeignRatio)  # 외국인 지분율(%)
                    else:
                        ForeignRatio = 0
                    Rank = float(arr_tmp[15])  # 시가총액 순위 (당일)
                    Rank = int(Rank)
                    Date = arr_tmp[16].strip()[1:-1].replace("-","")    # 날짜 (DatetimeIndex)
                    #print(Date)
                    row_data.append(Code)
                    row_data.append(Name)
                    row_data.append(Close)
                    row_data.append(Changes)
                    row_data.append(ChagesRatio)
                    row_data.append(Volume)
                    row_data.append(Amount)
                    row_data.append(Open)
                    row_data.append(High)
                    row_data.append(Low)
                    row_data.append(Marcap)
                    row_data.append(MarcapRatio)
                    row_data.append(Stocks)
                    row_data.append(ForeignShares)
                    row_data.append(ForeignRatio)
                    row_data.append(Rank)
                    row_data.append(Date)
                    cnt+=1
                    # if cnt==10:
                    #     break
                    file_data.append(row_data)
            print(len(file_data))
            total_cnt=len(file_data)
        except (Exception, psycopg2.DatabaseError) as error:
            print(cnt)
            print(len(file_data))
            print(file_data[len(file_data)-1])
            print(error)
            raise error

        conn_str ="host='localhost' dbname='stockweb' user='postgres' password='pwd'"
        conn = psycopg2.connect(conn_str)
        print(conn)
        cur = conn.cursor()
        print(cur)
        cnt=0;
        try:
            for d in file_data:
                cur.execute('CALL insert_tb_marcap_stock('
                            '%s'  #[0]stock_cd
                            ',%s' #[1]stock_nm
                            ',%s' #[2]cls_amt
                            ',%s' #[3]changes_amt
                            ',%s' #[4]p_changes_rt
                            ',%s' #[5]p_trade_qty
                            ',%s' #[6]p_trade_amt
                            ',%s' #[7]p_start_amt
                            ',%s' #[8]p_high_amt
                            ',%s' #[9]p_low_amt
                            ',%s' #[10]p_total_mrkt_amt
                            ',%s' #[11]p_total_mrkt_amt_rt
                            ',%s' #[12]p_stock_cnt
                            ',%s' #[13]p_frgn_cnt
                            ',%s' #[14]p_frgn_rt
                            ',%s' #[15]p_rnk
                            ',%s' #[16]stock_dt                        
                            ')'
                            '', (
                                    d[0],
                                    d[1],
                                    d[2], #p_cls_amt
                                    d[3], #p_changes_amt
                                    d[4], #p_changes_rt
                                    d[5], #p_trade_qty
                                    d[6], #p_trade_amt
                                    d[7], #p_start_amt
                                    d[8], #p_high_amt
                                    d[9], #p_low_amt
                                    d[10], #p_total_mrkt_amt
                                    d[11], #p_total_mrkt_amt_rt
                                    d[12], #p_stock_cnt
                                    d[13], #p_frgn_cnt
                                    d[14], #p_frgn_rt
                                    d[15], #p_rnk
                                    d[16]
                                )
                            )
                conn.commit()
                cnt+=1
                if (cnt % 10000) == 0:
                    print("[%s]진행율 %s / %s  진행되고 있습니다(진행시간: %s)." % (file_name,cnt, total_cnt,(time.time()-self.start)))
                elif total_cnt<=(cnt+100):
                    print("[%s]진행율 %s / %s  진행되고 있습니다(진행시간: %s)." % (file_name,cnt, total_cnt,(time.time()-self.start)))

        except (Exception, psycopg2.DatabaseError) as error:
            print(file_data[cnt-1])
            print(error)
            cur.close()
            conn.close()
            raise error
        finally:
            if conn is not None:
                conn.close()
        cur.close()
        conn.close()


if __name__== "__main__":
    Main()
    # pip install psycopg2  # postgresql 연결 library

