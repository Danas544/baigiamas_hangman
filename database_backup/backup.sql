--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.4 (Debian 15.4-1.pgdg120+1)

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
-- Name: stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stats (
    id integer NOT NULL,
    type character varying(4) NOT NULL,
    score integer,
    date timestamp without time zone,
    user_id integer
);


ALTER TABLE public.stats OWNER TO postgres;

--
-- Name: stats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stats_id_seq OWNER TO postgres;

--
-- Name: stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stats_id_seq OWNED BY public.stats.id;


--
-- Name: theme; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.theme (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    activate boolean
);


ALTER TABLE public.theme OWNER TO postgres;

--
-- Name: theme_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.theme_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.theme_id_seq OWNER TO postgres;

--
-- Name: theme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.theme_id_seq OWNED BY public.theme.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(120) NOT NULL,
    photo character varying(20) NOT NULL,
    password character varying(60) NOT NULL,
    email_confirm boolean,
    admin boolean
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.word (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    activate boolean,
    theme_id integer
);


ALTER TABLE public.word OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_id_seq OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- Name: stats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stats ALTER COLUMN id SET DEFAULT nextval('public.stats_id_seq'::regclass);


--
-- Name: theme id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.theme ALTER COLUMN id SET DEFAULT nextval('public.theme_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: stats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stats (id, type, score, date, user_id) FROM stdin;
1	win	6	2023-08-26 02:17:08.197033	1
2	lose	0	2023-08-26 02:17:08.197033	1
3	win	9	2023-08-26 02:17:08.197033	1
4	win	4	2023-08-26 02:17:08.197033	3
5	win	3	2023-08-26 02:17:08.197033	3
6	win	4	2023-08-26 02:17:08.197033	4
7	lose	0	2023-08-26 02:17:08.197033	4
8	win	10	2023-08-27 15:41:42.124953	3
\.


--
-- Data for Name: theme; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.theme (id, name, activate) FROM stdin;
1	Animals	t
2	Colors	t
3	Professions	t
4	Countries	t
5	Fruits	t
6	Movies	t
7	Sports	t
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, email, photo, password, email_confirm, admin) FROM stdin;
1	Danielius	Danielius.au@gmail.com	afc3745f33f1275d.jpg	$2b$12$tms7kB2uRl25saV1uT8QPOZuYzvPsuuckMH08nyDAZw9kbw5toEuO	t	t
2	username	pastas@gmail.lt	default.jpg	$2b$12$vP3OyTIRDTeGqTuYSVvJAuFLNugZkCY3gDbjXPJ2fDxgbDtICjcxC	f	f
3	artiomas3000	arturasshadow@inbox.lt	default.jpg	$2b$12$/N1mWsteMDtyivQr8gheLOzIsqrtHpURmmEDfY3TDzo24zjNS/O6q	t	f
4	barba	dobarbara3@gmail.com	default.jpg	$2b$12$.K4bSgXlQy0.WRlmxQL0.Oogo6gs8l9.sD.f7eUaWw7ztZiTKugUe	t	f
5	Efka	evaliulis123@gmail.com	default.jpg	$2b$12$V3DHDO3HwaNrsJN5yux9gOhPjni6K7I4QHSyJxieVrSg4zu25ATZO	t	f
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.word (id, name, activate, theme_id) FROM stdin;
12	Lion	t	1
13	Elephant	t	1
14	Giraffe	t	1
15	Tiger	t	1
16	Monkey	t	1
17	Zebra	t	1
18	Kangaroo	t	1
19	Dolphin	t	1
20	Penguin	t	1
21	Panda	t	1
22	Koala	t	1
23	Cheetah	t	1
24	Rhinoceros	t	1
25	Gorilla	t	1
26	Hippopotamus	t	1
27	Ostrich	t	1
28	Crocodile	t	1
29	Flamingo	t	1
30	Octopus	t	1
31	Seahorse	t	1
32	Red	t	2
33	Blue	t	2
34	Green	t	2
35	Yellow	t	2
36	Orange	t	2
37	Purple	t	2
38	Pink	t	2
39	Brown	t	2
40	Black	t	2
41	White	t	2
42	Gray	t	2
43	Silver	t	2
44	Gold	t	2
45	Indigo	t	2
46	Turquoise	t	2
47	Maroon	t	2
48	Cyan	t	2
49	Magenta	t	2
50	Beige	t	2
51	Lavender	t	2
52	Doctor	t	3
53	Engineer	t	3
54	Teacher	t	3
55	Chef	t	3
56	Lawyer	t	3
57	Artist	t	3
58	Pilot	t	3
59	Nurse	t	3
60	Firefighter	t	3
61	Police Officer	t	3
62	Accountant	t	3
63	Photographer	t	3
64	Musician	t	3
65	Writer	t	3
66	Athlete	t	3
67	Scientist	t	3
68	Architect	t	3
69	Carpenter	t	3
70	Electrician	t	3
71	Farmer	t	3
72	United States	t	4
73	Canada	t	4
74	Australia	t	4
75	United Kingdom	t	4
76	Germany	t	4
77	France	t	4
78	Japan	t	4
79	Brazil	t	4
80	China	t	4
81	India	t	4
82	Italy	t	4
83	Russia	t	4
84	South Africa	t	4
85	Mexico	t	4
86	Spain	t	4
87	Argentina	t	4
88	South Korea	t	4
89	Turkey	t	4
90	Egypt	t	4
91	Greece	t	4
92	Apple	t	5
93	Banana	t	5
94	Orange	t	5
95	Mango	t	5
96	Strawberry	t	5
97	Pineapple	t	5
98	Grape	t	5
99	Watermelon	t	5
100	Kiwi	t	5
101	Peach	t	5
102	Pear	t	5
103	Cherry	t	5
104	Plum	t	5
105	Blueberry	t	5
106	Raspberry	t	5
107	Lemon	t	5
108	Lime	t	5
109	Avocado	t	5
110	Papaya	t	5
111	Fig	t	5
112	Soccer	t	7
113	Basketball	t	7
114	Football	t	7
115	Tennis	t	7
116	Golf	t	7
117	Swimming	t	7
118	Baseball	t	7
119	Volleyball	t	7
120	Cricket	t	7
121	Rugby	t	7
122	Hockey	t	7
123	Boxing	t	7
124	Skiing	t	7
125	Running	t	7
126	Cycling	t	7
127	Gymnastics	t	7
128	Wrestling	t	7
129	Surfing	t	7
130	Snowboarding	t	7
131	MartialArts	t	7
132	Titanic	t	6
133	Avatar	t	6
134	JurassicPark	t	6
135	StarWars	t	6
136	TheMatrix	t	6
137	TheLordOfTheRings	t	6
138	Inception	t	6
139	HarryPotter	t	6
140	TheAvengers	t	6
141	ForrestGump	t	6
142	TheLionKing	t	6
143	FindingNemo	t	6
144	ToyStory	t	6
145	Frozen	t	6
146	SpiderMan	t	6
147	BlackPanther	t	6
148	WonderWoman	t	6
149	PulpFiction	t	6
150	TheDarkKnight	t	6
151	AmericanPie	t	6
\.


--
-- Name: stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stats_id_seq', 8, true);


--
-- Name: theme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.theme_id_seq', 7, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 5, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.word_id_seq', 151, true);


--
-- Name: stats stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stats
    ADD CONSTRAINT stats_pkey PRIMARY KEY (id);


--
-- Name: theme theme_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.theme
    ADD CONSTRAINT theme_name_key UNIQUE (name);


--
-- Name: theme theme_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.theme
    ADD CONSTRAINT theme_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: word word_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word
    ADD CONSTRAINT word_pkey PRIMARY KEY (id);


--
-- Name: stats stats_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stats
    ADD CONSTRAINT stats_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: word word_theme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word
    ADD CONSTRAINT word_theme_id_fkey FOREIGN KEY (theme_id) REFERENCES public.theme(id);


--
-- PostgreSQL database dump complete
--

