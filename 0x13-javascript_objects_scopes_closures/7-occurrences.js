#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const answer = list.reduce((nbOccurences, currentElement) => currentElement === searchElement ? nbOccurences + 1 : nbOccurences, 0);
  return answer;
};
