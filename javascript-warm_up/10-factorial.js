#!/usr/bin/node
/**
 * Calcule la factorielle de n de manière récursive.
 * @param {Number} n - Le nombre à traiter.
 * @returns {Number} La factorielle de n.
 */
function factorial (n) {
  // Cas de base : si n est NaN (selon le sujet) ou si on atteint 0/1
  if (isNaN(n) || n === 0) {
    return 1;
  }
  // Cas récursif : n! = n * (n - 1)!
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
