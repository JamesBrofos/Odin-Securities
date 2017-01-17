-- This code inserts data vendors into the database. At the moment, data is
-- harvested from Quandl and Yahoo! Finance.
--
-- Nota Bene: Note that the order of Yahoo! Finance and Quandl (and whatever
-- other data vendors there might be is significant). This is because the
-- smaller the vendor id, the more its data is prioritized in price and volume
-- queries to the database.
INSERT INTO vendors (vendor) VALUES ('Yahoo! Finance'), ('Quandl');

-- Insert a portfolio for testing purposes only. This portfolio is constructed
-- by default for convenience so that it does not need to be added every time
-- the database is torn down.
INSERT INTO portfolios (portfolio, maximum_capacity, capital, updated) VALUES (
'test_portfolio_id', 1, 100000.0, current_timestamp);
