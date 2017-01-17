-- These commands completely tear down the database if a fresh restart is
-- required.
DROP TABLE IF EXISTS actions CASCADE;
DROP TABLE IF EXISTS symbols CASCADE;
DROP TABLE IF EXISTS vendors CASCADE;
DROP TABLE IF EXISTS symbol_vendor CASCADE;
DROP TABLE IF EXISTS prices CASCADE;
DROP TABLE IF EXISTS funds CASCADE;
DROP TABLE IF EXISTS portfolios CASCADE;
DROP TABLE IF EXISTS positions CASCADE;
DROP TABLE IF EXISTS closed_positions CASCADE;
