ALTER FUNCTION now() RENAME TO system_now;
CREATE FUNCTION now()
    RETURNS TIMESTAMPTZ as $$
    BEGIN
        RETURN TIMESTAMP '2020-01-01';
    END;
$$ LANGUAGE plpgsql;