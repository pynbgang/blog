#!/usr/bin/python3
import remoteconnection as rc
import os,sys
from multiprocessing import Pool
from datetime import datetime
import time
if __name__ == '__main__':
    while 1:
        try:
            now = str(datetime.now())
            date=rc.cur_time()
            filename="RE_memusage"
            boxname=["erebus.ultralab.juniper.net","hypnos.ultralab.juniper.net","moros.ultralab.juniper.net","norfolk.ultralab.juniper.net","alcoholix.ultralab.juniper.net","antalya.ultralab.juniper.net","automatix.ultralab.juniper.net","beltway.ultralab.juniper.net","bethesda.ultralab.juniper.net","botanix.ultralab.juniper.net","dogmatix.ultralab.juniper.net","getafix.ultralab.juniper.net","idefix.ultralab.juniper.net","kratos.ultralab.juniper.net","pacifix.ultralab.juniper.net","photogenix.ultralab.juniper.net","rio.ultralab.juniper.net","matrix.ultralab.juniper.net","cacofonix.ultralab.juniper.net","asterix.ultralab.juniper.net","timex.ultralab.juniper.net","greece.ultralab.juniper.net","holland.ultralab.juniper.net","nyx.ultralab.juniper.net","atlantix.ultralab.juniper.net","obelix.ultralab.juniper.net","camaro.ultralab.juniper.net","mustang.ultralab.juniper.net"]
            instance,data_map=[],{}
            pool=Pool(5)
            for i in boxname:
                dir_name="data/"+i.split(".")[0]+date
                data_map[i]=dir_name
                pool.apply_async(rc.build_directory,args = (dir_name,))
            pool.close()
            pool.join()

        ###get memory usage
            cli_cmd="cli show chassis routing-engine \|match memo   "
            pool1=Pool(5)
            for i in boxname:
                pool1.apply_async(rc.getoutput,args = (i,cli_cmd,filename,data_map[i]))
            pool1.close()
            pool1.join()
            print('record date to sql')
            data_map={i:data_map[i]+'/'+filename for i in data_map}
            all_sql,set_name=[],set()
            for i in data_map:
                try:
                    with open(data_map[i],'r') as f:
                        for j in f.readlines():
                            if "Memory utilization" in j:
                                temp=[z for z in j.split(" ") if z!=""]
                                if i not in set_name:
                                    all_sql.append((i+"-re0",'0',now,temp[-2]))
                                    set_name.add(i)
                                else:all_sql.append((i+"-re1",'1',now,temp[-2]))
                except:pass
            sql='INSERT INTO attlab.REmemusage VALUES(%s,%s,%s,%s)'
            rc.record2mysql(sql,all_sql)
            os.system("rm -rf data/*")
        # remove data
        except:pass
        finally:
            os.system("rm -rf data/*")
        time.sleep(60)



