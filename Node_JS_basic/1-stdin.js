// 1. Write a program that takes input from the user using the process.stdin.on() method.

console.log('Welcome to Holberton School, what is your name?');

process.stdin
  .on('readable', () => {
    const name = process.stdin.read();
    if (name) {
      process.stdout.write(`Your name is: ${name}`);
    }
  })

  .on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
