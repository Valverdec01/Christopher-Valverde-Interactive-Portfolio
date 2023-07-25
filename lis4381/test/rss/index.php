<html>
 <head>
 	<meta> charset="utf-8">
 	<title> Using RSS Feeds</title>
 </head>
 <body>

 $html = ""
 $publisher = "wired"
 $url = "https://www.wired.com/feed"

 $html .= '<h2> .$publisher . '</h2>';
 $html .= $url;

 $rss = simplexml_load_file($url);
 $count = 0;
 $html .= '<ul>';
 foreach($rss->channel->item as $item)
 {
  $count++
  if($count > 10)
  {
   break;
  }
  $html .= '<li> <a href ="' htmlspecialchars($item->link).'">'. htmlspecialchars($item->title) . '</a><br />';
  $html .= htmlspecialchars($item->description) . '<br />';
  $html .= htmlspecialchars($item->pubDate) . '</li><br/>';
  }
  $html .= '</ul>';

  print$html;
  ?>

  </body>
  </html>
