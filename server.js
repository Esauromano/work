var http = require('http');
var fs = require('fs');
var url = require('url');
const request = require('request');
var formidable = require('formidable');

var server = http.createServer(function (req, res) {
    if (req.method.toLowerCase() == 'get') {

        if(req.url =="/favicon.ico"){
			console.log(req.url);
		} 
		else{ 
			var url_parts = url.parse(req.url, true);
			//console.log(url_parts);
			var query = url_parts.query;
			
			displayForm(res);
		}

		
    } else if (req.method.toLowerCase() == 'post') {
    	console.log("POST")
        processAllFieldsOfTheForm(req, res);
    }

});

function displayForm(res) {

    fs.readFile('form.html', function (err, data) {
        res.writeHead(200, {
            'Content-Type': 'text/html',
                'Content-Length': data.length
        });
        res.write(data);
        res.end();
    });
}



function palCouch(dato){
	dato = JSON.stringify(dato);
	//Validar existencia de todos los campos antes de la inserción en la DB aquí

	request.post({
        	headers: {'content-type' : 'application/json'},
        	url:     'http://romano:xmatrixy@10.1.4.205:5984/alianza',
        	body:    dato
        }, function(error, response, body){
        console.log(body);
        });

}


function processAllFieldsOfTheForm(req, res) {
	//console.log("processAllFieldsOfTheForm");
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
    	//console.log(fields);
	
        palCouch(JSON.stringify(fields));

    });
}






server.listen(1185);
console.log("server listening on 1185");
