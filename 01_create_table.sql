CREATE TABLE dbo.Restaurant_Final (
    order_id        INT,
    order_date      DATE,
    hour            TINYINT,
    category        NVARCHAR(100),
    item_name       NVARCHAR(200),
    price           DECIMAL(10,2),
    quantity        SMALLINT,
    discount        DECIMAL(5,2),
    total_amount    DECIMAL(10,2),
    branch          NVARCHAR(100),
    payment_method  NVARCHAR(50),
    order_type      NVARCHAR(50),
    customer_id     INT,
    rating          TINYINT,
    is_weekend      TINYINT
)
