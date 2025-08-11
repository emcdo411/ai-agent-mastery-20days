# W3D16 Profile Report

**Rows x Cols:** 15 x 11

## Column Summary
| column        | dtype          |   non_null |   nulls |   null_% |   unique |
|:--------------|:---------------|-----------:|--------:|---------:|---------:|
| discount      | float64        |         14 |       1 |     6.67 |        3 |
| order_date    | datetime64[ns] |         14 |       1 |     6.67 |       13 |
| quantity      | float64        |         15 |       0 |     0    |        1 |
| segment       | object         |         15 |       0 |     0    |        3 |
| country       | object         |         15 |       0 |     0    |        4 |
| url           | object         |         15 |       0 |     0    |       10 |
| product       | object         |         15 |       0 |     0    |       11 |
| unit_price    | float64        |         15 |       0 |     0    |       11 |
| total         | float64        |         15 |       0 |     0    |       12 |
| order_id      | int64          |         15 |       0 |     0    |       14 |
| customer_name | object         |         15 |       0 |     0    |       14 |

## Sample Rows
|   order_id | order_date          | customer_name   | segment     | country   | product              |   unit_price |   quantity |   discount |   total | url                        |
|-----------:|:--------------------|:----------------|:------------|:----------|:---------------------|-------------:|-----------:|-----------:|--------:|:---------------------------|
|       1001 | 2024-06-01 00:00:00 | Alice Johnson   | Consumer    | US        | Laptop Pro 14        |      1480.05 |          1 |       0    | 1480.04 | https://example.com/p/LP14 |
|       1002 | 2024-06-02 00:00:00 | Bob Smith       | Corporate   | US        | Ergo Chair           |       299.5  |          1 |       0.1  |  269.55 | https://example.com/p/CH01 |
|       1003 | 2024-06-03 00:00:00 | Carla  Diaz     | Home Office | CA        | 4K Monitor           |       399    |          1 |       0    |  399    | https://example.com/p/MN4K |
|       1003 | 2024-06-03 00:00:00 | Carla Diaz      | Home Office | CA        | 4K Monitor           |       399    |          1 |       0    |  399    | https://example.com/p/MN4K |
|       1004 | 2024-06-04 00:00:00 | DeShawn Lee     | Consumer    | US        | USB-C Dock           |       129    |          1 |     nan    |  129    | https://example.com/p/DK01 |
|       1005 | 2024-06-05 00:00:00 | Eve O'Neil      | Consumer    | UK        | Noise-Cancel Headset |       199.99 |          1 |       0.05 |  189.99 | https://example.com/p/HS01 |
|       1006 | 2024-06-06 00:00:00 | Frank  Moore    | Corporate   | US        | Standing Desk        |       899    |          1 |       0    |  899    | https://example.com/p/SD01 |
|       1007 | 2024-06-07 10:30:00 | Grace  Kim      | Home Office | US        | Portable SSD         |       119.99 |          1 |       0    |  119.99 | https://example.com/p/SSD1 |
|       1008 | 2024-06-08 00:00:00 | Hank  Zhao      | Consumer    | CA        | Webcam 1080p         |        69.95 |          1 |       0    |   69.95 | https://example.com/p/WC10 |
|       1009 | NaT                 | Ivan Petrov     | Corporate   | DE        | Wireless Mouse       |        49.99 |          1 |       0    |   49.99 | https://example.com/p/MSWL |
