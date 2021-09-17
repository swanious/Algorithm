const fs = require("fs");

fs.readdirSync("./").forEach((file) => {
  const reg1 = /\_/g;
  const reg2 = /^\d{4,5}/;
  const reg3 = /^\d{4,5}\./;
  const is_ = file.match(reg1) !== null;

  const fileName = is_ ? file : file.replace(reg2, file.match(reg2) + "_");
  fs.renameSync(file, fileName);
  console.log(fileName);
});
