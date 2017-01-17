all:
	psql -d securities_master -U securities -w -f ./database/teardown.sql
	psql -d securities_master -U securities -w -f ./database/schema.sql
	psql -d securities_master -U securities -w -f ./database/initialize.sql

restart:
	sudo /etc/init.d/postgresql restart
