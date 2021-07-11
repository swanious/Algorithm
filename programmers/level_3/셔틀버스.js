function solution(n, t, m, timetable) {
  let answer = "";
  let shuttle = "09:00";
  const map = new Map();

  timetable.sort((a, b) => (isBelowThanShuttleTime(b, a) ? 1 : -1));
  timetable.forEach((time) => {
    if (map.has(time)) map.set(time, map.get(time) + 1);
    else map.set(time, 1);
  });

  for (let i = 0; i < n; i++) {
    const pendinglist = [];
    for (const [key, value] of map) {
      if (isBelowThanShuttleTime(key, shuttle)) {
        for (let j = 0; j < m; j++) {
          if (!map.get(key)) {
            map.delete(key);
            break;
          }

          if (pendinglist.length === m) break;

          pendinglist.push(key);
          map.set(key, map.get(key) - 1);
        }

        if (!map.get(key)) map.delete(key);
      } else break;
    }

    if (pendinglist.length < m) answer = shuttle;
    else if (pendinglist.length === m)
      answer = updateShuttleTime(pendinglist[pendinglist.length - 1], -1);

    shuttle = updateShuttleTime(shuttle, t);
  }

  return answer;
}

const isBelowThanShuttleTime = (time1, time2) => {
  const [hour1, minute1] = time1.split(":");
  const [hour2, minute2] = time2.split(":");
  const times1 = hour1 * 60 + minute1 * 1;
  const times2 = hour2 * 60 + minute2 * 1;
  return times2 - times1 >= 0 ? true : false;
};

const updateShuttleTime = (time, period) => {
  const [hour, minute] = time.split(":");
  const times = hour * 60 + minute * 1;
  const next = times + period;
  return format_to_timeStr(next);
};

const format_to_timeStr = (time) => {
  const hour = (time / 60) >> 0;
  const minute = time % 60;
  const hstr = hour > 9 ? hour : "0" + hour;
  const mstr = minute > 9 ? minute : "0" + minute;
  return hstr + ":" + mstr;
};
