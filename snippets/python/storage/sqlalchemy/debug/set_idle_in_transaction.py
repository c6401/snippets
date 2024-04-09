from sqlalchemy import text
session.execute(text("SET idle_in_transaction_session_timeout TO '1000';"))