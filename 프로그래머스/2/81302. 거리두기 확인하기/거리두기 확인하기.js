function solution(places) {
    var answer = [];
    
    let t = places.length;
    
    
    const bfs = (x, y, place) => {
        let visited = Array.from({length : 5}, () => Array.from({length: 5}, () => false))
        let queue = [];
        queue.push([x, y, 0])
        visited[x][y] = true
        while(queue.length !== 0){
            let [curX, curY, cnt] = queue.shift();
            for(let [dx, dy] of [[0,1],[0,-1],[1,0],[-1,0]]){
                let nx = curX + dx
                let ny = curY + dy
                if(nx < 0 || ny < 0 || nx >= 5 || ny >= 5) continue
                if(place[nx][ny] === 'X') continue;
                if(visited[nx][ny] === true) continue;
                if(cnt + 1 > 2) continue;
                if(place[nx][ny] === 'P' && !visited[nx][ny]){
                    if(Math.abs(x - nx) + Math.abs(y - ny) <= 2 && cnt <= 2){
                        // 사이에 벽이 있는지 체크하기 cnt?
                        return false;
                    }
                }
                
                queue.push([nx, ny, cnt + 1])
                visited[nx][ny] = true
            }
        }
        return true
    }
    
    for(let tc = 0; tc < t; tc++){
        let place = places[tc];
        let flag = true
        for(let i = 0; i < 5; i++){
            for(let j = 0; j < 5; j++){
                if(place[i][j] === 'P' && flag){
                    flag = bfs(i, j, place)
                }
            }
        }
        answer.push(flag ? 1 : 0);
    }
    return answer.length === 0 ? [0, 0, 0, 0, 0] : answer;
}