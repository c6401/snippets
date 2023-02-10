env PGPASSWORD=devel pg_dump -h localhost -p 5432 -U user -d db --table table --schema-only
