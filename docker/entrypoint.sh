#!/bin/bash


function test_postgres {
	pg_isready -h "${PRETTIQUE_BE_POSTGRESQL_HOST}" -U "${PRETTIQUE_BE_POSTGRESQL_USER}"
}

RUN_CMD="${@:-python3 manage.py runserver 0.0.0.0:8000}"

DEBUG="${DEBUG:False}"

if [[ $RUN_CMD == *"python3 manage.py"* ]]; then

	count=0
	until ( test_postgres )
	do
	  ((count++))
	  if [ ${count} -gt 1500 ]
	  then
		echo "Services didn't become ready in time"
		exit 1
	  fi
	  sleep 0.1
	done

	if [[ $RUN_CMD != *"python3 manage.py test"* ]]; then
		python3 manage.py migrate
	fi
fi

if [[ $DEBUG == "False" ]] || [[ $DEBUG == "false" ]]; then
	python3 manage.py collectstatic --noinput
fi

exec $RUN_CMD