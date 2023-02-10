class AsyncQueue {
  constructor() {
    this.queue = [];
    this.resolve = null;
  }

  push(item) {
    if (this.resolve) {
      this.resolve(item);
      this.resolve = null;
    } else {
      this.queue.push(item);
    }
  }

  shift() {
    return new Promise(resolve => {
      if (this.queue.length > 0) {
        resolve(this.queue.shift());
      } else {
        this.resolve = resolve;
      }
    });
  }
}

queue = new AsyncQueue();

async function process() {
  while (true) {
    const item = await queue.shift();
    console.log(item);
  }
}

process();
