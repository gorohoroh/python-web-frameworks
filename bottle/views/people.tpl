<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<h1>People</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur, cupiditate?</p>

<ul>
% for person in people:
    <li>{{person['name']+ ", " + person['job']}}</li>
% end
</ul>
</body>
</html>