const getSubsets = (arr) => {
  const visit = new Array(arr.length).fill(false);
  const res = [];
  const dfs = (depth) => {
    if (depth === arr.length) {
      const subset = arr.filter((_, index) => visit[index]);
      res.push(subset);
      return;
    }

    visit[depth] = true;
    dfs(depth + 1);

    visit[depth] = false;
    dfs(depth + 1);
  };
  dfs(0);
  return res;
};

const example = [1, 2, 3, 4];
console.log(getSubsets(example));
