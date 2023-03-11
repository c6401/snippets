xmlhttp=new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
  if (xmlhttp.readyState == 4) {
    console.log(xmlhttp.responseText);
  }
};

xmlhttp.open("GET","http://example.com");
xmlhttp.send();
