--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg120+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: stats; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.stats (
    id integer NOT NULL,
    type character varying(4) NOT NULL,
    score integer,
    date timestamp without time zone,
    user_id integer
);


ALTER TABLE public.stats OWNER TO "user";

--
-- Name: stats_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stats_id_seq OWNER TO "user";

--
-- Name: stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.stats_id_seq OWNED BY public.stats.id;


--
-- Name: theme; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.theme (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    activate boolean
);


ALTER TABLE public.theme OWNER TO "user";

--
-- Name: theme_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.theme_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.theme_id_seq OWNER TO "user";

--
-- Name: theme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.theme_id_seq OWNED BY public.theme.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    email character varying(120) NOT NULL,
    photo character varying(20) NOT NULL,
    password character varying(60) NOT NULL,
    admin boolean
);


ALTER TABLE public."user" OWNER TO "user";

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO "user";

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.word (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    activate boolean,
    theme_id integer
);


ALTER TABLE public.word OWNER TO "user";

--
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_id_seq OWNER TO "user";

--
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- Name: stats id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.stats ALTER COLUMN id SET DEFAULT nextval('public.stats_id_seq'::regclass);


--
-- Name: theme id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.theme ALTER COLUMN id SET DEFAULT nextval('public.theme_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: stats; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.stats (id, type, score, date, user_id) FROM stdin;
1	win	10	2023-08-23 17:52:31.104003	1
2	lose	0	2023-08-23 17:57:52.264793	2
3	win	9	2023-08-23 18:50:37.801477	1
\.


--
-- Data for Name: theme; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.theme (id, name, activate) FROM stdin;
1	Animals	t
2	Fruits	t
3	Countries	t
4	Colors	t
5	Professions	t
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public."user" (id, username, email, photo, password, admin) FROM stdin;
2	d	d@gmail.com	default.jpg	$2b$12$t6T/tA1kNP5G11gkHEkxpu8RRKNJXITogFIpZUIyB.dAvhuLzENr2	f
1	Danielius	Danielius.au@gmail.com	da894e05ebed6c6b.jpg	$2b$12$iQH3wD/YPYbsPrcrF9K9aOxwrmF4LiQoHdaJHu2oSK25qWFf4h2Pi	t
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.word (id, name, activate, theme_id) FROM stdin;
1	Dog	t	1
2	Cat	t	1
3	Elephant	t	1
4	Giraffe	t	1
5	Lion	t	1
6	apple	t	2
7	banana	t	2
8	orange	t	2
9	grape	t	2
10	pear	t	2
11	usa	t	3
12	uk	t	3
13	canada	t	3
14	japan	t	3
15	germany	t	3
16	red	t	4
17	blue	t	4
18	green	t	4
19	yellow	t	4
20	orange	t	4
21	doctor	t	5
22	teacher	t	5
23	engineer	t	5
24	artist	t	5
25	chef	t	5
\.


--
-- Name: stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.stats_id_seq', 3, true);


--
-- Name: theme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.theme_id_seq', 5, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.word_id_seq', 25, true);


--
-- Name: stats stats_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.stats
    ADD CONSTRAINT stats_pkey PRIMARY KEY (id);


--
-- Name: theme theme_name_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.theme
    ADD CONSTRAINT theme_name_key UNIQUE (name);


--
-- Name: theme theme_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.theme
    ADD CONSTRAINT theme_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: word word_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.word
    ADD CONSTRAINT word_pkey PRIMARY KEY (id);


--
-- Name: stats stats_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.stats
    ADD CONSTRAINT stats_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: word word_theme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.word
    ADD CONSTRAINT word_theme_id_fkey FOREIGN KEY (theme_id) REFERENCES public.theme(id);


--
-- PostgreSQL database dump complete
--

