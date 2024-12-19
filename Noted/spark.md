	1. cd //app/pyspark/../sbin/
  2. chay lênh duới để start master
      bash start-master.sh -h 10.60.3.14 -p 4041 --webui-port 8888  
      bash start-master.sh -h 127.0.0.1 -p 4041 --webui-port 8888    
  3. chạy lênh duới để stop master
      bash stop-master.sh
  4. chạy file spark
      spark-submit --jars  /home/sonnn/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar /home/sonnn/spark/spark_apflayer.py
  5. start worker
      bash start-slave.sh  spark://127.0.0.1:4041

Server: //app/pyspark/../sbin/
Local: /home/sonnn/spark..
Chỉnh worker
https://mallikarjuna_g.gitbooks.io/spark/content/spark-standalone-example-2-workers-on-1-node-cluster.html![image](https://github.com/user-attachments/assets/48297bc2-f46e-4403-a963-685e287cecba)


Oralce jdbc
  spark-submit --jars /home/sonnn/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar /home/sonnn/spark/spark_apflayer.py
  spark-submit --jars /app/spark/spark-3.4.1-bin-hadoop3/jars/ojdbc8-21.5.0.0.jar /app/airflow/spark/u_sta_camp_user_voucher_detail_backup_plan.py --total-executor-cores 8


Redshift jdbc
  spark-submit --jars /home/sonnn/spark-3.4.1-bin-hadoop3/jars/redshift-jdbc42-2.1.0.16.jar /home/sonnn/spark/redshift.py
  ![image](https://github.com/user-attachments/assets/ef31db87-6c69-42b3-b118-b0b6c5d130e0)
