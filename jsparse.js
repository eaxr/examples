const obj = JSON.parse(value);
if (obj.status == "normal") {
    return 1
}
return 0;
