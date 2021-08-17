function solution(N, road, K) {
  const dist = new Array(N + 1).fill(Number.MAX_SAFE_INTEGER);
  const adj = Array.from(Array(N + 1), () => []);
  
  road.forEach(([a,b,c]) => {        
      adj[a].push({ to: b, time: c }); 
      adj[b].push({ to: a, time: c }); 
  });
  
  const pq = [{to: 1, time: 0}]
  dist[1] = 0;
  
  while(pq.length) {
      let {to, time} = pq.pop();
      
      adj[to].forEach(next => {
          if (dist[next.to] > dist[to] + next.time) {
              dist[next.to] = dist[to] + next.time;
              pq.push(next);
          }
      })
  }
  return dist.filter(item => item <= K).length;
}