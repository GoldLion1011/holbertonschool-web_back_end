// 1. Write a program that takes input from the user using the process.stdin.on() method.

process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.once('data', (data) => {
  const name = data.toString().trim();
  if (name !== '') {
    process.stdout.write(`Your name is: ${name}\n`);
  } else {
    process.stdout.write('Your name is: undefined\n');
  }

  process.stdout.write('This important software is now closing\n');
  process.exit();
});
