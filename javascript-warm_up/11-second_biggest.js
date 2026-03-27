#!/usr/bin/node

// On récupère uniquement les arguments passés par l'utilisateur
const args = process.argv.slice(2);

if (args.length <= 1) {
  // Cas où il n'y a pas assez d'arguments pour un "second"
  console.log(0);
} else {
  // 1. On convertit tout en nombres
  // 2. On trie par ordre décroissant (b - a)
  const list = args.map(Number).sort((a, b) => b - a);
  // On affiche le deuxième élément (indice 1)
  console.log(list[1]);
}
