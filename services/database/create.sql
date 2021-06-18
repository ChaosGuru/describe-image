--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3 (Debian 13.3-1.pgdg100+1)

-- Started on 2021-06-18 21:55:37 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE image_describe;
--
-- TOC entry 2944 (class 1262 OID 16388)
-- Name: image_describe; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE image_describe WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


\connect image_describe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 16389)
-- Name: game; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA game;


SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 16402)
-- Name: player; Type: TABLE; Schema: game; Owner: -
--

CREATE TABLE game.player (
    nick character(20)[] NOT NULL,
    id integer NOT NULL,
    conn text NOT NULL
);


--
-- TOC entry 2806 (class 2606 OID 16411)
-- Name: player conn_unique; Type: CONSTRAINT; Schema: game; Owner: -
--

ALTER TABLE ONLY game.player
    ADD CONSTRAINT conn_unique UNIQUE (conn);


--
-- TOC entry 2808 (class 2606 OID 16409)
-- Name: player player_pkey; Type: CONSTRAINT; Schema: game; Owner: -
--

ALTER TABLE ONLY game.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);


-- Completed on 2021-06-18 21:55:37 EEST

--
-- PostgreSQL database dump complete
--

