<html>
<body>
%ifname == None :
    {{str(names)}}
%if extra != None : 
    <h2>Hello, {{name}} {{extra}}!</h2>
%else :
    <h2> Hello, {{name}}! Have a great day!</h2>
<br>
...from the template!
</body>
</html>