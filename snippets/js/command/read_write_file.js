var text = fs.readFileSync(fileName, "utf8");

var file = fs.createWriteStream(fileName, { encoding: "utf8" });
file.write("???");
file.end();
