{
   "_id": "_design/rest",
   "_rev": "28-214c191b44bd9b274504fcc3a6a8d059",
   "lists": {
       "lista": "function(doc, req){ provides('html', function(){html = '<!DOCTYPE html> <html> <head> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <link rel=\"stylesheet\" href=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css\"><script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script><script src=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js\"></script><style type=\"text/css\">  </style> </head> <body> <div data-role=\"page\" id=\"pageone\"><div data-role=\"header\"></div><div data-role=\"main\" class=\"ui-content\"><form class=\"ui-filterable\"><input id=\"filterBasic-input\" data-type=\"search\"></form><ul data-role=\"listview\" id=\"lista\" data-filter=\"true\" data-input=\"#filterBasic-input\" >'; while( row = getRow() ){ html += '<li><a href=\"http://132.248.13.184:5984/work/_design/rest/_list/lista/item?key=%22' + row.value.item +'%22\">'+ row.value.item + '</a><p><a href=\"http://132.248.13.184:5984/work/_design/rest/_list/lista/area?key=%22' + row.value.area +'%22\">' + row.value.area + '</a></p></li>';} html += '</ul></div><div data-role=\"footer\" data-position=\"fixed\"><h1>#BRKNRBT</h1></div> </div> </body> </html>'; return html;});}",
       "catalogo": "function(doc, req){ provides('html', function(){html = '<!DOCTYPE html> <html> <head> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <link rel=\"stylesheet\" href=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css\"><script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script><script src=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js\"></script><style type=\"text/css\">  </style> </head> <body> <div data-role=\"page\" id=\"pageone\"><div data-role=\"header\"></div><div data-role=\"main\" class=\"ui-content\"><form class=\"ui-filterable\"><input id=\"filterBasic-input\" data-type=\"search\"></form><ul data-role=\"listview\" id=\"lista\" data-filter=\"true\" data-input=\"#filterBasic-input\" >'; var ser = []; while( row = getRow() ){  if(ser.indexOf(row.value) == -1){ser.push(row.value);} }  for (var i = 0; i < ser.length; i++) { html += '<li><a href=\"http://132.248.13.184:5984/work/_design/rest/_list/lista/servicio?key=%22' + ser[i] + '%22\">' + ser[i] + '</a></li>';} html += '</ul></div><div data-role=\"footer\" data-position=\"fixed\"><h1>#BRKNRBT</h1></div> </div> </body> </html>'; return html;});}"
   },
   "views": {
       "id": {
           "map": "function (doc) {\n  emit(doc['_id'], doc);\n}"
       },
       "area": {
           "map": "function (doc) {\n  emit(doc['area'], doc);\n}"
       },
       "servicio": {
           "map": "function (doc) {\n  emit(doc['servicio'], doc);\n}"
       },
       "servicios": {
           "map": "function (doc) {\n emit(doc['_id'], doc.servicio);\n}"
       },
       "item": {
           "map": "function (doc) {\n  emit(doc['item'], doc);\n}"
       }
   }
}