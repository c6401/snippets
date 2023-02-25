def update_relation(
    table: str,
    left_rel: str,
    left_fk: int,
    right_rel: str,
    right_fks: list[int],
    connection: connection = None
):
    relations = database.fetchall('''
        select * from %(table)s
        where %(left_rel)s = %(left_fk)d;
    ''', {
        "table": table, "left_rel": left_rel, "left_fk": left_fk,
    }, connection=connection)
    existing = {getattr(r, right_rel) for r  in relations}
    new = set(right_fks)

    delete = existing - new
    insert = new - existing
    database.delete(table, {left_rel: left_fk, f'{right_rel} in': delete}, connection=connection)
    database.insert(table, [{left_rel: left_fk, right_rel: fk} for fk in insert])

