var data = JSON.parse(value);
var descriptions = {};
var out = [];

data.forEach(function(elem) {
    if (elem["{#IFDESCR}"]) {
        var parts = elem["{#IFDESCR}"].split(":");
        var port = parts[parts.length-1].split(' ');
        descriptions[parts[0] + ':' + port[port.length-1]] = {
            "{#IFDESCR}": elem["{#IFDESCR}"],
            "{#SNMPINDEX}": elem["{#SNMPINDEX}"]
        }
    }
});

data.forEach(function(elem) {
    if (elem["{#IFNAME}"]) {
        var port = descriptions[elem["{#NODE}"] + ':' + elem["{#IFNAME}"]];

        elem["{#IFDESCR}"] = port["{#IFDESCR}"];
        elem["{#IFSNMPINDEX}"] = port["{#SNMPINDEX}"];


        switch(elem["{#TYPE}"]) {
            case '0':
                elem["{#TYPE}"] = 'physical';
                break;
            case '1':
                elem["{#TYPE}"] = 'if-group';
                break;
            case '2':
                elem["{#TYPE}"] = 'vlan';
                break;
            case '3':
                elem["{#TYPE}"] = 'undef';
                break;
        };
    
        out.push(elem);
    }
});

return JSON.stringify(out);
