CREATE TABLE Star (
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(20) NOT NULL,
  t_eff INTEGER,
  radius FLOAT(5),
  PRIMARY KEY (koi_name)
);


COPY Star (kepler_id, koi_name, t_eff, radius) FROM 'stars.csv' CSV;