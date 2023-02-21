-- Create database
CREATE DATABASE marvel;


CREATE TABLE hero (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(500),
    n_comics INTEGER,
    n_series INTEGER,
    thumbnail VARCHAR(500)
);

-- Create user
CREATE USER macia WITH PASSWORD 'macia';

-- Set privileges
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO macia; 
GRANT ALL PRIVILEGES ON DATABASE marvel TO macia;
GRANT ALL PRIVILEGES ON TABLE hero TO macia;