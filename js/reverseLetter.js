function reverseLetter(str) {
  let fixStr = str
    .replace(/[^a-zA-Z]/gi, "")
    .split("")
    .reverse()
    .join("");

  return fixStr;
}
