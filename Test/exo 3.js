/*
TODO :
retourner "Hello, Nalios" sans utiliser de string

utiliser le code ascii et écrire en brute ?
 -> oui
*/

let char_array = [72, 101, 108, 108, 111, 44, 32, 78, 97, 108, 105, 111, 115, 32, 33];

console.log(String.fromCharCode(...char_array));
