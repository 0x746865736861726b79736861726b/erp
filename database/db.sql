-- Table: products
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    sku TEXT NOT NULL UNIQUE
);

-- Table: services
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT NOT NULL UNIQUE
);

-- Table: partners
CREATE TABLE partners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

-- Table: documents
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_type TEXT NOT NULL CHECK (doc_type IN ('invoice', 'order', 'tax_invoice')),
    doc_number TEXT NOT NULL UNIQUE,
    doc_date TEXT NOT NULL,
    partner_id INTEGER NOT NULL,
    FOREIGN KEY (partner_id) REFERENCES partners(id)
);


-- Table: product_lines
CREATE TABLE product_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    line_number INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity NUMERIC NOT NULL,
    price NUMERIC NOT NULL,
    total NUMERIC NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    UNIQUE (document_id, line_number) 
);

-- Table: service_lines
CREATE TABLE service_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    line_number INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity NUMERIC NOT NULL,
    price NUMERIC NOT NULL,
    total NUMERIC NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (service_id) REFERENCES services(id),
    UNIQUE (document_id, line_number)
);

-- Table: inventory
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    batch_number TEXT NOT NULL,
    entry_date TEXT NOT NULL,
    quantity NUMERIC NOT NULL,
    cost NUMERIC NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Table: orders
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_number TEXT NOT NULL UNIQUE,
    order_date TEXT NOT NULL,
    client_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('new', 'accepted')),
    FOREIGN KEY (client_id) REFERENCES partners(id)
);

-- Table: invoices
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT NOT NULL UNIQUE,
    invoice_date TEXT NOT NULL,
    order_id INTEGER NOT NULL,
    total NUMERIC NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Table: tax_invoices
CREATE TABLE tax_invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tax_invoice_number TEXT NOT NULL UNIQUE,
    tax_invoice_date TEXT NOT NULL,
    document_id INTEGER NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

-- Table: document_links
CREATE TABLE document_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER NOT NULL,
    child_id INTEGER NOT NULL,
    link_type TEXT NOT NULL CHECK (link_type IN ('parent-child', 'related', 'reference')),
    FOREIGN KEY (parent_id) REFERENCES documents(id),
    FOREIGN KEY (child_id) REFERENCES documents(id)
);

-- Indexes for frequently queried columns
CREATE INDEX idx_documents_doc_date ON documents (doc_date);
CREATE INDEX idx_inventory_product_id ON inventory (product_id);
CREATE INDEX idx_orders_order_date ON orders (order_date);
CREATE INDEX idx_invoices_invoice_date ON invoices (invoice_date);
CREATE INDEX idx_tax_invoices_tax_invoice_date ON tax_invoices (tax_invoice_date);
