## Table: `products`

| Field    | Type        | Description                 |
| -------- | ----------- | --------------------------- |
| `id`     | SERIAL (PK) | Unique indeficator          |
| `name`   | VARCHAR     | Product name                |
| `unit`   | VARCHAR     |  Product unit (eg. kg, pcs) |
| `sku`    | VARCHAR     | Product code (SKU)          |


## Table: `services`

| Field    | Type        | Description        |
| -------- | ----------- | ------------------ |
| `id`     | SERIAL (PK) | Unique indeficator |
| `name`   | VARCHAR     | Service name       |
| `code`   | VARCHAR     | serivce code       |


## Table `partners`

| Field    | Type        | Description         |
| -------- | ----------- | ------------------- |
| `id`     | SERIAL (PK) | Unique indeficator  |
| `name`   | VARCHAR     | Partner name        |
| `type`   | VARCHAR     | Partner type        |

## Table `documents`

| Field        | Type        | Description        |
| ------------ | ----------- | ------------------ |
| `id`         | SERIAL (PK) | Unique indeficator |
| `doc_type`   | ENUM        | Document type      |
| `doc_number` | VARCHAR     | Document number    |
| `doc_date`   | TIMESTAMP   | Document date      |
| `partner_id` | UUID (FK)   | Partner ID         |

## Table `document_lines`

| Field         | Type        | Description                          |
| ------------- | ----------- | ------------------------------------ |
| `id`          | SERIAL (PK) | Unique indeficator                   |
| `document_id` | UUID (FK)   | Document ID                          |
| `line_type`   | ENUM        | String type (eg. Product or Service) |
| `product_id`  | UUID (FK)   | Product ID (MULL if service)         |
| `service_id`  | UUID (FK)   | Partner ID (NULL is product)         |
| `quantity`    | NUMERIC     | Quantity of product or service       |
| `price`       | NUMERIC     | Price                                |
| `total`       | NUMERIC     | Total price                          |

## Table `inventory`

| Field          | Type        | Description           |
| -------------- | ----------- | --------------------- |
| `id`           | SERIAL (PK) | Unique indeficator    |
| `product_id`   | UUID (FK)   | Document ID           |
| `batch_number` | VARCHAR     | Batch number          |
| `entry_date`   | TIMESTAMP   | Date of batch arrived |
| `quantity`     | NUMERIC     | Amount of balance     |
| `cost`         | NUMERIC     | Unit cost             |

## Table `orders`

| Field          | Type        | Description                |
| -------------- | ----------- | -------------------------- |
| `id`           | SERIAL (PK) | Unique indeficator         |
| `order_number` | VARCHAR     | Order number               |
| `order_date`   | TIMESTAMP   | Order date                 |
| `client_id`    | UUID (FK)   | Foreign key for client     |
| `status`       | NUMERIC     | Order status: new, accpted |

## Table `invoices`

| Field            | Type        | Description           |
| ---------------- | ----------- | --------------------- |
| `id`             | SERIAL (PK) | Unique indeficator    |
| `invoice_number` | VARCHAR     | Invoce number         |
| `invoice_date`   | TIMESTAMP   | Invoce date           |
| `order_id`       | UUID (FK)   | Foreign key for order |
| `total`          | NUMERIC     | Total price           |

## Table `tax_invoices`

| Field                | Type        | Description              |
| -------------------- | ----------- | ------------------------ |
| `id`                 | SERIAL (PK) | Unique indeficator       |
| `tax_invoice_number` | VARCHAR     | Number of tax invoice    |
| `tax_invoice_date`   | TIMESTAMP   | Date of tax invoice      |
| `document_id`        | UUID (FK)   | Foreign key for document |

## Table `document_links`

| Field       | Type        | Description                     |
| ----------- | ----------- | ------------------------------- |
| `id`        | SERIAL (PK) | Unique indeficator              |
| `parent_id` | UUID (FK)   | Foreign key for parent document |
| `child_id`  | UUID (FK)   | Foreign key for child document  |
