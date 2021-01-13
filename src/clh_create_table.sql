CREATE TABLE tutorial.pageview_counts (
    pagename String ,
    pageviewcount Int16 ,
    `index` Int16 ,
    datetime DateTime
)
ENGINE = MergeTree()
ORDER BY datetime
