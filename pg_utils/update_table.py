CREATE TABLE public.brands
(
    brand_id integer NOT NULL,
    brand_name text,
    PRIMARY KEY (brand_id)
);

ALTER TABLE IF EXISTS public.brands
    OWNER to postgres;