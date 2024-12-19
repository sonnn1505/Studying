# Vận hành TIP***:
          
        l_dsc_pam : password vib@123
	airflow webserver -p 8080 -D &
	airflow scheduler -D &
	
	Kill xxx
	
	ps aux | grep airflow
	
	GRANT ALL ON SCHEMA public TO air_db_u;
	
	From <https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html> 
	
	liêt kê dags
		 airflow dags list
		 airflow providers list
	
	Start :
		airflow webserver -p 8080 -D
		airflow scheduler -D
		(nếu không start được scheduler in background :
		 cd $AIRFLOW_HOME
		 ls -l
		 rm airflow-scheduler.err
		airflow scheduler -D
	           )
	
		KILL ALL process:
		
		lsof -t -i:8080 | xargs kill -9
	postgresql: 
	
		Cài đặt tho document của hãng:
		https://www.postgresql.org/docs/devel/install-make.html
		
		su - postgres01
		password: sa
		
		start server:
		/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data/ start
		stopr Server
		/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data/ stop
		
		Kiêm tra status DB:
		
		/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data/ status
		
		connect to database :
		 
		/usr/local/pgsql/bin/psql airflow_db
		
		--->su dung psql theo link:
		https://www.freecodecamp.org/news/manage-postgresql-with-psql/
		help : \?
		list all table : \dt
		quit : \q
		
		-->tìm file config:
		
		sudo find / -name pg\*.conf
		vi /usr/local/pgsql/data/postgresql.conf
		vi /usr/local/pgsql/data/pg_hba.conf
			□ Esc – switch to command mode
			□ :w – write out changes that were made
			□ :q – exit Vim
			□ :q! – exit Vim and discard any changes
			□ :wq – saves the changes, and exits Vim
			□ :x – save the changes made, and exits Vim
			□ i - insert
chỉnh remote connection: https://o7planning.org/12255/configure-postgresql-to-allow-remote-connections![image](https://github.com/user-attachments/assets/7be6e3e5-c047-49c5-ac6f-e73dfa29b614)
