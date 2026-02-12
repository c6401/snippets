WITH RECURSIVE tree AS (
    SELECT id, parent, title, 0 AS level, '' AS path
    FROM table
    WHERE parent = 0

    UNION ALL

    SELECT b.id, b.parent, b.title, t.level + 1, t.path || ' / ' || b.title
    FROM table b
    JOIN tree t ON b.parent = t.id
)
    SELECT t.id, t.path, t.title
    FROM tree as t
