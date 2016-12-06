curl -s http://www.quotationspage.com/random.php3|grep -Po '<dt class="quote"><a title=[^>]+>\K.*' |head -n 1 | sed 's@</a>.*<a href="/quotes/[^/<>]*/">@\n@' | sed 's@</a>.*@@'
