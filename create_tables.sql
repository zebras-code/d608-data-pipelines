DROP table IF EXISTS public.artists;
DROP table IF EXISTS public.songplays;
DROP table IF EXISTS public.songs;
DROP table IF EXISTS public.staging_events;
DROP table IF EXISTS public.staging_songs;
DROP table IF EXISTS public."time";
DROP table IF EXISTS public.users;

CREATE TABLE public.artists (
    artistid varchar(256) NOT NULL,
    name varchar(512),
    location varchar(512),
    lattitude numeric(18,0),
    longitude numeric(18,0)
);

CREATE TABLE IF NOT EXISTS songplays (
    songplay_id VARCHAR PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location VARCHAR,
    user_agent TEXT
);

CREATE TABLE public.songs (
    songid varchar(256) NOT NULL,
    title varchar(512),
    artistid varchar(256),
    "year" int4,
    duration numeric(18,0),
    CONSTRAINT songs_pkey PRIMARY KEY (songid)
);

CREATE TABLE public.staging_events (
    artist varchar(256),
    auth varchar(256),
    firstname varchar(256),
    gender varchar(256),
    iteminsession int4,
    lastname varchar(256),
    length numeric(18,0),
    "level" varchar(256),
    location varchar(256),
    "method" varchar(256),
    page varchar(256),
    registration numeric(18,0),
    sessionid int4,
    song varchar(256),
    status int4,
    ts int8,
    useragent varchar(256),
    userid int4
);

CREATE TABLE public.staging_songs (
    num_songs int4,
    artist_id varchar(256),
    artist_name varchar(512),
    artist_latitude numeric(18,0),
    artist_longitude numeric(18,0),
    artist_location varchar(512),
    song_id varchar(256),
    title varchar(512),
    duration numeric(18,0),
    "year" int4
);

CREATE TABLE public."time" (
    start_time timestamp NOT NULL,
    "hour" int4,
    "day" int4,
    week int4,
    "month" varchar(256),
    "year" int4,
    weekday varchar(256),
    CONSTRAINT time_pkey PRIMARY KEY (start_time)
);

CREATE TABLE public.users (
    userid int4 NOT NULL,
    first_name varchar(256),
    last_name varchar(256),
    gender varchar(256),
    "level" varchar(256),
    CONSTRAINT users_pkey PRIMARY KEY (userid)
);
