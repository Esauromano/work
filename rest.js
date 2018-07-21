{
   "_id": "_design/rest",
   "lists": {
       "lista": "function(doc, req){ provides('html', function(){html = '<!DOCTYPE html> <html> <head> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <link rel=\"stylesheet\" href=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css\"><script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script><script src=\"https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js\"></script><style type=\"text/css\">  </style> </head> <body> <div data-role=\"page\" id=\"pageone\"><div data-role=\"header\"></div><div data-role=\"main\" class=\"ui-content\"><form class=\"ui-filterable\"><input id=\"filterBasic-input\" data-type=\"search\"></form><ul data-role=\"listview\" id=\"lista\" data-filter=\"true\" data-input=\"#filterBasic-input\" class=\"has-odd-thumb\">'; while( row = getRow() ){ html += '<li><a href=\"http://132.248.13.184:5984/work/_design/rest/_list/lista/item?key=%22' + row.value.item +'%22\"><h3>'+ row.value.item + '</h3></a><h4>' + row.value.area + '</h4></a><h5>' + row.value.servicio + '</h5></li>';} html += '</ul></div><div data-role=\"footer\" data-position=\"fixed\"><h1>#BRKNRBT</h1></div> </div> </body> </html>'; return html;});}"
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
       "item": {
           "map": "function (doc) {\n  emit(doc['item'], doc);\n}"
       }
   }
}
