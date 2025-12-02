function main() {
    console.log("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ");
    console.log(getMelonBestAlbum(
        ["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500]));

    console.log("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ");
    console.log(getMelonBestAlbum(
        ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
        [2000, 500, 600, 150, 800, 2500, 2000]));
}

function getMelonBestAlbum(genreArray, playArray) {
    const n = genreArray.length;
    const genreTotalPlayDict = new Map(); // 장르별로 플레이수 합산 - ie ('classic': 1300, 'pop': '560)
    const genreIndexPlayArrayDict = new Map(); // 장르별로 [인덱스, 플레이수] 모아놓기 - ie ('classic': [[2, 600], [3, 200]], 'pop': [[0, 560], [1, 200]])

    // 2 개 배열을 순회하면서,
    for (let i = 0; i < n; i++) {
        const genre = genreArray[i];
        const play = playArray[i];

        if (genreTotalPlayDict.has(genre)) {
            const currentPlay = genreTotalPlayDict.get(genre)
            genreTotalPlayDict.set(genre, currentPlay + play)
            // genreIndexPlayArrayDict.get(genre).push([i, play]) // 값이 레퍼런스 값이라서 가능
            // or,
            const currentIndexPlayArray = genreIndexPlayArrayDict.get(genre)
            genreIndexPlayArrayDict.set(genre, [...currentIndexPlayArray, [i, play]] )
        } else {
            genreTotalPlayDict.set(genre, play)
            genreIndexPlayArrayDict.set(genre, [[i, play]])
        }
    }

    const sortedGenrePlayList = Array.from(genreTotalPlayDict.entries()); // Map을 Array로
    sortedGenrePlayList.sort((a, b) => b[1] - a[1]); // 장르별 합산을 정렬

    const result = [];
    for (let [genre, totalPlay] of sortedGenrePlayList) {
        const genreIndexPlayList = genreIndexPlayArrayDict.get(genre); // -> [ [index, play], [index, play]]
        genreIndexPlayList.sort((a, b) => { // 장르별 모아놓은 [인덱스, 플레이수]를 장르 안에서 정렬
            if (b[1] !== a[1]) {
                return b[1] - a[1]; // 재생 횟수 내림차순으로
            } else {
                return a[0] - b[0]; // 재생 횟수가 같다면 인덱스 오름차순 순으로
            }
        })

        let genreSongCount = 0;
        for (let [index, play] of genreIndexPlayList) {
            if (genreSongCount >= 2) {
                break;
            }
            result.push(index);
            genreSongCount++;
        }
    }

    return result;
}