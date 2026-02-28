CREATE TABLE staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin','staff')),
    password TEXT NOT NULL
);

CREATE TABLE guests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT,
    category TEXT,
    pax INTEGER,
    visit_date TEXT,
    visit_time TEXT,
    staff_id INTEGER,
    FOREIGN KEY(staff_id) REFERENCES staff(id)
);

CREATE TABLE bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER,
    amount REAL,
    platform TEXT,
    bill_time TEXT,
    FOREIGN KEY(guest_id) REFERENCES guests(id)
);

CREATE TABLE fraud_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER,
    issue TEXT,
    score REAL,
    created_at TEXT
);
