process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Handle user input
process.stdin.on('data', (data) => {
  const name = data.toString().trim();

  // Output the name
  process.stdout.write(`Your name is: ${name}\n`);

  // Exit the program and trigger the 'exit' message
  process.exit();
});

// Handle exit event
process.on('exit', () => {
  process.stdout.write('This important software is now closing\n');
});
