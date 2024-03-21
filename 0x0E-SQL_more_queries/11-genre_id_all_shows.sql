-- lists all shows contained in the database hbtn_0d_tvshows
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS S
     LEFT JOIN `tv_shows_genres` AS G
     ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
