#!/usr/bin/env python
import psycopg2
# -*- coding: utf-8 -*-
# fct specify the most popular artical


def pupular_artical():
    '''from log file aggregate the path and orederd decreasing and give only the
    4th element'''
    cursor.execute("select title, count(*) as views from articles join\
    log on concat('/article/', articles.slug) = log.path\
    where log.status like '%200%'\
    group by log.path, articles.title order by views desc limit 3")
    results = cursor.fetchall()
    return results


# fct specify the most popular
def pupluar_author():
    '''sum up all of the articles each author has written, which authors get the
    most page views'''
    cursor.execute("select authors.name, count(*) as views from articles join\
    authors on articles.author = authors.id join\
    log on concat('/article/', articles.slug) = log.path where\
    log.status like '%200%' group by authors.name order by views desc")
    results = cursor.fetchall()
    return results


# this fct specify which days more than 1% of requests lead to errors
def errors_days():
    ''' sum up all of the articles each author has written, which authors get the
    most page views'''
    cursor.execute("select * from (\
    select a.day,\
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)\
    as perc from\
    (select date(time) as day, count(*) as hits from log group by day) as a\
    join\
    (select date(time) as day, count(*) as hits from log where status\
    like '%404%' group by day) as b\
    on a.day = b.day)\
    as t where perc >= 1.0")
    results = cursor.fetchall()
    return results


# this function that print out the first 2 queries
def print_query(query):
    for index in range(len(query)):
        a = query[index][0]
        res = query[index][1]
        print("\t" + "%s - %d" % (a, res) + " views")
    print("\n")


# this function that print out the last query
def print_last_query(query_result):
    for index in range(len(query_result)):
        d = query_result[index][0]
        perc = query_result[index][1]
        print("\t" + "%s - %.1f %%" % (d, perc))


dbname = 'news'
db = psycopg2.connect("dbname=news")
cursor = db.cursor()
print "the pupluar article is:"
result = pupular_artical()
print_query(result)
print "the pupluar author is:"
result = pupluar_author()
print_query(result)
print "days more than 1% of requests lead to errors"
result = errors_days()
print_last_query(result)
db.close()
