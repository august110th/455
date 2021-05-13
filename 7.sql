INSERT INTO public.genre(
	genreid, name)
	VALUES
	(1, 'rock'),
	(2, 'jazz'),
	(3, 'electronic'),
	(4, 'pop'),
	(5, 'ambient');
INSERT INTO public.author(
authorid, name)
	VALUES
	(1, 'plaid'),
	(2, 'plone'),
	(3, 'pluxus'),
	(4, 'aha'),
	(5, 'brian eno'),
	(6, 'ddt'),
	(7,'jazzamore'),
	(8, 'beyonce');
INSERT INTO public.album(
	albumid, name, year)
 	VALUES
 	(1, 'spokes', 2019),
 	(2, 'for beginner piano', 1999),
 	(3, 'solid state', 2006),
 	(4, 'lifelines', 2002),
 	(5, 'neroli', 1993),
 	(6, 'lubov', 1996),
 	(7,'beautiful day', 2020),
 	(8, 'lemonade', 2018);
INSERT INTO public.song(
	songid, albumid, name, duration_sec)
 	VALUES
 	(1, 1, 'marry', 388),
 	(2, 1, 'upona', 304),
 	(3, 2, 'plock', 214),
	(4, 2, 'on my bus', 256),
	(5, 3, 'perm', 267),
	(6, 3, 'transient', 267),
 	(7, 4, 'lifelines', 249),
	(8, 4, 'you wanted more', 204),
 	(9, 5, 'neroli', 3482),
	(10, 5, 'new space music', 3675),
 	(11, 6, 'lubov', 310),
	(12, 6, 'ya u vas', 309),
 	(13, 7, 'beautiful day', 199),
	(14, 7, 'time is running', 252),
 	(15, 8, 'sorry', 211);
INSERT INTO public.genre_author(
authorid, genreid)
	VALUES
	(1, 3),
	(2, 3),
	(3, 3),
	(4, 4),
	(5, 3),
	(5, 5),
	(6, 1),
	(6, 4),
	(7, 2),
	(7, 3),
	(7, 4),
	(8, 1),
	(8, 4);
INSERT INTO public.feat(
authorid, albumid)
	VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(4, 4),
	(4, 3),
	(5, 5),
	(5, 3),
	(6, 6),
	(6, 3),
	(7, 7),
	(7, 3);
INSERT INTO public.collection(
 	collectionid, name, year)
  	VALUES
 	(1, 'VA_spokes', 2019),
 	(2, 'VA_for beginner piano', 2020),
 	(3, 'VA_solid state', 2006),
 	(4, 'VA_lifelines', 2002),
  	(5, 'VA_neroli', 1993),
 	(6, 'VA_lubov', 1996),
 	(7,'VA_beautiful day', 2007),
 	(8, 'VA_lemonade', 2016);
INSERT INTO public.song_collection(
 songid, collectionid)
 	VALUES
 	(1, 3),
 	(2, 3),
 	(3, 3),
 	(4, 4),
 	(5, 3),
 	(5, 5),
 	(6, 1),
 	(6, 4),
 	(7, 2),
 	(7, 3),
 	(7, 4),
 	(8, 1),
 	(8, 4);