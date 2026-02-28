-- Future SaaS expansion tables
CREATE TABLE billing_sync(
id INTEGER PRIMARY KEY AUTOINCREMENT,
bill_no TEXT,
total REAL,
discount REAL,
staff_id INTEGER,
datetime TEXT
);

CREATE TABLE billing_modifications(
id INTEGER PRIMARY KEY AUTOINCREMENT,
bill_no TEXT,
staff_id INTEGER,
mod_type TEXT,
old_value TEXT,
new_value TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);