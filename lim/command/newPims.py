# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-07-11'
'''
Created on 2017年3月22日

@author: Administrator
'''
from django.core.management.base import BaseCommand
import cx_Oracle
import pypyodbc
import thread
import threading
import time


class PimsCommand(BaseCommand):

    def handle(self, *args, **options):
        startTime = time.time()
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        msg = cur_oracle.var(cx_Oracle.STRING)  # plsql出参
        # 调用存储过程
        cur_oracle.callproc('pro_truncate', [msg])
        t1=threading.Thread(target=p.insertComponent,args=())
        t2=threading.Thread(target=p.insertCapacity,args=())
        t3=threading.Thread(target=p.insertFeedstock,args=())
        t4=threading.Thread(target=p.insertInventory,args=())
        t5=threading.Thread(target=p.insertProduct,args=())
        t6=threading.Thread(target=p.insertStrqua,args=())
        t7=threading.Thread(target=p.insertUnitStream,args=())
        t8=threading.Thread(target=p.inserUnitUtility,args=())
        t9=threading.Thread(target=p.insertUpurchase,args=())
        t10=threading.Thread(target=p.insertEconomic,args=())
        t11=threading.Thread(target=p.insertUsal,args=())
        t12=threading.Thread(target=p.insertCase,args=())
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        endTime=time.time()
        print("结束时间为%s") %endTime
        print("用时%s") %(endTime-startTime)
        

#         # 打印返回值
#         msg = 'y'
#         print(msg)  # <cx_Oracle.STRING with value 'y'>
# #         print(msg.getvalue())  # y
#         if(msg == 'y'):
#             
#             print(conn_mdb)
        

    #         # 往AA_PIMS_BLEND里面存取数据
    #         sql_blend_mdb = """SELECT  RW_Blends.SolutionID,RW_Blends.CaseID,RW_Blends.PeriodID,RW_Blends.BlendID, RW_Blends.BlendTag, RW_Blends.BlendDescription,PrBlendQuality.QualityID, PrQuality.ReportTag AS QualityTag, PrQuality.Description AS QualityDescription,CStr(PrBlendQuality.BlendValue)
    #         FROM ((RW_Blends INNER JOIN PrBlendQuality ON (RW_Blends.SolutionID=PrBlendQuality.SolutionID) AND (RW_Blends.CaseID=PrBlendQuality.CaseID) AND (RW_Blends.PeriodID=PrBlendQuality.PeriodID) AND (RW_Blends.NodeID=PrBlendQuality.NodeID) AND (RW_Blends.BlendID=PrBlendQuality.BlendID)) INNER JOIN PrQuality ON (PrBlendQuality.SolutionID=PrQuality.SolutionID) AND (PrBlendQuality.CaseID=PrQuality.CaseID) AND (PrBlendQuality.NodeID=PrQuality.ModelID) AND (PrBlendQuality.QualityID=PrQuality.QualityID)) INNER JOIN PrQualityOrigin ON PrBlendQuality.OriginID=PrQualityOrigin.OriginID
    #         where PrBlendQuality.BlendValue<>0 and (RW_Blends.caseid not in(""" + caseStr + """) or RW_Blends.SolutionID not in(""" + solutionStr + """))
    #         ORDER BY RW_Blends.SolutionID, RW_Blends.NodeTag, RW_Blends.CaseID, RW_Blends.PeriodID, RW_Blends.BlendReportOrder, PrQuality.ReportOrder"""
    #         cur_mdb.execute(sql_blend_mdb)
    #         rows = cur_mdb.fetchall()
    #
    #         for row in rows:
    #             mylist = []
    #             for i in range(0, len(row)):
    #                 if row[i] == None:
    #                     mylist.append(str(0))
    #                 else:
    #                     if type(row[i]) is int:
    #                         mylist.append(str(row[i]))
    #                     else:
    #                         mylist.append(row[i])
    #             print(mylist)
    #             sql_blend_oracle = "insert into AA_PIMS_BLEND(solutionid,caseid,periodid,blendid,blend_tag,blend_name,qualityid,quality_tag,quality_name,value) values(" + mylist[0] + "," + mylist[
    #                 1] + "," + mylist[2] + "," + mylist[3] + ",'" + mylist[4] + "','" + mylist[5] + "'," + mylist[6] + ",'" + mylist[7] + "','" + mylist[8] + "'," + str(mylist[9]) + ")"
    #             print(sql_blend_oracle)
    #             cur_oracle.execute(sql_blend_oracle)
    #             conn_oracle.commit()
    
    def insertComponent(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        p=PimsCommand()
        print("insertComponent开始时间：%s") %time.time()
            # AA_PIMS_BLEND_COMPONENT
        sql_component_mdb = """SELECT RW_BlendActivity.SolutionID, RW_BlendActivity.CaseID, RW_BlendActivity.PeriodID, RW_BlendActivity.BlendID, RW_BlendActivity.BlendTag, RW_BlendActivity.BlendDescription,PrBlendRecipe.StreamID AS ComponentID, PrStream.ReportTag AS ComponentTag, PrStream.Description AS ComponentDescription, CStr(PrBlendRecipe.WgtActivity), CStr(PrBlendRecipe.WgtActivity/RW_BlendActivity.WgtActivity) AS WgtPercent
        FROM RW_BlendActivity INNER JOIN (PrBlendRecipe INNER JOIN PrStream ON (PrBlendRecipe.SolutionID=PrStream.SolutionID) AND (PrBlendRecipe.CaseID=PrStream.CaseID) AND (PrBlendRecipe.NodeID=PrStream.NodeID) AND (PrBlendRecipe.StreamID=PrStream.StreamID)) ON (RW_BlendActivity.SolutionID=PrBlendRecipe.SolutionID) AND (RW_BlendActivity.NodeID=PrBlendRecipe.NodeID) AND (RW_BlendActivity.CaseID=PrBlendRecipe.CaseID) AND (RW_BlendActivity.PeriodID=PrBlendRecipe.PeriodID) AND (RW_BlendActivity.BlendID=PrBlendRecipe.BlendID)
        WHERE (((RW_BlendActivity.VolActivity)<>0)) 
        ORDER BY RW_BlendActivity.SolutionID, RW_BlendActivity.NodeTag, RW_BlendActivity.CaseID, RW_BlendActivity.PeriodID, RW_BlendActivity.BlendReportOrder, PrStream.ReportOrder"""

        cur_mdb.execute(sql_component_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    mylist.append(row[i])

        #     params = "'" + "','".join(mylist) + "'"
        #
        #     print(params)
        #     print(params.split(','))
            row_list.append(mylist)
        sql_component_oracle = "insert into f_pims_blend_component(solutionid,caseid,periodid,blendid,blend_tag,blend_name,componentid,Component_Tag,component_name,activity,percent) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)"
        cur_oracle.executemany(sql_component_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()

    def insertCapacity(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        p=PimsCommand()
        print("insertCapacity开始时间：%s") %time.time()
            # 往AA_PIMS_CAPACITY中存数据
        sql_capacity_mdb = """SELECT PrCapacityLimit.SolutionID, PrCapacityLimit.CaseID, PrCapacityLimit.PeriodID, PrCapacityLimit.CapacityID, PrCapacity.Tag AS CapacityTag, PrCapacity.Description AS CapacityDescription,CStr(PrCapacityLimit.Activity), CStr(PrCapacityLimit.MinValue), CStr(PrCapacityLimit.MaxValue)
        FROM (prperiod INNER JOIN PrCapacityLimit ON (prperiod.PeriodID=PrCapacityLimit.PeriodID) AND (prperiod.CaseID=PrCapacityLimit.CaseID) AND (prperiod.SolutionID=PrCapacityLimit.SolutionID)) INNER JOIN PrCapacity ON (PrCapacityLimit.CapacityID=PrCapacity.CapacityID) AND (PrCapacityLimit.ModelID=PrCapacity.ModelID) AND (PrCapacityLimit.CaseID=PrCapacity.CaseID) AND (PrCapacityLimit.SolutionID=PrCapacity.SolutionID)
        ORDER BY PrCapacityLimit.SolutionID,PrCapacityLimit.CaseID, PrCapacityLimit.PeriodID, PrCapacity.ReportOrder;"""

        cur_mdb.execute(sql_capacity_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_capacity_oracle = "insert into f_pims_capacity(SolutionID,CaseID,PeriodID,CapacityID,Capacity_Tag,Capacity_name,Activity,MinValue,MaxValue) values(:1,:2,:3,:4,:5,:6,:7,:8,:9)"
        cur_oracle.executemany(sql_capacity_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()

        
    def insertFeedstock(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        p=PimsCommand()
        # 往AA_PIMS_FEEDSTOCK_PURCHASE中添加数据
        sql_feedstock_mdb = """SELECT PrPurchase.SolutionID, PrPurchase.CaseID, PrPurchase.PeriodID, PrPurchase.StreamID, PrStream.ReportTag AS StreamTag, PrStream.Description AS StreamDescription,CStr(PrPurchase.activity),CStr(PrPurchase.cost),CStr(PrPurchase.minvalue),CStr(PrPurchase.maxvalue)
        FROM RW_CasePeriod INNER JOIN ((PrPurchase INNER JOIN PrVTW ON (PrPurchase.SolutionID=PrVTW.SolutionID) AND (PrPurchase.CaseID=PrVTW.CaseID) AND (PrPurchase.PeriodID=PrVTW.PeriodID) AND (PrPurchase.NodeID=PrVTW.NodeID) AND (PrPurchase.StreamID=PrVTW.StreamID)) INNER JOIN PrStream ON (PrVTW.SolutionID=PrStream.SolutionID) AND (PrVTW.CaseID=PrStream.CaseID) AND (PrVTW.NodeID=PrStream.NodeID) AND (PrVTW.StreamID=PrStream.StreamID)) ON (RW_CasePeriod.SolutionID=PrPurchase.SolutionID) AND (RW_CasePeriod.NodeID=PrPurchase.NodeID) AND (RW_CasePeriod.CaseID=PrPurchase.CaseID) AND (RW_CasePeriod.PeriodID=PrPurchase.PeriodID)
        where (PrPurchase.maxvalue<>0 or PrPurchase.maxvalue=0) """
        cur_mdb.execute(sql_feedstock_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_feedstock_oracle = "insert into f_PIMS_FEEDSTOCK_PURCHASE(SolutionID,CaseID,PeriodID,StreamID,Stream_Tag,Stream_name,Activity,Cost,Minvalue,MaxValue) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
        cur_oracle.executemany(sql_feedstock_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()


    def insertInventory(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        p=PimsCommand()
        # 往aa_pims_inventory存数据
        sql_inventory_mdb = """SELECT prInventory.SolutionID, PrInventory.CaseID, PrInventory.PeriodID, PrInventory.StreamID, PrStream.ReportTag AS StreamTag, PrStream.Description AS StreamDescription, CStr(PrInventory.Opening) AS WgtOpen, CStr(PrInventory.Closing) AS WgtClose, CStr((PrInventory.Closing-PrInventory.Opening)) AS WgtActivity, CStr(PrInventory.Target) AS WgtTarget, CStr(PrInventory.MinValue) AS WgtMin,CStr(PrInventory.MaxValue)
        FROM ((RW_CasePeriod INNER JOIN PrInventory ON (RW_CasePeriod.PeriodID=PrInventory.PeriodID) AND (RW_CasePeriod.CaseID=PrInventory.CaseID) AND (RW_CasePeriod.NodeID=PrInventory.NodeID) AND (RW_CasePeriod.SolutionID=PrInventory.SolutionID)) INNER JOIN RW_VTW ON (PrInventory.StreamID=RW_VTW.StreamID) AND (PrInventory.NodeID=RW_VTW.NodeID) AND (PrInventory.PeriodID=RW_VTW.PeriodID) AND (PrInventory.CaseID=RW_VTW.CaseID) AND (PrInventory.SolutionID=RW_VTW.SolutionID)) INNER JOIN PrStream ON (RW_VTW.StreamID=PrStream.StreamID) AND (RW_VTW.NodeID=PrStream.NodeID) AND (RW_VTW.CaseID=PrStream.CaseID) AND (RW_VTW.SolutionID=PrStream.SolutionID)
        WHERE PrInventory.VWBasisID = 0 and (PrInventory.MaxValue<>0 or PrInventory.MaxValue=0)"""
        cur_mdb.execute(sql_inventory_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_inventory_oracle = "insert into f_pims_inventory(SolutionID,CaseID,PeriodID,StreamID,Stream_Tag,Stream_name,OPEN_INVENTORY,CLOSE_INVENTORY,activity,TARGET_INVENTORY,minvalue,maxvalue) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"
        cur_oracle.executemany(sql_inventory_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
        
    def insertProduct(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        p=PimsCommand()
        # 往aa_pims_product_sale表里插数据
        sql_product_mdb = """SELECT PrSale.SolutionID, PrSale.CaseID, PrSale.PeriodID, PrSale.StreamID, PrStream.ReportTag AS StreamTag, PrStream.Description AS StreamDescription, CStr(PrSale.Activity) AS WgtActivity, CStr(PrSale.Price) AS WgtPrice, CStr(PrSale.MinValue) AS WgtMin, CStr(PrSale.MaxValue) AS WgtMax
        FROM PrMarket INNER JOIN (((RW_CasePeriod INNER JOIN PrSale ON (RW_CasePeriod.SolutionID=PrSale.SolutionID) AND (RW_CasePeriod.NodeID=PrSale.NodeID) AND (RW_CasePeriod.CaseID=PrSale.CaseID) AND (RW_CasePeriod.PeriodID=PrSale.PeriodID)) INNER JOIN PrVTW ON (PrSale.SolutionID=PrVTW.SolutionID) AND (PrSale.CaseID=PrVTW.CaseID) AND (PrSale.PeriodID=PrVTW.PeriodID) AND (PrSale.NodeID=PrVTW.NodeID) AND (PrSale.StreamID=PrVTW.StreamID)) INNER JOIN PrStream ON (PrVTW.SolutionID=PrStream.SolutionID) AND (PrVTW.CaseID=PrStream.CaseID) AND (PrVTW.NodeID=PrStream.NodeID) AND (PrVTW.StreamID=PrStream.StreamID)) ON (PrMarket.SolutionID=PrSale.SolutionID) AND (PrMarket.CaseID=PrSale.CaseID) AND (PrMarket.MarketID=PrSale.MarketID)
        where (PrSale.MaxValue=0 or PrSale.MaxValue<>0);"""
        cur_mdb.execute(sql_product_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_inventory_oracle = "insert into f_pims_product_sale(SolutionID,CaseID,PeriodID,StreamID,Stream_Tag,Stream_name,Activity,cost,minvalue,maxvalue) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
        cur_oracle.executemany(sql_inventory_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
        
    def insertStrqua(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        # 往AA_pims_stream_quality里添加数据
        sql_strqua_mdb = """SELECT prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrStream.StreamID, PrStream.ReportTag AS StreamTag, PrStream.Description AS StreamDescription, PrQuality.QualityID, PrQuality.ReportTag AS QualityTag, PrQuality.Description AS QualityDescription, CStr(PrStreamQuality.Value)
        FROM (((prperiod INNER JOIN PrStreamQuality ON (prperiod.SolutionID = PrStreamQuality.SolutionID) AND (prperiod.CaseID = PrStreamQuality.CaseID) AND (prperiod.PeriodID = PrStreamQuality.PeriodID)) INNER JOIN PrStream ON (PrStreamQuality.SolutionID = PrStream.SolutionID) AND (PrStreamQuality.CaseID = PrStream.CaseID) AND (PrStreamQuality.NodeID = PrStream.NodeID) AND (PrStreamQuality.StreamID = PrStream.StreamID)) INNER JOIN PrQuality ON (PrStreamQuality.SolutionID = PrQuality.SolutionID) AND (PrStreamQuality.CaseID = PrQuality.CaseID) AND (PrStreamQuality.NodeID = PrQuality.ModelID) AND (PrStreamQuality.QualityID = PrQuality.QualityID)) INNER JOIN PrQualityOrigin ON PrStreamQuality.OriginID = PrQualityOrigin.OriginID
        where  PrQuality.Description is not null
        ORDER BY prperiod.SolutionID,prperiod.CaseID, prperiod.PeriodID, PrStream.ReportOrder, PrQuality.ReportOrder;"""
        cur_mdb.execute(sql_strqua_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_strqua_oralce = "insert into f_pims_stream_quality(SolutionID,CaseID,PeriodID,StreamID,Stream_Tag,Stream_name,qualityid,Quality_Tag,Quality_name,value) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
        cur_oracle.executemany(sql_strqua_oralce, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
         
    def insertUnitStream(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        # 往unit_stream表里添加数据
        sql_unitStream_mdb = """SELECT RW_UnitMaterials.SolutionID,RW_UnitMaterials.CaseID,RW_UnitMaterials.PeriodID,RW_UnitMaterials.StreamID,RW_UnitMaterials.StreamTag,RW_UnitMaterials.Streamdescription,RW_UnitMaterials.unitid,RW_UnitMaterials.unittag,RW_UnitMaterials.unitdescription,CStr(RW_UnitMaterials.activity),RW_UnitMaterials.feedflag, RW_UnitOfMeasure.UOM, RW_ModelVWBasisIDs.VWBasisID
        FROM RW_UnitMaterials, RW_UnitOfMeasure, RW_ModelVWBasisIDs
        WHERE RW_UnitMaterials.StreamID=RW_UnitOfMeasure.StreamID AND RW_UnitMaterials.NodeID=RW_UnitOfMeasure.ModelID
        AND RW_UnitMaterials.CaseID=RW_UnitOfMeasure.CaseID AND RW_UnitMaterials.SolutionID=RW_UnitOfMeasure.SolutionID
        AND RW_ModelVWBasisIDs.SolutionID=RW_UnitMaterials.SolutionID AND RW_ModelVWBasisIDs.ModelID=RW_UnitMaterials.NodeID
        AND RW_ModelVWBasisIDs.CaseID=RW_UnitMaterials.CaseID AND RW_UnitOfMeasure.VWBasisID=RW_ModelVWBasisIDs.VWBasisID
        and RW_UnitMaterials.activity<>0;"""
        cur_mdb.execute(sql_unitStream_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_strqua_oralce = "insert into f_pims_unit_stream(SolutionID,CaseID,PeriodID,StreamID,Stream_Tag,Stream_name,unitid,unit_tag,unit_name,activity,feedflag,units,VWBasisID) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)"
        cur_oracle.executemany(sql_strqua_oralce, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()

    def inserUnitUtility(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        # 往unit_utility中添加数据
        sql_unitUtility_mdb = """SELECT prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUnit.UnitID, PrUnit.Tag AS UnitTag, PrUnit.Description AS UnitDescription, PrUtility.UtilityID, PrUtility.Tag AS UtilityTag, PrUtility.Description AS UtilityDescription, CStr(PrUnitOperationUtility.Activity), PrUnitOperationUtility.FeedFlag
        FROM ((prperiod INNER JOIN PrUnitOperationUtility ON (prperiod.SolutionID = PrUnitOperationUtility.SolutionID) AND (prperiod.CaseID = PrUnitOperationUtility.CaseID) AND (prperiod.PeriodID = PrUnitOperationUtility.PeriodID)) INNER JOIN PrUnit ON (PrUnitOperationUtility.SolutionID = PrUnit.SolutionID) AND (PrUnitOperationUtility.CaseID = PrUnit.CaseID) AND (PrUnitOperationUtility.ModelID = PrUnit.ModelID) AND (PrUnitOperationUtility.UnitID = PrUnit.UnitID)) INNER JOIN PrUtility ON (PrUnitOperationUtility.SolutionID = PrUtility.SolutionID) AND (PrUnitOperationUtility.CaseID = PrUtility.CaseID) AND (PrUnitOperationUtility.ModelID = PrUtility.ModelID) AND (PrUnitOperationUtility.UtilityID = PrUtility.UtilityID)
        where  PrUnitOperationUtility.Activity<>0
        ORDER BY prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUnit.ReportOrder, PrUtility.ReportOrder;"""
        cur_mdb.execute(sql_unitUtility_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_unitUtility_orcal = "insert into f_PIMS_UNIT_UTILITY(SolutionID,CaseID,PeriodID,unitid,unit_tag,unit_name,utilityid,utility_tag,utility_name,activity,feedflag) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)"
        cur_oracle.executemany(sql_unitUtility_orcal, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
    
    def insertUpurchase(self):
        # 往utility_purchase中添加数据
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        sql_upurchase_mdb = """SELECT prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUtility.UtilityID, PrUtility.Tag AS UtilityTag, PrUtility.Description AS UtilityDescription, PrUtilityPurchase.Activity, PrUtilityPurchase.Cost
        FROM (prperiod INNER JOIN PrUtilityPurchase ON (prperiod.PeriodID = PrUtilityPurchase.PeriodID) AND (prperiod.CaseID = PrUtilityPurchase.CaseID) AND (prperiod.SolutionID = PrUtilityPurchase.SolutionID)) INNER JOIN PrUtility ON (PrUtilityPurchase.UtilityID = PrUtility.UtilityID) AND (PrUtilityPurchase.NodeID = PrUtility.ModelID) AND (PrUtilityPurchase.CaseID = PrUtility.CaseID) AND (PrUtilityPurchase.SolutionID = PrUtility.SolutionID)
        where PrUtilityPurchase.Activity<>0                                   
        ORDER BY prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUtility.ReportOrder, PrUtility.UtilityID;"""
        cur_mdb.execute(sql_upurchase_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_upurchase_oracle = "insert into f_PIMS_UTILITY_purchase(SolutionID,CaseID,PeriodID,utilityid,utility_tag,utility_name,activity,cost) values(:1,:2,:3,:4,:5,:6,:7,:8)"
        cur_oracle.executemany(sql_upurchase_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
        
    def insertUsal(self):
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        # 往utility_sale中添加数据
        sql_usal_mdb = """SELECT prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUtility.UtilityID, PrUtility.Tag AS UtilityTag, PrUtility.Description AS UtilityDescription, PrUtilitySale.Activity, PrUtilitySale.Price
        FROM (prperiod INNER JOIN PrUtilitySale ON (prperiod.PeriodID = PrUtilitySale.PeriodID) AND (prperiod.CaseID = PrUtilitySale.CaseID) AND (prperiod.SolutionID = PrUtilitySale.SolutionID)) INNER JOIN PrUtility ON (PrUtilitySale.UtilityID = PrUtility.UtilityID) AND (PrUtilitySale.NodeID = PrUtility.ModelID) AND (PrUtilitySale.CaseID = PrUtility.CaseID) AND (PrUtilitySale.SolutionID = PrUtility.SolutionID)
        where  PrUtilitySale.Activity<>0
        ORDER BY prperiod.SolutionID, prperiod.CaseID, prperiod.PeriodID, PrUtility.ReportOrder, PrUtility.UtilityID;"""
        cur_mdb.execute(sql_usal_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_usal_oracle = "insert into f_PIMS_utility_sale values(:1,:2,:3,:4,:5,:6,:7,:8)"
        cur_oracle.executemany(sql_usal_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()
        
    def insertEconomic(self):

        # 往ECONOMIC_SUMMARY里面存储数据
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        sql_economic_mdb = """SELECT PrEconomicSummary.SolutionID,PrEconomicSummary.CaseID, PrEconomicSummary.PeriodID, PrEconomicSummaryType.Description,CStr(PrEconomicSummary.Activity)
FROM (prperiod INNER JOIN PrEconomicSummary ON (prperiod.SolutionID=PrEconomicSummary.SolutionID) AND (prperiod.CaseID=PrEconomicSummary.CaseID) AND (prperiod.PeriodID=PrEconomicSummary.PeriodID)) INNER JOIN PrEconomicSummaryType ON PrEconomicSummary.EconomicSummaryTypeID=PrEconomicSummaryType.EconomicSummaryTypeID
where PrEconomicSummary.Activity<>0 
ORDER BY PrEconomicSummary.SolutionID,PrEconomicSummary.CaseID, PrEconomicSummary.PeriodID, PrEconomicSummary.EconomicSummaryTypeID;"""
        cur_mdb.execute(sql_economic_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_economic_oracle = "insert into f_PIMS_ECONOMIC_SUMMARY values(:1,:2,:3,:4,:5)"
        cur_oracle.executemany(sql_economic_oracle, row_list)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertComponent结束时间：%s") %time.time()

    def insertCase(self):
        # 往case表里存数据
        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn_oracle = cx_Oracle.connect(oacle_str)
        cur_oracle = conn_oracle.cursor()
        mdb_str = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Results.Mdb'
        conn_mdb = pypyodbc.win_connect_mdb(mdb_str)
        cur_mdb = conn_mdb.cursor()
        sql_case_mdb = "select caseid,description,solutionid,solutionstatus,objectivefunction from prcase"
        cur_mdb.execute(sql_case_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_case_oracle = "insert into f_PIMS_case values(:1,:2,:3,:4,:5)"
        cur_oracle.executemany(sql_case_oracle, row_list)
        print(sql_case_oracle)
        conn_oracle.commit()
        cur_mdb.close()
        conn_mdb.close()
        cur_oracle.close()
        conn_oracle.close()
        endTime = time.time()
        print("insertCase结束时间：%s") %time.time()

    
    def insertSolution(self,conn_oracle,cur_oracle,cur_mdb):
        # 往solution里存数据
        sql_solution_mdb = "select solutionid,username from prsolution"
        cur_mdb.execute(sql_solution_mdb)
        rows = cur_mdb.fetchall()
        row_list = []
        for row in rows:
            mylist = []
            for i in range(0, len(row)):
                if row[i] == None:
                    mylist.append(str(0))
                else:
                    if type(row[i]) is int:
                        mylist.append(str(row[i]))
                    else:
                        mylist.append(row[i])
            row_list.append(mylist)
        sql_solution_oracle = "insert into d_PIMS_solution(solutionid,username)  values(:1,:2)"
        cur_oracle.executemany(sql_solution_oracle, row_list)
        conn_oracle.commit()

#             # 往period里存数据
#             sql_prperiod_mdb = "select solutionid,username from prsolution"

#             cur_mdb.close()
#             conn_mdb.close()
#             cur_oracle.close()
#             conn_oracle.close()
#             endTime = time.time()
#             print("导入成功")
#             print("耗时：" + str(endTime - startTime))
if __name__=="__main__":
    p=PimsCommand()
    p.handle()

