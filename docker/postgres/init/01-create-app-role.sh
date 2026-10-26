#!/bin/bash
# Runs once, on first initialisation of an empty data volume (official postgres image entrypoint).
# Creates the non-superuser application role and its databases. The password is passed as a psql variable and quoted
# by psql (:'app_pw'), so it is never interpolated into SQL by the shell and never echoed.
set -euo pipefail
: "${PISMO_DB_APP_PASSWORD:?PISMO_DB_APP_PASSWORD is not set}"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname postgres -v app_pw="$PISMO_DB_APP_PASSWORD" <<'SQL'
CREATE ROLE pismo_app LOGIN PASSWORD :'app_pw' NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION;
CREATE DATABASE pismo_assistant OWNER pismo_app;
CREATE DATABASE pismo_assistant_test OWNER pismo_app;
REVOKE CONNECT ON DATABASE pismo_assistant FROM PUBLIC;
REVOKE CONNECT ON DATABASE pismo_assistant_test FROM PUBLIC;
GRANT CONNECT ON DATABASE pismo_assistant TO pismo_app;
GRANT CONNECT ON DATABASE pismo_assistant_test TO pismo_app;
SQL
echo "pismo_app role and databases pismo_assistant, pismo_assistant_test created"
